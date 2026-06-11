"""94 beta decay and regime shift base features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Macro_Factor - Institutional-grade short-side signal.
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

def f94_beta_301_struct_v301(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=168, w3=49, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=49, adjust=False).mean() * 1.491875 + 0.0043502 * anchor

def f94_beta_302_struct_v302(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=179, w3=62, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(179, min_periods=max(179//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.50625 + 0.0043503 * anchor

def f94_beta_303_struct_v303(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=190, w3=75, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(63)
    rank = change.rolling(190, min_periods=max(190//3, 2)).rank(pct=True)
    persistence = change.rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1786 * persistence + 0.0043504 * anchor

def f94_beta_304_struct_v304(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=201, w3=88, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.535 + 0.0043505 * anchor

def f94_beta_305_struct_v305(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=212, w3=101, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1938 * slope + 0.0043506 * anchor

def f94_beta_306_struct_v306(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=223, w3=114, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(84)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.56375 + 0.0043507 * anchor

def f94_beta_307_struct_v307(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=234, w3=127, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 127)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.209 * acceleration + 0.0043508 * anchor

def f94_beta_308_struct_v308(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=245, w3=140, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(245, min_periods=max(245//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5925 + 0.0043509 * anchor

def f94_beta_309_struct_v309(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=256, w3=153, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(256, min_periods=max(256//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2242 * _rolling_slope(draw, 153) + 0.004351 * anchor

def f94_beta_310_struct_v310(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=267, w3=166, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(267, min_periods=max(267//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.62125 + 0.0043511 * anchor

def f94_beta_311_struct_v311(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=278, w3=179, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 278)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=179, adjust=False).mean() * 0.8625 + 0.0043512 * anchor

def f94_beta_312_struct_v312(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=289, w3=192, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(289, min_periods=max(289//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.876875 + 0.0043513 * anchor

def f94_beta_313_struct_v313(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=300, w3=205, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2546 * persistence + 0.0043514 * anchor

def f94_beta_314_struct_v314(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=311, w3=218, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.905625 + 0.0043515 * anchor

def f94_beta_315_struct_v315(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=322, w3=231, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(322, min_periods=max(322//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2698 * slope + 0.0043516 * anchor

def f94_beta_316_struct_v316(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=333, w3=244, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(333, min_periods=max(333//3, 2)).mean()
    noise = impulse.abs().rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.934375 + 0.0043517 * anchor

def f94_beta_317_struct_v317(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=344, w3=257, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 344)
    curvature = _rolling_slope(acceleration, 257)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.285 * acceleration + 0.0043518 * anchor

def f94_beta_318_struct_v318(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=355, w3=270, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(355, min_periods=max(355//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.963125 + 0.0043519 * anchor

def f94_beta_319_struct_v319(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=366, w3=283, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(366, min_periods=max(366//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3002 * _rolling_slope(draw, 283) + 0.004352 * anchor

def f94_beta_320_struct_v320(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=377, w3=296, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(377, min_periods=max(377//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.991875 + 0.0043521 * anchor

def f94_beta_321_struct_v321(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=388, w3=309, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 388)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.00625 + 0.0043522 * anchor

def f94_beta_322_struct_v322(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=399, w3=322, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(399, min_periods=max(399//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.020625 + 0.0043523 * anchor

def f94_beta_323_struct_v323(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=410, w3=335, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(410, min_periods=max(410//3, 2)).rank(pct=True)
    persistence = change.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3306 * persistence + 0.0043524 * anchor

def f94_beta_324_struct_v324(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=421, w3=348, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(421, min_periods=max(421//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.049375 + 0.0043525 * anchor

def f94_beta_325_struct_v325(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=432, w3=361, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(432, min_periods=max(432//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3458 * slope + 0.0043526 * anchor

def f94_beta_326_struct_v326(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=443, w3=374, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(443, min_periods=max(443//3, 2)).mean()
    noise = impulse.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.078125 + 0.0043527 * anchor

def f94_beta_327_struct_v327(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=454, w3=387, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 454)
    curvature = _rolling_slope(acceleration, 387)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.361 * acceleration + 0.0043528 * anchor

def f94_beta_328_struct_v328(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=465, w3=400, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(465, min_periods=max(465//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.106875 + 0.0043529 * anchor

def f94_beta_329_struct_v329(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=476, w3=413, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3762 * _rolling_slope(draw, 413) + 0.004353 * anchor

def f94_beta_330_struct_v330(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=487, w3=426, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 252)
    baseline = trend.rolling(487, min_periods=max(487//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.135625 + 0.0043531 * anchor

def f94_beta_331_struct_v331(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=498, w3=439, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 8)
    slow = _rolling_slope(x, 498)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.15 + 0.0043532 * anchor

def f94_beta_332_struct_v332(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=509, w3=452, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.164375 + 0.0043533 * anchor

def f94_beta_333_struct_v333(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=17, w3=465, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(22)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4066 * persistence + 0.0043534 * anchor

def f94_beta_334_struct_v334(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=28, w3=478, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(28, min_periods=max(28//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.193125 + 0.0043535 * anchor

def f94_beta_335_struct_v335(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=39, w3=491, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(39, min_periods=max(39//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 36)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0454 * slope + 0.0043536 * anchor

def f94_beta_336_struct_v336(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=50, w3=504, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(43)
    drag = impulse.rolling(50, min_periods=max(50//3, 2)).mean()
    noise = impulse.abs().rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.221875 + 0.0043537 * anchor

def f94_beta_337_struct_v337(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=61, w3=517, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 50)
    acceleration = _rolling_slope(velocity, 61)
    curvature = _rolling_slope(acceleration, 517)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0606 * acceleration + 0.0043538 * anchor

def f94_beta_338_struct_v338(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=72, w3=530, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(72, min_periods=max(72//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.250625 + 0.0043539 * anchor

def f94_beta_339_struct_v339(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=83, w3=543, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(83, min_periods=max(83//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0758 * _rolling_slope(draw, 543) + 0.004354 * anchor

def f94_beta_340_struct_v340(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=94, w3=556, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(94, min_periods=max(94//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.279375 + 0.0043541 * anchor

def f94_beta_341_struct_v341(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=105, w3=569, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 105)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.29375 + 0.0043542 * anchor

def f94_beta_342_struct_v342(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=116, w3=582, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(116, min_periods=max(116//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.308125 + 0.0043543 * anchor

def f94_beta_343_struct_v343(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=127, w3=595, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(92)
    rank = change.rolling(127, min_periods=max(127//3, 2)).rank(pct=True)
    persistence = change.rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1062 * persistence + 0.0043544 * anchor

def f94_beta_344_struct_v344(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=138, w3=608, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(138, min_periods=max(138//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.336875 + 0.0043545 * anchor

def f94_beta_345_struct_v345(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=149, w3=621, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(149, min_periods=max(149//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1214 * slope + 0.0043546 * anchor

def f94_beta_346_struct_v346(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=160, w3=634, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(113)
    drag = impulse.rolling(160, min_periods=max(160//3, 2)).mean()
    noise = impulse.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.365625 + 0.0043547 * anchor

def f94_beta_347_struct_v347(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=171, w3=647, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 171)
    curvature = _rolling_slope(acceleration, 647)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1366 * acceleration + 0.0043548 * anchor

def f94_beta_348_struct_v348(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=182, w3=660, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(182, min_periods=max(182//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.394375 + 0.0043549 * anchor

def f94_beta_349_struct_v349(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=193, w3=673, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(193, min_periods=max(193//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1518 * _rolling_slope(draw, 673) + 0.004355 * anchor

def f94_beta_350_struct_v350(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=204, w3=686, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(204, min_periods=max(204//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.423125 + 0.0043551 * anchor

def f94_beta_351_struct_v351(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=215, w3=699, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 215)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4375 + 0.0043552 * anchor

def f94_beta_352_struct_v352(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=226, w3=712, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(226, min_periods=max(226//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.451875 + 0.0043553 * anchor

def f94_beta_353_struct_v353(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=237, w3=725, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(237, min_periods=max(237//3, 2)).rank(pct=True)
    persistence = change.rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1822 * persistence + 0.0043554 * anchor

def f94_beta_354_struct_v354(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=248, w3=738, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(248, min_periods=max(248//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.480625 + 0.0043555 * anchor

def f94_beta_355_struct_v355(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=259, w3=751, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(259, min_periods=max(259//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1974 * slope + 0.0043556 * anchor

def f94_beta_356_struct_v356(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=270, w3=764, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(270, min_periods=max(270//3, 2)).mean()
    noise = impulse.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.509375 + 0.0043557 * anchor

def f94_beta_357_struct_v357(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=281, w3=20, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 281)
    curvature = _rolling_slope(acceleration, 20)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2126 * acceleration + 0.0043558 * anchor

def f94_beta_358_struct_v358(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=292, w3=33, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(292, min_periods=max(292//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(33) * 1.538125 + 0.0043559 * anchor

def f94_beta_359_struct_v359(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=303, w3=46, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(303, min_periods=max(303//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2278 * _rolling_slope(draw, 46) + 0.004356 * anchor

def f94_beta_360_struct_v360(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=314, w3=59, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(314, min_periods=max(314//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.566875 + 0.0043561 * anchor

def f94_beta_361_struct_v361(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=325, w3=72, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 325)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=72, adjust=False).mean() * 1.58125 + 0.0043562 * anchor

def f94_beta_362_struct_v362(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=336, w3=85, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(336, min_periods=max(336//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.595625 + 0.0043563 * anchor

def f94_beta_363_struct_v363(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=347, w3=98, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(347, min_periods=max(347//3, 2)).rank(pct=True)
    persistence = change.rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2582 * persistence + 0.0043564 * anchor

def f94_beta_364_struct_v364(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=358, w3=111, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(358, min_periods=max(358//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85125 + 0.0043565 * anchor

def f94_beta_365_struct_v365(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=369, w3=124, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(369, min_periods=max(369//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2734 * slope + 0.0043566 * anchor

def f94_beta_366_struct_v366(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=380, w3=137, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(380, min_periods=max(380//3, 2)).mean()
    noise = impulse.abs().rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88 + 0.0043567 * anchor

def f94_beta_367_struct_v367(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=391, w3=150, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 391)
    curvature = _rolling_slope(acceleration, 150)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2886 * acceleration + 0.0043568 * anchor

def f94_beta_368_struct_v368(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=402, w3=163, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(402, min_periods=max(402//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.90875 + 0.0043569 * anchor

def f94_beta_369_struct_v369(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=413, w3=176, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(413, min_periods=max(413//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3038 * _rolling_slope(draw, 176) + 0.004357 * anchor

def f94_beta_370_struct_v370(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=424, w3=189, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(424, min_periods=max(424//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9375 + 0.0043571 * anchor

def f94_beta_371_struct_v371(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=435, w3=202, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 435)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=202, adjust=False).mean() * 0.951875 + 0.0043572 * anchor

def f94_beta_372_struct_v372(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=446, w3=215, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(446, min_periods=max(446//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.96625 + 0.0043573 * anchor

def f94_beta_373_struct_v373(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=457, w3=228, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(51)
    rank = change.rolling(457, min_periods=max(457//3, 2)).rank(pct=True)
    persistence = change.rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3342 * persistence + 0.0043574 * anchor

def f94_beta_374_struct_v374(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=468, w3=241, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(468, min_periods=max(468//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.995 + 0.0043575 * anchor

def f94_beta_375_struct_v375(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=479, w3=254, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(479, min_periods=max(479//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3494 * slope + 0.0043576 * anchor
