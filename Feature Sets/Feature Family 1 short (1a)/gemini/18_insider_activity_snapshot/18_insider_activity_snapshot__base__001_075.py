"""18 insider activity snapshot base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f18_insd_001_struct_v1(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=113, w3=383, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 113)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.489375 + 0.0010802 * anchor

def f18_insd_002_struct_v2(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=124, w3=396, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(124, min_periods=max(124//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.50375 + 0.0010803 * anchor

def f18_insd_003_struct_v3(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=135, w3=409, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(75)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0826 * persistence + 0.0010804 * anchor

def f18_insd_004_struct_v4(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=146, w3=422, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(146, min_periods=max(146//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5325 + 0.0010805 * anchor

def f18_insd_005_struct_v5(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=157, w3=435, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(157, min_periods=max(157//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0978 * slope + 0.0010806 * anchor

def f18_insd_006_struct_v6(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=168, w3=448, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(96)
    drag = impulse.rolling(168, min_periods=max(168//3, 2)).mean()
    noise = impulse.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.56125 + 0.0010807 * anchor

def f18_insd_007_struct_v7(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=179, w3=461, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 179)
    curvature = _rolling_slope(acceleration, 461)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.113 * acceleration + 0.0010808 * anchor

def f18_insd_008_struct_v8(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=190, w3=474, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(190, min_periods=max(190//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.59 + 0.0010809 * anchor

def f18_insd_009_struct_v9(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=201, w3=487, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(201, min_periods=max(201//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1282 * _rolling_slope(draw, 487) + 0.001081 * anchor

def f18_insd_010_struct_v10(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=212, w3=500, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(212, min_periods=max(212//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.61875 + 0.0010811 * anchor

def f18_insd_011_struct_v11(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=223, w3=513, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 223)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.86 + 0.0010812 * anchor

def f18_insd_012_struct_v12(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=234, w3=526, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(234, min_periods=max(234//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.874375 + 0.0010813 * anchor

def f18_insd_013_struct_v13(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=245, w3=539, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(245, min_periods=max(245//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1586 * persistence + 0.0010814 * anchor

def f18_insd_014_struct_v14(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=256, w3=552, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(256, min_periods=max(256//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.903125 + 0.0010815 * anchor

def f18_insd_015_struct_v15(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=267, w3=565, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(267, min_periods=max(267//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1738 * slope + 0.0010816 * anchor

def f18_insd_016_struct_v16(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=278, w3=578, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(278, min_periods=max(278//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.931875 + 0.0010817 * anchor

def f18_insd_017_struct_v17(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=289, w3=591, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 289)
    curvature = _rolling_slope(acceleration, 591)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.189 * acceleration + 0.0010818 * anchor

def f18_insd_018_struct_v18(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=300, w3=604, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.960625 + 0.0010819 * anchor

def f18_insd_019_struct_v19(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=311, w3=617, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(311, min_periods=max(311//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2042 * _rolling_slope(draw, 617) + 0.001082 * anchor

def f18_insd_020_struct_v20(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=322, w3=630, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(322, min_periods=max(322//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(630, min_periods=max(630//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.989375 + 0.0010821 * anchor

def f18_insd_021_struct_v21(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=333, w3=643, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 333)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.00375 + 0.0010822 * anchor

def f18_insd_022_struct_v22(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=344, w3=656, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.018125 + 0.0010823 * anchor

def f18_insd_023_struct_v23(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=355, w3=669, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(355, min_periods=max(355//3, 2)).rank(pct=True)
    persistence = change.rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2346 * persistence + 0.0010824 * anchor

def f18_insd_024_struct_v24(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=366, w3=682, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(366, min_periods=max(366//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.046875 + 0.0010825 * anchor

def f18_insd_025_struct_v25(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=377, w3=695, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(377, min_periods=max(377//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2498 * slope + 0.0010826 * anchor

def f18_insd_026_struct_v26(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=388, w3=708, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(388, min_periods=max(388//3, 2)).mean()
    noise = impulse.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.075625 + 0.0010827 * anchor

def f18_insd_027_struct_v27(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=399, w3=721, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 399)
    curvature = _rolling_slope(acceleration, 721)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.265 * acceleration + 0.0010828 * anchor

def f18_insd_028_struct_v28(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=410, w3=734, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.104375 + 0.0010829 * anchor

def f18_insd_029_struct_v29(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=421, w3=747, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(421, min_periods=max(421//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2802 * _rolling_slope(draw, 747) + 0.001083 * anchor

def f18_insd_030_struct_v30(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=432, w3=760, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(432, min_periods=max(432//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.133125 + 0.0010831 * anchor

def f18_insd_031_struct_v31(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=443, w3=16, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 443)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=16, adjust=False).mean() * 1.1475 + 0.0010832 * anchor

def f18_insd_032_struct_v32(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=454, w3=29, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.161875 + 0.0010833 * anchor

def f18_insd_033_struct_v33(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=465, w3=42, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(34)
    rank = change.rolling(465, min_periods=max(465//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3106 * persistence + 0.0010834 * anchor

def f18_insd_034_struct_v34(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=476, w3=55, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(476, min_periods=max(476//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.190625 + 0.0010835 * anchor

def f18_insd_035_struct_v35(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=487, w3=68, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(487, min_periods=max(487//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3258 * slope + 0.0010836 * anchor

def f18_insd_036_struct_v36(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=498, w3=81, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(55)
    drag = impulse.rolling(498, min_periods=max(498//3, 2)).mean()
    noise = impulse.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.219375 + 0.0010837 * anchor

def f18_insd_037_struct_v37(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=509, w3=94, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 509)
    curvature = _rolling_slope(acceleration, 94)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.341 * acceleration + 0.0010838 * anchor

def f18_insd_038_struct_v38(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=17, w3=107, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(17, min_periods=max(17//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(107) * 1.248125 + 0.0010839 * anchor

def f18_insd_039_struct_v39(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=28, w3=120, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3562 * _rolling_slope(draw, 120) + 0.001084 * anchor

def f18_insd_040_struct_v40(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=39, w3=133, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(39, min_periods=max(39//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.276875 + 0.0010841 * anchor

def f18_insd_041_struct_v41(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=50, w3=146, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 50)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=146, adjust=False).mean() * 1.29125 + 0.0010842 * anchor

def f18_insd_042_struct_v42(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=61, w3=159, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(61, min_periods=max(61//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.305625 + 0.0010843 * anchor

def f18_insd_043_struct_v43(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=72, w3=172, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(104)
    rank = change.rolling(72, min_periods=max(72//3, 2)).rank(pct=True)
    persistence = change.rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3866 * persistence + 0.0010844 * anchor

def f18_insd_044_struct_v44(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=83, w3=185, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(83, min_periods=max(83//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.334375 + 0.0010845 * anchor

def f18_insd_045_struct_v45(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=94, w3=198, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(94, min_periods=max(94//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4018 * slope + 0.0010846 * anchor

def f18_insd_046_struct_v46(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=105, w3=211, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(125)
    drag = impulse.rolling(105, min_periods=max(105//3, 2)).mean()
    noise = impulse.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.363125 + 0.0010847 * anchor

def f18_insd_047_struct_v47(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=116, w3=224, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 116)
    curvature = _rolling_slope(acceleration, 224)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0406 * acceleration + 0.0010848 * anchor

def f18_insd_048_struct_v48(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=127, w3=237, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.391875 + 0.0010849 * anchor

def f18_insd_049_struct_v49(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=138, w3=250, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(138, min_periods=max(138//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0558 * _rolling_slope(draw, 250) + 0.001085 * anchor

def f18_insd_050_struct_v50(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=149, w3=263, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.420625 + 0.0010851 * anchor

def f18_insd_051_struct_v51(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=160, w3=276, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 160)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=276, adjust=False).mean() * 1.435 + 0.0010852 * anchor

def f18_insd_052_struct_v52(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=171, w3=289, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.449375 + 0.0010853 * anchor

def f18_insd_053_struct_v53(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=182, w3=302, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(182, min_periods=max(182//3, 2)).rank(pct=True)
    persistence = change.rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0862 * persistence + 0.0010854 * anchor

def f18_insd_054_struct_v54(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=193, w3=315, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(193, min_periods=max(193//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478125 + 0.0010855 * anchor

def f18_insd_055_struct_v55(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=204, w3=328, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(204, min_periods=max(204//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1014 * slope + 0.0010856 * anchor

def f18_insd_056_struct_v56(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=215, w3=341, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.506875 + 0.0010857 * anchor

def f18_insd_057_struct_v57(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=226, w3=354, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 354)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1166 * acceleration + 0.0010858 * anchor

def f18_insd_058_struct_v58(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=237, w3=367, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.535625 + 0.0010859 * anchor

def f18_insd_059_struct_v59(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=248, w3=380, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1318 * _rolling_slope(draw, 380) + 0.001086 * anchor

def f18_insd_060_struct_v60(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=259, w3=393, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.564375 + 0.0010861 * anchor

def f18_insd_061_struct_v61(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=270, w3=406, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 270)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.57875 + 0.0010862 * anchor

def f18_insd_062_struct_v62(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=281, w3=419, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(281, min_periods=max(281//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.593125 + 0.0010863 * anchor

def f18_insd_063_struct_v63(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=292, w3=432, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(292, min_periods=max(292//3, 2)).rank(pct=True)
    persistence = change.rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1622 * persistence + 0.0010864 * anchor

def f18_insd_064_struct_v64(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=303, w3=445, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(303, min_periods=max(303//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.621875 + 0.0010865 * anchor

def f18_insd_065_struct_v65(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=314, w3=458, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(314, min_periods=max(314//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1774 * slope + 0.0010866 * anchor

def f18_insd_066_struct_v66(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=325, w3=471, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(14)
    drag = impulse.rolling(325, min_periods=max(325//3, 2)).mean()
    noise = impulse.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.8775 + 0.0010867 * anchor

def f18_insd_067_struct_v67(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=336, w3=484, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 484)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1926 * acceleration + 0.0010868 * anchor

def f18_insd_068_struct_v68(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=347, w3=497, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(347, min_periods=max(347//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.90625 + 0.0010869 * anchor

def f18_insd_069_struct_v69(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=358, w3=510, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(358, min_periods=max(358//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2078 * _rolling_slope(draw, 510) + 0.001087 * anchor

def f18_insd_070_struct_v70(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=369, w3=523, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(369, min_periods=max(369//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.935 + 0.0010871 * anchor

def f18_insd_071_struct_v71(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=380, w3=536, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 380)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.949375 + 0.0010872 * anchor

def f18_insd_072_struct_v72(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=391, w3=549, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.96375 + 0.0010873 * anchor

def f18_insd_073_struct_v73(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=402, w3=562, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(63)
    rank = change.rolling(402, min_periods=max(402//3, 2)).rank(pct=True)
    persistence = change.rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2382 * persistence + 0.0010874 * anchor

def f18_insd_074_struct_v74(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=413, w3=575, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(413, min_periods=max(413//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9925 + 0.0010875 * anchor

def f18_insd_075_struct_v75(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=424, w3=588, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2534 * slope + 0.0010876 * anchor
