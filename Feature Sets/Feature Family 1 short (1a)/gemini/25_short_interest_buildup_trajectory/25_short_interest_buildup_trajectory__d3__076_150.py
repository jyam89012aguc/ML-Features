"""25 short interest buildup trajectory d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Securities_Lending - Institutional-grade short-side signal.
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

def f25_sib_076_struct_v76_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=117, w2=359, w3=697, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(117)
    drag = impulse.rolling(359, min_periods=max(359//3, 2)).mean()
    noise = impulse.abs().rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0925 + 0.0015077 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_077_struct_v77_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=124, w2=370, w3=710, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 370)
    curvature = _rolling_slope(acceleration, 710)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1946 * acceleration + 0.0015078 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_078_struct_v78_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=131, w2=381, w3=723, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(381, min_periods=max(381//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.12125 + 0.0015079 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_079_struct_v79_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=138, w2=392, w3=736, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(392, min_periods=max(392//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2098 * _rolling_slope(draw, 736) + 0.001508 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_080_struct_v80_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=403, w3=749, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(403, min_periods=max(403//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15 + 0.0015081 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_081_struct_v81_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=414, w3=762, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 414)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.164375 + 0.0015082 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_082_struct_v82_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=425, w3=18, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(425, min_periods=max(425//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17875 + 0.0015083 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_083_struct_v83_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=436, w3=31, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(436, min_periods=max(436//3, 2)).rank(pct=True)
    persistence = change.rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2402 * persistence + 0.0015084 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_084_struct_v84_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=447, w3=44, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(447, min_periods=max(447//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2075 + 0.0015085 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_085_struct_v85_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=458, w3=57, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(458, min_periods=max(458//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2554 * slope + 0.0015086 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_086_struct_v86_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=469, w3=70, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(469, min_periods=max(469//3, 2)).mean()
    noise = impulse.abs().rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.23625 + 0.0015087 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_087_struct_v87_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=480, w3=83, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 480)
    curvature = _rolling_slope(acceleration, 83)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2706 * acceleration + 0.0015088 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_088_struct_v88_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=491, w3=96, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(491, min_periods=max(491//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(96) * 1.265 + 0.0015089 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_089_struct_v89_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=502, w3=109, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(502, min_periods=max(502//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2858 * _rolling_slope(draw, 109) + 0.001509 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_090_struct_v90_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=10, w3=122, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 215)
    baseline = trend.rolling(10, min_periods=max(10//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.29375 + 0.0015091 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_091_struct_v91_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=21, w3=135, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=135, adjust=False).mean() * 1.308125 + 0.0015092 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_092_struct_v92_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=32, w3=148, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3225 + 0.0015093 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_093_struct_v93_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=43, w3=161, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3162 * persistence + 0.0015094 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_094_struct_v94_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=54, w3=174, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35125 + 0.0015095 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_095_struct_v95_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=65, w3=187, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3314 * slope + 0.0015096 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_096_struct_v96_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=76, w3=200, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(6)
    drag = impulse.rolling(76, min_periods=max(76//3, 2)).mean()
    noise = impulse.abs().rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.38 + 0.0015097 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_097_struct_v97_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=87, w3=213, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 13)
    acceleration = _rolling_slope(velocity, 87)
    curvature = _rolling_slope(acceleration, 213)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3466 * acceleration + 0.0015098 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_098_struct_v98_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=98, w3=226, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.40875 + 0.0015099 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_099_struct_v99_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=109, w3=239, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(109, min_periods=max(109//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3618 * _rolling_slope(draw, 239) + 0.00151 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_100_struct_v100_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=120, w3=252, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 34)
    baseline = trend.rolling(120, min_periods=max(120//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4375 + 0.0015101 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_101_struct_v101_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=131, w3=265, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 41)
    slow = _rolling_slope(x, 131)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=265, adjust=False).mean() * 1.451875 + 0.0015102 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_102_struct_v102_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=142, w3=278, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(142, min_periods=max(142//3, 2)).max()
    trough = x.rolling(48, min_periods=max(48//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.46625 + 0.0015103 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_103_struct_v103_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=153, w3=291, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(55)
    rank = change.rolling(153, min_periods=max(153//3, 2)).rank(pct=True)
    persistence = change.rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3922 * persistence + 0.0015104 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_104_struct_v104_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=164, w3=304, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(62, min_periods=max(62//3, 2)).std()
    vol_slow = ret.rolling(164, min_periods=max(164//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.495 + 0.0015105 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_105_struct_v105_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=175, w3=317, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(175, min_periods=max(175//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 69)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4074 * slope + 0.0015106 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_106_struct_v106_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=186, w3=330, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(76)
    drag = impulse.rolling(186, min_periods=max(186//3, 2)).mean()
    noise = impulse.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.52375 + 0.0015107 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_107_struct_v107_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=197, w3=343, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 83)
    acceleration = _rolling_slope(velocity, 197)
    curvature = _rolling_slope(acceleration, 343)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0462 * acceleration + 0.0015108 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_108_struct_v108_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=208, w3=356, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(208, min_periods=max(208//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5525 + 0.0015109 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_109_struct_v109_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=219, w3=369, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(219, min_periods=max(219//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0614 * _rolling_slope(draw, 369) + 0.001511 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_110_struct_v110_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=230, w3=382, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 104)
    baseline = trend.rolling(230, min_periods=max(230//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58125 + 0.0015111 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_111_struct_v111_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=241, w3=395, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 111)
    slow = _rolling_slope(x, 241)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.595625 + 0.0015112 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_112_struct_v112_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=252, w3=408, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(252, min_periods=max(252//3, 2)).max()
    trough = x.rolling(118, min_periods=max(118//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.61 + 0.0015113 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_113_struct_v113_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=263, w3=421, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(125)
    rank = change.rolling(263, min_periods=max(263//3, 2)).rank(pct=True)
    persistence = change.rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0918 * persistence + 0.0015114 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_114_struct_v114_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=274, w3=434, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(132, min_periods=max(132//3, 2)).std()
    vol_slow = ret.rolling(274, min_periods=max(274//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.865625 + 0.0015115 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_115_struct_v115_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=285, w3=447, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 139)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.107 * slope + 0.0015116 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_116_struct_v116_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=296, w3=460, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(296, min_periods=max(296//3, 2)).mean()
    noise = impulse.abs().rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.894375 + 0.0015117 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_117_struct_v117_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=307, w3=473, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 153)
    acceleration = _rolling_slope(velocity, 307)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1222 * acceleration + 0.0015118 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_118_struct_v118_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=318, w3=486, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(160, min_periods=max(160//3, 2)).mean(), upside.rolling(318, min_periods=max(318//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.923125 + 0.0015119 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_119_struct_v119_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=329, w3=499, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(329, min_periods=max(329//3, 2)).max()
    rebound = x - x.rolling(167, min_periods=max(167//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1374 * _rolling_slope(draw, 499) + 0.001512 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_120_struct_v120_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=340, w3=512, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 174)
    baseline = trend.rolling(340, min_periods=max(340//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.951875 + 0.0015121 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_121_struct_v121_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=351, w3=525, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 181)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.96625 + 0.0015122 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_122_struct_v122_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=362, w3=538, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(362, min_periods=max(362//3, 2)).max()
    trough = x.rolling(188, min_periods=max(188//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.980625 + 0.0015123 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_123_struct_v123_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=373, w3=551, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1678 * persistence + 0.0015124 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_124_struct_v124_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=384, w3=564, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(202, min_periods=max(202//3, 2)).std()
    vol_slow = ret.rolling(384, min_periods=max(384//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.009375 + 0.0015125 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_125_struct_v125_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=395, w3=577, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 209)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.183 * slope + 0.0015126 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_126_struct_v126_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=406, w3=590, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(406, min_periods=max(406//3, 2)).mean()
    noise = impulse.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.038125 + 0.0015127 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_127_struct_v127_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=417, w3=603, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 223)
    acceleration = _rolling_slope(velocity, 417)
    curvature = _rolling_slope(acceleration, 603)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1982 * acceleration + 0.0015128 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_128_struct_v128_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=428, w3=616, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(428, min_periods=max(428//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.066875 + 0.0015129 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_129_struct_v129_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=439, w3=629, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(439, min_periods=max(439//3, 2)).max()
    rebound = x - x.rolling(237, min_periods=max(237//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2134 * _rolling_slope(draw, 629) + 0.001513 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_130_struct_v130_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=450, w3=642, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.095625 + 0.0015131 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_131_struct_v131_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=461, w3=655, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 461)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.11 + 0.0015132 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_132_struct_v132_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=472, w3=668, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(472, min_periods=max(472//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.124375 + 0.0015133 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_133_struct_v133_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=483, w3=681, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(14)
    rank = change.rolling(483, min_periods=max(483//3, 2)).rank(pct=True)
    persistence = change.rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2438 * persistence + 0.0015134 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_134_struct_v134_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=494, w3=694, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(494, min_periods=max(494//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.153125 + 0.0015135 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_135_struct_v135_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=505, w3=707, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.259 * slope + 0.0015136 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_136_struct_v136_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=13, w3=720, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(35)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.181875 + 0.0015137 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_137_struct_v137_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=24, w3=733, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 24)
    curvature = _rolling_slope(acceleration, 733)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2742 * acceleration + 0.0015138 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_138_struct_v138_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=35, w3=746, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(35, min_periods=max(35//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.210625 + 0.0015139 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_139_struct_v139_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=46, w3=759, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(46, min_periods=max(46//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2894 * _rolling_slope(draw, 759) + 0.001514 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_140_struct_v140_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=57, w3=15, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(57, min_periods=max(57//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.239375 + 0.0015141 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_141_struct_v141_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=68, w3=28, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 68)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=28, adjust=False).mean() * 1.25375 + 0.0015142 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_142_struct_v142_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=79, w3=41, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(79, min_periods=max(79//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.268125 + 0.0015143 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_143_struct_v143_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=90, w3=54, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(84)
    rank = change.rolling(90, min_periods=max(90//3, 2)).rank(pct=True)
    persistence = change.rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3198 * persistence + 0.0015144 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_144_struct_v144_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=101, w3=67, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(101, min_periods=max(101//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.296875 + 0.0015145 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_145_struct_v145_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=112, w3=80, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(112, min_periods=max(112//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.335 * slope + 0.0015146 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_146_struct_v146_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=123, w3=93, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(105)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.325625 + 0.0015147 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_147_struct_v147_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=134, w3=106, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 134)
    curvature = _rolling_slope(acceleration, 106)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3502 * acceleration + 0.0015148 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_148_struct_v148_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=145, w3=119, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(145, min_periods=max(145//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(119) * 1.354375 + 0.0015149 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_149_struct_v149_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=156, w3=132, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(156, min_periods=max(156//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3654 * _rolling_slope(draw, 132) + 0.001515 * anchor
    return base_signal.diff().diff().diff()

def f25_sib_150_struct_v150_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=133, w2=167, w3=145, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(167, min_periods=max(167//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.383125 + 0.0015151 * anchor
    return base_signal.diff().diff().diff()
