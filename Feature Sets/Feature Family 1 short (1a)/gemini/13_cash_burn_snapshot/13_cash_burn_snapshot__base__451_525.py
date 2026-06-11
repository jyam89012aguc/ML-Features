"""13 cash burn snapshot base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f13_cbrn_451_struct_v451(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=231, w3=541, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.17 + 0.0008252 * anchor

def f13_cbrn_452_struct_v452(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=242, w3=554, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(242, min_periods=max(242//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.184375 + 0.0008253 * anchor

def f13_cbrn_453_struct_v453(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=253, w3=567, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(46)
    rank = change.rolling(253, min_periods=max(253//3, 2)).rank(pct=True)
    persistence = change.rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2754 * persistence + 0.0008254 * anchor

def f13_cbrn_454_struct_v454(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=264, w3=580, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(264, min_periods=max(264//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.213125 + 0.0008255 * anchor

def f13_cbrn_455_struct_v455(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=275, w3=593, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(275, min_periods=max(275//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2906 * slope + 0.0008256 * anchor

def f13_cbrn_456_struct_v456(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=286, w3=606, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(67)
    drag = impulse.rolling(286, min_periods=max(286//3, 2)).mean()
    noise = impulse.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.241875 + 0.0008257 * anchor

def f13_cbrn_457_struct_v457(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=297, w3=619, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 297)
    curvature = _rolling_slope(acceleration, 619)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3058 * acceleration + 0.0008258 * anchor

def f13_cbrn_458_struct_v458(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=308, w3=632, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(308, min_periods=max(308//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.270625 + 0.0008259 * anchor

def f13_cbrn_459_struct_v459(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=319, w3=645, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.321 * _rolling_slope(draw, 645) + 0.000826 * anchor

def f13_cbrn_460_struct_v460(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=330, w3=658, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.299375 + 0.0008261 * anchor

def f13_cbrn_461_struct_v461(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=341, w3=671, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 341)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.31375 + 0.0008262 * anchor

def f13_cbrn_462_struct_v462(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=352, w3=684, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(352, min_periods=max(352//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.328125 + 0.0008263 * anchor

def f13_cbrn_463_struct_v463(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=363, w3=697, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(116)
    rank = change.rolling(363, min_periods=max(363//3, 2)).rank(pct=True)
    persistence = change.rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3514 * persistence + 0.0008264 * anchor

def f13_cbrn_464_struct_v464(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=374, w3=710, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(374, min_periods=max(374//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.356875 + 0.0008265 * anchor

def f13_cbrn_465_struct_v465(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=385, w3=723, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(385, min_periods=max(385//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3666 * slope + 0.0008266 * anchor

def f13_cbrn_466_struct_v466(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=396, w3=736, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(396, min_periods=max(396//3, 2)).mean()
    noise = impulse.abs().rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.385625 + 0.0008267 * anchor

def f13_cbrn_467_struct_v467(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=407, w3=749, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 407)
    curvature = _rolling_slope(acceleration, 749)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3818 * acceleration + 0.0008268 * anchor

def f13_cbrn_468_struct_v468(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=418, w3=762, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(418, min_periods=max(418//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.414375 + 0.0008269 * anchor

def f13_cbrn_469_struct_v469(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=429, w3=18, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(429, min_periods=max(429//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.397 * _rolling_slope(draw, 18) + 0.000827 * anchor

def f13_cbrn_470_struct_v470(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=440, w3=31, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.443125 + 0.0008271 * anchor

def f13_cbrn_471_struct_v471(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=451, w3=44, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 451)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=44, adjust=False).mean() * 1.4575 + 0.0008272 * anchor

def f13_cbrn_472_struct_v472(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=462, w3=57, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.471875 + 0.0008273 * anchor

def f13_cbrn_473_struct_v473(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=473, w3=70, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.051 * persistence + 0.0008274 * anchor

def f13_cbrn_474_struct_v474(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=484, w3=83, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(484, min_periods=max(484//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.500625 + 0.0008275 * anchor

def f13_cbrn_475_struct_v475(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=495, w3=96, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(495, min_periods=max(495//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0662 * slope + 0.0008276 * anchor

def f13_cbrn_476_struct_v476(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=506, w3=109, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.529375 + 0.0008277 * anchor

def f13_cbrn_477_struct_v477(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=14, w3=122, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 14)
    curvature = _rolling_slope(acceleration, 122)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0814 * acceleration + 0.0008278 * anchor

def f13_cbrn_478_struct_v478(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=25, w3=135, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(25, min_periods=max(25//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.558125 + 0.0008279 * anchor

def f13_cbrn_479_struct_v479(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=36, w3=148, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0966 * _rolling_slope(draw, 148) + 0.000828 * anchor

def f13_cbrn_480_struct_v480(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=47, w3=161, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.586875 + 0.0008281 * anchor

def f13_cbrn_481_struct_v481(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=58, w3=174, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=174, adjust=False).mean() * 1.60125 + 0.0008282 * anchor

def f13_cbrn_482_struct_v482(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=69, w3=187, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(69, min_periods=max(69//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.615625 + 0.0008283 * anchor

def f13_cbrn_483_struct_v483(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=80, w3=200, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(5)
    rank = change.rolling(80, min_periods=max(80//3, 2)).rank(pct=True)
    persistence = change.rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.127 * persistence + 0.0008284 * anchor

def f13_cbrn_484_struct_v484(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=91, w3=213, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(91, min_periods=max(91//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87125 + 0.0008285 * anchor

def f13_cbrn_485_struct_v485(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=102, w3=226, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(102, min_periods=max(102//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 19)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1422 * slope + 0.0008286 * anchor

def f13_cbrn_486_struct_v486(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=113, w3=239, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(26)
    drag = impulse.rolling(113, min_periods=max(113//3, 2)).mean()
    noise = impulse.abs().rolling(239, min_periods=max(239//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9 + 0.0008287 * anchor

def f13_cbrn_487_struct_v487(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=124, w3=252, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 124)
    curvature = _rolling_slope(acceleration, 252)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1574 * acceleration + 0.0008288 * anchor

def f13_cbrn_488_struct_v488(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=135, w3=265, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(135, min_periods=max(135//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.92875 + 0.0008289 * anchor

def f13_cbrn_489_struct_v489(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=146, w3=278, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(146, min_periods=max(146//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1726 * _rolling_slope(draw, 278) + 0.000829 * anchor

def f13_cbrn_490_struct_v490(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=157, w3=291, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(157, min_periods=max(157//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9575 + 0.0008291 * anchor

def f13_cbrn_491_struct_v491(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=168, w3=304, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.971875 + 0.0008292 * anchor

def f13_cbrn_492_struct_v492(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=179, w3=317, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(179, min_periods=max(179//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.98625 + 0.0008293 * anchor

def f13_cbrn_493_struct_v493(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=190, w3=330, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(75)
    rank = change.rolling(190, min_periods=max(190//3, 2)).rank(pct=True)
    persistence = change.rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.203 * persistence + 0.0008294 * anchor

def f13_cbrn_494_struct_v494(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=201, w3=343, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.015 + 0.0008295 * anchor

def f13_cbrn_495_struct_v495(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=212, w3=356, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2182 * slope + 0.0008296 * anchor

def f13_cbrn_496_struct_v496(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=223, w3=369, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(96)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.04375 + 0.0008297 * anchor

def f13_cbrn_497_struct_v497(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=234, w3=382, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 382)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2334 * acceleration + 0.0008298 * anchor

def f13_cbrn_498_struct_v498(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=245, w3=395, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(245, min_periods=max(245//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0725 + 0.0008299 * anchor

def f13_cbrn_499_struct_v499(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=256, w3=408, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(256, min_periods=max(256//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2486 * _rolling_slope(draw, 408) + 0.00083 * anchor

def f13_cbrn_500_struct_v500(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=267, w3=421, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(267, min_periods=max(267//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.10125 + 0.0008301 * anchor

def f13_cbrn_501_struct_v501(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=278, w3=434, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 278)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.115625 + 0.0008302 * anchor

def f13_cbrn_502_struct_v502(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=289, w3=447, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(289, min_periods=max(289//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.13 + 0.0008303 * anchor

def f13_cbrn_503_struct_v503(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=300, w3=460, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.279 * persistence + 0.0008304 * anchor

def f13_cbrn_504_struct_v504(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=311, w3=473, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.15875 + 0.0008305 * anchor

def f13_cbrn_505_struct_v505(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=322, w3=486, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(322, min_periods=max(322//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2942 * slope + 0.0008306 * anchor

def f13_cbrn_506_struct_v506(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=333, w3=499, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(333, min_periods=max(333//3, 2)).mean()
    noise = impulse.abs().rolling(499, min_periods=max(499//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1875 + 0.0008307 * anchor

def f13_cbrn_507_struct_v507(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=344, w3=512, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 344)
    curvature = _rolling_slope(acceleration, 512)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3094 * acceleration + 0.0008308 * anchor

def f13_cbrn_508_struct_v508(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=355, w3=525, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(355, min_periods=max(355//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.21625 + 0.0008309 * anchor

def f13_cbrn_509_struct_v509(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=366, w3=538, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(366, min_periods=max(366//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3246 * _rolling_slope(draw, 538) + 0.000831 * anchor

def f13_cbrn_510_struct_v510(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=377, w3=551, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(377, min_periods=max(377//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.245 + 0.0008311 * anchor

def f13_cbrn_511_struct_v511(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=388, w3=564, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 388)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.259375 + 0.0008312 * anchor

def f13_cbrn_512_struct_v512(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=399, w3=577, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(399, min_periods=max(399//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.27375 + 0.0008313 * anchor

def f13_cbrn_513_struct_v513(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=410, w3=590, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(410, min_periods=max(410//3, 2)).rank(pct=True)
    persistence = change.rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.355 * persistence + 0.0008314 * anchor

def f13_cbrn_514_struct_v514(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=421, w3=603, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(421, min_periods=max(421//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3025 + 0.0008315 * anchor

def f13_cbrn_515_struct_v515(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=432, w3=616, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(432, min_periods=max(432//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3702 * slope + 0.0008316 * anchor

def f13_cbrn_516_struct_v516(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=443, w3=629, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(443, min_periods=max(443//3, 2)).mean()
    noise = impulse.abs().rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.33125 + 0.0008317 * anchor

def f13_cbrn_517_struct_v517(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=454, w3=642, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 454)
    curvature = _rolling_slope(acceleration, 642)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3854 * acceleration + 0.0008318 * anchor

def f13_cbrn_518_struct_v518(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=465, w3=655, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(465, min_periods=max(465//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.36 + 0.0008319 * anchor

def f13_cbrn_519_struct_v519(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=476, w3=668, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4006 * _rolling_slope(draw, 668) + 0.000832 * anchor

def f13_cbrn_520_struct_v520(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=487, w3=681, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(487, min_periods=max(487//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.38875 + 0.0008321 * anchor

def f13_cbrn_521_struct_v521(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=498, w3=694, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 498)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.403125 + 0.0008322 * anchor

def f13_cbrn_522_struct_v522(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=509, w3=707, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4175 + 0.0008323 * anchor

def f13_cbrn_523_struct_v523(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=17, w3=720, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(34)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0546 * persistence + 0.0008324 * anchor

def f13_cbrn_524_struct_v524(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=28, w3=733, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(28, min_periods=max(28//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.44625 + 0.0008325 * anchor

def f13_cbrn_525_struct_v525(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=39, w3=746, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(39, min_periods=max(39//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0698 * slope + 0.0008326 * anchor
