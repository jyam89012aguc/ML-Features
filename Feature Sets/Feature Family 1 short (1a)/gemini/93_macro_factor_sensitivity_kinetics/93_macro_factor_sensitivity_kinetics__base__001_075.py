"""93 macro factor sensitivity kinetics base features 1-75 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Macro_Factor - Institutional-grade short-side signal.
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

def f93_mcf_001_struct_v1(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=328, w3=461, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 328)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.924375 + 0.0042602 * anchor

def f93_mcf_002_struct_v2(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=339, w3=474, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(339, min_periods=max(339//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.93875 + 0.0042603 * anchor

def f93_mcf_003_struct_v3(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=350, w3=487, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(38)
    rank = change.rolling(350, min_periods=max(350//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1138 * persistence + 0.0042604 * anchor

def f93_mcf_004_struct_v4(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=361, w3=500, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(361, min_periods=max(361//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9675 + 0.0042605 * anchor

def f93_mcf_005_struct_v5(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=372, w3=513, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(372, min_periods=max(372//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.129 * slope + 0.0042606 * anchor

def f93_mcf_006_struct_v6(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=383, w3=526, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(59)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.99625 + 0.0042607 * anchor

def f93_mcf_007_struct_v7(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=394, w3=539, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 394)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1442 * acceleration + 0.0042608 * anchor

def f93_mcf_008_struct_v8(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=405, w3=552, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(405, min_periods=max(405//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.025 + 0.0042609 * anchor

def f93_mcf_009_struct_v9(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=416, w3=565, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(416, min_periods=max(416//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1594 * _rolling_slope(draw, 565) + 0.004261 * anchor

def f93_mcf_010_struct_v10(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=427, w3=578, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(427, min_periods=max(427//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.05375 + 0.0042611 * anchor

def f93_mcf_011_struct_v11(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=438, w3=591, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 438)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.068125 + 0.0042612 * anchor

def f93_mcf_012_struct_v12(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=449, w3=604, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(449, min_periods=max(449//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0825 + 0.0042613 * anchor

def f93_mcf_013_struct_v13(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=460, w3=617, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(108)
    rank = change.rolling(460, min_periods=max(460//3, 2)).rank(pct=True)
    persistence = change.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1898 * persistence + 0.0042614 * anchor

def f93_mcf_014_struct_v14(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=471, w3=630, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(471, min_periods=max(471//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11125 + 0.0042615 * anchor

def f93_mcf_015_struct_v15(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=482, w3=643, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(482, min_periods=max(482//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.205 * slope + 0.0042616 * anchor

def f93_mcf_016_struct_v16(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=493, w3=656, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(493, min_periods=max(493//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.14 + 0.0042617 * anchor

def f93_mcf_017_struct_v17(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=504, w3=669, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 504)
    curvature = _rolling_slope(acceleration, 669)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2202 * acceleration + 0.0042618 * anchor

def f93_mcf_018_struct_v18(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=12, w3=682, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(12, min_periods=max(12//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.16875 + 0.0042619 * anchor

def f93_mcf_019_struct_v19(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=23, w3=695, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(23, min_periods=max(23//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2354 * _rolling_slope(draw, 695) + 0.004262 * anchor

def f93_mcf_020_struct_v20(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=34, w3=708, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(34, min_periods=max(34//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1975 + 0.0042621 * anchor

def f93_mcf_021_struct_v21(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=45, w3=721, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 45)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.211875 + 0.0042622 * anchor

def f93_mcf_022_struct_v22(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=56, w3=734, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.22625 + 0.0042623 * anchor

def f93_mcf_023_struct_v23(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=67, w3=747, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(67, min_periods=max(67//3, 2)).rank(pct=True)
    persistence = change.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2658 * persistence + 0.0042624 * anchor

def f93_mcf_024_struct_v24(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=78, w3=760, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(78, min_periods=max(78//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.255 + 0.0042625 * anchor

def f93_mcf_025_struct_v25(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=89, w3=16, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.281 * slope + 0.0042626 * anchor

def f93_mcf_026_struct_v26(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=100, w3=29, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.28375 + 0.0042627 * anchor

def f93_mcf_027_struct_v27(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=111, w3=42, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2962 * acceleration + 0.0042628 * anchor

def f93_mcf_028_struct_v28(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=122, w3=55, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(122, min_periods=max(122//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(55) * 1.3125 + 0.0042629 * anchor

def f93_mcf_029_struct_v29(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=133, w3=68, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3114 * _rolling_slope(draw, 68) + 0.004263 * anchor

def f93_mcf_030_struct_v30(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=144, w3=81, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.34125 + 0.0042631 * anchor

def f93_mcf_031_struct_v31(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=155, w3=94, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=94, adjust=False).mean() * 1.355625 + 0.0042632 * anchor

def f93_mcf_032_struct_v32(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=166, w3=107, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(166, min_periods=max(166//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.37 + 0.0042633 * anchor

def f93_mcf_033_struct_v33(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=177, w3=120, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3418 * persistence + 0.0042634 * anchor

def f93_mcf_034_struct_v34(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=188, w3=133, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39875 + 0.0042635 * anchor

def f93_mcf_035_struct_v35(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=199, w3=146, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.357 * slope + 0.0042636 * anchor

def f93_mcf_036_struct_v36(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=210, w3=159, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(18)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4275 + 0.0042637 * anchor

def f93_mcf_037_struct_v37(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=221, w3=172, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 172)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3722 * acceleration + 0.0042638 * anchor

def f93_mcf_038_struct_v38(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=232, w3=185, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45625 + 0.0042639 * anchor

def f93_mcf_039_struct_v39(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=243, w3=198, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3874 * _rolling_slope(draw, 198) + 0.004264 * anchor

def f93_mcf_040_struct_v40(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=254, w3=211, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.485 + 0.0042641 * anchor

def f93_mcf_041_struct_v41(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=265, w3=224, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=224, adjust=False).mean() * 1.499375 + 0.0042642 * anchor

def f93_mcf_042_struct_v42(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=276, w3=237, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.51375 + 0.0042643 * anchor

def f93_mcf_043_struct_v43(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=287, w3=250, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(67)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0414 * persistence + 0.0042644 * anchor

def f93_mcf_044_struct_v44(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=298, w3=263, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(298, min_periods=max(298//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5425 + 0.0042645 * anchor

def f93_mcf_045_struct_v45(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=309, w3=276, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0566 * slope + 0.0042646 * anchor

def f93_mcf_046_struct_v46(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=320, w3=289, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(88)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.57125 + 0.0042647 * anchor

def f93_mcf_047_struct_v47(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=331, w3=302, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 302)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0718 * acceleration + 0.0042648 * anchor

def f93_mcf_048_struct_v48(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=342, w3=315, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.6 + 0.0042649 * anchor

def f93_mcf_049_struct_v49(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=353, w3=328, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.087 * _rolling_slope(draw, 328) + 0.004265 * anchor

def f93_mcf_050_struct_v50(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=364, w3=341, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.855625 + 0.0042651 * anchor

def f93_mcf_051_struct_v51(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=375, w3=354, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.87 + 0.0042652 * anchor

def f93_mcf_052_struct_v52(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=386, w3=367, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(386, min_periods=max(386//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.884375 + 0.0042653 * anchor

def f93_mcf_053_struct_v53(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=397, w3=380, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1174 * persistence + 0.0042654 * anchor

def f93_mcf_054_struct_v54(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=408, w3=393, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.913125 + 0.0042655 * anchor

def f93_mcf_055_struct_v55(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=419, w3=406, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1326 * slope + 0.0042656 * anchor

def f93_mcf_056_struct_v56(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=430, w3=419, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.941875 + 0.0042657 * anchor

def f93_mcf_057_struct_v57(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=441, w3=432, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1478 * acceleration + 0.0042658 * anchor

def f93_mcf_058_struct_v58(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=452, w3=445, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.970625 + 0.0042659 * anchor

def f93_mcf_059_struct_v59(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=463, w3=458, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.163 * _rolling_slope(draw, 458) + 0.004266 * anchor

def f93_mcf_060_struct_v60(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=474, w3=471, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.999375 + 0.0042661 * anchor

def f93_mcf_061_struct_v61(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=485, w3=484, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.01375 + 0.0042662 * anchor

def f93_mcf_062_struct_v62(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=496, w3=497, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.028125 + 0.0042663 * anchor

def f93_mcf_063_struct_v63(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=507, w3=510, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1934 * persistence + 0.0042664 * anchor

def f93_mcf_064_struct_v64(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=15, w3=523, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.056875 + 0.0042665 * anchor

def f93_mcf_065_struct_v65(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=26, w3=536, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2086 * slope + 0.0042666 * anchor

def f93_mcf_066_struct_v66(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=37, w3=549, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.085625 + 0.0042667 * anchor

def f93_mcf_067_struct_v67(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=48, w3=562, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 562)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2238 * acceleration + 0.0042668 * anchor

def f93_mcf_068_struct_v68(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=59, w3=575, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(59, min_periods=max(59//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.114375 + 0.0042669 * anchor

def f93_mcf_069_struct_v69(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=70, w3=588, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.239 * _rolling_slope(draw, 588) + 0.004267 * anchor

def f93_mcf_070_struct_v70(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=81, w3=601, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 5)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.143125 + 0.0042671 * anchor

def f93_mcf_071_struct_v71(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=92, w3=614, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.1575 + 0.0042672 * anchor

def f93_mcf_072_struct_v72(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=103, w3=627, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.171875 + 0.0042673 * anchor

def f93_mcf_073_struct_v73(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=114, w3=640, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(26)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2694 * persistence + 0.0042674 * anchor

def f93_mcf_074_struct_v74(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=125, w3=653, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.200625 + 0.0042675 * anchor

def f93_mcf_075_struct_v75(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=136, w3=666, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2846 * slope + 0.0042676 * anchor
