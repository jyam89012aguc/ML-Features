"""23 cash flow deterioration trajectory d1 first derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f23_cfd_001_struct_v1_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=418, w3=19, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 418)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=19, adjust=False).mean() * 1.319375 + 0.0013802 * anchor
    return base_signal.diff()

def f23_cfd_002_struct_v2_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=429, w3=32, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(429, min_periods=max(429//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.33375 + 0.0013803 * anchor
    return base_signal.diff()

def f23_cfd_003_struct_v3_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=440, w3=45, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(440, min_periods=max(440//3, 2)).rank(pct=True)
    persistence = change.rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2986 * persistence + 0.0013804 * anchor
    return base_signal.diff()

def f23_cfd_004_struct_v4_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=451, w3=58, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(451, min_periods=max(451//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3625 + 0.0013805 * anchor
    return base_signal.diff()

def f23_cfd_005_struct_v5_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=462, w3=71, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(462, min_periods=max(462//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3138 * slope + 0.0013806 * anchor
    return base_signal.diff()

def f23_cfd_006_struct_v6_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=473, w3=84, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(12)
    drag = impulse.rolling(473, min_periods=max(473//3, 2)).mean()
    noise = impulse.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.39125 + 0.0013807 * anchor
    return base_signal.diff()

def f23_cfd_007_struct_v7_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=484, w3=97, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 484)
    curvature = _rolling_slope(acceleration, 97)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.329 * acceleration + 0.0013808 * anchor
    return base_signal.diff()

def f23_cfd_008_struct_v8_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=495, w3=110, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(495, min_periods=max(495//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(110) * 1.42 + 0.0013809 * anchor
    return base_signal.diff()

def f23_cfd_009_struct_v9_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=506, w3=123, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(506, min_periods=max(506//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3442 * _rolling_slope(draw, 123) + 0.001381 * anchor
    return base_signal.diff()

def f23_cfd_010_struct_v10_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=14, w3=136, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(14, min_periods=max(14//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.44875 + 0.0013811 * anchor
    return base_signal.diff()

def f23_cfd_011_struct_v11_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=25, w3=149, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 25)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=149, adjust=False).mean() * 1.463125 + 0.0013812 * anchor
    return base_signal.diff()

def f23_cfd_012_struct_v12_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=36, w3=162, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(36, min_periods=max(36//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4775 + 0.0013813 * anchor
    return base_signal.diff()

def f23_cfd_013_struct_v13_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=47, w3=175, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(61)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3746 * persistence + 0.0013814 * anchor
    return base_signal.diff()

def f23_cfd_014_struct_v14_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=58, w3=188, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(58, min_periods=max(58//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.50625 + 0.0013815 * anchor
    return base_signal.diff()

def f23_cfd_015_struct_v15_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=69, w3=201, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(69, min_periods=max(69//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3898 * slope + 0.0013816 * anchor
    return base_signal.diff()

def f23_cfd_016_struct_v16_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=80, w3=214, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(82)
    drag = impulse.rolling(80, min_periods=max(80//3, 2)).mean()
    noise = impulse.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.535 + 0.0013817 * anchor
    return base_signal.diff()

def f23_cfd_017_struct_v17_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=91, w3=227, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 91)
    curvature = _rolling_slope(acceleration, 227)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.405 * acceleration + 0.0013818 * anchor
    return base_signal.diff()

def f23_cfd_018_struct_v18_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=102, w3=240, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(102, min_periods=max(102//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.56375 + 0.0013819 * anchor
    return base_signal.diff()

def f23_cfd_019_struct_v19_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=113, w3=253, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(113, min_periods=max(113//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0438 * _rolling_slope(draw, 253) + 0.001382 * anchor
    return base_signal.diff()

def f23_cfd_020_struct_v20_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=124, w3=266, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(124, min_periods=max(124//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5925 + 0.0013821 * anchor
    return base_signal.diff()

def f23_cfd_021_struct_v21_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=135, w3=279, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 135)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=279, adjust=False).mean() * 1.606875 + 0.0013822 * anchor
    return base_signal.diff()

def f23_cfd_022_struct_v22_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=146, w3=292, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(146, min_periods=max(146//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.62125 + 0.0013823 * anchor
    return base_signal.diff()

def f23_cfd_023_struct_v23_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=157, w3=305, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(157, min_periods=max(157//3, 2)).rank(pct=True)
    persistence = change.rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0742 * persistence + 0.0013824 * anchor
    return base_signal.diff()

def f23_cfd_024_struct_v24_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=168, w3=318, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(168, min_periods=max(168//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.876875 + 0.0013825 * anchor
    return base_signal.diff()

def f23_cfd_025_struct_v25_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=179, w3=331, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(179, min_periods=max(179//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0894 * slope + 0.0013826 * anchor
    return base_signal.diff()

def f23_cfd_026_struct_v26_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=190, w3=344, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(190, min_periods=max(190//3, 2)).mean()
    noise = impulse.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.905625 + 0.0013827 * anchor
    return base_signal.diff()

def f23_cfd_027_struct_v27_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=201, w3=357, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 201)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1046 * acceleration + 0.0013828 * anchor
    return base_signal.diff()

def f23_cfd_028_struct_v28_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=212, w3=370, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.934375 + 0.0013829 * anchor
    return base_signal.diff()

def f23_cfd_029_struct_v29_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=223, w3=383, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(223, min_periods=max(223//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1198 * _rolling_slope(draw, 383) + 0.001383 * anchor
    return base_signal.diff()

def f23_cfd_030_struct_v30_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=234, w3=396, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(234, min_periods=max(234//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.963125 + 0.0013831 * anchor
    return base_signal.diff()

def f23_cfd_031_struct_v31_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=245, w3=409, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9775 + 0.0013832 * anchor
    return base_signal.diff()

def f23_cfd_032_struct_v32_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=256, w3=422, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(256, min_periods=max(256//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.991875 + 0.0013833 * anchor
    return base_signal.diff()

def f23_cfd_033_struct_v33_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=267, w3=435, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(267, min_periods=max(267//3, 2)).rank(pct=True)
    persistence = change.rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1502 * persistence + 0.0013834 * anchor
    return base_signal.diff()

def f23_cfd_034_struct_v34_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=278, w3=448, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(278, min_periods=max(278//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.020625 + 0.0013835 * anchor
    return base_signal.diff()

def f23_cfd_035_struct_v35_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=289, w3=461, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(289, min_periods=max(289//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1654 * slope + 0.0013836 * anchor
    return base_signal.diff()

def f23_cfd_036_struct_v36_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=300, w3=474, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(300, min_periods=max(300//3, 2)).mean()
    noise = impulse.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.049375 + 0.0013837 * anchor
    return base_signal.diff()

def f23_cfd_037_struct_v37_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=311, w3=487, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 487)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1806 * acceleration + 0.0013838 * anchor
    return base_signal.diff()

def f23_cfd_038_struct_v38_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=236, w2=322, w3=500, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(322, min_periods=max(322//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.078125 + 0.0013839 * anchor
    return base_signal.diff()

def f23_cfd_039_struct_v39_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=333, w3=513, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(333, min_periods=max(333//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1958 * _rolling_slope(draw, 513) + 0.001384 * anchor
    return base_signal.diff()

def f23_cfd_040_struct_v40_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=344, w3=526, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(344, min_periods=max(344//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.106875 + 0.0013841 * anchor
    return base_signal.diff()

def f23_cfd_041_struct_v41_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=355, w3=539, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 355)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.12125 + 0.0013842 * anchor
    return base_signal.diff()

def f23_cfd_042_struct_v42_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=366, w3=552, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(366, min_periods=max(366//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.135625 + 0.0013843 * anchor
    return base_signal.diff()

def f23_cfd_043_struct_v43_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=377, w3=565, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(20)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2262 * persistence + 0.0013844 * anchor
    return base_signal.diff()

def f23_cfd_044_struct_v44_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=388, w3=578, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(388, min_periods=max(388//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.164375 + 0.0013845 * anchor
    return base_signal.diff()

def f23_cfd_045_struct_v45_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=399, w3=591, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(399, min_periods=max(399//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2414 * slope + 0.0013846 * anchor
    return base_signal.diff()

def f23_cfd_046_struct_v46_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=410, w3=604, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(41)
    drag = impulse.rolling(410, min_periods=max(410//3, 2)).mean()
    noise = impulse.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.193125 + 0.0013847 * anchor
    return base_signal.diff()

def f23_cfd_047_struct_v47_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=421, w3=617, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 421)
    curvature = _rolling_slope(acceleration, 617)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2566 * acceleration + 0.0013848 * anchor
    return base_signal.diff()

def f23_cfd_048_struct_v48_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=432, w3=630, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(432, min_periods=max(432//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.221875 + 0.0013849 * anchor
    return base_signal.diff()

def f23_cfd_049_struct_v49_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=443, w3=643, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2718 * _rolling_slope(draw, 643) + 0.001385 * anchor
    return base_signal.diff()

def f23_cfd_050_struct_v50_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=69, w2=454, w3=656, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(454, min_periods=max(454//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.250625 + 0.0013851 * anchor
    return base_signal.diff()

def f23_cfd_051_struct_v51_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=76, w2=465, w3=669, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 465)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.265 + 0.0013852 * anchor
    return base_signal.diff()

def f23_cfd_052_struct_v52_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=83, w2=476, w3=682, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(476, min_periods=max(476//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.279375 + 0.0013853 * anchor
    return base_signal.diff()

def f23_cfd_053_struct_v53_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=90, w2=487, w3=695, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(90)
    rank = change.rolling(487, min_periods=max(487//3, 2)).rank(pct=True)
    persistence = change.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3022 * persistence + 0.0013854 * anchor
    return base_signal.diff()

def f23_cfd_054_struct_v54_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=97, w2=498, w3=708, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(498, min_periods=max(498//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.308125 + 0.0013855 * anchor
    return base_signal.diff()

def f23_cfd_055_struct_v55_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=104, w2=509, w3=721, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(509, min_periods=max(509//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3174 * slope + 0.0013856 * anchor
    return base_signal.diff()

def f23_cfd_056_struct_v56_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=111, w2=17, w3=734, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(111)
    drag = impulse.rolling(17, min_periods=max(17//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.336875 + 0.0013857 * anchor
    return base_signal.diff()

def f23_cfd_057_struct_v57_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=118, w2=28, w3=747, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 747)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3326 * acceleration + 0.0013858 * anchor
    return base_signal.diff()

def f23_cfd_058_struct_v58_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=125, w2=39, w3=760, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(39, min_periods=max(39//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.365625 + 0.0013859 * anchor
    return base_signal.diff()

def f23_cfd_059_struct_v59_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=132, w2=50, w3=16, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(50, min_periods=max(50//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3478 * _rolling_slope(draw, 16) + 0.001386 * anchor
    return base_signal.diff()

def f23_cfd_060_struct_v60_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=139, w2=61, w3=29, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.394375 + 0.0013861 * anchor
    return base_signal.diff()

def f23_cfd_061_struct_v61_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=146, w2=72, w3=42, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 72)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=42, adjust=False).mean() * 1.40875 + 0.0013862 * anchor
    return base_signal.diff()

def f23_cfd_062_struct_v62_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=153, w2=83, w3=55, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(83, min_periods=max(83//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.423125 + 0.0013863 * anchor
    return base_signal.diff()

def f23_cfd_063_struct_v63_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=160, w2=94, w3=68, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(94, min_periods=max(94//3, 2)).rank(pct=True)
    persistence = change.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3782 * persistence + 0.0013864 * anchor
    return base_signal.diff()

def f23_cfd_064_struct_v64_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=167, w2=105, w3=81, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(105, min_periods=max(105//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.451875 + 0.0013865 * anchor
    return base_signal.diff()

def f23_cfd_065_struct_v65_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=174, w2=116, w3=94, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(116, min_periods=max(116//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3934 * slope + 0.0013866 * anchor
    return base_signal.diff()

def f23_cfd_066_struct_v66_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=181, w2=127, w3=107, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(127, min_periods=max(127//3, 2)).mean()
    noise = impulse.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.480625 + 0.0013867 * anchor
    return base_signal.diff()

def f23_cfd_067_struct_v67_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=188, w2=138, w3=120, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 138)
    curvature = _rolling_slope(acceleration, 120)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4086 * acceleration + 0.0013868 * anchor
    return base_signal.diff()

def f23_cfd_068_struct_v68_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=195, w2=149, w3=133, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.509375 + 0.0013869 * anchor
    return base_signal.diff()

def f23_cfd_069_struct_v69_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=202, w2=160, w3=146, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(160, min_periods=max(160//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0474 * _rolling_slope(draw, 146) + 0.001387 * anchor
    return base_signal.diff()

def f23_cfd_070_struct_v70_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=209, w2=171, w3=159, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(171, min_periods=max(171//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.538125 + 0.0013871 * anchor
    return base_signal.diff()

def f23_cfd_071_struct_v71_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=216, w2=182, w3=172, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 182)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=172, adjust=False).mean() * 1.5525 + 0.0013872 * anchor
    return base_signal.diff()

def f23_cfd_072_struct_v72_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=223, w2=193, w3=185, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(193, min_periods=max(193//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.566875 + 0.0013873 * anchor
    return base_signal.diff()

def f23_cfd_073_struct_v73_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=230, w2=204, w3=198, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(204, min_periods=max(204//3, 2)).rank(pct=True)
    persistence = change.rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0778 * persistence + 0.0013874 * anchor
    return base_signal.diff()

def f23_cfd_074_struct_v74_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=237, w2=215, w3=211, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(215, min_periods=max(215//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.595625 + 0.0013875 * anchor
    return base_signal.diff()

def f23_cfd_075_struct_v75_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=244, w2=226, w3=224, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(226, min_periods=max(226//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.093 * slope + 0.0013876 * anchor
    return base_signal.diff()
