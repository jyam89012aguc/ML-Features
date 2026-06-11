"""43 hypergrowth deceleration cliff d2 second derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f43_hdc_226_struct_v226_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=145, w2=150, w3=204, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.901875 + 0.0026627 * anchor
    return base_signal.diff().diff()

def f43_hdc_227_struct_v227_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=152, w2=161, w3=217, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 161)
    curvature = _rolling_slope(acceleration, 217)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2734 * acceleration + 0.0026628 * anchor
    return base_signal.diff().diff()

def f43_hdc_228_struct_v228_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=159, w2=172, w3=230, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(172, min_periods=max(172//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.930625 + 0.0026629 * anchor
    return base_signal.diff().diff()

def f43_hdc_229_struct_v229_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=166, w2=183, w3=243, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(183, min_periods=max(183//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2886 * _rolling_slope(draw, 243) + 0.002663 * anchor
    return base_signal.diff().diff()

def f43_hdc_230_struct_v230_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=173, w2=194, w3=256, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(194, min_periods=max(194//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.959375 + 0.0026631 * anchor
    return base_signal.diff().diff()

def f43_hdc_231_struct_v231_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=180, w2=205, w3=269, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 205)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=269, adjust=False).mean() * 0.97375 + 0.0026632 * anchor
    return base_signal.diff().diff()

def f43_hdc_232_struct_v232_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=187, w2=216, w3=282, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(216, min_periods=max(216//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.988125 + 0.0026633 * anchor
    return base_signal.diff().diff()

def f43_hdc_233_struct_v233_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=194, w2=227, w3=295, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(227, min_periods=max(227//3, 2)).rank(pct=True)
    persistence = change.rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319 * persistence + 0.0026634 * anchor
    return base_signal.diff().diff()

def f43_hdc_234_struct_v234_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=201, w2=238, w3=308, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(238, min_periods=max(238//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.016875 + 0.0026635 * anchor
    return base_signal.diff().diff()

def f43_hdc_235_struct_v235_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=208, w2=249, w3=321, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(249, min_periods=max(249//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3342 * slope + 0.0026636 * anchor
    return base_signal.diff().diff()

def f43_hdc_236_struct_v236_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=215, w2=260, w3=334, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(260, min_periods=max(260//3, 2)).mean()
    noise = impulse.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.045625 + 0.0026637 * anchor
    return base_signal.diff().diff()

def f43_hdc_237_struct_v237_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=222, w2=271, w3=347, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 271)
    curvature = _rolling_slope(acceleration, 347)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3494 * acceleration + 0.0026638 * anchor
    return base_signal.diff().diff()

def f43_hdc_238_struct_v238_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=229, w2=282, w3=360, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.074375 + 0.0026639 * anchor
    return base_signal.diff().diff()

def f43_hdc_239_struct_v239_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=236, w2=293, w3=373, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(293, min_periods=max(293//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3646 * _rolling_slope(draw, 373) + 0.002664 * anchor
    return base_signal.diff().diff()

def f43_hdc_240_struct_v240_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=243, w2=304, w3=386, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.103125 + 0.0026641 * anchor
    return base_signal.diff().diff()

def f43_hdc_241_struct_v241_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=250, w2=315, w3=399, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 315)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1175 + 0.0026642 * anchor
    return base_signal.diff().diff()

def f43_hdc_242_struct_v242_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=6, w2=326, w3=412, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(326, min_periods=max(326//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.131875 + 0.0026643 * anchor
    return base_signal.diff().diff()

def f43_hdc_243_struct_v243_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=13, w2=337, w3=425, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(13)
    rank = change.rolling(337, min_periods=max(337//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.395 * persistence + 0.0026644 * anchor
    return base_signal.diff().diff()

def f43_hdc_244_struct_v244_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=20, w2=348, w3=438, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(348, min_periods=max(348//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.160625 + 0.0026645 * anchor
    return base_signal.diff().diff()

def f43_hdc_245_struct_v245_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=27, w2=359, w3=451, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(359, min_periods=max(359//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4102 * slope + 0.0026646 * anchor
    return base_signal.diff().diff()

def f43_hdc_246_struct_v246_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=34, w2=370, w3=464, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(34)
    drag = impulse.rolling(370, min_periods=max(370//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.189375 + 0.0026647 * anchor
    return base_signal.diff().diff()

def f43_hdc_247_struct_v247_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=41, w2=381, w3=477, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 41)
    acceleration = _rolling_slope(velocity, 381)
    curvature = _rolling_slope(acceleration, 477)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.049 * acceleration + 0.0026648 * anchor
    return base_signal.diff().diff()

def f43_hdc_248_struct_v248_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=48, w2=392, w3=490, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(48, min_periods=max(48//3, 2)).mean(), upside.rolling(392, min_periods=max(392//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.218125 + 0.0026649 * anchor
    return base_signal.diff().diff()

def f43_hdc_249_struct_v249_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=55, w2=403, w3=503, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(403, min_periods=max(403//3, 2)).max()
    rebound = x - x.rolling(55, min_periods=max(55//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0642 * _rolling_slope(draw, 503) + 0.002665 * anchor
    return base_signal.diff().diff()

def f43_hdc_250_struct_v250_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=62, w2=414, w3=516, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 62)
    baseline = trend.rolling(414, min_periods=max(414//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.246875 + 0.0026651 * anchor
    return base_signal.diff().diff()

def f43_hdc_251_struct_v251_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=69, w2=425, w3=529, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 69)
    slow = _rolling_slope(x, 425)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.26125 + 0.0026652 * anchor
    return base_signal.diff().diff()

def f43_hdc_252_struct_v252_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=76, w2=436, w3=542, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(76, min_periods=max(76//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.275625 + 0.0026653 * anchor
    return base_signal.diff().diff()

def f43_hdc_253_struct_v253_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=83, w2=447, w3=555, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(83)
    rank = change.rolling(447, min_periods=max(447//3, 2)).rank(pct=True)
    persistence = change.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0946 * persistence + 0.0026654 * anchor
    return base_signal.diff().diff()

def f43_hdc_254_struct_v254_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=90, w2=458, w3=568, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(90, min_periods=max(90//3, 2)).std()
    vol_slow = ret.rolling(458, min_periods=max(458//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.304375 + 0.0026655 * anchor
    return base_signal.diff().diff()

def f43_hdc_255_struct_v255_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=97, w2=469, w3=581, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(469, min_periods=max(469//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 97)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1098 * slope + 0.0026656 * anchor
    return base_signal.diff().diff()

def f43_hdc_256_struct_v256_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=104, w2=480, w3=594, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(104)
    drag = impulse.rolling(480, min_periods=max(480//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.333125 + 0.0026657 * anchor
    return base_signal.diff().diff()

def f43_hdc_257_struct_v257_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=111, w2=491, w3=607, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 111)
    acceleration = _rolling_slope(velocity, 491)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125 * acceleration + 0.0026658 * anchor
    return base_signal.diff().diff()

def f43_hdc_258_struct_v258_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=118, w2=502, w3=620, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(502, min_periods=max(502//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.361875 + 0.0026659 * anchor
    return base_signal.diff().diff()

def f43_hdc_259_struct_v259_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=125, w2=10, w3=633, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(10, min_periods=max(10//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1402 * _rolling_slope(draw, 633) + 0.002666 * anchor
    return base_signal.diff().diff()

def f43_hdc_260_struct_v260_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=132, w2=21, w3=646, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(21, min_periods=max(21//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.390625 + 0.0026661 * anchor
    return base_signal.diff().diff()

def f43_hdc_261_struct_v261_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=139, w2=32, w3=659, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 32)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.405 + 0.0026662 * anchor
    return base_signal.diff().diff()

def f43_hdc_262_struct_v262_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=146, w2=43, w3=672, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(43, min_periods=max(43//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.419375 + 0.0026663 * anchor
    return base_signal.diff().diff()

def f43_hdc_263_struct_v263_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=153, w2=54, w3=685, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(54, min_periods=max(54//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1706 * persistence + 0.0026664 * anchor
    return base_signal.diff().diff()

def f43_hdc_264_struct_v264_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=160, w2=65, w3=698, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(65, min_periods=max(65//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.448125 + 0.0026665 * anchor
    return base_signal.diff().diff()

def f43_hdc_265_struct_v265_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=167, w2=76, w3=711, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(76, min_periods=max(76//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1858 * slope + 0.0026666 * anchor
    return base_signal.diff().diff()

def f43_hdc_266_struct_v266_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=174, w2=87, w3=724, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(87, min_periods=max(87//3, 2)).mean()
    noise = impulse.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.476875 + 0.0026667 * anchor
    return base_signal.diff().diff()

def f43_hdc_267_struct_v267_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=181, w2=98, w3=737, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 737)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.201 * acceleration + 0.0026668 * anchor
    return base_signal.diff().diff()

def f43_hdc_268_struct_v268_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=188, w2=109, w3=750, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(109, min_periods=max(109//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.505625 + 0.0026669 * anchor
    return base_signal.diff().diff()

def f43_hdc_269_struct_v269_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=195, w2=120, w3=763, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2162 * _rolling_slope(draw, 763) + 0.002667 * anchor
    return base_signal.diff().diff()

def f43_hdc_270_struct_v270_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=202, w2=131, w3=19, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(131, min_periods=max(131//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.534375 + 0.0026671 * anchor
    return base_signal.diff().diff()

def f43_hdc_271_struct_v271_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=209, w2=142, w3=32, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 1.54875 + 0.0026672 * anchor
    return base_signal.diff().diff()

def f43_hdc_272_struct_v272_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=216, w2=153, w3=45, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(153, min_periods=max(153//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.563125 + 0.0026673 * anchor
    return base_signal.diff().diff()

def f43_hdc_273_struct_v273_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=223, w2=164, w3=58, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(164, min_periods=max(164//3, 2)).rank(pct=True)
    persistence = change.rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2466 * persistence + 0.0026674 * anchor
    return base_signal.diff().diff()

def f43_hdc_274_struct_v274_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=230, w2=175, w3=71, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.591875 + 0.0026675 * anchor
    return base_signal.diff().diff()

def f43_hdc_275_struct_v275_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=237, w2=186, w3=84, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(186, min_periods=max(186//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2618 * slope + 0.0026676 * anchor
    return base_signal.diff().diff()

def f43_hdc_276_struct_v276_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=244, w2=197, w3=97, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(197, min_periods=max(197//3, 2)).mean()
    noise = impulse.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.620625 + 0.0026677 * anchor
    return base_signal.diff().diff()

def f43_hdc_277_struct_v277_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=251, w2=208, w3=110, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 208)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.277 * acceleration + 0.0026678 * anchor
    return base_signal.diff().diff()

def f43_hdc_278_struct_v278_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=7, w2=219, w3=123, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(219, min_periods=max(219//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(123) * 0.87625 + 0.0026679 * anchor
    return base_signal.diff().diff()

def f43_hdc_279_struct_v279_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=14, w2=230, w3=136, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(230, min_periods=max(230//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2922 * _rolling_slope(draw, 136) + 0.002668 * anchor
    return base_signal.diff().diff()

def f43_hdc_280_struct_v280_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=21, w2=241, w3=149, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(241, min_periods=max(241//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.905 + 0.0026681 * anchor
    return base_signal.diff().diff()

def f43_hdc_281_struct_v281_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=28, w2=252, w3=162, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 252)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=162, adjust=False).mean() * 0.919375 + 0.0026682 * anchor
    return base_signal.diff().diff()

def f43_hdc_282_struct_v282_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=35, w2=263, w3=175, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(263, min_periods=max(263//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.93375 + 0.0026683 * anchor
    return base_signal.diff().diff()

def f43_hdc_283_struct_v283_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=42, w2=274, w3=188, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(42)
    rank = change.rolling(274, min_periods=max(274//3, 2)).rank(pct=True)
    persistence = change.rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3226 * persistence + 0.0026684 * anchor
    return base_signal.diff().diff()

def f43_hdc_284_struct_v284_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=49, w2=285, w3=201, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(285, min_periods=max(285//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9625 + 0.0026685 * anchor
    return base_signal.diff().diff()

def f43_hdc_285_struct_v285_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=56, w2=296, w3=214, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(296, min_periods=max(296//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3378 * slope + 0.0026686 * anchor
    return base_signal.diff().diff()

def f43_hdc_286_struct_v286_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=63, w2=307, w3=227, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(63)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.99125 + 0.0026687 * anchor
    return base_signal.diff().diff()

def f43_hdc_287_struct_v287_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=70, w2=318, w3=240, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 318)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.353 * acceleration + 0.0026688 * anchor
    return base_signal.diff().diff()

def f43_hdc_288_struct_v288_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=77, w2=329, w3=253, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.02 + 0.0026689 * anchor
    return base_signal.diff().diff()

def f43_hdc_289_struct_v289_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=84, w2=340, w3=266, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3682 * _rolling_slope(draw, 266) + 0.002669 * anchor
    return base_signal.diff().diff()

def f43_hdc_290_struct_v290_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=91, w2=351, w3=279, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(351, min_periods=max(351//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04875 + 0.0026691 * anchor
    return base_signal.diff().diff()

def f43_hdc_291_struct_v291_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=98, w2=362, w3=292, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 362)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=292, adjust=False).mean() * 1.063125 + 0.0026692 * anchor
    return base_signal.diff().diff()

def f43_hdc_292_struct_v292_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=105, w2=373, w3=305, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(373, min_periods=max(373//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0775 + 0.0026693 * anchor
    return base_signal.diff().diff()

def f43_hdc_293_struct_v293_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=112, w2=384, w3=318, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(112)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3986 * persistence + 0.0026694 * anchor
    return base_signal.diff().diff()

def f43_hdc_294_struct_v294_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=119, w2=395, w3=331, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10625 + 0.0026695 * anchor
    return base_signal.diff().diff()

def f43_hdc_295_struct_v295_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=126, w2=406, w3=344, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(406, min_periods=max(406//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0374 * slope + 0.0026696 * anchor
    return base_signal.diff().diff()

def f43_hdc_296_struct_v296_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=133, w2=417, w3=357, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.135 + 0.0026697 * anchor
    return base_signal.diff().diff()

def f43_hdc_297_struct_v297_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=140, w2=428, w3=370, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 428)
    curvature = _rolling_slope(acceleration, 370)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0526 * acceleration + 0.0026698 * anchor
    return base_signal.diff().diff()

def f43_hdc_298_struct_v298_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=147, w2=439, w3=383, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.16375 + 0.0026699 * anchor
    return base_signal.diff().diff()

def f43_hdc_299_struct_v299_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=154, w2=450, w3=396, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(450, min_periods=max(450//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0678 * _rolling_slope(draw, 396) + 0.00267 * anchor
    return base_signal.diff().diff()

def f43_hdc_300_struct_v300_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=161, w2=461, w3=409, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1925 + 0.0026701 * anchor
    return base_signal.diff().diff()
