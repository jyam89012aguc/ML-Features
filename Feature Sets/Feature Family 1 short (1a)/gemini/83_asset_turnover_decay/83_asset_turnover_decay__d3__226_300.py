"""83 asset turnover decay d3 third derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f83_atd_226_struct_v226_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=110, w2=44, w3=195, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(110)
    drag = impulse.rolling(44, min_periods=max(44//3, 2)).mean()
    noise = impulse.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.356875 + 0.0040427 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_227_struct_v227_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=117, w2=55, w3=208, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 55)
    curvature = _rolling_slope(acceleration, 208)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1378 * acceleration + 0.0040428 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_228_struct_v228_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=124, w2=66, w3=221, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(66, min_periods=max(66//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.385625 + 0.0040429 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_229_struct_v229_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=131, w2=77, w3=234, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(77, min_periods=max(77//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.153 * _rolling_slope(draw, 234) + 0.004043 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_230_struct_v230_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=138, w2=88, w3=247, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(88, min_periods=max(88//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.414375 + 0.0040431 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_231_struct_v231_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=99, w3=260, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 99)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=260, adjust=False).mean() * 1.42875 + 0.0040432 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_232_struct_v232_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=110, w3=273, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(110, min_periods=max(110//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.443125 + 0.0040433 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_233_struct_v233_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=121, w3=286, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(121, min_periods=max(121//3, 2)).rank(pct=True)
    persistence = change.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1834 * persistence + 0.0040434 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_234_struct_v234_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=132, w3=299, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(132, min_periods=max(132//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.471875 + 0.0040435 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_235_struct_v235_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=143, w3=312, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(143, min_periods=max(143//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1986 * slope + 0.0040436 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_236_struct_v236_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=154, w3=325, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(154, min_periods=max(154//3, 2)).mean()
    noise = impulse.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.500625 + 0.0040437 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_237_struct_v237_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=165, w3=338, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 165)
    curvature = _rolling_slope(acceleration, 338)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2138 * acceleration + 0.0040438 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_238_struct_v238_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=176, w3=351, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.529375 + 0.0040439 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_239_struct_v239_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=187, w3=364, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(187, min_periods=max(187//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.229 * _rolling_slope(draw, 364) + 0.004044 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_240_struct_v240_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=198, w3=377, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(198, min_periods=max(198//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.558125 + 0.0040441 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_241_struct_v241_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=209, w3=390, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.5725 + 0.0040442 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_242_struct_v242_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=220, w3=403, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(220, min_periods=max(220//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.586875 + 0.0040443 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_243_struct_v243_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=231, w3=416, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(231, min_periods=max(231//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2594 * persistence + 0.0040444 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_244_struct_v244_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=242, w3=429, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(242, min_periods=max(242//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.615625 + 0.0040445 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_245_struct_v245_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=253, w3=442, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(253, min_periods=max(253//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2746 * slope + 0.0040446 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_246_struct_v246_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=264, w3=455, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(264, min_periods=max(264//3, 2)).mean()
    noise = impulse.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87125 + 0.0040447 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_247_struct_v247_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=275, w3=468, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 275)
    curvature = _rolling_slope(acceleration, 468)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2898 * acceleration + 0.0040448 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_248_struct_v248_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=286, w3=481, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(286, min_periods=max(286//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9 + 0.0040449 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_249_struct_v249_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=297, w3=494, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(297, min_periods=max(297//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.305 * _rolling_slope(draw, 494) + 0.004045 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_250_struct_v250_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=308, w3=507, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(308, min_periods=max(308//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.92875 + 0.0040451 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_251_struct_v251_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=319, w3=520, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 319)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.943125 + 0.0040452 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_252_struct_v252_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=330, w3=533, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9575 + 0.0040453 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_253_struct_v253_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=341, w3=546, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(48)
    rank = change.rolling(341, min_periods=max(341//3, 2)).rank(pct=True)
    persistence = change.rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3354 * persistence + 0.0040454 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_254_struct_v254_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=352, w3=559, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(352, min_periods=max(352//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.98625 + 0.0040455 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_255_struct_v255_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=363, w3=572, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3506 * slope + 0.0040456 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_256_struct_v256_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=374, w3=585, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(69)
    drag = impulse.rolling(374, min_periods=max(374//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.015 + 0.0040457 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_257_struct_v257_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=385, w3=598, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 385)
    curvature = _rolling_slope(acceleration, 598)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3658 * acceleration + 0.0040458 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_258_struct_v258_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=396, w3=611, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(396, min_periods=max(396//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04375 + 0.0040459 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_259_struct_v259_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=407, w3=624, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(407, min_periods=max(407//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.381 * _rolling_slope(draw, 624) + 0.004046 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_260_struct_v260_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=418, w3=637, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(418, min_periods=max(418//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0725 + 0.0040461 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_261_struct_v261_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=429, w3=650, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 429)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.086875 + 0.0040462 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_262_struct_v262_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=440, w3=663, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.10125 + 0.0040463 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_263_struct_v263_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=451, w3=676, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(118)
    rank = change.rolling(451, min_periods=max(451//3, 2)).rank(pct=True)
    persistence = change.rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.035 * persistence + 0.0040464 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_264_struct_v264_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=462, w3=689, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.13 + 0.0040465 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_265_struct_v265_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=473, w3=702, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(473, min_periods=max(473//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0502 * slope + 0.0040466 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_266_struct_v266_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=484, w3=715, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(484, min_periods=max(484//3, 2)).mean()
    noise = impulse.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.15875 + 0.0040467 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_267_struct_v267_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=495, w3=728, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 495)
    curvature = _rolling_slope(acceleration, 728)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0654 * acceleration + 0.0040468 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_268_struct_v268_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=506, w3=741, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(506, min_periods=max(506//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1875 + 0.0040469 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_269_struct_v269_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=14, w3=754, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(14, min_periods=max(14//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0806 * _rolling_slope(draw, 754) + 0.004047 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_270_struct_v270_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=25, w3=767, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(25, min_periods=max(25//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.21625 + 0.0040471 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_271_struct_v271_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=36, w3=23, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 36)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=23, adjust=False).mean() * 1.230625 + 0.0040472 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_272_struct_v272_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=47, w3=36, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(47, min_periods=max(47//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.245 + 0.0040473 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_273_struct_v273_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=58, w3=49, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(58, min_periods=max(58//3, 2)).rank(pct=True)
    persistence = change.rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 0.0040474 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_274_struct_v274_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=69, w3=62, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(69, min_periods=max(69//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.27375 + 0.0040475 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_275_struct_v275_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=80, w3=75, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(80, min_periods=max(80//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1262 * slope + 0.0040476 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_276_struct_v276_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=91, w3=88, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(91, min_periods=max(91//3, 2)).mean()
    noise = impulse.abs().rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3025 + 0.0040477 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_277_struct_v277_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=102, w3=101, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 102)
    curvature = _rolling_slope(acceleration, 101)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1414 * acceleration + 0.0040478 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_278_struct_v278_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=113, w3=114, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(113, min_periods=max(113//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(114) * 1.33125 + 0.0040479 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_279_struct_v279_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=124, w3=127, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(124, min_periods=max(124//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1566 * _rolling_slope(draw, 127) + 0.004048 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_280_struct_v280_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=135, w3=140, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(135, min_periods=max(135//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36 + 0.0040481 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_281_struct_v281_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=146, w3=153, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 146)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=153, adjust=False).mean() * 1.374375 + 0.0040482 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_282_struct_v282_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=157, w3=166, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(157, min_periods=max(157//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.38875 + 0.0040483 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_283_struct_v283_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=168, w3=179, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(7)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.187 * persistence + 0.0040484 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_284_struct_v284_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=179, w3=192, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(179, min_periods=max(179//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4175 + 0.0040485 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_285_struct_v285_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=190, w3=205, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(190, min_periods=max(190//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2022 * slope + 0.0040486 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_286_struct_v286_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=201, w3=218, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(28)
    drag = impulse.rolling(201, min_periods=max(201//3, 2)).mean()
    noise = impulse.abs().rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.44625 + 0.0040487 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_287_struct_v287_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=212, w3=231, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 212)
    curvature = _rolling_slope(acceleration, 231)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2174 * acceleration + 0.0040488 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_288_struct_v288_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=223, w3=244, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(223, min_periods=max(223//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.475 + 0.0040489 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_289_struct_v289_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=234, w3=257, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(234, min_periods=max(234//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2326 * _rolling_slope(draw, 257) + 0.004049 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_290_struct_v290_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=245, w3=270, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(245, min_periods=max(245//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.50375 + 0.0040491 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_291_struct_v291_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=256, w3=283, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 256)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=283, adjust=False).mean() * 1.518125 + 0.0040492 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_292_struct_v292_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=267, w3=296, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(267, min_periods=max(267//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5325 + 0.0040493 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_293_struct_v293_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=278, w3=309, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(77)
    rank = change.rolling(278, min_periods=max(278//3, 2)).rank(pct=True)
    persistence = change.rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.263 * persistence + 0.0040494 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_294_struct_v294_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=289, w3=322, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(289, min_periods=max(289//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56125 + 0.0040495 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_295_struct_v295_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=300, w3=335, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(300, min_periods=max(300//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2782 * slope + 0.0040496 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_296_struct_v296_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=311, w3=348, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(98)
    drag = impulse.rolling(311, min_periods=max(311//3, 2)).mean()
    noise = impulse.abs().rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.59 + 0.0040497 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_297_struct_v297_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=322, w3=361, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 322)
    curvature = _rolling_slope(acceleration, 361)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2934 * acceleration + 0.0040498 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_298_struct_v298_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=333, w3=374, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.61875 + 0.0040499 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_299_struct_v299_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=344, w3=387, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(344, min_periods=max(344//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3086 * _rolling_slope(draw, 387) + 0.00405 * anchor
    return base_signal.diff().diff().diff()

def f83_atd_300_struct_v300_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=355, w3=400, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(355, min_periods=max(355//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(400, min_periods=max(400//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.874375 + 0.0040501 * anchor
    return base_signal.diff().diff().diff()
