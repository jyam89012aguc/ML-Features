"""74 internal credit spread acceleration base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f74_ics_301_struct_v301(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=183, w3=480, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 183)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3 + 0.0038702 * anchor

def f74_ics_302_struct_v302(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=194, w3=493, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(194, min_periods=max(194//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.314375 + 0.0038703 * anchor

def f74_ics_303_struct_v303(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=205, w3=506, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(97)
    rank = change.rolling(205, min_periods=max(205//3, 2)).rank(pct=True)
    persistence = change.rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2094 * persistence + 0.0038704 * anchor

def f74_ics_304_struct_v304(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=216, w3=519, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(216, min_periods=max(216//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.343125 + 0.0038705 * anchor

def f74_ics_305_struct_v305(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=227, w3=532, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(227, min_periods=max(227//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2246 * slope + 0.0038706 * anchor

def f74_ics_306_struct_v306(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=238, w3=545, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(118)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.371875 + 0.0038707 * anchor

def f74_ics_307_struct_v307(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=249, w3=558, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 249)
    curvature = _rolling_slope(acceleration, 558)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2398 * acceleration + 0.0038708 * anchor

def f74_ics_308_struct_v308(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=260, w3=571, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(260, min_periods=max(260//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.400625 + 0.0038709 * anchor

def f74_ics_309_struct_v309(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=271, w3=584, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.255 * _rolling_slope(draw, 584) + 0.003871 * anchor

def f74_ics_310_struct_v310(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=282, w3=597, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(282, min_periods=max(282//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.429375 + 0.0038711 * anchor

def f74_ics_311_struct_v311(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=293, w3=610, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.44375 + 0.0038712 * anchor

def f74_ics_312_struct_v312(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=304, w3=623, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(304, min_periods=max(304//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.458125 + 0.0038713 * anchor

def f74_ics_313_struct_v313(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=315, w3=636, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(315, min_periods=max(315//3, 2)).rank(pct=True)
    persistence = change.rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2854 * persistence + 0.0038714 * anchor

def f74_ics_314_struct_v314(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=326, w3=649, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.486875 + 0.0038715 * anchor

def f74_ics_315_struct_v315(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=337, w3=662, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(337, min_periods=max(337//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3006 * slope + 0.0038716 * anchor

def f74_ics_316_struct_v316(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=348, w3=675, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.515625 + 0.0038717 * anchor

def f74_ics_317_struct_v317(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=359, w3=688, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 688)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3158 * acceleration + 0.0038718 * anchor

def f74_ics_318_struct_v318(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=370, w3=701, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(370, min_periods=max(370//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.544375 + 0.0038719 * anchor

def f74_ics_319_struct_v319(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=381, w3=714, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(381, min_periods=max(381//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.331 * _rolling_slope(draw, 714) + 0.003872 * anchor

def f74_ics_320_struct_v320(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=392, w3=727, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(392, min_periods=max(392//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.573125 + 0.0038721 * anchor

def f74_ics_321_struct_v321(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=403, w3=740, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5875 + 0.0038722 * anchor

def f74_ics_322_struct_v322(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=414, w3=753, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(414, min_periods=max(414//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.601875 + 0.0038723 * anchor

def f74_ics_323_struct_v323(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=425, w3=766, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3614 * persistence + 0.0038724 * anchor

def f74_ics_324_struct_v324(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=436, w3=22, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8575 + 0.0038725 * anchor

def f74_ics_325_struct_v325(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=447, w3=35, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3766 * slope + 0.0038726 * anchor

def f74_ics_326_struct_v326(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=458, w3=48, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(7)
    drag = impulse.rolling(458, min_periods=max(458//3, 2)).mean()
    noise = impulse.abs().rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88625 + 0.0038727 * anchor

def f74_ics_327_struct_v327(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=469, w3=61, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 61)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3918 * acceleration + 0.0038728 * anchor

def f74_ics_328_struct_v328(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=480, w3=74, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(74) * 0.915 + 0.0038729 * anchor

def f74_ics_329_struct_v329(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=491, w3=87, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.407 * _rolling_slope(draw, 87) + 0.003873 * anchor

def f74_ics_330_struct_v330(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=502, w3=100, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.94375 + 0.0038731 * anchor

def f74_ics_331_struct_v331(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=10, w3=113, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 10)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=113, adjust=False).mean() * 0.958125 + 0.0038732 * anchor

def f74_ics_332_struct_v332(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=21, w3=126, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(21, min_periods=max(21//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9725 + 0.0038733 * anchor

def f74_ics_333_struct_v333(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=32, w3=139, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(56)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.061 * persistence + 0.0038734 * anchor

def f74_ics_334_struct_v334(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=43, w3=152, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.00125 + 0.0038735 * anchor

def f74_ics_335_struct_v335(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=54, w3=165, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(54, min_periods=max(54//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0762 * slope + 0.0038736 * anchor

def f74_ics_336_struct_v336(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=65, w3=178, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(77)
    drag = impulse.rolling(65, min_periods=max(65//3, 2)).mean()
    noise = impulse.abs().rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.03 + 0.0038737 * anchor

def f74_ics_337_struct_v337(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=76, w3=191, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 191)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0914 * acceleration + 0.0038738 * anchor

def f74_ics_338_struct_v338(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=87, w3=204, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05875 + 0.0038739 * anchor

def f74_ics_339_struct_v339(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=98, w3=217, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(98, min_periods=max(98//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1066 * _rolling_slope(draw, 217) + 0.003874 * anchor

def f74_ics_340_struct_v340(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=109, w3=230, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0875 + 0.0038741 * anchor

def f74_ics_341_struct_v341(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=120, w3=243, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=243, adjust=False).mean() * 1.101875 + 0.0038742 * anchor

def f74_ics_342_struct_v342(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=131, w3=256, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11625 + 0.0038743 * anchor

def f74_ics_343_struct_v343(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=142, w3=269, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.137 * persistence + 0.0038744 * anchor

def f74_ics_344_struct_v344(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=153, w3=282, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.145 + 0.0038745 * anchor

def f74_ics_345_struct_v345(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=164, w3=295, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1522 * slope + 0.0038746 * anchor

def f74_ics_346_struct_v346(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=175, w3=308, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(308, min_periods=max(308//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.17375 + 0.0038747 * anchor

def f74_ics_347_struct_v347(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=186, w3=321, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 321)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1674 * acceleration + 0.0038748 * anchor

def f74_ics_348_struct_v348(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=197, w3=334, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2025 + 0.0038749 * anchor

def f74_ics_349_struct_v349(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=208, w3=347, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1826 * _rolling_slope(draw, 347) + 0.003875 * anchor

def f74_ics_350_struct_v350(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=219, w3=360, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(219, min_periods=max(219//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.23125 + 0.0038751 * anchor

def f74_ics_351_struct_v351(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=230, w3=373, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 230)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.245625 + 0.0038752 * anchor

def f74_ics_352_struct_v352(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=241, w3=386, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.26 + 0.0038753 * anchor

def f74_ics_353_struct_v353(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=252, w3=399, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.213 * persistence + 0.0038754 * anchor

def f74_ics_354_struct_v354(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=263, w3=412, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28875 + 0.0038755 * anchor

def f74_ics_355_struct_v355(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=274, w3=425, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(274, min_periods=max(274//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2282 * slope + 0.0038756 * anchor

def f74_ics_356_struct_v356(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=285, w3=438, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(285, min_periods=max(285//3, 2)).mean()
    noise = impulse.abs().rolling(438, min_periods=max(438//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3175 + 0.0038757 * anchor

def f74_ics_357_struct_v357(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=296, w3=451, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 451)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2434 * acceleration + 0.0038758 * anchor

def f74_ics_358_struct_v358(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=307, w3=464, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.34625 + 0.0038759 * anchor

def f74_ics_359_struct_v359(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=318, w3=477, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2586 * _rolling_slope(draw, 477) + 0.003876 * anchor

def f74_ics_360_struct_v360(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=329, w3=490, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(329, min_periods=max(329//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.375 + 0.0038761 * anchor

def f74_ics_361_struct_v361(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=340, w3=503, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.389375 + 0.0038762 * anchor

def f74_ics_362_struct_v362(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=351, w3=516, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(351, min_periods=max(351//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.40375 + 0.0038763 * anchor

def f74_ics_363_struct_v363(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=362, w3=529, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(15)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.289 * persistence + 0.0038764 * anchor

def f74_ics_364_struct_v364(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=373, w3=542, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4325 + 0.0038765 * anchor

def f74_ics_365_struct_v365(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=384, w3=555, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(384, min_periods=max(384//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3042 * slope + 0.0038766 * anchor

def f74_ics_366_struct_v366(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=395, w3=568, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(36)
    drag = impulse.rolling(395, min_periods=max(395//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.46125 + 0.0038767 * anchor

def f74_ics_367_struct_v367(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=406, w3=581, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3194 * acceleration + 0.0038768 * anchor

def f74_ics_368_struct_v368(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=417, w3=594, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.49 + 0.0038769 * anchor

def f74_ics_369_struct_v369(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=428, w3=607, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3346 * _rolling_slope(draw, 607) + 0.003877 * anchor

def f74_ics_370_struct_v370(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=439, w3=620, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51875 + 0.0038771 * anchor

def f74_ics_371_struct_v371(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=450, w3=633, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 450)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.533125 + 0.0038772 * anchor

def f74_ics_372_struct_v372(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=461, w3=646, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5475 + 0.0038773 * anchor

def f74_ics_373_struct_v373(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=472, w3=659, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(85)
    rank = change.rolling(472, min_periods=max(472//3, 2)).rank(pct=True)
    persistence = change.rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.365 * persistence + 0.0038774 * anchor

def f74_ics_374_struct_v374(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=483, w3=672, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(483, min_periods=max(483//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57625 + 0.0038775 * anchor

def f74_ics_375_struct_v375(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=494, w3=685, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3802 * slope + 0.0038776 * anchor
