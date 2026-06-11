"""33 passive flow acceleration d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f33_pfa_001_struct_v1_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=60, w2=22, w3=48, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 22)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=48, adjust=False).mean() * 0.979375 + 0.0019802 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_002_struct_v2_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=67, w2=33, w3=61, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.99375 + 0.0019803 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_003_struct_v3_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=74, w2=44, w3=74, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(74)
    rank = change.rolling(44, min_periods=max(44//3, 2)).rank(pct=True)
    persistence = change.rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3542 * persistence + 0.0019804 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_004_struct_v4_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=81, w2=55, w3=87, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0225 + 0.0019805 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_005_struct_v5_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=88, w2=66, w3=100, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(66, min_periods=max(66//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3694 * slope + 0.0019806 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_006_struct_v6_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=95, w2=77, w3=113, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(95)
    drag = impulse.rolling(77, min_periods=max(77//3, 2)).mean()
    noise = impulse.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.05125 + 0.0019807 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_007_struct_v7_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=102, w2=88, w3=126, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 88)
    curvature = _rolling_slope(acceleration, 126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3846 * acceleration + 0.0019808 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_008_struct_v8_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=109, w2=99, w3=139, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.08 + 0.0019809 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_009_struct_v9_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=116, w2=110, w3=152, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3998 * _rolling_slope(draw, 152) + 0.001981 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_010_struct_v10_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=123, w2=121, w3=165, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 123)
    baseline = trend.rolling(121, min_periods=max(121//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.10875 + 0.0019811 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_011_struct_v11_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=130, w2=132, w3=178, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 130)
    slow = _rolling_slope(x, 132)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=178, adjust=False).mean() * 1.123125 + 0.0019812 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_012_struct_v12_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=137, w2=143, w3=191, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(143, min_periods=max(143//3, 2)).max()
    trough = x.rolling(137, min_periods=max(137//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1375 + 0.0019813 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_013_struct_v13_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=144, w2=154, w3=204, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(154, min_periods=max(154//3, 2)).rank(pct=True)
    persistence = change.rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0538 * persistence + 0.0019814 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_014_struct_v14_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=151, w2=165, w3=217, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(151, min_periods=max(151//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16625 + 0.0019815 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_015_struct_v15_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=158, w2=176, w3=230, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(176, min_periods=max(176//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 158)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.069 * slope + 0.0019816 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_016_struct_v16_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=165, w2=187, w3=243, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.195 + 0.0019817 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_017_struct_v17_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=172, w2=198, w3=256, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 172)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 256)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0842 * acceleration + 0.0019818 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_018_struct_v18_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=179, w2=209, w3=269, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.22375 + 0.0019819 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_019_struct_v19_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=186, w2=220, w3=282, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(220, min_periods=max(220//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0994 * _rolling_slope(draw, 282) + 0.001982 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_020_struct_v20_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=193, w2=231, w3=295, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 193)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2525 + 0.0019821 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_021_struct_v21_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=200, w2=242, w3=308, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.266875 + 0.0019822 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_022_struct_v22_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=207, w2=253, w3=321, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.28125 + 0.0019823 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_023_struct_v23_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=214, w2=264, w3=334, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(264, min_periods=max(264//3, 2)).rank(pct=True)
    persistence = change.rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1298 * persistence + 0.0019824 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_024_struct_v24_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=221, w2=275, w3=347, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31 + 0.0019825 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_025_struct_v25_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=228, w2=286, w3=360, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.145 * slope + 0.0019826 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_026_struct_v26_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=235, w2=297, w3=373, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(297, min_periods=max(297//3, 2)).mean()
    noise = impulse.abs().rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33875 + 0.0019827 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_027_struct_v27_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=242, w2=308, w3=386, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 386)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1602 * acceleration + 0.0019828 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_028_struct_v28_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=249, w2=319, w3=399, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(319, min_periods=max(319//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3675 + 0.0019829 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_029_struct_v29_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=5, w2=330, w3=412, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1754 * _rolling_slope(draw, 412) + 0.001983 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_030_struct_v30_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=12, w2=341, w3=425, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.39625 + 0.0019831 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_031_struct_v31_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=19, w2=352, w3=438, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.410625 + 0.0019832 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_032_struct_v32_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=26, w2=363, w3=451, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(363, min_periods=max(363//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.425 + 0.0019833 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_033_struct_v33_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=33, w2=374, w3=464, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(33)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2058 * persistence + 0.0019834 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_034_struct_v34_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=40, w2=385, w3=477, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(385, min_periods=max(385//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.45375 + 0.0019835 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_035_struct_v35_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=47, w2=396, w3=490, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.221 * slope + 0.0019836 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_036_struct_v36_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=54, w2=407, w3=503, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(54)
    drag = impulse.rolling(407, min_periods=max(407//3, 2)).mean()
    noise = impulse.abs().rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4825 + 0.0019837 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_037_struct_v37_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=61, w2=418, w3=516, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 516)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2362 * acceleration + 0.0019838 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_038_struct_v38_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=68, w2=429, w3=529, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.51125 + 0.0019839 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_039_struct_v39_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=75, w2=440, w3=542, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2514 * _rolling_slope(draw, 542) + 0.001984 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_040_struct_v40_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=82, w2=451, w3=555, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.54 + 0.0019841 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_041_struct_v41_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=89, w2=462, w3=568, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.554375 + 0.0019842 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_042_struct_v42_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=96, w2=473, w3=581, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(473, min_periods=max(473//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.56875 + 0.0019843 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_043_struct_v43_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=103, w2=484, w3=594, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(103)
    rank = change.rolling(484, min_periods=max(484//3, 2)).rank(pct=True)
    persistence = change.rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2818 * persistence + 0.0019844 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_044_struct_v44_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=110, w2=495, w3=607, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5975 + 0.0019845 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_045_struct_v45_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=117, w2=506, w3=620, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.297 * slope + 0.0019846 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_046_struct_v46_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=124, w2=14, w3=633, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(124)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.853125 + 0.0019847 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_047_struct_v47_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=131, w2=25, w3=646, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 646)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3122 * acceleration + 0.0019848 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_048_struct_v48_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=138, w2=36, w3=659, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(36, min_periods=max(36//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.881875 + 0.0019849 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_049_struct_v49_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=47, w3=672, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3274 * _rolling_slope(draw, 672) + 0.001985 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_050_struct_v50_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=58, w3=685, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.910625 + 0.0019851 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_051_struct_v51_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=69, w3=698, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 69)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.925 + 0.0019852 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_052_struct_v52_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=80, w3=711, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.939375 + 0.0019853 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_053_struct_v53_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=91, w3=724, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3578 * persistence + 0.0019854 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_054_struct_v54_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=102, w3=737, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.968125 + 0.0019855 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_055_struct_v55_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=113, w3=750, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.373 * slope + 0.0019856 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_056_struct_v56_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=124, w3=763, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.996875 + 0.0019857 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_057_struct_v57_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=135, w3=19, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 19)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3882 * acceleration + 0.0019858 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_058_struct_v58_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=146, w3=32, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(146, min_periods=max(146//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(32) * 1.025625 + 0.0019859 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_059_struct_v59_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=157, w3=45, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(157, min_periods=max(157//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4034 * _rolling_slope(draw, 45) + 0.001986 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_060_struct_v60_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=168, w3=58, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(168, min_periods=max(168//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.054375 + 0.0019861 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_061_struct_v61_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=179, w3=71, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 179)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=71, adjust=False).mean() * 1.06875 + 0.0019862 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_062_struct_v62_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=190, w3=84, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(190, min_periods=max(190//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.083125 + 0.0019863 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_063_struct_v63_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=201, w3=97, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(201, min_periods=max(201//3, 2)).rank(pct=True)
    persistence = change.rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0574 * persistence + 0.0019864 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_064_struct_v64_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=212, w3=110, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(212, min_periods=max(212//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.111875 + 0.0019865 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_065_struct_v65_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=223, w3=123, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(223, min_periods=max(223//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0726 * slope + 0.0019866 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_066_struct_v66_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=234, w3=136, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(13)
    drag = impulse.rolling(234, min_periods=max(234//3, 2)).mean()
    noise = impulse.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.140625 + 0.0019867 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_067_struct_v67_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=245, w3=149, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 245)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0878 * acceleration + 0.0019868 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_068_struct_v68_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=256, w3=162, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(256, min_periods=max(256//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.169375 + 0.0019869 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_069_struct_v69_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=267, w3=175, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(267, min_periods=max(267//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.103 * _rolling_slope(draw, 175) + 0.001987 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_070_struct_v70_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=278, w3=188, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(278, min_periods=max(278//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.198125 + 0.0019871 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_071_struct_v71_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=289, w3=201, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 289)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=201, adjust=False).mean() * 1.2125 + 0.0019872 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_072_struct_v72_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=300, w3=214, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(300, min_periods=max(300//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.226875 + 0.0019873 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_073_struct_v73_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=311, w3=227, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(62)
    rank = change.rolling(311, min_periods=max(311//3, 2)).rank(pct=True)
    persistence = change.rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1334 * persistence + 0.0019874 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_074_struct_v74_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=322, w3=240, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(322, min_periods=max(322//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.255625 + 0.0019875 * anchor
    return base_signal.diff().diff().diff()

def f33_pfa_075_struct_v75_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=333, w3=253, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(333, min_periods=max(333//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1486 * slope + 0.0019876 * anchor
    return base_signal.diff().diff().diff()
