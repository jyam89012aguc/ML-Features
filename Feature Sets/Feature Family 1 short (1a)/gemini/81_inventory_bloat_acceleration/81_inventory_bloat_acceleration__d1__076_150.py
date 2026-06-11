"""81 inventory bloat acceleration d1 first derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Operating_Efficiency - Institutional-grade short-side signal.
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

def f81_invb_076_struct_v76_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=284, w3=56, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(284, min_periods=max(284//3, 2)).mean()
    noise = impulse.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27875 + 0.0039077 * anchor
    return base_signal.diff()

def f81_invb_077_struct_v77_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=295, w3=69, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 295)
    curvature = _rolling_slope(acceleration, 69)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0406 * acceleration + 0.0039078 * anchor
    return base_signal.diff()

def f81_invb_078_struct_v78_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=306, w3=82, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(82) * 1.3075 + 0.0039079 * anchor
    return base_signal.diff()

def f81_invb_079_struct_v79_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=317, w3=95, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0558 * _rolling_slope(draw, 95) + 0.003908 * anchor
    return base_signal.diff()

def f81_invb_080_struct_v80_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=328, w3=108, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(328, min_periods=max(328//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33625 + 0.0039081 * anchor
    return base_signal.diff()

def f81_invb_081_struct_v81_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=339, w3=121, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 339)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=121, adjust=False).mean() * 1.350625 + 0.0039082 * anchor
    return base_signal.diff()

def f81_invb_082_struct_v82_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=350, w3=134, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(350, min_periods=max(350//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.365 + 0.0039083 * anchor
    return base_signal.diff()

def f81_invb_083_struct_v83_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=361, w3=147, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(361, min_periods=max(361//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0862 * persistence + 0.0039084 * anchor
    return base_signal.diff()

def f81_invb_084_struct_v84_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=372, w3=160, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(372, min_periods=max(372//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39375 + 0.0039085 * anchor
    return base_signal.diff()

def f81_invb_085_struct_v85_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=383, w3=173, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(383, min_periods=max(383//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1014 * slope + 0.0039086 * anchor
    return base_signal.diff()

def f81_invb_086_struct_v86_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=394, w3=186, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(17)
    drag = impulse.rolling(394, min_periods=max(394//3, 2)).mean()
    noise = impulse.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4225 + 0.0039087 * anchor
    return base_signal.diff()

def f81_invb_087_struct_v87_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=405, w3=199, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 405)
    curvature = _rolling_slope(acceleration, 199)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1166 * acceleration + 0.0039088 * anchor
    return base_signal.diff()

def f81_invb_088_struct_v88_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=416, w3=212, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(416, min_periods=max(416//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.45125 + 0.0039089 * anchor
    return base_signal.diff()

def f81_invb_089_struct_v89_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=427, w3=225, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(427, min_periods=max(427//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1318 * _rolling_slope(draw, 225) + 0.003909 * anchor
    return base_signal.diff()

def f81_invb_090_struct_v90_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=438, w3=238, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(438, min_periods=max(438//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.48 + 0.0039091 * anchor
    return base_signal.diff()

def f81_invb_091_struct_v91_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=449, w3=251, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=251, adjust=False).mean() * 1.494375 + 0.0039092 * anchor
    return base_signal.diff()

def f81_invb_092_struct_v92_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=460, w3=264, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50875 + 0.0039093 * anchor
    return base_signal.diff()

def f81_invb_093_struct_v93_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=471, w3=277, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(66)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1622 * persistence + 0.0039094 * anchor
    return base_signal.diff()

def f81_invb_094_struct_v94_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=482, w3=290, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(482, min_periods=max(482//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5375 + 0.0039095 * anchor
    return base_signal.diff()

def f81_invb_095_struct_v95_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=493, w3=303, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1774 * slope + 0.0039096 * anchor
    return base_signal.diff()

def f81_invb_096_struct_v96_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=504, w3=316, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(87)
    drag = impulse.rolling(504, min_periods=max(504//3, 2)).mean()
    noise = impulse.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.56625 + 0.0039097 * anchor
    return base_signal.diff()

def f81_invb_097_struct_v97_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=12, w3=329, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 12)
    curvature = _rolling_slope(acceleration, 329)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1926 * acceleration + 0.0039098 * anchor
    return base_signal.diff()

def f81_invb_098_struct_v98_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=23, w3=342, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(23, min_periods=max(23//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.595 + 0.0039099 * anchor
    return base_signal.diff()

def f81_invb_099_struct_v99_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=34, w3=355, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(34, min_periods=max(34//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2078 * _rolling_slope(draw, 355) + 0.00391 * anchor
    return base_signal.diff()

def f81_invb_100_struct_v100_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=45, w3=368, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(45, min_periods=max(45//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.850625 + 0.0039101 * anchor
    return base_signal.diff()

def f81_invb_101_struct_v101_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=56, w3=381, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 56)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.865 + 0.0039102 * anchor
    return base_signal.diff()

def f81_invb_102_struct_v102_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=67, w3=394, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(67, min_periods=max(67//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.879375 + 0.0039103 * anchor
    return base_signal.diff()

def f81_invb_103_struct_v103_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=78, w3=407, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(78, min_periods=max(78//3, 2)).rank(pct=True)
    persistence = change.rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2382 * persistence + 0.0039104 * anchor
    return base_signal.diff()

def f81_invb_104_struct_v104_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=89, w3=420, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(89, min_periods=max(89//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.908125 + 0.0039105 * anchor
    return base_signal.diff()

def f81_invb_105_struct_v105_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=100, w3=433, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(100, min_periods=max(100//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2534 * slope + 0.0039106 * anchor
    return base_signal.diff()

def f81_invb_106_struct_v106_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=111, w3=446, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(111, min_periods=max(111//3, 2)).mean()
    noise = impulse.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.936875 + 0.0039107 * anchor
    return base_signal.diff()

def f81_invb_107_struct_v107_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=122, w3=459, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 122)
    curvature = _rolling_slope(acceleration, 459)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2686 * acceleration + 0.0039108 * anchor
    return base_signal.diff()

def f81_invb_108_struct_v108_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=133, w3=472, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(133, min_periods=max(133//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.965625 + 0.0039109 * anchor
    return base_signal.diff()

def f81_invb_109_struct_v109_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=144, w3=485, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(144, min_periods=max(144//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2838 * _rolling_slope(draw, 485) + 0.003911 * anchor
    return base_signal.diff()

def f81_invb_110_struct_v110_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=155, w3=498, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(155, min_periods=max(155//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.994375 + 0.0039111 * anchor
    return base_signal.diff()

def f81_invb_111_struct_v111_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=166, w3=511, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 166)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.00875 + 0.0039112 * anchor
    return base_signal.diff()

def f81_invb_112_struct_v112_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=177, w3=524, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(177, min_periods=max(177//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.023125 + 0.0039113 * anchor
    return base_signal.diff()

def f81_invb_113_struct_v113_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=188, w3=537, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(188, min_periods=max(188//3, 2)).rank(pct=True)
    persistence = change.rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3142 * persistence + 0.0039114 * anchor
    return base_signal.diff()

def f81_invb_114_struct_v114_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=199, w3=550, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(199, min_periods=max(199//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.051875 + 0.0039115 * anchor
    return base_signal.diff()

def f81_invb_115_struct_v115_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=210, w3=563, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(210, min_periods=max(210//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3294 * slope + 0.0039116 * anchor
    return base_signal.diff()

def f81_invb_116_struct_v116_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=221, w3=576, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(221, min_periods=max(221//3, 2)).mean()
    noise = impulse.abs().rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.080625 + 0.0039117 * anchor
    return base_signal.diff()

def f81_invb_117_struct_v117_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=232, w3=589, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 232)
    curvature = _rolling_slope(acceleration, 589)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3446 * acceleration + 0.0039118 * anchor
    return base_signal.diff()

def f81_invb_118_struct_v118_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=243, w3=602, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(243, min_periods=max(243//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.109375 + 0.0039119 * anchor
    return base_signal.diff()

def f81_invb_119_struct_v119_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=254, w3=615, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(254, min_periods=max(254//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3598 * _rolling_slope(draw, 615) + 0.003912 * anchor
    return base_signal.diff()

def f81_invb_120_struct_v120_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=265, w3=628, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 255)
    baseline = trend.rolling(265, min_periods=max(265//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(628, min_periods=max(628//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.138125 + 0.0039121 * anchor
    return base_signal.diff()

def f81_invb_121_struct_v121_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=276, w3=641, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 11)
    slow = _rolling_slope(x, 276)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1525 + 0.0039122 * anchor
    return base_signal.diff()

def f81_invb_122_struct_v122_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=287, w3=654, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(18, min_periods=max(18//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.166875 + 0.0039123 * anchor
    return base_signal.diff()

def f81_invb_123_struct_v123_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=298, w3=667, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(25)
    rank = change.rolling(298, min_periods=max(298//3, 2)).rank(pct=True)
    persistence = change.rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3902 * persistence + 0.0039124 * anchor
    return base_signal.diff()

def f81_invb_124_struct_v124_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=309, w3=680, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(32, min_periods=max(32//3, 2)).std()
    vol_slow = ret.rolling(309, min_periods=max(309//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.195625 + 0.0039125 * anchor
    return base_signal.diff()

def f81_invb_125_struct_v125_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=320, w3=693, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(320, min_periods=max(320//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 39)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4054 * slope + 0.0039126 * anchor
    return base_signal.diff()

def f81_invb_126_struct_v126_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=331, w3=706, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(46)
    drag = impulse.rolling(331, min_periods=max(331//3, 2)).mean()
    noise = impulse.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.224375 + 0.0039127 * anchor
    return base_signal.diff()

def f81_invb_127_struct_v127_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=342, w3=719, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 53)
    acceleration = _rolling_slope(velocity, 342)
    curvature = _rolling_slope(acceleration, 719)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0442 * acceleration + 0.0039128 * anchor
    return base_signal.diff()

def f81_invb_128_struct_v128_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=353, w3=732, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(60, min_periods=max(60//3, 2)).mean(), upside.rolling(353, min_periods=max(353//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.253125 + 0.0039129 * anchor
    return base_signal.diff()

def f81_invb_129_struct_v129_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=364, w3=745, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(67, min_periods=max(67//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0594 * _rolling_slope(draw, 745) + 0.003913 * anchor
    return base_signal.diff()

def f81_invb_130_struct_v130_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=375, w3=758, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(375, min_periods=max(375//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.281875 + 0.0039131 * anchor
    return base_signal.diff()

def f81_invb_131_struct_v131_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=386, w3=771, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 386)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.29625 + 0.0039132 * anchor
    return base_signal.diff()

def f81_invb_132_struct_v132_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=397, w3=27, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(397, min_periods=max(397//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.310625 + 0.0039133 * anchor
    return base_signal.diff()

def f81_invb_133_struct_v133_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=408, w3=40, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(95)
    rank = change.rolling(408, min_periods=max(408//3, 2)).rank(pct=True)
    persistence = change.rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0898 * persistence + 0.0039134 * anchor
    return base_signal.diff()

def f81_invb_134_struct_v134_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=419, w3=53, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(419, min_periods=max(419//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.339375 + 0.0039135 * anchor
    return base_signal.diff()

def f81_invb_135_struct_v135_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=430, w3=66, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(430, min_periods=max(430//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.105 * slope + 0.0039136 * anchor
    return base_signal.diff()

def f81_invb_136_struct_v136_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=441, w3=79, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(116)
    drag = impulse.rolling(441, min_periods=max(441//3, 2)).mean()
    noise = impulse.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.368125 + 0.0039137 * anchor
    return base_signal.diff()

def f81_invb_137_struct_v137_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=452, w3=92, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 452)
    curvature = _rolling_slope(acceleration, 92)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1202 * acceleration + 0.0039138 * anchor
    return base_signal.diff()

def f81_invb_138_struct_v138_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=463, w3=105, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(130, min_periods=max(130//3, 2)).mean(), upside.rolling(463, min_periods=max(463//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(105) * 1.396875 + 0.0039139 * anchor
    return base_signal.diff()

def f81_invb_139_struct_v139_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=474, w3=118, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(474, min_periods=max(474//3, 2)).max()
    rebound = x - x.rolling(137, min_periods=max(137//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1354 * _rolling_slope(draw, 118) + 0.003914 * anchor
    return base_signal.diff()

def f81_invb_140_struct_v140_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=485, w3=131, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(485, min_periods=max(485//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.425625 + 0.0039141 * anchor
    return base_signal.diff()

def f81_invb_141_struct_v141_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=496, w3=144, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=144, adjust=False).mean() * 1.44 + 0.0039142 * anchor
    return base_signal.diff()

def f81_invb_142_struct_v142_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=507, w3=157, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(507, min_periods=max(507//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.454375 + 0.0039143 * anchor
    return base_signal.diff()

def f81_invb_143_struct_v143_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=15, w3=170, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(15, min_periods=max(15//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1658 * persistence + 0.0039144 * anchor
    return base_signal.diff()

def f81_invb_144_struct_v144_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=26, w3=183, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(26, min_periods=max(26//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.483125 + 0.0039145 * anchor
    return base_signal.diff()

def f81_invb_145_struct_v145_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=37, w3=196, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(37, min_periods=max(37//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.181 * slope + 0.0039146 * anchor
    return base_signal.diff()

def f81_invb_146_struct_v146_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=48, w3=209, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(48, min_periods=max(48//3, 2)).mean()
    noise = impulse.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.511875 + 0.0039147 * anchor
    return base_signal.diff()

def f81_invb_147_struct_v147_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=59, w3=222, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 59)
    curvature = _rolling_slope(acceleration, 222)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1962 * acceleration + 0.0039148 * anchor
    return base_signal.diff()

def f81_invb_148_struct_v148_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=70, w3=235, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(70, min_periods=max(70//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.540625 + 0.0039149 * anchor
    return base_signal.diff()

def f81_invb_149_struct_v149_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=81, w3=248, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(81, min_periods=max(81//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2114 * _rolling_slope(draw, 248) + 0.003915 * anchor
    return base_signal.diff()

def f81_invb_150_struct_v150_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=92, w3=261, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(92, min_periods=max(92//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.569375 + 0.0039151 * anchor
    return base_signal.diff()
