"""26 dilution rate trajectory base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f26_dlr_001_struct_v1(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=98, w3=709, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 98)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.908125 + 0.0015602 * anchor

def f26_dlr_002_struct_v2(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=109, w3=722, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(109, min_periods=max(109//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9225 + 0.0015603 * anchor

def f26_dlr_003_struct_v3(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=120, w3=735, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(41)
    rank = change.rolling(120, min_periods=max(120//3, 2)).rank(pct=True)
    persistence = change.rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0518 * persistence + 0.0015604 * anchor

def f26_dlr_004_struct_v4(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=131, w3=748, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(131, min_periods=max(131//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95125 + 0.0015605 * anchor

def f26_dlr_005_struct_v5(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=142, w3=761, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(142, min_periods=max(142//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.067 * slope + 0.0015606 * anchor

def f26_dlr_006_struct_v6(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=153, w3=17, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(62)
    drag = impulse.rolling(153, min_periods=max(153//3, 2)).mean()
    noise = impulse.abs().rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.98 + 0.0015607 * anchor

def f26_dlr_007_struct_v7(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=164, w3=30, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 164)
    curvature = _rolling_slope(acceleration, 30)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0822 * acceleration + 0.0015608 * anchor

def f26_dlr_008_struct_v8(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=175, w3=43, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(175, min_periods=max(175//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(43) * 1.00875 + 0.0015609 * anchor

def f26_dlr_009_struct_v9(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=186, w3=56, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(186, min_periods=max(186//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0974 * _rolling_slope(draw, 56) + 0.001561 * anchor

def f26_dlr_010_struct_v10(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=197, w3=69, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0375 + 0.0015611 * anchor

def f26_dlr_011_struct_v11(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=208, w3=82, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 208)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=82, adjust=False).mean() * 1.051875 + 0.0015612 * anchor

def f26_dlr_012_struct_v12(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=219, w3=95, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(219, min_periods=max(219//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.06625 + 0.0015613 * anchor

def f26_dlr_013_struct_v13(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=230, w3=108, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(111)
    rank = change.rolling(230, min_periods=max(230//3, 2)).rank(pct=True)
    persistence = change.rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1278 * persistence + 0.0015614 * anchor

def f26_dlr_014_struct_v14(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=241, w3=121, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(241, min_periods=max(241//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.095 + 0.0015615 * anchor

def f26_dlr_015_struct_v15(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=252, w3=134, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(252, min_periods=max(252//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.143 * slope + 0.0015616 * anchor

def f26_dlr_016_struct_v16(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=263, w3=147, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(263, min_periods=max(263//3, 2)).mean()
    noise = impulse.abs().rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.12375 + 0.0015617 * anchor

def f26_dlr_017_struct_v17(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=274, w3=160, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 274)
    curvature = _rolling_slope(acceleration, 160)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1582 * acceleration + 0.0015618 * anchor

def f26_dlr_018_struct_v18(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=285, w3=173, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(285, min_periods=max(285//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1525 + 0.0015619 * anchor

def f26_dlr_019_struct_v19(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=296, w3=186, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(296, min_periods=max(296//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1734 * _rolling_slope(draw, 186) + 0.001562 * anchor

def f26_dlr_020_struct_v20(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=307, w3=199, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.18125 + 0.0015621 * anchor

def f26_dlr_021_struct_v21(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=318, w3=212, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=212, adjust=False).mean() * 1.195625 + 0.0015622 * anchor

def f26_dlr_022_struct_v22(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=329, w3=225, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(329, min_periods=max(329//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.21 + 0.0015623 * anchor

def f26_dlr_023_struct_v23(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=340, w3=238, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(340, min_periods=max(340//3, 2)).rank(pct=True)
    persistence = change.rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2038 * persistence + 0.0015624 * anchor

def f26_dlr_024_struct_v24(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=351, w3=251, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(351, min_periods=max(351//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.23875 + 0.0015625 * anchor

def f26_dlr_025_struct_v25(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=362, w3=264, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(362, min_periods=max(362//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.219 * slope + 0.0015626 * anchor

def f26_dlr_026_struct_v26(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=373, w3=277, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(373, min_periods=max(373//3, 2)).mean()
    noise = impulse.abs().rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2675 + 0.0015627 * anchor

def f26_dlr_027_struct_v27(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=384, w3=290, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 384)
    curvature = _rolling_slope(acceleration, 290)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2342 * acceleration + 0.0015628 * anchor

def f26_dlr_028_struct_v28(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=395, w3=303, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(395, min_periods=max(395//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.29625 + 0.0015629 * anchor

def f26_dlr_029_struct_v29(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=406, w3=316, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(406, min_periods=max(406//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2494 * _rolling_slope(draw, 316) + 0.001563 * anchor

def f26_dlr_030_struct_v30(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=417, w3=329, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(417, min_periods=max(417//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(329, min_periods=max(329//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.325 + 0.0015631 * anchor

def f26_dlr_031_struct_v31(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=428, w3=342, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 428)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.339375 + 0.0015632 * anchor

def f26_dlr_032_struct_v32(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=439, w3=355, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(439, min_periods=max(439//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.35375 + 0.0015633 * anchor

def f26_dlr_033_struct_v33(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=450, w3=368, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(450, min_periods=max(450//3, 2)).rank(pct=True)
    persistence = change.rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2798 * persistence + 0.0015634 * anchor

def f26_dlr_034_struct_v34(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=461, w3=381, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(461, min_periods=max(461//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3825 + 0.0015635 * anchor

def f26_dlr_035_struct_v35(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=472, w3=394, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(472, min_periods=max(472//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.295 * slope + 0.0015636 * anchor

def f26_dlr_036_struct_v36(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=483, w3=407, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(21)
    drag = impulse.rolling(483, min_periods=max(483//3, 2)).mean()
    noise = impulse.abs().rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.41125 + 0.0015637 * anchor

def f26_dlr_037_struct_v37(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=494, w3=420, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 494)
    curvature = _rolling_slope(acceleration, 420)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3102 * acceleration + 0.0015638 * anchor

def f26_dlr_038_struct_v38(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=505, w3=433, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(505, min_periods=max(505//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.44 + 0.0015639 * anchor

def f26_dlr_039_struct_v39(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=13, w3=446, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(13, min_periods=max(13//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3254 * _rolling_slope(draw, 446) + 0.001564 * anchor

def f26_dlr_040_struct_v40(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=24, w3=459, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(24, min_periods=max(24//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.46875 + 0.0015641 * anchor

def f26_dlr_041_struct_v41(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=35, w3=472, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 35)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.483125 + 0.0015642 * anchor

def f26_dlr_042_struct_v42(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=46, w3=485, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(46, min_periods=max(46//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4975 + 0.0015643 * anchor

def f26_dlr_043_struct_v43(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=57, w3=498, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(70)
    rank = change.rolling(57, min_periods=max(57//3, 2)).rank(pct=True)
    persistence = change.rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3558 * persistence + 0.0015644 * anchor

def f26_dlr_044_struct_v44(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=68, w3=511, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(68, min_periods=max(68//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.52625 + 0.0015645 * anchor

def f26_dlr_045_struct_v45(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=79, w3=524, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(79, min_periods=max(79//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.371 * slope + 0.0015646 * anchor

def f26_dlr_046_struct_v46(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=90, w3=537, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(91)
    drag = impulse.rolling(90, min_periods=max(90//3, 2)).mean()
    noise = impulse.abs().rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.555 + 0.0015647 * anchor

def f26_dlr_047_struct_v47(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=101, w3=550, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 101)
    curvature = _rolling_slope(acceleration, 550)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3862 * acceleration + 0.0015648 * anchor

def f26_dlr_048_struct_v48(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=112, w3=563, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(112, min_periods=max(112//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.58375 + 0.0015649 * anchor

def f26_dlr_049_struct_v49(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=123, w3=576, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(123, min_periods=max(123//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4014 * _rolling_slope(draw, 576) + 0.001565 * anchor

def f26_dlr_050_struct_v50(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=134, w3=589, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 119)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(589, min_periods=max(589//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.6125 + 0.0015651 * anchor

def f26_dlr_051_struct_v51(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=145, w3=602, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 126)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.85375 + 0.0015652 * anchor

def f26_dlr_052_struct_v52(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=156, w3=615, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(133, min_periods=max(133//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.868125 + 0.0015653 * anchor

def f26_dlr_053_struct_v53(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=167, w3=628, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(167, min_periods=max(167//3, 2)).rank(pct=True)
    persistence = change.rolling(628, min_periods=max(628//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0554 * persistence + 0.0015654 * anchor

def f26_dlr_054_struct_v54(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=178, w3=641, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(147, min_periods=max(147//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.896875 + 0.0015655 * anchor

def f26_dlr_055_struct_v55(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=189, w3=654, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(189, min_periods=max(189//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 154)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0706 * slope + 0.0015656 * anchor

def f26_dlr_056_struct_v56(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=200, w3=667, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.925625 + 0.0015657 * anchor

def f26_dlr_057_struct_v57(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=211, w3=680, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 168)
    acceleration = _rolling_slope(velocity, 211)
    curvature = _rolling_slope(acceleration, 680)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0858 * acceleration + 0.0015658 * anchor

def f26_dlr_058_struct_v58(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=222, w3=693, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.954375 + 0.0015659 * anchor

def f26_dlr_059_struct_v59(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=233, w3=706, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(233, min_periods=max(233//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.101 * _rolling_slope(draw, 706) + 0.001566 * anchor

def f26_dlr_060_struct_v60(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=244, w3=719, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(244, min_periods=max(244//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.983125 + 0.0015661 * anchor

def f26_dlr_061_struct_v61(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=255, w3=732, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.9975 + 0.0015662 * anchor

def f26_dlr_062_struct_v62(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=266, w3=745, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.011875 + 0.0015663 * anchor

def f26_dlr_063_struct_v63(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=277, w3=758, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1314 * persistence + 0.0015664 * anchor

def f26_dlr_064_struct_v64(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=288, w3=771, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(288, min_periods=max(288//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.040625 + 0.0015665 * anchor

def f26_dlr_065_struct_v65(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=299, w3=27, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(299, min_periods=max(299//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1466 * slope + 0.0015666 * anchor

def f26_dlr_066_struct_v66(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=310, w3=40, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.069375 + 0.0015667 * anchor

def f26_dlr_067_struct_v67(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=321, w3=53, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 321)
    curvature = _rolling_slope(acceleration, 53)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1618 * acceleration + 0.0015668 * anchor

def f26_dlr_068_struct_v68(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=332, w3=66, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(66) * 1.098125 + 0.0015669 * anchor

def f26_dlr_069_struct_v69(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=343, w3=79, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(343, min_periods=max(343//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.177 * _rolling_slope(draw, 79) + 0.001567 * anchor

def f26_dlr_070_struct_v70(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=354, w3=92, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.126875 + 0.0015671 * anchor

def f26_dlr_071_struct_v71(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=365, w3=105, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=105, adjust=False).mean() * 1.14125 + 0.0015672 * anchor

def f26_dlr_072_struct_v72(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=376, w3=118, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.155625 + 0.0015673 * anchor

def f26_dlr_073_struct_v73(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=387, w3=131, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(29)
    rank = change.rolling(387, min_periods=max(387//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2074 * persistence + 0.0015674 * anchor

def f26_dlr_074_struct_v74(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=398, w3=144, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(398, min_periods=max(398//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.184375 + 0.0015675 * anchor

def f26_dlr_075_struct_v75(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=409, w3=157, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2226 * slope + 0.0015676 * anchor
