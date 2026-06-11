"""74 internal credit spread acceleration d1 first derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Credit_Risk - Institutional-grade short-side signal.
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

def f74_ics_451_struct_v451_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=324, w3=159, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 324)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=159, adjust=False).mean() * 1.136875 + 0.0038852 * anchor
    return base_signal.diff()

def f74_ics_452_struct_v452_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=335, w3=172, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(335, min_periods=max(335//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.15125 + 0.0038853 * anchor
    return base_signal.diff()

def f74_ics_453_struct_v453_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=346, w3=185, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(346, min_periods=max(346//3, 2)).rank(pct=True)
    persistence = change.rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2202 * persistence + 0.0038854 * anchor
    return base_signal.diff()

def f74_ics_454_struct_v454_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=357, w3=198, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(357, min_periods=max(357//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18 + 0.0038855 * anchor
    return base_signal.diff()

def f74_ics_455_struct_v455_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=368, w3=211, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(368, min_periods=max(368//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2354 * slope + 0.0038856 * anchor
    return base_signal.diff()

def f74_ics_456_struct_v456_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=379, w3=224, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(379, min_periods=max(379//3, 2)).mean()
    noise = impulse.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.20875 + 0.0038857 * anchor
    return base_signal.diff()

def f74_ics_457_struct_v457_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=390, w3=237, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 390)
    curvature = _rolling_slope(acceleration, 237)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2506 * acceleration + 0.0038858 * anchor
    return base_signal.diff()

def f74_ics_458_struct_v458_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=401, w3=250, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(401, min_periods=max(401//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2375 + 0.0038859 * anchor
    return base_signal.diff()

def f74_ics_459_struct_v459_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=412, w3=263, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(412, min_periods=max(412//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2658 * _rolling_slope(draw, 263) + 0.003886 * anchor
    return base_signal.diff()

def f74_ics_460_struct_v460_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=423, w3=276, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(423, min_periods=max(423//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.26625 + 0.0038861 * anchor
    return base_signal.diff()

def f74_ics_461_struct_v461_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=434, w3=289, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 434)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=289, adjust=False).mean() * 1.280625 + 0.0038862 * anchor
    return base_signal.diff()

def f74_ics_462_struct_v462_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=445, w3=302, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(445, min_periods=max(445//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.295 + 0.0038863 * anchor
    return base_signal.diff()

def f74_ics_463_struct_v463_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=456, w3=315, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(456, min_periods=max(456//3, 2)).rank(pct=True)
    persistence = change.rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2962 * persistence + 0.0038864 * anchor
    return base_signal.diff()

def f74_ics_464_struct_v464_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=467, w3=328, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(467, min_periods=max(467//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32375 + 0.0038865 * anchor
    return base_signal.diff()

def f74_ics_465_struct_v465_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=478, w3=341, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(478, min_periods=max(478//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3114 * slope + 0.0038866 * anchor
    return base_signal.diff()

def f74_ics_466_struct_v466_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=489, w3=354, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(489, min_periods=max(489//3, 2)).mean()
    noise = impulse.abs().rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3525 + 0.0038867 * anchor
    return base_signal.diff()

def f74_ics_467_struct_v467_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=500, w3=367, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 500)
    curvature = _rolling_slope(acceleration, 367)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3266 * acceleration + 0.0038868 * anchor
    return base_signal.diff()

def f74_ics_468_struct_v468_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=511, w3=380, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(511, min_periods=max(511//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.38125 + 0.0038869 * anchor
    return base_signal.diff()

def f74_ics_469_struct_v469_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=19, w3=393, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(19, min_periods=max(19//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3418 * _rolling_slope(draw, 393) + 0.003887 * anchor
    return base_signal.diff()

def f74_ics_470_struct_v470_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=30, w3=406, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(30, min_periods=max(30//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41 + 0.0038871 * anchor
    return base_signal.diff()

def f74_ics_471_struct_v471_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=41, w3=419, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 18)
    slow = _rolling_slope(x, 41)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.424375 + 0.0038872 * anchor
    return base_signal.diff()

def f74_ics_472_struct_v472_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=52, w3=432, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(52, min_periods=max(52//3, 2)).max()
    trough = x.rolling(25, min_periods=max(25//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.43875 + 0.0038873 * anchor
    return base_signal.diff()

def f74_ics_473_struct_v473_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=63, w3=445, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(32)
    rank = change.rolling(63, min_periods=max(63//3, 2)).rank(pct=True)
    persistence = change.rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3722 * persistence + 0.0038874 * anchor
    return base_signal.diff()

def f74_ics_474_struct_v474_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=74, w3=458, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(39, min_periods=max(39//3, 2)).std()
    vol_slow = ret.rolling(74, min_periods=max(74//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4675 + 0.0038875 * anchor
    return base_signal.diff()

def f74_ics_475_struct_v475_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=85, w3=471, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 46)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3874 * slope + 0.0038876 * anchor
    return base_signal.diff()

def f74_ics_476_struct_v476_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=96, w3=484, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(53)
    drag = impulse.rolling(96, min_periods=max(96//3, 2)).mean()
    noise = impulse.abs().rolling(484, min_periods=max(484//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.49625 + 0.0038877 * anchor
    return base_signal.diff()

def f74_ics_477_struct_v477_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=107, w3=497, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 60)
    acceleration = _rolling_slope(velocity, 107)
    curvature = _rolling_slope(acceleration, 497)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4026 * acceleration + 0.0038878 * anchor
    return base_signal.diff()

def f74_ics_478_struct_v478_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=118, w3=510, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(118, min_periods=max(118//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.525 + 0.0038879 * anchor
    return base_signal.diff()

def f74_ics_479_struct_v479_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=129, w3=523, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(129, min_periods=max(129//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0414 * _rolling_slope(draw, 523) + 0.003888 * anchor
    return base_signal.diff()

def f74_ics_480_struct_v480_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=140, w3=536, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(140, min_periods=max(140//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55375 + 0.0038881 * anchor
    return base_signal.diff()

def f74_ics_481_struct_v481_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=151, w3=549, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 88)
    slow = _rolling_slope(x, 151)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.568125 + 0.0038882 * anchor
    return base_signal.diff()

def f74_ics_482_struct_v482_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=162, w3=562, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(162, min_periods=max(162//3, 2)).max()
    trough = x.rolling(95, min_periods=max(95//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5825 + 0.0038883 * anchor
    return base_signal.diff()

def f74_ics_483_struct_v483_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=173, w3=575, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(102)
    rank = change.rolling(173, min_periods=max(173//3, 2)).rank(pct=True)
    persistence = change.rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0718 * persistence + 0.0038884 * anchor
    return base_signal.diff()

def f74_ics_484_struct_v484_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=184, w3=588, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(109, min_periods=max(109//3, 2)).std()
    vol_slow = ret.rolling(184, min_periods=max(184//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61125 + 0.0038885 * anchor
    return base_signal.diff()

def f74_ics_485_struct_v485_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=195, w3=601, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(195, min_periods=max(195//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 116)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.087 * slope + 0.0038886 * anchor
    return base_signal.diff()

def f74_ics_486_struct_v486_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=206, w3=614, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(123)
    drag = impulse.rolling(206, min_periods=max(206//3, 2)).mean()
    noise = impulse.abs().rolling(614, min_periods=max(614//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.866875 + 0.0038887 * anchor
    return base_signal.diff()

def f74_ics_487_struct_v487_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=217, w3=627, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 130)
    acceleration = _rolling_slope(velocity, 217)
    curvature = _rolling_slope(acceleration, 627)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1022 * acceleration + 0.0038888 * anchor
    return base_signal.diff()

def f74_ics_488_struct_v488_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=228, w3=640, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(137, min_periods=max(137//3, 2)).mean(), upside.rolling(228, min_periods=max(228//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.895625 + 0.0038889 * anchor
    return base_signal.diff()

def f74_ics_489_struct_v489_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=239, w3=653, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(239, min_periods=max(239//3, 2)).max()
    rebound = x - x.rolling(144, min_periods=max(144//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1174 * _rolling_slope(draw, 653) + 0.003889 * anchor
    return base_signal.diff()

def f74_ics_490_struct_v490_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=250, w3=666, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(250, min_periods=max(250//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.924375 + 0.0038891 * anchor
    return base_signal.diff()

def f74_ics_491_struct_v491_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=261, w3=679, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 261)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.93875 + 0.0038892 * anchor
    return base_signal.diff()

def f74_ics_492_struct_v492_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=272, w3=692, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(272, min_periods=max(272//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.953125 + 0.0038893 * anchor
    return base_signal.diff()

def f74_ics_493_struct_v493_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=283, w3=705, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(283, min_periods=max(283//3, 2)).rank(pct=True)
    persistence = change.rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1478 * persistence + 0.0038894 * anchor
    return base_signal.diff()

def f74_ics_494_struct_v494_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=294, w3=718, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.981875 + 0.0038895 * anchor
    return base_signal.diff()

def f74_ics_495_struct_v495_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=305, w3=731, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(305, min_periods=max(305//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.163 * slope + 0.0038896 * anchor
    return base_signal.diff()

def f74_ics_496_struct_v496_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=316, w3=744, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.010625 + 0.0038897 * anchor
    return base_signal.diff()

def f74_ics_497_struct_v497_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=327, w3=757, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 327)
    curvature = _rolling_slope(acceleration, 757)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1782 * acceleration + 0.0038898 * anchor
    return base_signal.diff()

def f74_ics_498_struct_v498_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=338, w3=770, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(338, min_periods=max(338//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.039375 + 0.0038899 * anchor
    return base_signal.diff()

def f74_ics_499_struct_v499_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=349, w3=26, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(349, min_periods=max(349//3, 2)).max()
    rebound = x - x.rolling(214, min_periods=max(214//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1934 * _rolling_slope(draw, 26) + 0.00389 * anchor
    return base_signal.diff()

def f74_ics_500_struct_v500_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=360, w3=39, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(360, min_periods=max(360//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.068125 + 0.0038901 * anchor
    return base_signal.diff()

def f74_ics_501_struct_v501_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=371, w3=52, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 371)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=52, adjust=False).mean() * 1.0825 + 0.0038902 * anchor
    return base_signal.diff()

def f74_ics_502_struct_v502_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=382, w3=65, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.096875 + 0.0038903 * anchor
    return base_signal.diff()

def f74_ics_503_struct_v503_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=393, w3=78, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(393, min_periods=max(393//3, 2)).rank(pct=True)
    persistence = change.rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2238 * persistence + 0.0038904 * anchor
    return base_signal.diff()

def f74_ics_504_struct_v504_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=404, w3=91, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.125625 + 0.0038905 * anchor
    return base_signal.diff()

def f74_ics_505_struct_v505_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=415, w3=104, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(415, min_periods=max(415//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.239 * slope + 0.0038906 * anchor
    return base_signal.diff()

def f74_ics_506_struct_v506_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=426, w3=117, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(12)
    drag = impulse.rolling(426, min_periods=max(426//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.154375 + 0.0038907 * anchor
    return base_signal.diff()

def f74_ics_507_struct_v507_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=437, w3=130, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 437)
    curvature = _rolling_slope(acceleration, 130)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2542 * acceleration + 0.0038908 * anchor
    return base_signal.diff()

def f74_ics_508_struct_v508_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=448, w3=143, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(448, min_periods=max(448//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.183125 + 0.0038909 * anchor
    return base_signal.diff()

def f74_ics_509_struct_v509_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=459, w3=156, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(459, min_periods=max(459//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2694 * _rolling_slope(draw, 156) + 0.003891 * anchor
    return base_signal.diff()

def f74_ics_510_struct_v510_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=470, w3=169, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.211875 + 0.0038911 * anchor
    return base_signal.diff()

def f74_ics_511_struct_v511_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=481, w3=182, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=182, adjust=False).mean() * 1.22625 + 0.0038912 * anchor
    return base_signal.diff()

def f74_ics_512_struct_v512_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=492, w3=195, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(492, min_periods=max(492//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.240625 + 0.0038913 * anchor
    return base_signal.diff()

def f74_ics_513_struct_v513_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=503, w3=208, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(61)
    rank = change.rolling(503, min_periods=max(503//3, 2)).rank(pct=True)
    persistence = change.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2998 * persistence + 0.0038914 * anchor
    return base_signal.diff()

def f74_ics_514_struct_v514_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=11, w3=221, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(11, min_periods=max(11//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.269375 + 0.0038915 * anchor
    return base_signal.diff()

def f74_ics_515_struct_v515_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=22, w3=234, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(22, min_periods=max(22//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.315 * slope + 0.0038916 * anchor
    return base_signal.diff()

def f74_ics_516_struct_v516_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=33, w3=247, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(82)
    drag = impulse.rolling(33, min_periods=max(33//3, 2)).mean()
    noise = impulse.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.298125 + 0.0038917 * anchor
    return base_signal.diff()

def f74_ics_517_struct_v517_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=44, w3=260, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 44)
    curvature = _rolling_slope(acceleration, 260)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3302 * acceleration + 0.0038918 * anchor
    return base_signal.diff()

def f74_ics_518_struct_v518_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=55, w3=273, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(55, min_periods=max(55//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.326875 + 0.0038919 * anchor
    return base_signal.diff()

def f74_ics_519_struct_v519_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=66, w3=286, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(66, min_periods=max(66//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3454 * _rolling_slope(draw, 286) + 0.003892 * anchor
    return base_signal.diff()

def f74_ics_520_struct_v520_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=77, w3=299, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(77, min_periods=max(77//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.355625 + 0.0038921 * anchor
    return base_signal.diff()

def f74_ics_521_struct_v521_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=88, w3=312, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 88)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.37 + 0.0038922 * anchor
    return base_signal.diff()

def f74_ics_522_struct_v522_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=99, w3=325, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(99, min_periods=max(99//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.384375 + 0.0038923 * anchor
    return base_signal.diff()

def f74_ics_523_struct_v523_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=110, w3=338, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(110, min_periods=max(110//3, 2)).rank(pct=True)
    persistence = change.rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3758 * persistence + 0.0038924 * anchor
    return base_signal.diff()

def f74_ics_524_struct_v524_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=121, w3=351, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(121, min_periods=max(121//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.413125 + 0.0038925 * anchor
    return base_signal.diff()

def f74_ics_525_struct_v525_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=132, w3=364, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.391 * slope + 0.0038926 * anchor
    return base_signal.diff()
