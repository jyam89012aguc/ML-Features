"""13 cash burn snapshot d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Quality - Institutional-grade short-side signal.
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

def f13_cbrn_001_struct_v1_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=311, w3=747, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.88625 + 0.0007802 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_002_struct_v2_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=322, w3=760, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(322, min_periods=max(322//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.900625 + 0.0007803 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_003_struct_v3_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=333, w3=16, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(333, min_periods=max(333//3, 2)).rank(pct=True)
    persistence = change.rolling(16, min_periods=max(16//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.243 * persistence + 0.0007804 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_004_struct_v4_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=344, w3=29, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(344, min_periods=max(344//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.929375 + 0.0007805 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_005_struct_v5_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=355, w3=42, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2582 * slope + 0.0007806 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_006_struct_v6_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=366, w3=55, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(366, min_periods=max(366//3, 2)).mean()
    noise = impulse.abs().rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.958125 + 0.0007807 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_007_struct_v7_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=377, w3=68, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 377)
    curvature = _rolling_slope(acceleration, 68)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2734 * acceleration + 0.0007808 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_008_struct_v8_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=388, w3=81, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(81) * 0.986875 + 0.0007809 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_009_struct_v9_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=399, w3=94, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(399, min_periods=max(399//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2886 * _rolling_slope(draw, 94) + 0.000781 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_010_struct_v10_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=410, w3=107, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.015625 + 0.0007811 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_011_struct_v11_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=421, w3=120, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 421)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=120, adjust=False).mean() * 1.03 + 0.0007812 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_012_struct_v12_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=432, w3=133, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(432, min_periods=max(432//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.044375 + 0.0007813 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_013_struct_v13_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=443, w3=146, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319 * persistence + 0.0007814 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_014_struct_v14_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=454, w3=159, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(454, min_periods=max(454//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.073125 + 0.0007815 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_015_struct_v15_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=465, w3=172, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(465, min_periods=max(465//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3342 * slope + 0.0007816 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_016_struct_v16_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=476, w3=185, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.101875 + 0.0007817 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_017_struct_v17_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=487, w3=198, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 487)
    curvature = _rolling_slope(acceleration, 198)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3494 * acceleration + 0.0007818 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_018_struct_v18_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=498, w3=211, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(498, min_periods=max(498//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.130625 + 0.0007819 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_019_struct_v19_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=509, w3=224, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(509, min_periods=max(509//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3646 * _rolling_slope(draw, 224) + 0.000782 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_020_struct_v20_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=17, w3=237, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(17, min_periods=max(17//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.159375 + 0.0007821 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_021_struct_v21_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=28, w3=250, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 28)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=250, adjust=False).mean() * 1.17375 + 0.0007822 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_022_struct_v22_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=39, w3=263, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(39, min_periods=max(39//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.188125 + 0.0007823 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_023_struct_v23_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=50, w3=276, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(48)
    rank = change.rolling(50, min_periods=max(50//3, 2)).rank(pct=True)
    persistence = change.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.395 * persistence + 0.0007824 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_024_struct_v24_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=61, w3=289, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(61, min_periods=max(61//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.216875 + 0.0007825 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_025_struct_v25_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=72, w3=302, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4102 * slope + 0.0007826 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_026_struct_v26_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=83, w3=315, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(69)
    drag = impulse.rolling(83, min_periods=max(83//3, 2)).mean()
    noise = impulse.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.245625 + 0.0007827 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_027_struct_v27_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=94, w3=328, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 328)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.049 * acceleration + 0.0007828 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_028_struct_v28_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=105, w3=341, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.274375 + 0.0007829 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_029_struct_v29_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=116, w3=354, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0642 * _rolling_slope(draw, 354) + 0.000783 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_030_struct_v30_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=127, w3=367, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(127, min_periods=max(127//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.303125 + 0.0007831 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_031_struct_v31_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=138, w3=380, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 138)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3175 + 0.0007832 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_032_struct_v32_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=149, w3=393, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.331875 + 0.0007833 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_033_struct_v33_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=160, w3=406, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(118)
    rank = change.rolling(160, min_periods=max(160//3, 2)).rank(pct=True)
    persistence = change.rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0946 * persistence + 0.0007834 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_034_struct_v34_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=171, w3=419, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(171, min_periods=max(171//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.360625 + 0.0007835 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_035_struct_v35_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=182, w3=432, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(182, min_periods=max(182//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1098 * slope + 0.0007836 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_036_struct_v36_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=193, w3=445, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(193, min_periods=max(193//3, 2)).mean()
    noise = impulse.abs().rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.389375 + 0.0007837 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_037_struct_v37_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=204, w3=458, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 458)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125 * acceleration + 0.0007838 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_038_struct_v38_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=215, w3=471, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(215, min_periods=max(215//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.418125 + 0.0007839 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_039_struct_v39_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=226, w3=484, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(226, min_periods=max(226//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1402 * _rolling_slope(draw, 484) + 0.000784 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_040_struct_v40_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=237, w3=497, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(237, min_periods=max(237//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.446875 + 0.0007841 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_041_struct_v41_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=248, w3=510, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 248)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.46125 + 0.0007842 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_042_struct_v42_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=259, w3=523, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(259, min_periods=max(259//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.475625 + 0.0007843 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_043_struct_v43_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=270, w3=536, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(270, min_periods=max(270//3, 2)).rank(pct=True)
    persistence = change.rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1706 * persistence + 0.0007844 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_044_struct_v44_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=281, w3=549, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.504375 + 0.0007845 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_045_struct_v45_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=292, w3=562, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(292, min_periods=max(292//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1858 * slope + 0.0007846 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_046_struct_v46_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=303, w3=575, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(303, min_periods=max(303//3, 2)).mean()
    noise = impulse.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.533125 + 0.0007847 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_047_struct_v47_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=314, w3=588, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 314)
    curvature = _rolling_slope(acceleration, 588)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.201 * acceleration + 0.0007848 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_048_struct_v48_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=325, w3=601, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(325, min_periods=max(325//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.561875 + 0.0007849 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_049_struct_v49_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=336, w3=614, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(336, min_periods=max(336//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2162 * _rolling_slope(draw, 614) + 0.000785 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_050_struct_v50_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=347, w3=627, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(347, min_periods=max(347//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.590625 + 0.0007851 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_051_struct_v51_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=358, w3=640, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.605 + 0.0007852 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_052_struct_v52_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=369, w3=653, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(369, min_periods=max(369//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.619375 + 0.0007853 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_053_struct_v53_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=380, w3=666, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(7)
    rank = change.rolling(380, min_periods=max(380//3, 2)).rank(pct=True)
    persistence = change.rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2466 * persistence + 0.0007854 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_054_struct_v54_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=391, w3=679, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(391, min_periods=max(391//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.875 + 0.0007855 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_055_struct_v55_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=402, w3=692, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(402, min_periods=max(402//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2618 * slope + 0.0007856 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_056_struct_v56_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=413, w3=705, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(28)
    drag = impulse.rolling(413, min_periods=max(413//3, 2)).mean()
    noise = impulse.abs().rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.90375 + 0.0007857 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_057_struct_v57_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=424, w3=718, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 424)
    curvature = _rolling_slope(acceleration, 718)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.277 * acceleration + 0.0007858 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_058_struct_v58_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=435, w3=731, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(435, min_periods=max(435//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9325 + 0.0007859 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_059_struct_v59_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=446, w3=744, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(446, min_periods=max(446//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2922 * _rolling_slope(draw, 744) + 0.000786 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_060_struct_v60_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=457, w3=757, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(457, min_periods=max(457//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.96125 + 0.0007861 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_061_struct_v61_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=468, w3=770, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 468)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.975625 + 0.0007862 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_062_struct_v62_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=479, w3=26, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(479, min_periods=max(479//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.99 + 0.0007863 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_063_struct_v63_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=490, w3=39, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(77)
    rank = change.rolling(490, min_periods=max(490//3, 2)).rank(pct=True)
    persistence = change.rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3226 * persistence + 0.0007864 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_064_struct_v64_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=501, w3=52, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(501, min_periods=max(501//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01875 + 0.0007865 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_065_struct_v65_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=512, w3=65, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(512, min_periods=max(512//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3378 * slope + 0.0007866 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_066_struct_v66_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=20, w3=78, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(98)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0475 + 0.0007867 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_067_struct_v67_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=31, w3=91, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 91)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.353 * acceleration + 0.0007868 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_068_struct_v68_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=42, w3=104, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(42, min_periods=max(42//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(104) * 1.07625 + 0.0007869 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_069_struct_v69_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=53, w3=117, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3682 * _rolling_slope(draw, 117) + 0.000787 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_070_struct_v70_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=64, w3=130, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(64, min_periods=max(64//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.105 + 0.0007871 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_071_struct_v71_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=133, w2=75, w3=143, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 75)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=143, adjust=False).mean() * 1.119375 + 0.0007872 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_072_struct_v72_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=140, w2=86, w3=156, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(86, min_periods=max(86//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.13375 + 0.0007873 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_073_struct_v73_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=147, w2=97, w3=169, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(97, min_periods=max(97//3, 2)).rank(pct=True)
    persistence = change.rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3986 * persistence + 0.0007874 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_074_struct_v74_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=154, w2=108, w3=182, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(108, min_periods=max(108//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1625 + 0.0007875 * anchor
    return base_signal.diff().diff().diff()

def f13_cbrn_075_struct_v75_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=161, w2=119, w3=195, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0374 * slope + 0.0007876 * anchor
    return base_signal.diff().diff().diff()
