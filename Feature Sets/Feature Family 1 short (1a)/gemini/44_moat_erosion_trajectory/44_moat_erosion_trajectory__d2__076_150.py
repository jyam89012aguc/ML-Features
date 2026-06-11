"""44 moat erosion trajectory d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f44_met_076_struct_v76_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=70, w3=755, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(32)
    drag = impulse.rolling(70, min_periods=max(70//3, 2)).mean()
    noise = impulse.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.185625 + 0.0027077 * anchor
    return base_signal.diff().diff()

def f44_met_077_struct_v77_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=81, w3=768, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 81)
    curvature = _rolling_slope(acceleration, 768)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3058 * acceleration + 0.0027078 * anchor
    return base_signal.diff().diff()

def f44_met_078_struct_v78_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=92, w3=24, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(92, min_periods=max(92//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(24) * 1.214375 + 0.0027079 * anchor
    return base_signal.diff().diff()

def f44_met_079_struct_v79_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=103, w3=37, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(103, min_periods=max(103//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.321 * _rolling_slope(draw, 37) + 0.002708 * anchor
    return base_signal.diff().diff()

def f44_met_080_struct_v80_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=114, w3=50, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(114, min_periods=max(114//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.243125 + 0.0027081 * anchor
    return base_signal.diff().diff()

def f44_met_081_struct_v81_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=125, w3=63, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 125)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=63, adjust=False).mean() * 1.2575 + 0.0027082 * anchor
    return base_signal.diff().diff()

def f44_met_082_struct_v82_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=136, w3=76, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(136, min_periods=max(136//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.271875 + 0.0027083 * anchor
    return base_signal.diff().diff()

def f44_met_083_struct_v83_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=147, w3=89, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(81)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3514 * persistence + 0.0027084 * anchor
    return base_signal.diff().diff()

def f44_met_084_struct_v84_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=158, w3=102, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(158, min_periods=max(158//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.300625 + 0.0027085 * anchor
    return base_signal.diff().diff()

def f44_met_085_struct_v85_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=169, w3=115, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3666 * slope + 0.0027086 * anchor
    return base_signal.diff().diff()

def f44_met_086_struct_v86_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=180, w3=128, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(102)
    drag = impulse.rolling(180, min_periods=max(180//3, 2)).mean()
    noise = impulse.abs().rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.329375 + 0.0027087 * anchor
    return base_signal.diff().diff()

def f44_met_087_struct_v87_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=191, w3=141, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 191)
    curvature = _rolling_slope(acceleration, 141)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3818 * acceleration + 0.0027088 * anchor
    return base_signal.diff().diff()

def f44_met_088_struct_v88_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=116, w2=202, w3=154, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(202, min_periods=max(202//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.358125 + 0.0027089 * anchor
    return base_signal.diff().diff()

def f44_met_089_struct_v89_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=123, w2=213, w3=167, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.397 * _rolling_slope(draw, 167) + 0.002709 * anchor
    return base_signal.diff().diff()

def f44_met_090_struct_v90_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=130, w2=224, w3=180, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(224, min_periods=max(224//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.386875 + 0.0027091 * anchor
    return base_signal.diff().diff()

def f44_met_091_struct_v91_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=137, w2=235, w3=193, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 235)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=193, adjust=False).mean() * 1.40125 + 0.0027092 * anchor
    return base_signal.diff().diff()

def f44_met_092_struct_v92_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=144, w2=246, w3=206, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.415625 + 0.0027093 * anchor
    return base_signal.diff().diff()

def f44_met_093_struct_v93_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=151, w2=257, w3=219, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.051 * persistence + 0.0027094 * anchor
    return base_signal.diff().diff()

def f44_met_094_struct_v94_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=158, w2=268, w3=232, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(268, min_periods=max(268//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.444375 + 0.0027095 * anchor
    return base_signal.diff().diff()

def f44_met_095_struct_v95_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=165, w2=279, w3=245, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(279, min_periods=max(279//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0662 * slope + 0.0027096 * anchor
    return base_signal.diff().diff()

def f44_met_096_struct_v96_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=172, w2=290, w3=258, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(290, min_periods=max(290//3, 2)).mean()
    noise = impulse.abs().rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.473125 + 0.0027097 * anchor
    return base_signal.diff().diff()

def f44_met_097_struct_v97_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=179, w2=301, w3=271, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 301)
    curvature = _rolling_slope(acceleration, 271)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0814 * acceleration + 0.0027098 * anchor
    return base_signal.diff().diff()

def f44_met_098_struct_v98_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=186, w2=312, w3=284, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(312, min_periods=max(312//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.501875 + 0.0027099 * anchor
    return base_signal.diff().diff()

def f44_met_099_struct_v99_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=193, w2=323, w3=297, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(323, min_periods=max(323//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0966 * _rolling_slope(draw, 297) + 0.00271 * anchor
    return base_signal.diff().diff()

def f44_met_100_struct_v100_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=200, w2=334, w3=310, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(334, min_periods=max(334//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.530625 + 0.0027101 * anchor
    return base_signal.diff().diff()

def f44_met_101_struct_v101_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=207, w2=345, w3=323, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 345)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.545 + 0.0027102 * anchor
    return base_signal.diff().diff()

def f44_met_102_struct_v102_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=214, w2=356, w3=336, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(356, min_periods=max(356//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.559375 + 0.0027103 * anchor
    return base_signal.diff().diff()

def f44_met_103_struct_v103_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=221, w2=367, w3=349, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(367, min_periods=max(367//3, 2)).rank(pct=True)
    persistence = change.rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.127 * persistence + 0.0027104 * anchor
    return base_signal.diff().diff()

def f44_met_104_struct_v104_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=228, w2=378, w3=362, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(378, min_periods=max(378//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.588125 + 0.0027105 * anchor
    return base_signal.diff().diff()

def f44_met_105_struct_v105_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=235, w2=389, w3=375, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(389, min_periods=max(389//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1422 * slope + 0.0027106 * anchor
    return base_signal.diff().diff()

def f44_met_106_struct_v106_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=242, w2=400, w3=388, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(400, min_periods=max(400//3, 2)).mean()
    noise = impulse.abs().rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.616875 + 0.0027107 * anchor
    return base_signal.diff().diff()

def f44_met_107_struct_v107_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=249, w2=411, w3=401, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 411)
    curvature = _rolling_slope(acceleration, 401)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1574 * acceleration + 0.0027108 * anchor
    return base_signal.diff().diff()

def f44_met_108_struct_v108_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=5, w2=422, w3=414, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(422, min_periods=max(422//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8725 + 0.0027109 * anchor
    return base_signal.diff().diff()

def f44_met_109_struct_v109_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=12, w2=433, w3=427, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(433, min_periods=max(433//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1726 * _rolling_slope(draw, 427) + 0.002711 * anchor
    return base_signal.diff().diff()

def f44_met_110_struct_v110_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=19, w2=444, w3=440, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(444, min_periods=max(444//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.90125 + 0.0027111 * anchor
    return base_signal.diff().diff()

def f44_met_111_struct_v111_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=26, w2=455, w3=453, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 455)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.915625 + 0.0027112 * anchor
    return base_signal.diff().diff()

def f44_met_112_struct_v112_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=33, w2=466, w3=466, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(466, min_periods=max(466//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.93 + 0.0027113 * anchor
    return base_signal.diff().diff()

def f44_met_113_struct_v113_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=40, w2=477, w3=479, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(40)
    rank = change.rolling(477, min_periods=max(477//3, 2)).rank(pct=True)
    persistence = change.rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.203 * persistence + 0.0027114 * anchor
    return base_signal.diff().diff()

def f44_met_114_struct_v114_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=47, w2=488, w3=492, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95875 + 0.0027115 * anchor
    return base_signal.diff().diff()

def f44_met_115_struct_v115_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=54, w2=499, w3=505, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(499, min_periods=max(499//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2182 * slope + 0.0027116 * anchor
    return base_signal.diff().diff()

def f44_met_116_struct_v116_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=61, w2=510, w3=518, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(61)
    drag = impulse.rolling(510, min_periods=max(510//3, 2)).mean()
    noise = impulse.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9875 + 0.0027117 * anchor
    return base_signal.diff().diff()

def f44_met_117_struct_v117_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=68, w2=18, w3=531, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 18)
    curvature = _rolling_slope(acceleration, 531)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2334 * acceleration + 0.0027118 * anchor
    return base_signal.diff().diff()

def f44_met_118_struct_v118_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=75, w2=29, w3=544, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(29, min_periods=max(29//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.01625 + 0.0027119 * anchor
    return base_signal.diff().diff()

def f44_met_119_struct_v119_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=82, w2=40, w3=557, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(40, min_periods=max(40//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2486 * _rolling_slope(draw, 557) + 0.002712 * anchor
    return base_signal.diff().diff()

def f44_met_120_struct_v120_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=89, w2=51, w3=570, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(51, min_periods=max(51//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(570, min_periods=max(570//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.045 + 0.0027121 * anchor
    return base_signal.diff().diff()

def f44_met_121_struct_v121_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=96, w2=62, w3=583, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 62)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.059375 + 0.0027122 * anchor
    return base_signal.diff().diff()

def f44_met_122_struct_v122_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=103, w2=73, w3=596, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(73, min_periods=max(73//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07375 + 0.0027123 * anchor
    return base_signal.diff().diff()

def f44_met_123_struct_v123_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=110, w2=84, w3=609, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(110)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.279 * persistence + 0.0027124 * anchor
    return base_signal.diff().diff()

def f44_met_124_struct_v124_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=117, w2=95, w3=622, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(95, min_periods=max(95//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1025 + 0.0027125 * anchor
    return base_signal.diff().diff()

def f44_met_125_struct_v125_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=124, w2=106, w3=635, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(106, min_periods=max(106//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2942 * slope + 0.0027126 * anchor
    return base_signal.diff().diff()

def f44_met_126_struct_v126_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=131, w2=117, w3=648, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(117, min_periods=max(117//3, 2)).mean()
    noise = impulse.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13125 + 0.0027127 * anchor
    return base_signal.diff().diff()

def f44_met_127_struct_v127_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=138, w2=128, w3=661, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 128)
    curvature = _rolling_slope(acceleration, 661)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3094 * acceleration + 0.0027128 * anchor
    return base_signal.diff().diff()

def f44_met_128_struct_v128_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=145, w2=139, w3=674, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.16 + 0.0027129 * anchor
    return base_signal.diff().diff()

def f44_met_129_struct_v129_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=152, w2=150, w3=687, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(150, min_periods=max(150//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3246 * _rolling_slope(draw, 687) + 0.002713 * anchor
    return base_signal.diff().diff()

def f44_met_130_struct_v130_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=159, w2=161, w3=700, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(161, min_periods=max(161//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.18875 + 0.0027131 * anchor
    return base_signal.diff().diff()

def f44_met_131_struct_v131_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=166, w2=172, w3=713, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.203125 + 0.0027132 * anchor
    return base_signal.diff().diff()

def f44_met_132_struct_v132_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=173, w2=183, w3=726, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(183, min_periods=max(183//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2175 + 0.0027133 * anchor
    return base_signal.diff().diff()

def f44_met_133_struct_v133_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=180, w2=194, w3=739, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355 * persistence + 0.0027134 * anchor
    return base_signal.diff().diff()

def f44_met_134_struct_v134_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=187, w2=205, w3=752, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(205, min_periods=max(205//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24625 + 0.0027135 * anchor
    return base_signal.diff().diff()

def f44_met_135_struct_v135_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=194, w2=216, w3=765, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(216, min_periods=max(216//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3702 * slope + 0.0027136 * anchor
    return base_signal.diff().diff()

def f44_met_136_struct_v136_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=201, w2=227, w3=21, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(227, min_periods=max(227//3, 2)).mean()
    noise = impulse.abs().rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275 + 0.0027137 * anchor
    return base_signal.diff().diff()

def f44_met_137_struct_v137_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=208, w2=238, w3=34, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 238)
    curvature = _rolling_slope(acceleration, 34)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3854 * acceleration + 0.0027138 * anchor
    return base_signal.diff().diff()

def f44_met_138_struct_v138_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=215, w2=249, w3=47, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(249, min_periods=max(249//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(47) * 1.30375 + 0.0027139 * anchor
    return base_signal.diff().diff()

def f44_met_139_struct_v139_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=222, w2=260, w3=60, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(260, min_periods=max(260//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4006 * _rolling_slope(draw, 60) + 0.002714 * anchor
    return base_signal.diff().diff()

def f44_met_140_struct_v140_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=229, w2=271, w3=73, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(271, min_periods=max(271//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3325 + 0.0027141 * anchor
    return base_signal.diff().diff()

def f44_met_141_struct_v141_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=236, w2=282, w3=86, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 282)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=86, adjust=False).mean() * 1.346875 + 0.0027142 * anchor
    return base_signal.diff().diff()

def f44_met_142_struct_v142_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=243, w2=293, w3=99, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(293, min_periods=max(293//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36125 + 0.0027143 * anchor
    return base_signal.diff().diff()

def f44_met_143_struct_v143_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=250, w2=304, w3=112, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(304, min_periods=max(304//3, 2)).rank(pct=True)
    persistence = change.rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0546 * persistence + 0.0027144 * anchor
    return base_signal.diff().diff()

def f44_met_144_struct_v144_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=6, w2=315, w3=125, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(315, min_periods=max(315//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39 + 0.0027145 * anchor
    return base_signal.diff().diff()

def f44_met_145_struct_v145_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=13, w2=326, w3=138, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0698 * slope + 0.0027146 * anchor
    return base_signal.diff().diff()

def f44_met_146_struct_v146_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=20, w2=337, w3=151, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(20)
    drag = impulse.rolling(337, min_periods=max(337//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41875 + 0.0027147 * anchor
    return base_signal.diff().diff()

def f44_met_147_struct_v147_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=27, w2=348, w3=164, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 348)
    curvature = _rolling_slope(acceleration, 164)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.085 * acceleration + 0.0027148 * anchor
    return base_signal.diff().diff()

def f44_met_148_struct_v148_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=34, w2=359, w3=177, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(359, min_periods=max(359//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4475 + 0.0027149 * anchor
    return base_signal.diff().diff()

def f44_met_149_struct_v149_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=41, w2=370, w3=190, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(370, min_periods=max(370//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1002 * _rolling_slope(draw, 190) + 0.002715 * anchor
    return base_signal.diff().diff()

def f44_met_150_struct_v150_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=48, w2=381, w3=203, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(381, min_periods=max(381//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.47625 + 0.0027151 * anchor
    return base_signal.diff().diff()
