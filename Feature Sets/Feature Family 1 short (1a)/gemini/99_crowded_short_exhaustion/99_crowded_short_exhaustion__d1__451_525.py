"""99 crowded short exhaustion d1 first derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Securities_Lending - Institutional-grade short-side signal.
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

def f99_crowd_451_struct_v451_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=28, w2=370, w3=715, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 370)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.449375 + 0.0044252 * anchor
    return base_signal.diff()

def f99_crowd_452_struct_v452_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=35, w2=381, w3=728, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(381, min_periods=max(381//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.46375 + 0.0044253 * anchor
    return base_signal.diff()

def f99_crowd_453_struct_v453_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=42, w2=392, w3=741, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(42)
    rank = change.rolling(392, min_periods=max(392//3, 2)).rank(pct=True)
    persistence = change.rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2326 * persistence + 0.0044254 * anchor
    return base_signal.diff()

def f99_crowd_454_struct_v454_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=49, w2=403, w3=754, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(403, min_periods=max(403//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4925 + 0.0044255 * anchor
    return base_signal.diff()

def f99_crowd_455_struct_v455_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=56, w2=414, w3=767, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(414, min_periods=max(414//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2478 * slope + 0.0044256 * anchor
    return base_signal.diff()

def f99_crowd_456_struct_v456_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=63, w2=425, w3=23, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(63)
    drag = impulse.rolling(425, min_periods=max(425//3, 2)).mean()
    noise = impulse.abs().rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.52125 + 0.0044257 * anchor
    return base_signal.diff()

def f99_crowd_457_struct_v457_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=70, w2=436, w3=36, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 36)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.263 * acceleration + 0.0044258 * anchor
    return base_signal.diff()

def f99_crowd_458_struct_v458_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=77, w2=447, w3=49, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(447, min_periods=max(447//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(49) * 1.55 + 0.0044259 * anchor
    return base_signal.diff()

def f99_crowd_459_struct_v459_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=84, w2=458, w3=62, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(458, min_periods=max(458//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2782 * _rolling_slope(draw, 62) + 0.004426 * anchor
    return base_signal.diff()

def f99_crowd_460_struct_v460_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=91, w2=469, w3=75, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(469, min_periods=max(469//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.57875 + 0.0044261 * anchor
    return base_signal.diff()

def f99_crowd_461_struct_v461_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=98, w2=480, w3=88, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 480)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=88, adjust=False).mean() * 1.593125 + 0.0044262 * anchor
    return base_signal.diff()

def f99_crowd_462_struct_v462_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=105, w2=491, w3=101, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(491, min_periods=max(491//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6075 + 0.0044263 * anchor
    return base_signal.diff()

def f99_crowd_463_struct_v463_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=112, w2=502, w3=114, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(112)
    rank = change.rolling(502, min_periods=max(502//3, 2)).rank(pct=True)
    persistence = change.rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3086 * persistence + 0.0044264 * anchor
    return base_signal.diff()

def f99_crowd_464_struct_v464_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=119, w2=10, w3=127, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(10, min_periods=max(10//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.863125 + 0.0044265 * anchor
    return base_signal.diff()

def f99_crowd_465_struct_v465_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=126, w2=21, w3=140, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(21, min_periods=max(21//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3238 * slope + 0.0044266 * anchor
    return base_signal.diff()

def f99_crowd_466_struct_v466_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=133, w2=32, w3=153, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(32, min_periods=max(32//3, 2)).mean()
    noise = impulse.abs().rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.891875 + 0.0044267 * anchor
    return base_signal.diff()

def f99_crowd_467_struct_v467_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=140, w2=43, w3=166, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 43)
    curvature = _rolling_slope(acceleration, 166)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.339 * acceleration + 0.0044268 * anchor
    return base_signal.diff()

def f99_crowd_468_struct_v468_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=147, w2=54, w3=179, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(54, min_periods=max(54//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.920625 + 0.0044269 * anchor
    return base_signal.diff()

def f99_crowd_469_struct_v469_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=154, w2=65, w3=192, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(65, min_periods=max(65//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3542 * _rolling_slope(draw, 192) + 0.004427 * anchor
    return base_signal.diff()

def f99_crowd_470_struct_v470_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=161, w2=76, w3=205, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(76, min_periods=max(76//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.949375 + 0.0044271 * anchor
    return base_signal.diff()

def f99_crowd_471_struct_v471_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=87, w3=218, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 87)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=218, adjust=False).mean() * 0.96375 + 0.0044272 * anchor
    return base_signal.diff()

def f99_crowd_472_struct_v472_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=98, w3=231, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(98, min_periods=max(98//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.978125 + 0.0044273 * anchor
    return base_signal.diff()

def f99_crowd_473_struct_v473_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=109, w3=244, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(109, min_periods=max(109//3, 2)).rank(pct=True)
    persistence = change.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3846 * persistence + 0.0044274 * anchor
    return base_signal.diff()

def f99_crowd_474_struct_v474_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=120, w3=257, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(120, min_periods=max(120//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.006875 + 0.0044275 * anchor
    return base_signal.diff()

def f99_crowd_475_struct_v475_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=131, w3=270, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3998 * slope + 0.0044276 * anchor
    return base_signal.diff()

def f99_crowd_476_struct_v476_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=142, w3=283, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(142, min_periods=max(142//3, 2)).mean()
    noise = impulse.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.035625 + 0.0044277 * anchor
    return base_signal.diff()

def f99_crowd_477_struct_v477_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=153, w3=296, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 153)
    curvature = _rolling_slope(acceleration, 296)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0386 * acceleration + 0.0044278 * anchor
    return base_signal.diff()

def f99_crowd_478_struct_v478_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=164, w3=309, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(164, min_periods=max(164//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.064375 + 0.0044279 * anchor
    return base_signal.diff()

def f99_crowd_479_struct_v479_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=175, w3=322, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(175, min_periods=max(175//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0538 * _rolling_slope(draw, 322) + 0.004428 * anchor
    return base_signal.diff()

def f99_crowd_480_struct_v480_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=186, w3=335, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(186, min_periods=max(186//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.093125 + 0.0044281 * anchor
    return base_signal.diff()

def f99_crowd_481_struct_v481_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=197, w3=348, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 197)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1075 + 0.0044282 * anchor
    return base_signal.diff()

def f99_crowd_482_struct_v482_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=208, w3=361, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(208, min_periods=max(208//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.121875 + 0.0044283 * anchor
    return base_signal.diff()

def f99_crowd_483_struct_v483_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=219, w3=374, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(219, min_periods=max(219//3, 2)).rank(pct=True)
    persistence = change.rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0842 * persistence + 0.0044284 * anchor
    return base_signal.diff()

def f99_crowd_484_struct_v484_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=230, w3=387, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.150625 + 0.0044285 * anchor
    return base_signal.diff()

def f99_crowd_485_struct_v485_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=241, w3=400, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0994 * slope + 0.0044286 * anchor
    return base_signal.diff()

def f99_crowd_486_struct_v486_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=252, w3=413, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(22)
    drag = impulse.rolling(252, min_periods=max(252//3, 2)).mean()
    noise = impulse.abs().rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.179375 + 0.0044287 * anchor
    return base_signal.diff()

def f99_crowd_487_struct_v487_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=263, w3=426, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 263)
    curvature = _rolling_slope(acceleration, 426)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1146 * acceleration + 0.0044288 * anchor
    return base_signal.diff()

def f99_crowd_488_struct_v488_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=274, w3=439, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(274, min_periods=max(274//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.208125 + 0.0044289 * anchor
    return base_signal.diff()

def f99_crowd_489_struct_v489_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=285, w3=452, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(285, min_periods=max(285//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1298 * _rolling_slope(draw, 452) + 0.004429 * anchor
    return base_signal.diff()

def f99_crowd_490_struct_v490_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=296, w3=465, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(296, min_periods=max(296//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.236875 + 0.0044291 * anchor
    return base_signal.diff()

def f99_crowd_491_struct_v491_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=307, w3=478, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 307)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.25125 + 0.0044292 * anchor
    return base_signal.diff()

def f99_crowd_492_struct_v492_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=318, w3=491, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(318, min_periods=max(318//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.265625 + 0.0044293 * anchor
    return base_signal.diff()

def f99_crowd_493_struct_v493_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=329, w3=504, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(71)
    rank = change.rolling(329, min_periods=max(329//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1602 * persistence + 0.0044294 * anchor
    return base_signal.diff()

def f99_crowd_494_struct_v494_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=340, w3=517, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(340, min_periods=max(340//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.294375 + 0.0044295 * anchor
    return base_signal.diff()

def f99_crowd_495_struct_v495_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=351, w3=530, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(351, min_periods=max(351//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1754 * slope + 0.0044296 * anchor
    return base_signal.diff()

def f99_crowd_496_struct_v496_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=362, w3=543, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(92)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.323125 + 0.0044297 * anchor
    return base_signal.diff()

def f99_crowd_497_struct_v497_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=373, w3=556, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 373)
    curvature = _rolling_slope(acceleration, 556)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1906 * acceleration + 0.0044298 * anchor
    return base_signal.diff()

def f99_crowd_498_struct_v498_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=384, w3=569, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.351875 + 0.0044299 * anchor
    return base_signal.diff()

def f99_crowd_499_struct_v499_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=395, w3=582, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(395, min_periods=max(395//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2058 * _rolling_slope(draw, 582) + 0.00443 * anchor
    return base_signal.diff()

def f99_crowd_500_struct_v500_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=406, w3=595, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(406, min_periods=max(406//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.380625 + 0.0044301 * anchor
    return base_signal.diff()

def f99_crowd_501_struct_v501_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=417, w3=608, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 417)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.395 + 0.0044302 * anchor
    return base_signal.diff()

def f99_crowd_502_struct_v502_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=428, w3=621, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(428, min_periods=max(428//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.409375 + 0.0044303 * anchor
    return base_signal.diff()

def f99_crowd_503_struct_v503_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=439, w3=634, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(439, min_periods=max(439//3, 2)).rank(pct=True)
    persistence = change.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2362 * persistence + 0.0044304 * anchor
    return base_signal.diff()

def f99_crowd_504_struct_v504_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=450, w3=647, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.438125 + 0.0044305 * anchor
    return base_signal.diff()

def f99_crowd_505_struct_v505_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=461, w3=660, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(461, min_periods=max(461//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2514 * slope + 0.0044306 * anchor
    return base_signal.diff()

def f99_crowd_506_struct_v506_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=472, w3=673, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(472, min_periods=max(472//3, 2)).mean()
    noise = impulse.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.466875 + 0.0044307 * anchor
    return base_signal.diff()

def f99_crowd_507_struct_v507_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=483, w3=686, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 483)
    curvature = _rolling_slope(acceleration, 686)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2666 * acceleration + 0.0044308 * anchor
    return base_signal.diff()

def f99_crowd_508_struct_v508_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=494, w3=699, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(494, min_periods=max(494//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.495625 + 0.0044309 * anchor
    return base_signal.diff()

def f99_crowd_509_struct_v509_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=505, w3=712, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(505, min_periods=max(505//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2818 * _rolling_slope(draw, 712) + 0.004431 * anchor
    return base_signal.diff()

def f99_crowd_510_struct_v510_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=13, w3=725, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.524375 + 0.0044311 * anchor
    return base_signal.diff()

def f99_crowd_511_struct_v511_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=24, w3=738, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 24)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.53875 + 0.0044312 * anchor
    return base_signal.diff()

def f99_crowd_512_struct_v512_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=35, w3=751, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(35, min_periods=max(35//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.553125 + 0.0044313 * anchor
    return base_signal.diff()

def f99_crowd_513_struct_v513_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=46, w3=764, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3122 * persistence + 0.0044314 * anchor
    return base_signal.diff()

def f99_crowd_514_struct_v514_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=57, w3=20, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(57, min_periods=max(57//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.581875 + 0.0044315 * anchor
    return base_signal.diff()

def f99_crowd_515_struct_v515_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=68, w3=33, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3274 * slope + 0.0044316 * anchor
    return base_signal.diff()

def f99_crowd_516_struct_v516_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=79, w3=46, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(79, min_periods=max(79//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.610625 + 0.0044317 * anchor
    return base_signal.diff()

def f99_crowd_517_struct_v517_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=90, w3=59, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 90)
    curvature = _rolling_slope(acceleration, 59)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3426 * acceleration + 0.0044318 * anchor
    return base_signal.diff()

def f99_crowd_518_struct_v518_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=101, w3=72, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(101, min_periods=max(101//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(72) * 0.86625 + 0.0044319 * anchor
    return base_signal.diff()

def f99_crowd_519_struct_v519_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=112, w3=85, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3578 * _rolling_slope(draw, 85) + 0.004432 * anchor
    return base_signal.diff()

def f99_crowd_520_struct_v520_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=123, w3=98, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.895 + 0.0044321 * anchor
    return base_signal.diff()

def f99_crowd_521_struct_v521_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=134, w3=111, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 134)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=111, adjust=False).mean() * 0.909375 + 0.0044322 * anchor
    return base_signal.diff()

def f99_crowd_522_struct_v522_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=145, w3=124, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(145, min_periods=max(145//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92375 + 0.0044323 * anchor
    return base_signal.diff()

def f99_crowd_523_struct_v523_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=156, w3=137, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(30)
    rank = change.rolling(156, min_periods=max(156//3, 2)).rank(pct=True)
    persistence = change.rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3882 * persistence + 0.0044324 * anchor
    return base_signal.diff()

def f99_crowd_524_struct_v524_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=167, w3=150, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(167, min_periods=max(167//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9525 + 0.0044325 * anchor
    return base_signal.diff()

def f99_crowd_525_struct_v525_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=178, w3=163, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4034 * slope + 0.0044326 * anchor
    return base_signal.diff()
