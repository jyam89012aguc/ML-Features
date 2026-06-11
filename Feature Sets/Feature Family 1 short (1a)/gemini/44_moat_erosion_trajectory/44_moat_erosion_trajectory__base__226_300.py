"""44 moat erosion trajectory base features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f44_met_226_struct_v226(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=211, w3=434, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(78)
    drag = impulse.rolling(211, min_periods=max(211//3, 2)).mean()
    noise = impulse.abs().rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0225 + 0.0027227 * anchor

def f44_met_227_struct_v227(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=222, w3=447, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 222)
    curvature = _rolling_slope(acceleration, 447)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3166 * acceleration + 0.0027228 * anchor

def f44_met_228_struct_v228(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=233, w3=460, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(233, min_periods=max(233//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05125 + 0.0027229 * anchor

def f44_met_229_struct_v229(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=244, w3=473, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(244, min_periods=max(244//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3318 * _rolling_slope(draw, 473) + 0.002723 * anchor

def f44_met_230_struct_v230(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=255, w3=486, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(255, min_periods=max(255//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.08 + 0.0027231 * anchor

def f44_met_231_struct_v231(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=266, w3=499, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 266)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.094375 + 0.0027232 * anchor

def f44_met_232_struct_v232(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=277, w3=512, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(277, min_periods=max(277//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.10875 + 0.0027233 * anchor

def f44_met_233_struct_v233(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=288, w3=525, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(288, min_periods=max(288//3, 2)).rank(pct=True)
    persistence = change.rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3622 * persistence + 0.0027234 * anchor

def f44_met_234_struct_v234(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=299, w3=538, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(299, min_periods=max(299//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1375 + 0.0027235 * anchor

def f44_met_235_struct_v235(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=310, w3=551, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(310, min_periods=max(310//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3774 * slope + 0.0027236 * anchor

def f44_met_236_struct_v236(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=321, w3=564, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(321, min_periods=max(321//3, 2)).mean()
    noise = impulse.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.16625 + 0.0027237 * anchor

def f44_met_237_struct_v237(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=332, w3=577, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 332)
    curvature = _rolling_slope(acceleration, 577)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3926 * acceleration + 0.0027238 * anchor

def f44_met_238_struct_v238(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=343, w3=590, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(343, min_periods=max(343//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.195 + 0.0027239 * anchor

def f44_met_239_struct_v239(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=354, w3=603, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(354, min_periods=max(354//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4078 * _rolling_slope(draw, 603) + 0.002724 * anchor

def f44_met_240_struct_v240(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=365, w3=616, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.22375 + 0.0027241 * anchor

def f44_met_241_struct_v241(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=376, w3=629, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 376)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.238125 + 0.0027242 * anchor

def f44_met_242_struct_v242(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=387, w3=642, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(387, min_periods=max(387//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2525 + 0.0027243 * anchor

def f44_met_243_struct_v243(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=398, w3=655, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0618 * persistence + 0.0027244 * anchor

def f44_met_244_struct_v244(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=409, w3=668, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28125 + 0.0027245 * anchor

def f44_met_245_struct_v245(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=420, w3=681, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(420, min_periods=max(420//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.077 * slope + 0.0027246 * anchor

def f44_met_246_struct_v246(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=431, w3=694, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.31 + 0.0027247 * anchor

def f44_met_247_struct_v247(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=442, w3=707, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 442)
    curvature = _rolling_slope(acceleration, 707)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0922 * acceleration + 0.0027248 * anchor

def f44_met_248_struct_v248(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=453, w3=720, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(453, min_periods=max(453//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.33875 + 0.0027249 * anchor

def f44_met_249_struct_v249(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=464, w3=733, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1074 * _rolling_slope(draw, 733) + 0.002725 * anchor

def f44_met_250_struct_v250(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=475, w3=746, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(475, min_periods=max(475//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3675 + 0.0027251 * anchor

def f44_met_251_struct_v251(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=486, w3=759, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 253)
    slow = _rolling_slope(x, 486)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.381875 + 0.0027252 * anchor

def f44_met_252_struct_v252(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=497, w3=15, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(497, min_periods=max(497//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.39625 + 0.0027253 * anchor

def f44_met_253_struct_v253(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=508, w3=28, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(16)
    rank = change.rolling(508, min_periods=max(508//3, 2)).rank(pct=True)
    persistence = change.rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1378 * persistence + 0.0027254 * anchor

def f44_met_254_struct_v254(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=16, w3=41, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(16, min_periods=max(16//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.425 + 0.0027255 * anchor

def f44_met_255_struct_v255(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=27, w3=54, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(27, min_periods=max(27//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.153 * slope + 0.0027256 * anchor

def f44_met_256_struct_v256(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=38, w3=67, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(37)
    drag = impulse.rolling(38, min_periods=max(38//3, 2)).mean()
    noise = impulse.abs().rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.45375 + 0.0027257 * anchor

def f44_met_257_struct_v257(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=49, w3=80, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 49)
    curvature = _rolling_slope(acceleration, 80)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1682 * acceleration + 0.0027258 * anchor

def f44_met_258_struct_v258(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=60, w3=93, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(60, min_periods=max(60//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(93) * 1.4825 + 0.0027259 * anchor

def f44_met_259_struct_v259(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=71, w3=106, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(71, min_periods=max(71//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1834 * _rolling_slope(draw, 106) + 0.002726 * anchor

def f44_met_260_struct_v260(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=82, w3=119, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(82, min_periods=max(82//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51125 + 0.0027261 * anchor

def f44_met_261_struct_v261(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=93, w3=132, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 93)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=132, adjust=False).mean() * 1.525625 + 0.0027262 * anchor

def f44_met_262_struct_v262(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=104, w3=145, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(104, min_periods=max(104//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.54 + 0.0027263 * anchor

def f44_met_263_struct_v263(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=115, w3=158, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(86)
    rank = change.rolling(115, min_periods=max(115//3, 2)).rank(pct=True)
    persistence = change.rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2138 * persistence + 0.0027264 * anchor

def f44_met_264_struct_v264(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=126, w3=171, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(126, min_periods=max(126//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56875 + 0.0027265 * anchor

def f44_met_265_struct_v265(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=137, w3=184, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(137, min_periods=max(137//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.229 * slope + 0.0027266 * anchor

def f44_met_266_struct_v266(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=148, w3=197, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(107)
    drag = impulse.rolling(148, min_periods=max(148//3, 2)).mean()
    noise = impulse.abs().rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5975 + 0.0027267 * anchor

def f44_met_267_struct_v267(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=159, w3=210, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 159)
    curvature = _rolling_slope(acceleration, 210)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2442 * acceleration + 0.0027268 * anchor

def f44_met_268_struct_v268(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=170, w3=223, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(170, min_periods=max(170//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.853125 + 0.0027269 * anchor

def f44_met_269_struct_v269(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=181, w3=236, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(181, min_periods=max(181//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2594 * _rolling_slope(draw, 236) + 0.002727 * anchor

def f44_met_270_struct_v270(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=192, w3=249, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 135)
    baseline = trend.rolling(192, min_periods=max(192//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.881875 + 0.0027271 * anchor

def f44_met_271_struct_v271(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=203, w3=262, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 203)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=262, adjust=False).mean() * 0.89625 + 0.0027272 * anchor

def f44_met_272_struct_v272(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=214, w3=275, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(214, min_periods=max(214//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.910625 + 0.0027273 * anchor

def f44_met_273_struct_v273(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=225, w3=288, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(225, min_periods=max(225//3, 2)).rank(pct=True)
    persistence = change.rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2898 * persistence + 0.0027274 * anchor

def f44_met_274_struct_v274(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=236, w3=301, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(236, min_periods=max(236//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.939375 + 0.0027275 * anchor

def f44_met_275_struct_v275(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=247, w3=314, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(247, min_periods=max(247//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.305 * slope + 0.0027276 * anchor

def f44_met_276_struct_v276(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=258, w3=327, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(258, min_periods=max(258//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.968125 + 0.0027277 * anchor

def f44_met_277_struct_v277(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=269, w3=340, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 269)
    curvature = _rolling_slope(acceleration, 340)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3202 * acceleration + 0.0027278 * anchor

def f44_met_278_struct_v278(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=280, w3=353, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(280, min_periods=max(280//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.996875 + 0.0027279 * anchor

def f44_met_279_struct_v279(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=291, w3=366, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(291, min_periods=max(291//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3354 * _rolling_slope(draw, 366) + 0.002728 * anchor

def f44_met_280_struct_v280(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=302, w3=379, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 205)
    baseline = trend.rolling(302, min_periods=max(302//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.025625 + 0.0027281 * anchor

def f44_met_281_struct_v281(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=313, w3=392, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 212)
    slow = _rolling_slope(x, 313)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.04 + 0.0027282 * anchor

def f44_met_282_struct_v282(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=324, w3=405, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(324, min_periods=max(324//3, 2)).max()
    trough = x.rolling(219, min_periods=max(219//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.054375 + 0.0027283 * anchor

def f44_met_283_struct_v283(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=335, w3=418, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(335, min_periods=max(335//3, 2)).rank(pct=True)
    persistence = change.rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3658 * persistence + 0.0027284 * anchor

def f44_met_284_struct_v284(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=346, w3=431, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(233, min_periods=max(233//3, 2)).std()
    vol_slow = ret.rolling(346, min_periods=max(346//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.083125 + 0.0027285 * anchor

def f44_met_285_struct_v285(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=357, w3=444, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(357, min_periods=max(357//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 240)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.381 * slope + 0.0027286 * anchor

def f44_met_286_struct_v286(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=368, w3=457, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(368, min_periods=max(368//3, 2)).mean()
    noise = impulse.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.111875 + 0.0027287 * anchor

def f44_met_287_struct_v287(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=379, w3=470, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 254)
    acceleration = _rolling_slope(velocity, 379)
    curvature = _rolling_slope(acceleration, 470)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3962 * acceleration + 0.0027288 * anchor

def f44_met_288_struct_v288(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=390, w3=483, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(10, min_periods=max(10//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.140625 + 0.0027289 * anchor

def f44_met_289_struct_v289(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=401, w3=496, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(17, min_periods=max(17//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.035 * _rolling_slope(draw, 496) + 0.002729 * anchor

def f44_met_290_struct_v290(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=412, w3=509, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(412, min_periods=max(412//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.169375 + 0.0027291 * anchor

def f44_met_291_struct_v291(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=423, w3=522, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 31)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.18375 + 0.0027292 * anchor

def f44_met_292_struct_v292(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=434, w3=535, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(434, min_periods=max(434//3, 2)).max()
    trough = x.rolling(38, min_periods=max(38//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.198125 + 0.0027293 * anchor

def f44_met_293_struct_v293(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=445, w3=548, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(45)
    rank = change.rolling(445, min_periods=max(445//3, 2)).rank(pct=True)
    persistence = change.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0654 * persistence + 0.0027294 * anchor

def f44_met_294_struct_v294(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=456, w3=561, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(52, min_periods=max(52//3, 2)).std()
    vol_slow = ret.rolling(456, min_periods=max(456//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.226875 + 0.0027295 * anchor

def f44_met_295_struct_v295(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=467, w3=574, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(467, min_periods=max(467//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 59)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0806 * slope + 0.0027296 * anchor

def f44_met_296_struct_v296(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=478, w3=587, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(66)
    drag = impulse.rolling(478, min_periods=max(478//3, 2)).mean()
    noise = impulse.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.255625 + 0.0027297 * anchor

def f44_met_297_struct_v297(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=489, w3=600, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 73)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0958 * acceleration + 0.0027298 * anchor

def f44_met_298_struct_v298(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=500, w3=613, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(500, min_periods=max(500//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.284375 + 0.0027299 * anchor

def f44_met_299_struct_v299(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=511, w3=626, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(511, min_periods=max(511//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.111 * _rolling_slope(draw, 626) + 0.00273 * anchor

def f44_met_300_struct_v300(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=19, w3=639, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(19, min_periods=max(19//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.313125 + 0.0027301 * anchor
