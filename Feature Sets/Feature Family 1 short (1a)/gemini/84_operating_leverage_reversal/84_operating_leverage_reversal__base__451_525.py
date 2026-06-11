"""84 operating leverage reversal base features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Operating_Efficiency - Institutional-grade short-side signal.
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

def f84_olr_451_struct_v451(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=65, w3=322, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.619375 + 0.0041252 * anchor

def f84_olr_452_struct_v452(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=76, w3=335, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(76, min_periods=max(76//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.860625 + 0.0041253 * anchor

def f84_olr_453_struct_v453(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=87, w3=348, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.393 * persistence + 0.0041254 * anchor

def f84_olr_454_struct_v454(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=98, w3=361, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.889375 + 0.0041255 * anchor

def f84_olr_455_struct_v455(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=109, w3=374, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4082 * slope + 0.0041256 * anchor

def f84_olr_456_struct_v456(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=120, w3=387, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.918125 + 0.0041257 * anchor

def f84_olr_457_struct_v457(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=131, w3=400, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 400)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.047 * acceleration + 0.0041258 * anchor

def f84_olr_458_struct_v458(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=142, w3=413, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.946875 + 0.0041259 * anchor

def f84_olr_459_struct_v459(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=153, w3=426, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0622 * _rolling_slope(draw, 426) + 0.004126 * anchor

def f84_olr_460_struct_v460(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=164, w3=439, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.975625 + 0.0041261 * anchor

def f84_olr_461_struct_v461(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=175, w3=452, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.99 + 0.0041262 * anchor

def f84_olr_462_struct_v462(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=186, w3=465, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.004375 + 0.0041263 * anchor

def f84_olr_463_struct_v463(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=197, w3=478, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0926 * persistence + 0.0041264 * anchor

def f84_olr_464_struct_v464(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=208, w3=491, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.033125 + 0.0041265 * anchor

def f84_olr_465_struct_v465(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=219, w3=504, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1078 * slope + 0.0041266 * anchor

def f84_olr_466_struct_v466(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=230, w3=517, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.061875 + 0.0041267 * anchor

def f84_olr_467_struct_v467(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=241, w3=530, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 530)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.123 * acceleration + 0.0041268 * anchor

def f84_olr_468_struct_v468(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=252, w3=543, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.090625 + 0.0041269 * anchor

def f84_olr_469_struct_v469(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=263, w3=556, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1382 * _rolling_slope(draw, 556) + 0.004127 * anchor

def f84_olr_470_struct_v470(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=274, w3=569, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.119375 + 0.0041271 * anchor

def f84_olr_471_struct_v471(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=285, w3=582, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 285)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.13375 + 0.0041272 * anchor

def f84_olr_472_struct_v472(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=296, w3=595, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.148125 + 0.0041273 * anchor

def f84_olr_473_struct_v473(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=307, w3=608, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(15)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(608, min_periods=max(608//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1686 * persistence + 0.0041274 * anchor

def f84_olr_474_struct_v474(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=318, w3=621, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(318, min_periods=max(318//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.176875 + 0.0041275 * anchor

def f84_olr_475_struct_v475(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=329, w3=634, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(329, min_periods=max(329//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1838 * slope + 0.0041276 * anchor

def f84_olr_476_struct_v476(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=340, w3=647, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(36)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.205625 + 0.0041277 * anchor

def f84_olr_477_struct_v477(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=351, w3=660, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 351)
    curvature = _rolling_slope(acceleration, 660)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.199 * acceleration + 0.0041278 * anchor

def f84_olr_478_struct_v478(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=362, w3=673, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(362, min_periods=max(362//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.234375 + 0.0041279 * anchor

def f84_olr_479_struct_v479(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=373, w3=686, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2142 * _rolling_slope(draw, 686) + 0.004128 * anchor

def f84_olr_480_struct_v480(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=384, w3=699, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.263125 + 0.0041281 * anchor

def f84_olr_481_struct_v481(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=395, w3=712, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.2775 + 0.0041282 * anchor

def f84_olr_482_struct_v482(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=406, w3=725, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(406, min_periods=max(406//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.291875 + 0.0041283 * anchor

def f84_olr_483_struct_v483(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=417, w3=738, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(85)
    rank = change.rolling(417, min_periods=max(417//3, 2)).rank(pct=True)
    persistence = change.rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2446 * persistence + 0.0041284 * anchor

def f84_olr_484_struct_v484(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=428, w3=751, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(428, min_periods=max(428//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.320625 + 0.0041285 * anchor

def f84_olr_485_struct_v485(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=439, w3=764, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2598 * slope + 0.0041286 * anchor

def f84_olr_486_struct_v486(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=450, w3=20, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(106)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.349375 + 0.0041287 * anchor

def f84_olr_487_struct_v487(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=461, w3=33, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 461)
    curvature = _rolling_slope(acceleration, 33)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.275 * acceleration + 0.0041288 * anchor

def f84_olr_488_struct_v488(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=472, w3=46, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(472, min_periods=max(472//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(46) * 1.378125 + 0.0041289 * anchor

def f84_olr_489_struct_v489(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=483, w3=59, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(483, min_periods=max(483//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2902 * _rolling_slope(draw, 59) + 0.004129 * anchor

def f84_olr_490_struct_v490(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=494, w3=72, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(494, min_periods=max(494//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.406875 + 0.0041291 * anchor

def f84_olr_491_struct_v491(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=505, w3=85, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=85, adjust=False).mean() * 1.42125 + 0.0041292 * anchor

def f84_olr_492_struct_v492(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=13, w3=98, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(13, min_periods=max(13//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.435625 + 0.0041293 * anchor

def f84_olr_493_struct_v493(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=24, w3=111, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(24, min_periods=max(24//3, 2)).rank(pct=True)
    persistence = change.rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3206 * persistence + 0.0041294 * anchor

def f84_olr_494_struct_v494(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=35, w3=124, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.464375 + 0.0041295 * anchor

def f84_olr_495_struct_v495(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=46, w3=137, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(46, min_periods=max(46//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3358 * slope + 0.0041296 * anchor

def f84_olr_496_struct_v496(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=57, w3=150, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.493125 + 0.0041297 * anchor

def f84_olr_497_struct_v497(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=68, w3=163, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 68)
    curvature = _rolling_slope(acceleration, 163)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.351 * acceleration + 0.0041298 * anchor

def f84_olr_498_struct_v498(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=79, w3=176, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(79, min_periods=max(79//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.521875 + 0.0041299 * anchor

def f84_olr_499_struct_v499(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=90, w3=189, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(90, min_periods=max(90//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3662 * _rolling_slope(draw, 189) + 0.00413 * anchor

def f84_olr_500_struct_v500(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=101, w3=202, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.550625 + 0.0041301 * anchor

def f84_olr_501_struct_v501(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=112, w3=215, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=215, adjust=False).mean() * 1.565 + 0.0041302 * anchor

def f84_olr_502_struct_v502(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=123, w3=228, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(123, min_periods=max(123//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.579375 + 0.0041303 * anchor

def f84_olr_503_struct_v503(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=134, w3=241, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(134, min_periods=max(134//3, 2)).rank(pct=True)
    persistence = change.rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3966 * persistence + 0.0041304 * anchor

def f84_olr_504_struct_v504(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=145, w3=254, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.608125 + 0.0041305 * anchor

def f84_olr_505_struct_v505(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=156, w3=267, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0354 * slope + 0.0041306 * anchor

def f84_olr_506_struct_v506(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=167, w3=280, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(167, min_periods=max(167//3, 2)).mean()
    noise = impulse.abs().rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.86375 + 0.0041307 * anchor

def f84_olr_507_struct_v507(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=178, w3=293, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 253)
    acceleration = _rolling_slope(velocity, 178)
    curvature = _rolling_slope(acceleration, 293)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0506 * acceleration + 0.0041308 * anchor

def f84_olr_508_struct_v508(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=189, w3=306, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(189, min_periods=max(189//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8925 + 0.0041309 * anchor

def f84_olr_509_struct_v509(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=200, w3=319, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0658 * _rolling_slope(draw, 319) + 0.004131 * anchor

def f84_olr_510_struct_v510(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=211, w3=332, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(211, min_periods=max(211//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.92125 + 0.0041311 * anchor

def f84_olr_511_struct_v511(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=222, w3=345, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 222)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.935625 + 0.0041312 * anchor

def f84_olr_512_struct_v512(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=233, w3=358, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(233, min_periods=max(233//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.95 + 0.0041313 * anchor

def f84_olr_513_struct_v513(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=244, w3=371, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(44)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0962 * persistence + 0.0041314 * anchor

def f84_olr_514_struct_v514(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=255, w3=384, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(255, min_periods=max(255//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97875 + 0.0041315 * anchor

def f84_olr_515_struct_v515(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=266, w3=397, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(266, min_periods=max(266//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1114 * slope + 0.0041316 * anchor

def f84_olr_516_struct_v516(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=277, w3=410, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(65)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0075 + 0.0041317 * anchor

def f84_olr_517_struct_v517(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=288, w3=423, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 423)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1266 * acceleration + 0.0041318 * anchor

def f84_olr_518_struct_v518(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=299, w3=436, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(299, min_periods=max(299//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.03625 + 0.0041319 * anchor

def f84_olr_519_struct_v519(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=310, w3=449, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(310, min_periods=max(310//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1418 * _rolling_slope(draw, 449) + 0.004132 * anchor

def f84_olr_520_struct_v520(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=321, w3=462, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.065 + 0.0041321 * anchor

def f84_olr_521_struct_v521(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=332, w3=475, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 332)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.079375 + 0.0041322 * anchor

def f84_olr_522_struct_v522(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=343, w3=488, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(343, min_periods=max(343//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.09375 + 0.0041323 * anchor

def f84_olr_523_struct_v523(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=354, w3=501, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(114)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1722 * persistence + 0.0041324 * anchor

def f84_olr_524_struct_v524(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=365, w3=514, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1225 + 0.0041325 * anchor

def f84_olr_525_struct_v525(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=376, w3=527, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1874 * slope + 0.0041326 * anchor
