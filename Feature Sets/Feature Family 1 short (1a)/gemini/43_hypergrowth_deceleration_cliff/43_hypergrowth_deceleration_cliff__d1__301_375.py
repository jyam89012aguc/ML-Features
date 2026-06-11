"""43 hypergrowth deceleration cliff d1 first derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f43_hdc_301_struct_v301_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=472, w3=422, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.206875 + 0.0026702 * anchor
    return base_signal.diff()

def f43_hdc_302_struct_v302_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=483, w3=435, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.22125 + 0.0026703 * anchor
    return base_signal.diff()

def f43_hdc_303_struct_v303_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=494, w3=448, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0982 * persistence + 0.0026704 * anchor
    return base_signal.diff()

def f43_hdc_304_struct_v304_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=505, w3=461, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.25 + 0.0026705 * anchor
    return base_signal.diff()

def f43_hdc_305_struct_v305_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=13, w3=474, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1134 * slope + 0.0026706 * anchor
    return base_signal.diff()

def f43_hdc_306_struct_v306_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=24, w3=487, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27875 + 0.0026707 * anchor
    return base_signal.diff()

def f43_hdc_307_struct_v307_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=35, w3=500, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 500)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1286 * acceleration + 0.0026708 * anchor
    return base_signal.diff()

def f43_hdc_308_struct_v308_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=46, w3=513, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3075 + 0.0026709 * anchor
    return base_signal.diff()

def f43_hdc_309_struct_v309_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=57, w3=526, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1438 * _rolling_slope(draw, 526) + 0.002671 * anchor
    return base_signal.diff()

def f43_hdc_310_struct_v310_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=68, w3=539, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(68, min_periods=max(68//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33625 + 0.0026711 * anchor
    return base_signal.diff()

def f43_hdc_311_struct_v311_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=79, w3=552, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.350625 + 0.0026712 * anchor
    return base_signal.diff()

def f43_hdc_312_struct_v312_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=90, w3=565, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(90, min_periods=max(90//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.365 + 0.0026713 * anchor
    return base_signal.diff()

def f43_hdc_313_struct_v313_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=101, w3=578, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(101, min_periods=max(101//3, 2)).rank(pct=True)
    persistence = change.rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1742 * persistence + 0.0026714 * anchor
    return base_signal.diff()

def f43_hdc_314_struct_v314_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=112, w3=591, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(112, min_periods=max(112//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39375 + 0.0026715 * anchor
    return base_signal.diff()

def f43_hdc_315_struct_v315_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=123, w3=604, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(123, min_periods=max(123//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1894 * slope + 0.0026716 * anchor
    return base_signal.diff()

def f43_hdc_316_struct_v316_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=134, w3=617, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(22)
    drag = impulse.rolling(134, min_periods=max(134//3, 2)).mean()
    noise = impulse.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4225 + 0.0026717 * anchor
    return base_signal.diff()

def f43_hdc_317_struct_v317_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=145, w3=630, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 630)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2046 * acceleration + 0.0026718 * anchor
    return base_signal.diff()

def f43_hdc_318_struct_v318_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=156, w3=643, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(156, min_periods=max(156//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.45125 + 0.0026719 * anchor
    return base_signal.diff()

def f43_hdc_319_struct_v319_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=167, w3=656, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(167, min_periods=max(167//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2198 * _rolling_slope(draw, 656) + 0.002672 * anchor
    return base_signal.diff()

def f43_hdc_320_struct_v320_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=178, w3=669, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.48 + 0.0026721 * anchor
    return base_signal.diff()

def f43_hdc_321_struct_v321_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=189, w3=682, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.494375 + 0.0026722 * anchor
    return base_signal.diff()

def f43_hdc_322_struct_v322_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=200, w3=695, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(200, min_periods=max(200//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50875 + 0.0026723 * anchor
    return base_signal.diff()

def f43_hdc_323_struct_v323_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=211, w3=708, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(71)
    rank = change.rolling(211, min_periods=max(211//3, 2)).rank(pct=True)
    persistence = change.rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2502 * persistence + 0.0026724 * anchor
    return base_signal.diff()

def f43_hdc_324_struct_v324_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=222, w3=721, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(222, min_periods=max(222//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5375 + 0.0026725 * anchor
    return base_signal.diff()

def f43_hdc_325_struct_v325_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=233, w3=734, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(233, min_periods=max(233//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2654 * slope + 0.0026726 * anchor
    return base_signal.diff()

def f43_hdc_326_struct_v326_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=244, w3=747, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(92)
    drag = impulse.rolling(244, min_periods=max(244//3, 2)).mean()
    noise = impulse.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.56625 + 0.0026727 * anchor
    return base_signal.diff()

def f43_hdc_327_struct_v327_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=255, w3=760, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 255)
    curvature = _rolling_slope(acceleration, 760)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2806 * acceleration + 0.0026728 * anchor
    return base_signal.diff()

def f43_hdc_328_struct_v328_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=266, w3=16, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(266, min_periods=max(266//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(16) * 1.595 + 0.0026729 * anchor
    return base_signal.diff()

def f43_hdc_329_struct_v329_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=277, w3=29, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2958 * _rolling_slope(draw, 29) + 0.002673 * anchor
    return base_signal.diff()

def f43_hdc_330_struct_v330_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=288, w3=42, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(288, min_periods=max(288//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.850625 + 0.0026731 * anchor
    return base_signal.diff()

def f43_hdc_331_struct_v331_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=299, w3=55, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 299)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=55, adjust=False).mean() * 0.865 + 0.0026732 * anchor
    return base_signal.diff()

def f43_hdc_332_struct_v332_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=310, w3=68, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.879375 + 0.0026733 * anchor
    return base_signal.diff()

def f43_hdc_333_struct_v333_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=321, w3=81, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(321, min_periods=max(321//3, 2)).rank(pct=True)
    persistence = change.rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3262 * persistence + 0.0026734 * anchor
    return base_signal.diff()

def f43_hdc_334_struct_v334_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=332, w3=94, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.908125 + 0.0026735 * anchor
    return base_signal.diff()

def f43_hdc_335_struct_v335_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=343, w3=107, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(343, min_periods=max(343//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3414 * slope + 0.0026736 * anchor
    return base_signal.diff()

def f43_hdc_336_struct_v336_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=354, w3=120, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(354, min_periods=max(354//3, 2)).mean()
    noise = impulse.abs().rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.936875 + 0.0026737 * anchor
    return base_signal.diff()

def f43_hdc_337_struct_v337_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=365, w3=133, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 133)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3566 * acceleration + 0.0026738 * anchor
    return base_signal.diff()

def f43_hdc_338_struct_v338_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=376, w3=146, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(376, min_periods=max(376//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.965625 + 0.0026739 * anchor
    return base_signal.diff()

def f43_hdc_339_struct_v339_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=387, w3=159, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(387, min_periods=max(387//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3718 * _rolling_slope(draw, 159) + 0.002674 * anchor
    return base_signal.diff()

def f43_hdc_340_struct_v340_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=398, w3=172, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.994375 + 0.0026741 * anchor
    return base_signal.diff()

def f43_hdc_341_struct_v341_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=409, w3=185, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 409)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=185, adjust=False).mean() * 1.00875 + 0.0026742 * anchor
    return base_signal.diff()

def f43_hdc_342_struct_v342_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=420, w3=198, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(420, min_periods=max(420//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.023125 + 0.0026743 * anchor
    return base_signal.diff()

def f43_hdc_343_struct_v343_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=431, w3=211, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4022 * persistence + 0.0026744 * anchor
    return base_signal.diff()

def f43_hdc_344_struct_v344_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=442, w3=224, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.051875 + 0.0026745 * anchor
    return base_signal.diff()

def f43_hdc_345_struct_v345_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=453, w3=237, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(453, min_periods=max(453//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.041 * slope + 0.0026746 * anchor
    return base_signal.diff()

def f43_hdc_346_struct_v346_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=464, w3=250, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.080625 + 0.0026747 * anchor
    return base_signal.diff()

def f43_hdc_347_struct_v347_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=475, w3=263, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 263)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0562 * acceleration + 0.0026748 * anchor
    return base_signal.diff()

def f43_hdc_348_struct_v348_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=486, w3=276, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(486, min_periods=max(486//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.109375 + 0.0026749 * anchor
    return base_signal.diff()

def f43_hdc_349_struct_v349_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=497, w3=289, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(497, min_periods=max(497//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0714 * _rolling_slope(draw, 289) + 0.002675 * anchor
    return base_signal.diff()

def f43_hdc_350_struct_v350_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=508, w3=302, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(508, min_periods=max(508//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.138125 + 0.0026751 * anchor
    return base_signal.diff()

def f43_hdc_351_struct_v351_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=16, w3=315, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1525 + 0.0026752 * anchor
    return base_signal.diff()

def f43_hdc_352_struct_v352_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=27, w3=328, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(27, min_periods=max(27//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.166875 + 0.0026753 * anchor
    return base_signal.diff()

def f43_hdc_353_struct_v353_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=38, w3=341, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(30)
    rank = change.rolling(38, min_periods=max(38//3, 2)).rank(pct=True)
    persistence = change.rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1018 * persistence + 0.0026754 * anchor
    return base_signal.diff()

def f43_hdc_354_struct_v354_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=49, w3=354, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.195625 + 0.0026755 * anchor
    return base_signal.diff()

def f43_hdc_355_struct_v355_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=60, w3=367, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(60, min_periods=max(60//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.117 * slope + 0.0026756 * anchor
    return base_signal.diff()

def f43_hdc_356_struct_v356_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=71, w3=380, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(51)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.224375 + 0.0026757 * anchor
    return base_signal.diff()

def f43_hdc_357_struct_v357_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=82, w3=393, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 82)
    curvature = _rolling_slope(acceleration, 393)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1322 * acceleration + 0.0026758 * anchor
    return base_signal.diff()

def f43_hdc_358_struct_v358_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=93, w3=406, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.253125 + 0.0026759 * anchor
    return base_signal.diff()

def f43_hdc_359_struct_v359_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=104, w3=419, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(104, min_periods=max(104//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1474 * _rolling_slope(draw, 419) + 0.002676 * anchor
    return base_signal.diff()

def f43_hdc_360_struct_v360_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=115, w3=432, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(115, min_periods=max(115//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.281875 + 0.0026761 * anchor
    return base_signal.diff()

def f43_hdc_361_struct_v361_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=126, w3=445, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.29625 + 0.0026762 * anchor
    return base_signal.diff()

def f43_hdc_362_struct_v362_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=137, w3=458, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(137, min_periods=max(137//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.310625 + 0.0026763 * anchor
    return base_signal.diff()

def f43_hdc_363_struct_v363_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=148, w3=471, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(100)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1778 * persistence + 0.0026764 * anchor
    return base_signal.diff()

def f43_hdc_364_struct_v364_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=159, w3=484, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(159, min_periods=max(159//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.339375 + 0.0026765 * anchor
    return base_signal.diff()

def f43_hdc_365_struct_v365_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=170, w3=497, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.193 * slope + 0.0026766 * anchor
    return base_signal.diff()

def f43_hdc_366_struct_v366_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=181, w3=510, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(121)
    drag = impulse.rolling(181, min_periods=max(181//3, 2)).mean()
    noise = impulse.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.368125 + 0.0026767 * anchor
    return base_signal.diff()

def f43_hdc_367_struct_v367_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=192, w3=523, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 523)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2082 * acceleration + 0.0026768 * anchor
    return base_signal.diff()

def f43_hdc_368_struct_v368_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=203, w3=536, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.396875 + 0.0026769 * anchor
    return base_signal.diff()

def f43_hdc_369_struct_v369_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=214, w3=549, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2234 * _rolling_slope(draw, 549) + 0.002677 * anchor
    return base_signal.diff()

def f43_hdc_370_struct_v370_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=225, w3=562, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(225, min_periods=max(225//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.425625 + 0.0026771 * anchor
    return base_signal.diff()

def f43_hdc_371_struct_v371_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=236, w3=575, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 236)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.44 + 0.0026772 * anchor
    return base_signal.diff()

def f43_hdc_372_struct_v372_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=247, w3=588, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.454375 + 0.0026773 * anchor
    return base_signal.diff()

def f43_hdc_373_struct_v373_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=258, w3=601, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(258, min_periods=max(258//3, 2)).rank(pct=True)
    persistence = change.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2538 * persistence + 0.0026774 * anchor
    return base_signal.diff()

def f43_hdc_374_struct_v374_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=269, w3=614, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(269, min_periods=max(269//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.483125 + 0.0026775 * anchor
    return base_signal.diff()

def f43_hdc_375_struct_v375_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=280, w3=627, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.269 * slope + 0.0026776 * anchor
    return base_signal.diff()
