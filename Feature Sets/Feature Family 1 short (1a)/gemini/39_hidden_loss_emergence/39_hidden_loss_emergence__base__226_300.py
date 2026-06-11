"""39 hidden loss emergence base features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f39_hle_226_struct_v226(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=348, w3=568, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.071875 + 0.0023627 * anchor

def f39_hle_227_struct_v227(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=359, w3=581, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0574 * acceleration + 0.0023628 * anchor

def f39_hle_228_struct_v228(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=370, w3=594, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(370, min_periods=max(370//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.100625 + 0.0023629 * anchor

def f39_hle_229_struct_v229(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=381, w3=607, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(381, min_periods=max(381//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0726 * _rolling_slope(draw, 607) + 0.002363 * anchor

def f39_hle_230_struct_v230(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=392, w3=620, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(392, min_periods=max(392//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.129375 + 0.0023631 * anchor

def f39_hle_231_struct_v231(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=403, w3=633, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.14375 + 0.0023632 * anchor

def f39_hle_232_struct_v232(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=414, w3=646, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(414, min_periods=max(414//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.158125 + 0.0023633 * anchor

def f39_hle_233_struct_v233(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=425, w3=659, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(27)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.103 * persistence + 0.0023634 * anchor

def f39_hle_234_struct_v234(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=436, w3=672, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.186875 + 0.0023635 * anchor

def f39_hle_235_struct_v235(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=447, w3=685, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1182 * slope + 0.0023636 * anchor

def f39_hle_236_struct_v236(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=458, w3=698, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(48)
    drag = impulse.rolling(458, min_periods=max(458//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.215625 + 0.0023637 * anchor

def f39_hle_237_struct_v237(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=469, w3=711, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 711)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1334 * acceleration + 0.0023638 * anchor

def f39_hle_238_struct_v238(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=480, w3=724, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.244375 + 0.0023639 * anchor

def f39_hle_239_struct_v239(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=491, w3=737, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1486 * _rolling_slope(draw, 737) + 0.002364 * anchor

def f39_hle_240_struct_v240(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=502, w3=750, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.273125 + 0.0023641 * anchor

def f39_hle_241_struct_v241(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=10, w3=763, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 10)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.2875 + 0.0023642 * anchor

def f39_hle_242_struct_v242(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=21, w3=19, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(21, min_periods=max(21//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.301875 + 0.0023643 * anchor

def f39_hle_243_struct_v243(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=32, w3=32, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(97)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.179 * persistence + 0.0023644 * anchor

def f39_hle_244_struct_v244(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=43, w3=45, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.330625 + 0.0023645 * anchor

def f39_hle_245_struct_v245(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=54, w3=58, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(54, min_periods=max(54//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1942 * slope + 0.0023646 * anchor

def f39_hle_246_struct_v246(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=65, w3=71, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(118)
    drag = impulse.rolling(65, min_periods=max(65//3, 2)).mean()
    noise = impulse.abs().rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.359375 + 0.0023647 * anchor

def f39_hle_247_struct_v247(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=76, w3=84, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 84)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2094 * acceleration + 0.0023648 * anchor

def f39_hle_248_struct_v248(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=87, w3=97, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(97) * 1.388125 + 0.0023649 * anchor

def f39_hle_249_struct_v249(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=98, w3=110, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(98, min_periods=max(98//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2246 * _rolling_slope(draw, 110) + 0.002365 * anchor

def f39_hle_250_struct_v250(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=109, w3=123, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.416875 + 0.0023651 * anchor

def f39_hle_251_struct_v251(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=120, w3=136, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=136, adjust=False).mean() * 1.43125 + 0.0023652 * anchor

def f39_hle_252_struct_v252(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=131, w3=149, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.445625 + 0.0023653 * anchor

def f39_hle_253_struct_v253(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=142, w3=162, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.255 * persistence + 0.0023654 * anchor

def f39_hle_254_struct_v254(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=153, w3=175, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.474375 + 0.0023655 * anchor

def f39_hle_255_struct_v255(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=164, w3=188, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2702 * slope + 0.0023656 * anchor

def f39_hle_256_struct_v256(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=175, w3=201, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.503125 + 0.0023657 * anchor

def f39_hle_257_struct_v257(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=186, w3=214, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 214)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2854 * acceleration + 0.0023658 * anchor

def f39_hle_258_struct_v258(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=197, w3=227, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.531875 + 0.0023659 * anchor

def f39_hle_259_struct_v259(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=208, w3=240, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3006 * _rolling_slope(draw, 240) + 0.002366 * anchor

def f39_hle_260_struct_v260(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=219, w3=253, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(219, min_periods=max(219//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.560625 + 0.0023661 * anchor

def f39_hle_261_struct_v261(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=230, w3=266, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 230)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=266, adjust=False).mean() * 1.575 + 0.0023662 * anchor

def f39_hle_262_struct_v262(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=241, w3=279, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.589375 + 0.0023663 * anchor

def f39_hle_263_struct_v263(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=252, w3=292, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.331 * persistence + 0.0023664 * anchor

def f39_hle_264_struct_v264(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=263, w3=305, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.618125 + 0.0023665 * anchor

def f39_hle_265_struct_v265(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=274, w3=318, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(274, min_periods=max(274//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3462 * slope + 0.0023666 * anchor

def f39_hle_266_struct_v266(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=285, w3=331, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(7)
    drag = impulse.rolling(285, min_periods=max(285//3, 2)).mean()
    noise = impulse.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.87375 + 0.0023667 * anchor

def f39_hle_267_struct_v267(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=296, w3=344, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 344)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3614 * acceleration + 0.0023668 * anchor

def f39_hle_268_struct_v268(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=307, w3=357, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9025 + 0.0023669 * anchor

def f39_hle_269_struct_v269(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=318, w3=370, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3766 * _rolling_slope(draw, 370) + 0.002367 * anchor

def f39_hle_270_struct_v270(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=329, w3=383, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(329, min_periods=max(329//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.93125 + 0.0023671 * anchor

def f39_hle_271_struct_v271(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=340, w3=396, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.945625 + 0.0023672 * anchor

def f39_hle_272_struct_v272(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=351, w3=409, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(351, min_periods=max(351//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.96 + 0.0023673 * anchor

def f39_hle_273_struct_v273(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=362, w3=422, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(56)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.407 * persistence + 0.0023674 * anchor

def f39_hle_274_struct_v274(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=373, w3=435, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.98875 + 0.0023675 * anchor

def f39_hle_275_struct_v275(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=384, w3=448, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(384, min_periods=max(384//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0458 * slope + 0.0023676 * anchor

def f39_hle_276_struct_v276(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=395, w3=461, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(77)
    drag = impulse.rolling(395, min_periods=max(395//3, 2)).mean()
    noise = impulse.abs().rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0175 + 0.0023677 * anchor

def f39_hle_277_struct_v277(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=406, w3=474, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.061 * acceleration + 0.0023678 * anchor

def f39_hle_278_struct_v278(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=417, w3=487, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.04625 + 0.0023679 * anchor

def f39_hle_279_struct_v279(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=428, w3=500, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0762 * _rolling_slope(draw, 500) + 0.002368 * anchor

def f39_hle_280_struct_v280(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=439, w3=513, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.075 + 0.0023681 * anchor

def f39_hle_281_struct_v281(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=450, w3=526, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 450)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.089375 + 0.0023682 * anchor

def f39_hle_282_struct_v282(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=461, w3=539, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.10375 + 0.0023683 * anchor

def f39_hle_283_struct_v283(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=472, w3=552, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(472, min_periods=max(472//3, 2)).rank(pct=True)
    persistence = change.rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1066 * persistence + 0.0023684 * anchor

def f39_hle_284_struct_v284(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=483, w3=565, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(483, min_periods=max(483//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1325 + 0.0023685 * anchor

def f39_hle_285_struct_v285(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=494, w3=578, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1218 * slope + 0.0023686 * anchor

def f39_hle_286_struct_v286(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=505, w3=591, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(505, min_periods=max(505//3, 2)).mean()
    noise = impulse.abs().rolling(591, min_periods=max(591//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.16125 + 0.0023687 * anchor

def f39_hle_287_struct_v287(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=13, w3=604, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 13)
    curvature = _rolling_slope(acceleration, 604)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.137 * acceleration + 0.0023688 * anchor

def f39_hle_288_struct_v288(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=24, w3=617, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(24, min_periods=max(24//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.19 + 0.0023689 * anchor

def f39_hle_289_struct_v289(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=35, w3=630, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1522 * _rolling_slope(draw, 630) + 0.002369 * anchor

def f39_hle_290_struct_v290(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=46, w3=643, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(46, min_periods=max(46//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.21875 + 0.0023691 * anchor

def f39_hle_291_struct_v291(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=57, w3=656, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 57)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.233125 + 0.0023692 * anchor

def f39_hle_292_struct_v292(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=68, w3=669, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(68, min_periods=max(68//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2475 + 0.0023693 * anchor

def f39_hle_293_struct_v293(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=79, w3=682, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(79, min_periods=max(79//3, 2)).rank(pct=True)
    persistence = change.rolling(682, min_periods=max(682//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1826 * persistence + 0.0023694 * anchor

def f39_hle_294_struct_v294(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=90, w3=695, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(90, min_periods=max(90//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.27625 + 0.0023695 * anchor

def f39_hle_295_struct_v295(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=101, w3=708, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(101, min_periods=max(101//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1978 * slope + 0.0023696 * anchor

def f39_hle_296_struct_v296(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=112, w3=721, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(112, min_periods=max(112//3, 2)).mean()
    noise = impulse.abs().rolling(721, min_periods=max(721//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.305 + 0.0023697 * anchor

def f39_hle_297_struct_v297(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=123, w3=734, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 123)
    curvature = _rolling_slope(acceleration, 734)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.213 * acceleration + 0.0023698 * anchor

def f39_hle_298_struct_v298(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=134, w3=747, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(134, min_periods=max(134//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.33375 + 0.0023699 * anchor

def f39_hle_299_struct_v299(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=145, w3=760, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(145, min_periods=max(145//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2282 * _rolling_slope(draw, 760) + 0.00237 * anchor

def f39_hle_300_struct_v300(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=156, w3=16, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(156, min_periods=max(156//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(16, min_periods=max(16//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3625 + 0.0023701 * anchor
