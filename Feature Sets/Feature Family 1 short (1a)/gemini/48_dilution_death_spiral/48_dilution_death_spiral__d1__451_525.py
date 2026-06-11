"""48 dilution death spiral d1 first derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f48_dds_451_struct_v451_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=415, w3=494, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 130)
    slow = _rolling_slope(x, 415)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.87375 + 0.0029852 * anchor
    return base_signal.diff()

def f48_dds_452_struct_v452_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=426, w3=507, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(426, min_periods=max(426//3, 2)).max()
    trough = x.rolling(137, min_periods=max(137//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.888125 + 0.0029853 * anchor
    return base_signal.diff()

def f48_dds_453_struct_v453_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=437, w3=520, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.325 * persistence + 0.0029854 * anchor
    return base_signal.diff()

def f48_dds_454_struct_v454_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=448, w3=533, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(151, min_periods=max(151//3, 2)).std()
    vol_slow = ret.rolling(448, min_periods=max(448//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.916875 + 0.0029855 * anchor
    return base_signal.diff()

def f48_dds_455_struct_v455_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=459, w3=546, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(459, min_periods=max(459//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 158)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3402 * slope + 0.0029856 * anchor
    return base_signal.diff()

def f48_dds_456_struct_v456_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=470, w3=559, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(470, min_periods=max(470//3, 2)).mean()
    noise = impulse.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.945625 + 0.0029857 * anchor
    return base_signal.diff()

def f48_dds_457_struct_v457_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=481, w3=572, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 172)
    acceleration = _rolling_slope(velocity, 481)
    curvature = _rolling_slope(acceleration, 572)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3554 * acceleration + 0.0029858 * anchor
    return base_signal.diff()

def f48_dds_458_struct_v458_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=492, w3=585, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(492, min_periods=max(492//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.974375 + 0.0029859 * anchor
    return base_signal.diff()

def f48_dds_459_struct_v459_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=503, w3=598, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3706 * _rolling_slope(draw, 598) + 0.002986 * anchor
    return base_signal.diff()

def f48_dds_460_struct_v460_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=11, w3=611, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 193)
    baseline = trend.rolling(11, min_periods=max(11//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.003125 + 0.0029861 * anchor
    return base_signal.diff()

def f48_dds_461_struct_v461_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=22, w3=624, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 22)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.0175 + 0.0029862 * anchor
    return base_signal.diff()

def f48_dds_462_struct_v462_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=33, w3=637, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.031875 + 0.0029863 * anchor
    return base_signal.diff()

def f48_dds_463_struct_v463_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=44, w3=650, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(44, min_periods=max(44//3, 2)).rank(pct=True)
    persistence = change.rolling(650, min_periods=max(650//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.401 * persistence + 0.0029864 * anchor
    return base_signal.diff()

def f48_dds_464_struct_v464_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=55, w3=663, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.060625 + 0.0029865 * anchor
    return base_signal.diff()

def f48_dds_465_struct_v465_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=66, w3=676, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(66, min_periods=max(66//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0398 * slope + 0.0029866 * anchor
    return base_signal.diff()

def f48_dds_466_struct_v466_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=77, w3=689, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(77, min_periods=max(77//3, 2)).mean()
    noise = impulse.abs().rolling(689, min_periods=max(689//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.089375 + 0.0029867 * anchor
    return base_signal.diff()

def f48_dds_467_struct_v467_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=88, w3=702, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 88)
    curvature = _rolling_slope(acceleration, 702)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.055 * acceleration + 0.0029868 * anchor
    return base_signal.diff()

def f48_dds_468_struct_v468_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=99, w3=715, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.118125 + 0.0029869 * anchor
    return base_signal.diff()

def f48_dds_469_struct_v469_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=110, w3=728, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0702 * _rolling_slope(draw, 728) + 0.002987 * anchor
    return base_signal.diff()

def f48_dds_470_struct_v470_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=121, w3=741, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(121, min_periods=max(121//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.146875 + 0.0029871 * anchor
    return base_signal.diff()

def f48_dds_471_struct_v471_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=132, w3=754, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 132)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.16125 + 0.0029872 * anchor
    return base_signal.diff()

def f48_dds_472_struct_v472_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=143, w3=767, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(143, min_periods=max(143//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.175625 + 0.0029873 * anchor
    return base_signal.diff()

def f48_dds_473_struct_v473_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=154, w3=23, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(33)
    rank = change.rolling(154, min_periods=max(154//3, 2)).rank(pct=True)
    persistence = change.rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1006 * persistence + 0.0029874 * anchor
    return base_signal.diff()

def f48_dds_474_struct_v474_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=165, w3=36, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.204375 + 0.0029875 * anchor
    return base_signal.diff()

def f48_dds_475_struct_v475_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=176, w3=49, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(176, min_periods=max(176//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1158 * slope + 0.0029876 * anchor
    return base_signal.diff()

def f48_dds_476_struct_v476_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=187, w3=62, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(54)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(62, min_periods=max(62//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.233125 + 0.0029877 * anchor
    return base_signal.diff()

def f48_dds_477_struct_v477_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=198, w3=75, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 75)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.131 * acceleration + 0.0029878 * anchor
    return base_signal.diff()

def f48_dds_478_struct_v478_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=209, w3=88, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(88) * 1.261875 + 0.0029879 * anchor
    return base_signal.diff()

def f48_dds_479_struct_v479_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=220, w3=101, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(220, min_periods=max(220//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1462 * _rolling_slope(draw, 101) + 0.002988 * anchor
    return base_signal.diff()

def f48_dds_480_struct_v480_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=231, w3=114, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.290625 + 0.0029881 * anchor
    return base_signal.diff()

def f48_dds_481_struct_v481_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=242, w3=127, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=127, adjust=False).mean() * 1.305 + 0.0029882 * anchor
    return base_signal.diff()

def f48_dds_482_struct_v482_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=253, w3=140, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.319375 + 0.0029883 * anchor
    return base_signal.diff()

def f48_dds_483_struct_v483_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=264, w3=153, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(103)
    rank = change.rolling(264, min_periods=max(264//3, 2)).rank(pct=True)
    persistence = change.rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1766 * persistence + 0.0029884 * anchor
    return base_signal.diff()

def f48_dds_484_struct_v484_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=275, w3=166, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.348125 + 0.0029885 * anchor
    return base_signal.diff()

def f48_dds_485_struct_v485_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=286, w3=179, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1918 * slope + 0.0029886 * anchor
    return base_signal.diff()

def f48_dds_486_struct_v486_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=297, w3=192, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(124)
    drag = impulse.rolling(297, min_periods=max(297//3, 2)).mean()
    noise = impulse.abs().rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.376875 + 0.0029887 * anchor
    return base_signal.diff()

def f48_dds_487_struct_v487_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=308, w3=205, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 205)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.207 * acceleration + 0.0029888 * anchor
    return base_signal.diff()

def f48_dds_488_struct_v488_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=319, w3=218, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(319, min_periods=max(319//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.405625 + 0.0029889 * anchor
    return base_signal.diff()

def f48_dds_489_struct_v489_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=330, w3=231, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2222 * _rolling_slope(draw, 231) + 0.002989 * anchor
    return base_signal.diff()

def f48_dds_490_struct_v490_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=341, w3=244, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.434375 + 0.0029891 * anchor
    return base_signal.diff()

def f48_dds_491_struct_v491_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=352, w3=257, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=257, adjust=False).mean() * 1.44875 + 0.0029892 * anchor
    return base_signal.diff()

def f48_dds_492_struct_v492_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=363, w3=270, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(363, min_periods=max(363//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.463125 + 0.0029893 * anchor
    return base_signal.diff()

def f48_dds_493_struct_v493_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=374, w3=283, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2526 * persistence + 0.0029894 * anchor
    return base_signal.diff()

def f48_dds_494_struct_v494_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=385, w3=296, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(385, min_periods=max(385//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.491875 + 0.0029895 * anchor
    return base_signal.diff()

def f48_dds_495_struct_v495_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=396, w3=309, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2678 * slope + 0.0029896 * anchor
    return base_signal.diff()

def f48_dds_496_struct_v496_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=407, w3=322, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(407, min_periods=max(407//3, 2)).mean()
    noise = impulse.abs().rolling(322, min_periods=max(322//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.520625 + 0.0029897 * anchor
    return base_signal.diff()

def f48_dds_497_struct_v497_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=418, w3=335, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 335)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283 * acceleration + 0.0029898 * anchor
    return base_signal.diff()

def f48_dds_498_struct_v498_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=429, w3=348, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.549375 + 0.0029899 * anchor
    return base_signal.diff()

def f48_dds_499_struct_v499_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=440, w3=361, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2982 * _rolling_slope(draw, 361) + 0.00299 * anchor
    return base_signal.diff()

def f48_dds_500_struct_v500_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=451, w3=374, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.578125 + 0.0029901 * anchor
    return base_signal.diff()

def f48_dds_501_struct_v501_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=462, w3=387, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.5925 + 0.0029902 * anchor
    return base_signal.diff()

def f48_dds_502_struct_v502_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=236, w2=473, w3=400, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(473, min_periods=max(473//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.606875 + 0.0029903 * anchor
    return base_signal.diff()

def f48_dds_503_struct_v503_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=484, w3=413, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(484, min_periods=max(484//3, 2)).rank(pct=True)
    persistence = change.rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3286 * persistence + 0.0029904 * anchor
    return base_signal.diff()

def f48_dds_504_struct_v504_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=495, w3=426, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8625 + 0.0029905 * anchor
    return base_signal.diff()

def f48_dds_505_struct_v505_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=506, w3=439, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3438 * slope + 0.0029906 * anchor
    return base_signal.diff()

def f48_dds_506_struct_v506_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=14, w3=452, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(13)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(452, min_periods=max(452//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.89125 + 0.0029907 * anchor
    return base_signal.diff()

def f48_dds_507_struct_v507_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=25, w3=465, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 465)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.359 * acceleration + 0.0029908 * anchor
    return base_signal.diff()

def f48_dds_508_struct_v508_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=36, w3=478, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(36, min_periods=max(36//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.92 + 0.0029909 * anchor
    return base_signal.diff()

def f48_dds_509_struct_v509_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=47, w3=491, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3742 * _rolling_slope(draw, 491) + 0.002991 * anchor
    return base_signal.diff()

def f48_dds_510_struct_v510_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=58, w3=504, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.94875 + 0.0029911 * anchor
    return base_signal.diff()

def f48_dds_511_struct_v511_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=69, w3=517, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 69)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.963125 + 0.0029912 * anchor
    return base_signal.diff()

def f48_dds_512_struct_v512_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=80, w3=530, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9775 + 0.0029913 * anchor
    return base_signal.diff()

def f48_dds_513_struct_v513_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=91, w3=543, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(62)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4046 * persistence + 0.0029914 * anchor
    return base_signal.diff()

def f48_dds_514_struct_v514_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=69, w2=102, w3=556, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.00625 + 0.0029915 * anchor
    return base_signal.diff()

def f48_dds_515_struct_v515_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=76, w2=113, w3=569, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0434 * slope + 0.0029916 * anchor
    return base_signal.diff()

def f48_dds_516_struct_v516_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=83, w2=124, w3=582, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(83)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.035 + 0.0029917 * anchor
    return base_signal.diff()

def f48_dds_517_struct_v517_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=90, w2=135, w3=595, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 595)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0586 * acceleration + 0.0029918 * anchor
    return base_signal.diff()

def f48_dds_518_struct_v518_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=97, w2=146, w3=608, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(146, min_periods=max(146//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.06375 + 0.0029919 * anchor
    return base_signal.diff()

def f48_dds_519_struct_v519_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=104, w2=157, w3=621, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(157, min_periods=max(157//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0738 * _rolling_slope(draw, 621) + 0.002992 * anchor
    return base_signal.diff()

def f48_dds_520_struct_v520_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=111, w2=168, w3=634, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(168, min_periods=max(168//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0925 + 0.0029921 * anchor
    return base_signal.diff()

def f48_dds_521_struct_v521_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=118, w2=179, w3=647, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 179)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.106875 + 0.0029922 * anchor
    return base_signal.diff()

def f48_dds_522_struct_v522_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=125, w2=190, w3=660, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(190, min_periods=max(190//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.12125 + 0.0029923 * anchor
    return base_signal.diff()

def f48_dds_523_struct_v523_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=132, w2=201, w3=673, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(201, min_periods=max(201//3, 2)).rank(pct=True)
    persistence = change.rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1042 * persistence + 0.0029924 * anchor
    return base_signal.diff()

def f48_dds_524_struct_v524_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=139, w2=212, w3=686, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(212, min_periods=max(212//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.15 + 0.0029925 * anchor
    return base_signal.diff()

def f48_dds_525_struct_v525_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=146, w2=223, w3=699, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(223, min_periods=max(223//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1194 * slope + 0.0029926 * anchor
    return base_signal.diff()
