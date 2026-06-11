"""39 hidden loss emergence d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f39_hle_451_struct_v451_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=47, w2=308, w3=465, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 308)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.21375 + 0.0023852 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_452_struct_v452_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=54, w2=319, w3=478, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(319, min_periods=max(319//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.228125 + 0.0023853 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_453_struct_v453_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=61, w2=330, w3=491, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(61)
    rank = change.rolling(330, min_periods=max(330//3, 2)).rank(pct=True)
    persistence = change.rolling(491, min_periods=max(491//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2694 * persistence + 0.0023854 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_454_struct_v454_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=68, w2=341, w3=504, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(341, min_periods=max(341//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.256875 + 0.0023855 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_455_struct_v455_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=75, w2=352, w3=517, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(352, min_periods=max(352//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2846 * slope + 0.0023856 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_456_struct_v456_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=82, w2=363, w3=530, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(82)
    drag = impulse.rolling(363, min_periods=max(363//3, 2)).mean()
    noise = impulse.abs().rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.285625 + 0.0023857 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_457_struct_v457_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=89, w2=374, w3=543, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 374)
    curvature = _rolling_slope(acceleration, 543)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2998 * acceleration + 0.0023858 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_458_struct_v458_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=96, w2=385, w3=556, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(385, min_periods=max(385//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.314375 + 0.0023859 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_459_struct_v459_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=103, w2=396, w3=569, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(396, min_periods=max(396//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315 * _rolling_slope(draw, 569) + 0.002386 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_460_struct_v460_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=110, w2=407, w3=582, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(407, min_periods=max(407//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.343125 + 0.0023861 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_461_struct_v461_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=117, w2=418, w3=595, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 418)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3575 + 0.0023862 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_462_struct_v462_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=124, w2=429, w3=608, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(429, min_periods=max(429//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.371875 + 0.0023863 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_463_struct_v463_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=131, w2=440, w3=621, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(440, min_periods=max(440//3, 2)).rank(pct=True)
    persistence = change.rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3454 * persistence + 0.0023864 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_464_struct_v464_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=138, w2=451, w3=634, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(451, min_periods=max(451//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.400625 + 0.0023865 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_465_struct_v465_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=462, w3=647, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(462, min_periods=max(462//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3606 * slope + 0.0023866 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_466_struct_v466_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=473, w3=660, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(473, min_periods=max(473//3, 2)).mean()
    noise = impulse.abs().rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.429375 + 0.0023867 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_467_struct_v467_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=484, w3=673, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 484)
    curvature = _rolling_slope(acceleration, 673)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3758 * acceleration + 0.0023868 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_468_struct_v468_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=495, w3=686, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(495, min_periods=max(495//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.458125 + 0.0023869 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_469_struct_v469_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=506, w3=699, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(506, min_periods=max(506//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.391 * _rolling_slope(draw, 699) + 0.002387 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_470_struct_v470_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=14, w3=712, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(14, min_periods=max(14//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.486875 + 0.0023871 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_471_struct_v471_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=25, w3=725, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 25)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.50125 + 0.0023872 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_472_struct_v472_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=36, w3=738, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(36, min_periods=max(36//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.515625 + 0.0023873 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_473_struct_v473_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=47, w3=751, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.045 * persistence + 0.0023874 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_474_struct_v474_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=58, w3=764, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(58, min_periods=max(58//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.544375 + 0.0023875 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_475_struct_v475_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=69, w3=20, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(69, min_periods=max(69//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0602 * slope + 0.0023876 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_476_struct_v476_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=80, w3=33, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(80, min_periods=max(80//3, 2)).mean()
    noise = impulse.abs().rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.573125 + 0.0023877 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_477_struct_v477_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=91, w3=46, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 91)
    curvature = _rolling_slope(acceleration, 46)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0754 * acceleration + 0.0023878 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_478_struct_v478_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=102, w3=59, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(102, min_periods=max(102//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(59) * 1.601875 + 0.0023879 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_479_struct_v479_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=113, w3=72, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(113, min_periods=max(113//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0906 * _rolling_slope(draw, 72) + 0.002388 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_480_struct_v480_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=124, w3=85, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(124, min_periods=max(124//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8575 + 0.0023881 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_481_struct_v481_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=135, w3=98, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 135)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=98, adjust=False).mean() * 0.871875 + 0.0023882 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_482_struct_v482_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=146, w3=111, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(146, min_periods=max(146//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.88625 + 0.0023883 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_483_struct_v483_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=157, w3=124, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(20)
    rank = change.rolling(157, min_periods=max(157//3, 2)).rank(pct=True)
    persistence = change.rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.121 * persistence + 0.0023884 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_484_struct_v484_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=168, w3=137, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(168, min_periods=max(168//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.915 + 0.0023885 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_485_struct_v485_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=179, w3=150, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(179, min_periods=max(179//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1362 * slope + 0.0023886 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_486_struct_v486_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=190, w3=163, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(41)
    drag = impulse.rolling(190, min_periods=max(190//3, 2)).mean()
    noise = impulse.abs().rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94375 + 0.0023887 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_487_struct_v487_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=201, w3=176, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 201)
    curvature = _rolling_slope(acceleration, 176)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1514 * acceleration + 0.0023888 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_488_struct_v488_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=212, w3=189, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9725 + 0.0023889 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_489_struct_v489_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=223, w3=202, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(223, min_periods=max(223//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1666 * _rolling_slope(draw, 202) + 0.002389 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_490_struct_v490_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=234, w3=215, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(234, min_periods=max(234//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.00125 + 0.0023891 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_491_struct_v491_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=245, w3=228, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=228, adjust=False).mean() * 1.015625 + 0.0023892 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_492_struct_v492_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=256, w3=241, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(256, min_periods=max(256//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03 + 0.0023893 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_493_struct_v493_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=267, w3=254, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(90)
    rank = change.rolling(267, min_periods=max(267//3, 2)).rank(pct=True)
    persistence = change.rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.197 * persistence + 0.0023894 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_494_struct_v494_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=278, w3=267, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(278, min_periods=max(278//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.05875 + 0.0023895 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_495_struct_v495_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=289, w3=280, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(289, min_periods=max(289//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2122 * slope + 0.0023896 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_496_struct_v496_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=300, w3=293, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(111)
    drag = impulse.rolling(300, min_periods=max(300//3, 2)).mean()
    noise = impulse.abs().rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0875 + 0.0023897 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_497_struct_v497_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=311, w3=306, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 306)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2274 * acceleration + 0.0023898 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_498_struct_v498_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=322, w3=319, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(322, min_periods=max(322//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.11625 + 0.0023899 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_499_struct_v499_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=333, w3=332, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(333, min_periods=max(333//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2426 * _rolling_slope(draw, 332) + 0.00239 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_500_struct_v500_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=344, w3=345, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(344, min_periods=max(344//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.145 + 0.0023901 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_501_struct_v501_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=355, w3=358, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 355)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.159375 + 0.0023902 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_502_struct_v502_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=366, w3=371, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(366, min_periods=max(366//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17375 + 0.0023903 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_503_struct_v503_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=377, w3=384, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.273 * persistence + 0.0023904 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_504_struct_v504_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=388, w3=397, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(388, min_periods=max(388//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2025 + 0.0023905 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_505_struct_v505_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=399, w3=410, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(399, min_periods=max(399//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2882 * slope + 0.0023906 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_506_struct_v506_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=410, w3=423, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(410, min_periods=max(410//3, 2)).mean()
    noise = impulse.abs().rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.23125 + 0.0023907 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_507_struct_v507_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=421, w3=436, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 421)
    curvature = _rolling_slope(acceleration, 436)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3034 * acceleration + 0.0023908 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_508_struct_v508_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=432, w3=449, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(432, min_periods=max(432//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.26 + 0.0023909 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_509_struct_v509_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=443, w3=462, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3186 * _rolling_slope(draw, 462) + 0.002391 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_510_struct_v510_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=454, w3=475, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(454, min_periods=max(454//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(475, min_periods=max(475//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28875 + 0.0023911 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_511_struct_v511_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=465, w3=488, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 465)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.303125 + 0.0023912 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_512_struct_v512_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=476, w3=501, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(476, min_periods=max(476//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3175 + 0.0023913 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_513_struct_v513_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=487, w3=514, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(487, min_periods=max(487//3, 2)).rank(pct=True)
    persistence = change.rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.349 * persistence + 0.0023914 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_514_struct_v514_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=498, w3=527, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(498, min_periods=max(498//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34625 + 0.0023915 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_515_struct_v515_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=509, w3=540, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(509, min_periods=max(509//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3642 * slope + 0.0023916 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_516_struct_v516_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=17, w3=553, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(17, min_periods=max(17//3, 2)).mean()
    noise = impulse.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.375 + 0.0023917 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_517_struct_v517_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=28, w3=566, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 566)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3794 * acceleration + 0.0023918 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_518_struct_v518_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=39, w3=579, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(39, min_periods=max(39//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.40375 + 0.0023919 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_519_struct_v519_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=50, w3=592, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(50, min_periods=max(50//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3946 * _rolling_slope(draw, 592) + 0.002392 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_520_struct_v520_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=61, w3=605, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4325 + 0.0023921 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_521_struct_v521_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=72, w3=618, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 72)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.446875 + 0.0023922 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_522_struct_v522_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=83, w3=631, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(83, min_periods=max(83//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.46125 + 0.0023923 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_523_struct_v523_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=94, w3=644, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(49)
    rank = change.rolling(94, min_periods=max(94//3, 2)).rank(pct=True)
    persistence = change.rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0486 * persistence + 0.0023924 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_524_struct_v524_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=105, w3=657, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(105, min_periods=max(105//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49 + 0.0023925 * anchor
    return base_signal.diff().diff().diff()

def f39_hle_525_struct_v525_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=116, w3=670, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(116, min_periods=max(116//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0638 * slope + 0.0023926 * anchor
    return base_signal.diff().diff().diff()
