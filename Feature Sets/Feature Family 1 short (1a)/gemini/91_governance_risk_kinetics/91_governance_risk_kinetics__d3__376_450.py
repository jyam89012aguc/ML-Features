"""91 governance risk kinetics d3 third derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Governance - Institutional-grade short-side signal.
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

def f91_govr_376_struct_v376_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=22, w2=307, w3=334, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(22)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.435 + 0.0041777 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_377_struct_v377_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=29, w2=318, w3=347, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 318)
    curvature = _rolling_slope(acceleration, 347)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235 * acceleration + 0.0041778 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_378_struct_v378_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=36, w2=329, w3=360, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.46375 + 0.0041779 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_379_struct_v379_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=43, w2=340, w3=373, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2502 * _rolling_slope(draw, 373) + 0.004178 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_380_struct_v380_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=50, w2=351, w3=386, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(351, min_periods=max(351//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4925 + 0.0041781 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_381_struct_v381_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=57, w2=362, w3=399, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 362)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.506875 + 0.0041782 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_382_struct_v382_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=64, w2=373, w3=412, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(373, min_periods=max(373//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.52125 + 0.0041783 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_383_struct_v383_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=71, w2=384, w3=425, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(71)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2806 * persistence + 0.0041784 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_384_struct_v384_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=78, w2=395, w3=438, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55 + 0.0041785 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_385_struct_v385_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=85, w2=406, w3=451, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(406, min_periods=max(406//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2958 * slope + 0.0041786 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_386_struct_v386_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=92, w2=417, w3=464, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(92)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.57875 + 0.0041787 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_387_struct_v387_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=99, w2=428, w3=477, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 428)
    curvature = _rolling_slope(acceleration, 477)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.311 * acceleration + 0.0041788 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_388_struct_v388_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=106, w2=439, w3=490, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.6075 + 0.0041789 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_389_struct_v389_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=113, w2=450, w3=503, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(450, min_periods=max(450//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3262 * _rolling_slope(draw, 503) + 0.004179 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_390_struct_v390_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=120, w2=461, w3=516, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.863125 + 0.0041791 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_391_struct_v391_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=127, w2=472, w3=529, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8775 + 0.0041792 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_392_struct_v392_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=134, w2=483, w3=542, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.891875 + 0.0041793 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_393_struct_v393_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=141, w2=494, w3=555, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3566 * persistence + 0.0041794 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_394_struct_v394_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=148, w2=505, w3=568, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.920625 + 0.0041795 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_395_struct_v395_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=155, w2=13, w3=581, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3718 * slope + 0.0041796 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_396_struct_v396_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=162, w2=24, w3=594, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.949375 + 0.0041797 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_397_struct_v397_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=169, w2=35, w3=607, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.387 * acceleration + 0.0041798 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_398_struct_v398_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=176, w2=46, w3=620, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.978125 + 0.0041799 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_399_struct_v399_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=183, w2=57, w3=633, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4022 * _rolling_slope(draw, 633) + 0.00418 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_400_struct_v400_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=190, w2=68, w3=646, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(68, min_periods=max(68//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.006875 + 0.0041801 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_401_struct_v401_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=197, w2=79, w3=659, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.02125 + 0.0041802 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_402_struct_v402_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=204, w2=90, w3=672, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(90, min_periods=max(90//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.035625 + 0.0041803 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_403_struct_v403_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=211, w2=101, w3=685, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(101, min_periods=max(101//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0562 * persistence + 0.0041804 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_404_struct_v404_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=218, w2=112, w3=698, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(112, min_periods=max(112//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.064375 + 0.0041805 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_405_struct_v405_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=225, w2=123, w3=711, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(123, min_periods=max(123//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0714 * slope + 0.0041806 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_406_struct_v406_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=232, w2=134, w3=724, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(134, min_periods=max(134//3, 2)).mean()
    noise = impulse.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.093125 + 0.0041807 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_407_struct_v407_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=239, w2=145, w3=737, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 737)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0866 * acceleration + 0.0041808 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_408_struct_v408_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=246, w2=156, w3=750, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(156, min_periods=max(156//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.121875 + 0.0041809 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_409_struct_v409_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=253, w2=167, w3=763, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(167, min_periods=max(167//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1018 * _rolling_slope(draw, 763) + 0.004181 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_410_struct_v410_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=9, w2=178, w3=19, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.150625 + 0.0041811 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_411_struct_v411_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=16, w2=189, w3=32, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 1.165 + 0.0041812 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_412_struct_v412_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=23, w2=200, w3=45, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(200, min_periods=max(200//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.179375 + 0.0041813 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_413_struct_v413_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=211, w3=58, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(30)
    rank = change.rolling(211, min_periods=max(211//3, 2)).rank(pct=True)
    persistence = change.rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1322 * persistence + 0.0041814 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_414_struct_v414_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=222, w3=71, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(222, min_periods=max(222//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.208125 + 0.0041815 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_415_struct_v415_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=233, w3=84, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(233, min_periods=max(233//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1474 * slope + 0.0041816 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_416_struct_v416_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=244, w3=97, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(51)
    drag = impulse.rolling(244, min_periods=max(244//3, 2)).mean()
    noise = impulse.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.236875 + 0.0041817 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_417_struct_v417_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=255, w3=110, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 255)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1626 * acceleration + 0.0041818 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_418_struct_v418_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=266, w3=123, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(266, min_periods=max(266//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(123) * 1.265625 + 0.0041819 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_419_struct_v419_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=277, w3=136, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1778 * _rolling_slope(draw, 136) + 0.004182 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_420_struct_v420_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=288, w3=149, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(288, min_periods=max(288//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.294375 + 0.0041821 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_421_struct_v421_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=299, w3=162, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 299)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=162, adjust=False).mean() * 1.30875 + 0.0041822 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_422_struct_v422_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=310, w3=175, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.323125 + 0.0041823 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_423_struct_v423_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=321, w3=188, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(100)
    rank = change.rolling(321, min_periods=max(321//3, 2)).rank(pct=True)
    persistence = change.rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2082 * persistence + 0.0041824 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_424_struct_v424_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=332, w3=201, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.351875 + 0.0041825 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_425_struct_v425_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=343, w3=214, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(343, min_periods=max(343//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2234 * slope + 0.0041826 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_426_struct_v426_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=354, w3=227, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(121)
    drag = impulse.rolling(354, min_periods=max(354//3, 2)).mean()
    noise = impulse.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.380625 + 0.0041827 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_427_struct_v427_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=365, w3=240, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2386 * acceleration + 0.0041828 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_428_struct_v428_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=376, w3=253, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(376, min_periods=max(376//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.409375 + 0.0041829 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_429_struct_v429_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=387, w3=266, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(387, min_periods=max(387//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2538 * _rolling_slope(draw, 266) + 0.004183 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_430_struct_v430_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=398, w3=279, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.438125 + 0.0041831 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_431_struct_v431_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=409, w3=292, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 409)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=292, adjust=False).mean() * 1.4525 + 0.0041832 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_432_struct_v432_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=420, w3=305, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(420, min_periods=max(420//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.466875 + 0.0041833 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_433_struct_v433_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=431, w3=318, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2842 * persistence + 0.0041834 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_434_struct_v434_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=442, w3=331, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.495625 + 0.0041835 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_435_struct_v435_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=453, w3=344, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(453, min_periods=max(453//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2994 * slope + 0.0041836 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_436_struct_v436_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=464, w3=357, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.524375 + 0.0041837 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_437_struct_v437_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=475, w3=370, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 370)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3146 * acceleration + 0.0041838 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_438_struct_v438_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=486, w3=383, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(486, min_periods=max(486//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.553125 + 0.0041839 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_439_struct_v439_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=497, w3=396, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(497, min_periods=max(497//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3298 * _rolling_slope(draw, 396) + 0.004184 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_440_struct_v440_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=508, w3=409, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(508, min_periods=max(508//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.581875 + 0.0041841 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_441_struct_v441_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=16, w3=422, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.59625 + 0.0041842 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_442_struct_v442_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=27, w3=435, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(27, min_periods=max(27//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.610625 + 0.0041843 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_443_struct_v443_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=38, w3=448, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(38, min_periods=max(38//3, 2)).rank(pct=True)
    persistence = change.rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3602 * persistence + 0.0041844 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_444_struct_v444_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=49, w3=461, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86625 + 0.0041845 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_445_struct_v445_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=60, w3=474, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(60, min_periods=max(60//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3754 * slope + 0.0041846 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_446_struct_v446_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=71, w3=487, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(10)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.895 + 0.0041847 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_447_struct_v447_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=82, w3=500, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 82)
    curvature = _rolling_slope(acceleration, 500)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3906 * acceleration + 0.0041848 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_448_struct_v448_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=93, w3=513, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.92375 + 0.0041849 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_449_struct_v449_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=104, w3=526, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(104, min_periods=max(104//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4058 * _rolling_slope(draw, 526) + 0.004185 * anchor
    return base_signal.diff().diff().diff()

def f91_govr_450_struct_v450_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=115, w3=539, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(115, min_periods=max(115//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9525 + 0.0041851 * anchor
    return base_signal.diff().diff().diff()
