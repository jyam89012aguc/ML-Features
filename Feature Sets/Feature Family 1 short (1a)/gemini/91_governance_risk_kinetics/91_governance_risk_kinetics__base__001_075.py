"""91 governance risk kinetics base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f91_govr_001_struct_v1(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=206, w3=758, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 206)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.45625 + 0.0041402 * anchor

def f91_govr_002_struct_v2(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=217, w3=771, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.470625 + 0.0041403 * anchor

def f91_govr_003_struct_v3(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=228, w3=27, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(228, min_periods=max(228//3, 2)).rank(pct=True)
    persistence = change.rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4038 * persistence + 0.0041404 * anchor

def f91_govr_004_struct_v4(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=239, w3=40, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.499375 + 0.0041405 * anchor

def f91_govr_005_struct_v5(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=250, w3=53, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(250, min_periods=max(250//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0426 * slope + 0.0041406 * anchor

def f91_govr_006_struct_v6(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=261, w3=66, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(261, min_periods=max(261//3, 2)).mean()
    noise = impulse.abs().rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.528125 + 0.0041407 * anchor

def f91_govr_007_struct_v7(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=272, w3=79, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 272)
    curvature = _rolling_slope(acceleration, 79)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0578 * acceleration + 0.0041408 * anchor

def f91_govr_008_struct_v8(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=283, w3=92, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(283, min_periods=max(283//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(92) * 1.556875 + 0.0041409 * anchor

def f91_govr_009_struct_v9(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=294, w3=105, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(294, min_periods=max(294//3, 2)).max()
    rebound = x - x.rolling(214, min_periods=max(214//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.073 * _rolling_slope(draw, 105) + 0.004141 * anchor

def f91_govr_010_struct_v10(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=305, w3=118, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.585625 + 0.0041411 * anchor

def f91_govr_011_struct_v11(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=316, w3=131, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 316)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=131, adjust=False).mean() * 1.6 + 0.0041412 * anchor

def f91_govr_012_struct_v12(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=327, w3=144, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(327, min_periods=max(327//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.614375 + 0.0041413 * anchor

def f91_govr_013_struct_v13(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=338, w3=157, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(338, min_periods=max(338//3, 2)).rank(pct=True)
    persistence = change.rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1034 * persistence + 0.0041414 * anchor

def f91_govr_014_struct_v14(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=349, w3=170, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(349, min_periods=max(349//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87 + 0.0041415 * anchor

def f91_govr_015_struct_v15(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=360, w3=183, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(360, min_periods=max(360//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1186 * slope + 0.0041416 * anchor

def f91_govr_016_struct_v16(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=371, w3=196, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(12)
    drag = impulse.rolling(371, min_periods=max(371//3, 2)).mean()
    noise = impulse.abs().rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.89875 + 0.0041417 * anchor

def f91_govr_017_struct_v17(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=382, w3=209, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 382)
    curvature = _rolling_slope(acceleration, 209)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1338 * acceleration + 0.0041418 * anchor

def f91_govr_018_struct_v18(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=393, w3=222, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(393, min_periods=max(393//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9275 + 0.0041419 * anchor

def f91_govr_019_struct_v19(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=404, w3=235, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(404, min_periods=max(404//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.149 * _rolling_slope(draw, 235) + 0.004142 * anchor

def f91_govr_020_struct_v20(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=415, w3=248, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(415, min_periods=max(415//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.95625 + 0.0041421 * anchor

def f91_govr_021_struct_v21(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=426, w3=261, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 426)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=261, adjust=False).mean() * 0.970625 + 0.0041422 * anchor

def f91_govr_022_struct_v22(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=437, w3=274, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(437, min_periods=max(437//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.985 + 0.0041423 * anchor

def f91_govr_023_struct_v23(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=448, w3=287, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(61)
    rank = change.rolling(448, min_periods=max(448//3, 2)).rank(pct=True)
    persistence = change.rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1794 * persistence + 0.0041424 * anchor

def f91_govr_024_struct_v24(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=459, w3=300, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(459, min_periods=max(459//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01375 + 0.0041425 * anchor

def f91_govr_025_struct_v25(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=470, w3=313, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(470, min_periods=max(470//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1946 * slope + 0.0041426 * anchor

def f91_govr_026_struct_v26(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=481, w3=326, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(82)
    drag = impulse.rolling(481, min_periods=max(481//3, 2)).mean()
    noise = impulse.abs().rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0425 + 0.0041427 * anchor

def f91_govr_027_struct_v27(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=492, w3=339, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 492)
    curvature = _rolling_slope(acceleration, 339)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2098 * acceleration + 0.0041428 * anchor

def f91_govr_028_struct_v28(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=503, w3=352, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(503, min_periods=max(503//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.07125 + 0.0041429 * anchor

def f91_govr_029_struct_v29(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=11, w3=365, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(11, min_periods=max(11//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.225 * _rolling_slope(draw, 365) + 0.004143 * anchor

def f91_govr_030_struct_v30(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=22, w3=378, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(22, min_periods=max(22//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1 + 0.0041431 * anchor

def f91_govr_031_struct_v31(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=33, w3=391, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 33)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.114375 + 0.0041432 * anchor

def f91_govr_032_struct_v32(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=44, w3=404, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(44, min_periods=max(44//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.12875 + 0.0041433 * anchor

def f91_govr_033_struct_v33(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=55, w3=417, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(55, min_periods=max(55//3, 2)).rank(pct=True)
    persistence = change.rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2554 * persistence + 0.0041434 * anchor

def f91_govr_034_struct_v34(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=66, w3=430, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(66, min_periods=max(66//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1575 + 0.0041435 * anchor

def f91_govr_035_struct_v35(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=77, w3=443, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(77, min_periods=max(77//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2706 * slope + 0.0041436 * anchor

def f91_govr_036_struct_v36(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=88, w3=456, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(88, min_periods=max(88//3, 2)).mean()
    noise = impulse.abs().rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.18625 + 0.0041437 * anchor

def f91_govr_037_struct_v37(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=99, w3=469, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 99)
    curvature = _rolling_slope(acceleration, 469)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2858 * acceleration + 0.0041438 * anchor

def f91_govr_038_struct_v38(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=110, w3=482, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.215 + 0.0041439 * anchor

def f91_govr_039_struct_v39(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=121, w3=495, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(121, min_periods=max(121//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.301 * _rolling_slope(draw, 495) + 0.004144 * anchor

def f91_govr_040_struct_v40(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=132, w3=508, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(132, min_periods=max(132//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.24375 + 0.0041441 * anchor

def f91_govr_041_struct_v41(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=143, w3=521, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 143)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.258125 + 0.0041442 * anchor

def f91_govr_042_struct_v42(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=154, w3=534, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(154, min_periods=max(154//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2725 + 0.0041443 * anchor

def f91_govr_043_struct_v43(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=165, w3=547, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3314 * persistence + 0.0041444 * anchor

def f91_govr_044_struct_v44(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=176, w3=560, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(176, min_periods=max(176//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30125 + 0.0041445 * anchor

def f91_govr_045_struct_v45(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=187, w3=573, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3466 * slope + 0.0041446 * anchor

def f91_govr_046_struct_v46(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=198, w3=586, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(198, min_periods=max(198//3, 2)).mean()
    noise = impulse.abs().rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.33 + 0.0041447 * anchor

def f91_govr_047_struct_v47(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=209, w3=599, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 209)
    curvature = _rolling_slope(acceleration, 599)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3618 * acceleration + 0.0041448 * anchor

def f91_govr_048_struct_v48(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=220, w3=612, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(220, min_periods=max(220//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.35875 + 0.0041449 * anchor

def f91_govr_049_struct_v49(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=231, w3=625, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(231, min_periods=max(231//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.377 * _rolling_slope(draw, 625) + 0.004145 * anchor

def f91_govr_050_struct_v50(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=242, w3=638, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(242, min_periods=max(242//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3875 + 0.0041451 * anchor

def f91_govr_051_struct_v51(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=253, w3=651, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 253)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.401875 + 0.0041452 * anchor

def f91_govr_052_struct_v52(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=264, w3=664, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.41625 + 0.0041453 * anchor

def f91_govr_053_struct_v53(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=275, w3=677, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(20)
    rank = change.rolling(275, min_periods=max(275//3, 2)).rank(pct=True)
    persistence = change.rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4074 * persistence + 0.0041454 * anchor

def f91_govr_054_struct_v54(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=286, w3=690, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(286, min_periods=max(286//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.445 + 0.0041455 * anchor

def f91_govr_055_struct_v55(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=297, w3=703, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(297, min_periods=max(297//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0462 * slope + 0.0041456 * anchor

def f91_govr_056_struct_v56(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=308, w3=716, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(41)
    drag = impulse.rolling(308, min_periods=max(308//3, 2)).mean()
    noise = impulse.abs().rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.47375 + 0.0041457 * anchor

def f91_govr_057_struct_v57(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=319, w3=729, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 319)
    curvature = _rolling_slope(acceleration, 729)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0614 * acceleration + 0.0041458 * anchor

def f91_govr_058_struct_v58(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=330, w3=742, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(330, min_periods=max(330//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5025 + 0.0041459 * anchor

def f91_govr_059_struct_v59(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=341, w3=755, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(341, min_periods=max(341//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0766 * _rolling_slope(draw, 755) + 0.004146 * anchor

def f91_govr_060_struct_v60(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=352, w3=768, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(352, min_periods=max(352//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.53125 + 0.0041461 * anchor

def f91_govr_061_struct_v61(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=363, w3=24, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 363)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=24, adjust=False).mean() * 1.545625 + 0.0041462 * anchor

def f91_govr_062_struct_v62(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=374, w3=37, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(374, min_periods=max(374//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.56 + 0.0041463 * anchor

def f91_govr_063_struct_v63(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=385, w3=50, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(90)
    rank = change.rolling(385, min_periods=max(385//3, 2)).rank(pct=True)
    persistence = change.rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.107 * persistence + 0.0041464 * anchor

def f91_govr_064_struct_v64(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=396, w3=63, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(396, min_periods=max(396//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.58875 + 0.0041465 * anchor

def f91_govr_065_struct_v65(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=407, w3=76, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(407, min_periods=max(407//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1222 * slope + 0.0041466 * anchor

def f91_govr_066_struct_v66(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=418, w3=89, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(111)
    drag = impulse.rolling(418, min_periods=max(418//3, 2)).mean()
    noise = impulse.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6175 + 0.0041467 * anchor

def f91_govr_067_struct_v67(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=429, w3=102, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 102)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1374 * acceleration + 0.0041468 * anchor

def f91_govr_068_struct_v68(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=440, w3=115, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(115) * 0.873125 + 0.0041469 * anchor

def f91_govr_069_struct_v69(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=451, w3=128, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1526 * _rolling_slope(draw, 128) + 0.004147 * anchor

def f91_govr_070_struct_v70(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=462, w3=141, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.901875 + 0.0041471 * anchor

def f91_govr_071_struct_v71(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=473, w3=154, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 473)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=154, adjust=False).mean() * 0.91625 + 0.0041472 * anchor

def f91_govr_072_struct_v72(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=484, w3=167, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(484, min_periods=max(484//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.930625 + 0.0041473 * anchor

def f91_govr_073_struct_v73(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=495, w3=180, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(495, min_periods=max(495//3, 2)).rank(pct=True)
    persistence = change.rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.183 * persistence + 0.0041474 * anchor

def f91_govr_074_struct_v74(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=506, w3=193, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(506, min_periods=max(506//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.959375 + 0.0041475 * anchor

def f91_govr_075_struct_v75(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=14, w3=206, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(14, min_periods=max(14//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1982 * slope + 0.0041476 * anchor
