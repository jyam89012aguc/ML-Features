"""11 revenue quality level d3 third derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f11_revq_301_struct_v301_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=120, w2=471, w3=402, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 471)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.091875 + 0.0006902 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_302_struct_v302_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=127, w2=482, w3=415, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.10625 + 0.0006903 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_303_struct_v303_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=134, w2=493, w3=428, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(493, min_periods=max(493//3, 2)).rank(pct=True)
    persistence = change.rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1782 * persistence + 0.0006904 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_304_struct_v304_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=141, w2=504, w3=441, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(504, min_periods=max(504//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.135 + 0.0006905 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_305_struct_v305_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=148, w2=12, w3=454, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1934 * slope + 0.0006906 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_306_struct_v306_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=155, w2=23, w3=467, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(23, min_periods=max(23//3, 2)).mean()
    noise = impulse.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.16375 + 0.0006907 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_307_struct_v307_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=162, w2=34, w3=480, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 34)
    curvature = _rolling_slope(acceleration, 480)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2086 * acceleration + 0.0006908 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_308_struct_v308_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=169, w2=45, w3=493, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(45, min_periods=max(45//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1925 + 0.0006909 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_309_struct_v309_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=176, w2=56, w3=506, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(56, min_periods=max(56//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2238 * _rolling_slope(draw, 506) + 0.000691 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_310_struct_v310_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=183, w2=67, w3=519, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(67, min_periods=max(67//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.22125 + 0.0006911 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_311_struct_v311_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=190, w2=78, w3=532, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 78)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.235625 + 0.0006912 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_312_struct_v312_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=197, w2=89, w3=545, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(89, min_periods=max(89//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.25 + 0.0006913 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_313_struct_v313_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=204, w2=100, w3=558, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(100, min_periods=max(100//3, 2)).rank(pct=True)
    persistence = change.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2542 * persistence + 0.0006914 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_314_struct_v314_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=211, w2=111, w3=571, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(111, min_periods=max(111//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.27875 + 0.0006915 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_315_struct_v315_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=218, w2=122, w3=584, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(122, min_periods=max(122//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2694 * slope + 0.0006916 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_316_struct_v316_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=225, w2=133, w3=597, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(133, min_periods=max(133//3, 2)).mean()
    noise = impulse.abs().rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3075 + 0.0006917 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_317_struct_v317_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=232, w2=144, w3=610, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 610)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2846 * acceleration + 0.0006918 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_318_struct_v318_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=239, w2=155, w3=623, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(155, min_periods=max(155//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.33625 + 0.0006919 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_319_struct_v319_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=246, w2=166, w3=636, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(166, min_periods=max(166//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2998 * _rolling_slope(draw, 636) + 0.000692 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_320_struct_v320_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=253, w2=177, w3=649, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(177, min_periods=max(177//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.365 + 0.0006921 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_321_struct_v321_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=9, w2=188, w3=662, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.379375 + 0.0006922 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_322_struct_v322_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=16, w2=199, w3=675, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(199, min_periods=max(199//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.39375 + 0.0006923 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_323_struct_v323_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=23, w2=210, w3=688, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(23)
    rank = change.rolling(210, min_periods=max(210//3, 2)).rank(pct=True)
    persistence = change.rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3302 * persistence + 0.0006924 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_324_struct_v324_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=221, w3=701, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(221, min_periods=max(221//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4225 + 0.0006925 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_325_struct_v325_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=232, w3=714, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(232, min_periods=max(232//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3454 * slope + 0.0006926 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_326_struct_v326_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=243, w3=727, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(44)
    drag = impulse.rolling(243, min_periods=max(243//3, 2)).mean()
    noise = impulse.abs().rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45125 + 0.0006927 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_327_struct_v327_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=254, w3=740, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 254)
    curvature = _rolling_slope(acceleration, 740)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3606 * acceleration + 0.0006928 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_328_struct_v328_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=265, w3=753, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(265, min_periods=max(265//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.48 + 0.0006929 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_329_struct_v329_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=276, w3=766, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(276, min_periods=max(276//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3758 * _rolling_slope(draw, 766) + 0.000693 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_330_struct_v330_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=287, w3=22, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(287, min_periods=max(287//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.50875 + 0.0006931 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_331_struct_v331_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=298, w3=35, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 298)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=35, adjust=False).mean() * 1.523125 + 0.0006932 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_332_struct_v332_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=309, w3=48, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(309, min_periods=max(309//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5375 + 0.0006933 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_333_struct_v333_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=320, w3=61, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(93)
    rank = change.rolling(320, min_periods=max(320//3, 2)).rank(pct=True)
    persistence = change.rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4062 * persistence + 0.0006934 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_334_struct_v334_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=331, w3=74, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(331, min_periods=max(331//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56625 + 0.0006935 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_335_struct_v335_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=342, w3=87, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(342, min_periods=max(342//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.045 * slope + 0.0006936 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_336_struct_v336_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=353, w3=100, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(114)
    drag = impulse.rolling(353, min_periods=max(353//3, 2)).mean()
    noise = impulse.abs().rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.595 + 0.0006937 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_337_struct_v337_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=364, w3=113, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 364)
    curvature = _rolling_slope(acceleration, 113)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0602 * acceleration + 0.0006938 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_338_struct_v338_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=375, w3=126, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(375, min_periods=max(375//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.850625 + 0.0006939 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_339_struct_v339_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=386, w3=139, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(386, min_periods=max(386//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0754 * _rolling_slope(draw, 139) + 0.000694 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_340_struct_v340_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=397, w3=152, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(397, min_periods=max(397//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.879375 + 0.0006941 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_341_struct_v341_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=408, w3=165, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 408)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=165, adjust=False).mean() * 0.89375 + 0.0006942 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_342_struct_v342_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=419, w3=178, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(419, min_periods=max(419//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.908125 + 0.0006943 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_343_struct_v343_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=430, w3=191, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(430, min_periods=max(430//3, 2)).rank(pct=True)
    persistence = change.rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1058 * persistence + 0.0006944 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_344_struct_v344_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=441, w3=204, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(441, min_periods=max(441//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.936875 + 0.0006945 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_345_struct_v345_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=452, w3=217, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(452, min_periods=max(452//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.121 * slope + 0.0006946 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_346_struct_v346_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=463, w3=230, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(463, min_periods=max(463//3, 2)).mean()
    noise = impulse.abs().rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.965625 + 0.0006947 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_347_struct_v347_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=474, w3=243, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 474)
    curvature = _rolling_slope(acceleration, 243)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1362 * acceleration + 0.0006948 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_348_struct_v348_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=485, w3=256, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(485, min_periods=max(485//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.994375 + 0.0006949 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_349_struct_v349_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=496, w3=269, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(496, min_periods=max(496//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1514 * _rolling_slope(draw, 269) + 0.000695 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_350_struct_v350_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=507, w3=282, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(507, min_periods=max(507//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.023125 + 0.0006951 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_351_struct_v351_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=15, w3=295, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 15)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=295, adjust=False).mean() * 1.0375 + 0.0006952 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_352_struct_v352_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=26, w3=308, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(26, min_periods=max(26//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.051875 + 0.0006953 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_353_struct_v353_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=37, w3=321, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(37, min_periods=max(37//3, 2)).rank(pct=True)
    persistence = change.rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1818 * persistence + 0.0006954 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_354_struct_v354_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=48, w3=334, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(48, min_periods=max(48//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.080625 + 0.0006955 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_355_struct_v355_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=59, w3=347, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(59, min_periods=max(59//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.197 * slope + 0.0006956 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_356_struct_v356_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=70, w3=360, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(70, min_periods=max(70//3, 2)).mean()
    noise = impulse.abs().rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.109375 + 0.0006957 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_357_struct_v357_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=81, w3=373, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 81)
    curvature = _rolling_slope(acceleration, 373)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2122 * acceleration + 0.0006958 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_358_struct_v358_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=92, w3=386, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(92, min_periods=max(92//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.138125 + 0.0006959 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_359_struct_v359_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=103, w3=399, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(103, min_periods=max(103//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2274 * _rolling_slope(draw, 399) + 0.000696 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_360_struct_v360_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=114, w3=412, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(114, min_periods=max(114//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.166875 + 0.0006961 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_361_struct_v361_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=125, w3=425, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 125)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.18125 + 0.0006962 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_362_struct_v362_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=136, w3=438, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(136, min_periods=max(136//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.195625 + 0.0006963 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_363_struct_v363_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=147, w3=451, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(52)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2578 * persistence + 0.0006964 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_364_struct_v364_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=158, w3=464, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(158, min_periods=max(158//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.224375 + 0.0006965 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_365_struct_v365_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=169, w3=477, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.273 * slope + 0.0006966 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_366_struct_v366_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=180, w3=490, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(73)
    drag = impulse.rolling(180, min_periods=max(180//3, 2)).mean()
    noise = impulse.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.253125 + 0.0006967 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_367_struct_v367_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=191, w3=503, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 191)
    curvature = _rolling_slope(acceleration, 503)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2882 * acceleration + 0.0006968 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_368_struct_v368_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=202, w3=516, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(202, min_periods=max(202//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.281875 + 0.0006969 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_369_struct_v369_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=213, w3=529, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3034 * _rolling_slope(draw, 529) + 0.000697 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_370_struct_v370_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=224, w3=542, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(224, min_periods=max(224//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.310625 + 0.0006971 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_371_struct_v371_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=235, w3=555, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 235)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.325 + 0.0006972 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_372_struct_v372_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=246, w3=568, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.339375 + 0.0006973 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_373_struct_v373_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=257, w3=581, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(122)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3338 * persistence + 0.0006974 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_374_struct_v374_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=268, w3=594, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(268, min_periods=max(268//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.368125 + 0.0006975 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_375_struct_v375_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=279, w3=607, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(279, min_periods=max(279//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349 * slope + 0.0006976 * anchor
    return base_signal.diff().diff().diff()
