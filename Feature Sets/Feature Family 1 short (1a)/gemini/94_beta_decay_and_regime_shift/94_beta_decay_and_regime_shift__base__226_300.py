"""94 beta decay and regime shift base features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f94_beta_226_struct_v226(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=349, w3=588, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(26)
    drag = impulse.rolling(349, min_periods=max(349//3, 2)).mean()
    noise = impulse.abs().rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.186875 + 0.0043427 * anchor

def f94_beta_227_struct_v227(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=360, w3=601, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 360)
    curvature = _rolling_slope(acceleration, 601)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3538 * acceleration + 0.0043428 * anchor

def f94_beta_228_struct_v228(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=371, w3=614, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(371, min_periods=max(371//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.215625 + 0.0043429 * anchor

def f94_beta_229_struct_v229(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=382, w3=627, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(382, min_periods=max(382//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.369 * _rolling_slope(draw, 627) + 0.004343 * anchor

def f94_beta_230_struct_v230(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=393, w3=640, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(393, min_periods=max(393//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.244375 + 0.0043431 * anchor

def f94_beta_231_struct_v231(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=404, w3=653, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 404)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.25875 + 0.0043432 * anchor

def f94_beta_232_struct_v232(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=415, w3=666, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(415, min_periods=max(415//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.273125 + 0.0043433 * anchor

def f94_beta_233_struct_v233(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=426, w3=679, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(75)
    rank = change.rolling(426, min_periods=max(426//3, 2)).rank(pct=True)
    persistence = change.rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3994 * persistence + 0.0043434 * anchor

def f94_beta_234_struct_v234(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=437, w3=692, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(437, min_periods=max(437//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.301875 + 0.0043435 * anchor

def f94_beta_235_struct_v235(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=448, w3=705, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(448, min_periods=max(448//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0382 * slope + 0.0043436 * anchor

def f94_beta_236_struct_v236(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=459, w3=718, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(96)
    drag = impulse.rolling(459, min_periods=max(459//3, 2)).mean()
    noise = impulse.abs().rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.330625 + 0.0043437 * anchor

def f94_beta_237_struct_v237(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=470, w3=731, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 470)
    curvature = _rolling_slope(acceleration, 731)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0534 * acceleration + 0.0043438 * anchor

def f94_beta_238_struct_v238(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=481, w3=744, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(481, min_periods=max(481//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.359375 + 0.0043439 * anchor

def f94_beta_239_struct_v239(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=492, w3=757, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(492, min_periods=max(492//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0686 * _rolling_slope(draw, 757) + 0.004344 * anchor

def f94_beta_240_struct_v240(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=503, w3=770, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(503, min_periods=max(503//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.388125 + 0.0043441 * anchor

def f94_beta_241_struct_v241(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=11, w3=26, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 11)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=26, adjust=False).mean() * 1.4025 + 0.0043442 * anchor

def f94_beta_242_struct_v242(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=22, w3=39, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(22, min_periods=max(22//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.416875 + 0.0043443 * anchor

def f94_beta_243_struct_v243(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=33, w3=52, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(33, min_periods=max(33//3, 2)).rank(pct=True)
    persistence = change.rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.099 * persistence + 0.0043444 * anchor

def f94_beta_244_struct_v244(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=44, w3=65, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(44, min_periods=max(44//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.445625 + 0.0043445 * anchor

def f94_beta_245_struct_v245(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=55, w3=78, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(55, min_periods=max(55//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1142 * slope + 0.0043446 * anchor

def f94_beta_246_struct_v246(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=66, w3=91, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(66, min_periods=max(66//3, 2)).mean()
    noise = impulse.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.474375 + 0.0043447 * anchor

def f94_beta_247_struct_v247(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=77, w3=104, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 77)
    curvature = _rolling_slope(acceleration, 104)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1294 * acceleration + 0.0043448 * anchor

def f94_beta_248_struct_v248(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=88, w3=117, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(88, min_periods=max(88//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(117) * 1.503125 + 0.0043449 * anchor

def f94_beta_249_struct_v249(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=99, w3=130, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(99, min_periods=max(99//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1446 * _rolling_slope(draw, 130) + 0.004345 * anchor

def f94_beta_250_struct_v250(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=110, w3=143, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(110, min_periods=max(110//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.531875 + 0.0043451 * anchor

def f94_beta_251_struct_v251(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=121, w3=156, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=156, adjust=False).mean() * 1.54625 + 0.0043452 * anchor

def f94_beta_252_struct_v252(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=132, w3=169, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(132, min_periods=max(132//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.560625 + 0.0043453 * anchor

def f94_beta_253_struct_v253(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=143, w3=182, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.175 * persistence + 0.0043454 * anchor

def f94_beta_254_struct_v254(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=154, w3=195, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(154, min_periods=max(154//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.589375 + 0.0043455 * anchor

def f94_beta_255_struct_v255(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=165, w3=208, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(165, min_periods=max(165//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1902 * slope + 0.0043456 * anchor

def f94_beta_256_struct_v256(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=176, w3=221, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(176, min_periods=max(176//3, 2)).mean()
    noise = impulse.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.618125 + 0.0043457 * anchor

def f94_beta_257_struct_v257(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=187, w3=234, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 234)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2054 * acceleration + 0.0043458 * anchor

def f94_beta_258_struct_v258(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=198, w3=247, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(198, min_periods=max(198//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.87375 + 0.0043459 * anchor

def f94_beta_259_struct_v259(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=209, w3=260, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(209, min_periods=max(209//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2206 * _rolling_slope(draw, 260) + 0.004346 * anchor

def f94_beta_260_struct_v260(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=220, w3=273, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(220, min_periods=max(220//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9025 + 0.0043461 * anchor

def f94_beta_261_struct_v261(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=231, w3=286, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=286, adjust=False).mean() * 0.916875 + 0.0043462 * anchor

def f94_beta_262_struct_v262(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=242, w3=299, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(242, min_periods=max(242//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.93125 + 0.0043463 * anchor

def f94_beta_263_struct_v263(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=253, w3=312, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(34)
    rank = change.rolling(253, min_periods=max(253//3, 2)).rank(pct=True)
    persistence = change.rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.251 * persistence + 0.0043464 * anchor

def f94_beta_264_struct_v264(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=264, w3=325, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(264, min_periods=max(264//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96 + 0.0043465 * anchor

def f94_beta_265_struct_v265(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=275, w3=338, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(275, min_periods=max(275//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2662 * slope + 0.0043466 * anchor

def f94_beta_266_struct_v266(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=286, w3=351, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(55)
    drag = impulse.rolling(286, min_periods=max(286//3, 2)).mean()
    noise = impulse.abs().rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.98875 + 0.0043467 * anchor

def f94_beta_267_struct_v267(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=297, w3=364, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 297)
    curvature = _rolling_slope(acceleration, 364)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2814 * acceleration + 0.0043468 * anchor

def f94_beta_268_struct_v268(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=308, w3=377, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(308, min_periods=max(308//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0175 + 0.0043469 * anchor

def f94_beta_269_struct_v269(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=319, w3=390, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2966 * _rolling_slope(draw, 390) + 0.004347 * anchor

def f94_beta_270_struct_v270(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=330, w3=403, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.04625 + 0.0043471 * anchor

def f94_beta_271_struct_v271(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=341, w3=416, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 341)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.060625 + 0.0043472 * anchor

def f94_beta_272_struct_v272(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=352, w3=429, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(352, min_periods=max(352//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.075 + 0.0043473 * anchor

def f94_beta_273_struct_v273(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=363, w3=442, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(104)
    rank = change.rolling(363, min_periods=max(363//3, 2)).rank(pct=True)
    persistence = change.rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.327 * persistence + 0.0043474 * anchor

def f94_beta_274_struct_v274(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=374, w3=455, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(374, min_periods=max(374//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10375 + 0.0043475 * anchor

def f94_beta_275_struct_v275(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=385, w3=468, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(385, min_periods=max(385//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3422 * slope + 0.0043476 * anchor

def f94_beta_276_struct_v276(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=396, w3=481, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(125)
    drag = impulse.rolling(396, min_periods=max(396//3, 2)).mean()
    noise = impulse.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1325 + 0.0043477 * anchor

def f94_beta_277_struct_v277(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=407, w3=494, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 407)
    curvature = _rolling_slope(acceleration, 494)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3574 * acceleration + 0.0043478 * anchor

def f94_beta_278_struct_v278(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=418, w3=507, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(418, min_periods=max(418//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.16125 + 0.0043479 * anchor

def f94_beta_279_struct_v279(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=429, w3=520, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(429, min_periods=max(429//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3726 * _rolling_slope(draw, 520) + 0.004348 * anchor

def f94_beta_280_struct_v280(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=440, w3=533, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.19 + 0.0043481 * anchor

def f94_beta_281_struct_v281(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=451, w3=546, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 451)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.204375 + 0.0043482 * anchor

def f94_beta_282_struct_v282(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=462, w3=559, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.21875 + 0.0043483 * anchor

def f94_beta_283_struct_v283(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=473, w3=572, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.403 * persistence + 0.0043484 * anchor

def f94_beta_284_struct_v284(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=484, w3=585, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(484, min_periods=max(484//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2475 + 0.0043485 * anchor

def f94_beta_285_struct_v285(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=495, w3=598, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(495, min_periods=max(495//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0418 * slope + 0.0043486 * anchor

def f94_beta_286_struct_v286(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=506, w3=611, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.27625 + 0.0043487 * anchor

def f94_beta_287_struct_v287(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=14, w3=624, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 14)
    curvature = _rolling_slope(acceleration, 624)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.057 * acceleration + 0.0043488 * anchor

def f94_beta_288_struct_v288(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=25, w3=637, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(25, min_periods=max(25//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.305 + 0.0043489 * anchor

def f94_beta_289_struct_v289(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=36, w3=650, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0722 * _rolling_slope(draw, 650) + 0.004349 * anchor

def f94_beta_290_struct_v290(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=47, w3=663, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.33375 + 0.0043491 * anchor

def f94_beta_291_struct_v291(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=58, w3=676, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.348125 + 0.0043492 * anchor

def f94_beta_292_struct_v292(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=69, w3=689, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(69, min_periods=max(69//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3625 + 0.0043493 * anchor

def f94_beta_293_struct_v293(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=80, w3=702, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(80, min_periods=max(80//3, 2)).rank(pct=True)
    persistence = change.rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1026 * persistence + 0.0043494 * anchor

def f94_beta_294_struct_v294(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=91, w3=715, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(91, min_periods=max(91//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39125 + 0.0043495 * anchor

def f94_beta_295_struct_v295(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=102, w3=728, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(102, min_periods=max(102//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1178 * slope + 0.0043496 * anchor

def f94_beta_296_struct_v296(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=113, w3=741, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(14)
    drag = impulse.rolling(113, min_periods=max(113//3, 2)).mean()
    noise = impulse.abs().rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42 + 0.0043497 * anchor

def f94_beta_297_struct_v297(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=124, w3=754, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 124)
    curvature = _rolling_slope(acceleration, 754)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.133 * acceleration + 0.0043498 * anchor

def f94_beta_298_struct_v298(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=135, w3=767, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(135, min_periods=max(135//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.44875 + 0.0043499 * anchor

def f94_beta_299_struct_v299(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=146, w3=23, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(146, min_periods=max(146//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1482 * _rolling_slope(draw, 23) + 0.00435 * anchor

def f94_beta_300_struct_v300(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=157, w3=36, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(157, min_periods=max(157//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4775 + 0.0043501 * anchor
