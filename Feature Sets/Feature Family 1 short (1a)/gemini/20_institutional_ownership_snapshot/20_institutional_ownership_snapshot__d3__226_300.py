"""20 institutional ownership snapshot d3 third derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Ownership - Institutional-grade short-side signal.
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

def f20_inst_226_struct_v226_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=195, w3=740, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(195, min_periods=max(195//3, 2)).mean()
    noise = impulse.abs().rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.099375 + 0.0012227 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_227_struct_v227_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=206, w3=753, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 254)
    acceleration = _rolling_slope(velocity, 206)
    curvature = _rolling_slope(acceleration, 753)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3658 * acceleration + 0.0012228 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_228_struct_v228_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=217, w3=766, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(10, min_periods=max(10//3, 2)).mean(), upside.rolling(217, min_periods=max(217//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.128125 + 0.0012229 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_229_struct_v229_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=228, w3=22, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(228, min_periods=max(228//3, 2)).max()
    rebound = x - x.rolling(17, min_periods=max(17//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.381 * _rolling_slope(draw, 22) + 0.001223 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_230_struct_v230_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=239, w3=35, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(239, min_periods=max(239//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.156875 + 0.0012231 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_231_struct_v231_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=250, w3=48, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 31)
    slow = _rolling_slope(x, 250)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=48, adjust=False).mean() * 1.17125 + 0.0012232 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_232_struct_v232_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=261, w3=61, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(261, min_periods=max(261//3, 2)).max()
    trough = x.rolling(38, min_periods=max(38//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.185625 + 0.0012233 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_233_struct_v233_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=272, w3=74, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(45)
    rank = change.rolling(272, min_periods=max(272//3, 2)).rank(pct=True)
    persistence = change.rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.035 * persistence + 0.0012234 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_234_struct_v234_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=283, w3=87, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(52, min_periods=max(52//3, 2)).std()
    vol_slow = ret.rolling(283, min_periods=max(283//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.214375 + 0.0012235 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_235_struct_v235_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=294, w3=100, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 59)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0502 * slope + 0.0012236 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_236_struct_v236_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=305, w3=113, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(66)
    drag = impulse.rolling(305, min_periods=max(305//3, 2)).mean()
    noise = impulse.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.243125 + 0.0012237 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_237_struct_v237_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=316, w3=126, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 73)
    acceleration = _rolling_slope(velocity, 316)
    curvature = _rolling_slope(acceleration, 126)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0654 * acceleration + 0.0012238 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_238_struct_v238_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=327, w3=139, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(327, min_periods=max(327//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.271875 + 0.0012239 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_239_struct_v239_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=338, w3=152, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(338, min_periods=max(338//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0806 * _rolling_slope(draw, 152) + 0.001224 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_240_struct_v240_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=349, w3=165, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(349, min_periods=max(349//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.300625 + 0.0012241 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_241_struct_v241_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=360, w3=178, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 360)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=178, adjust=False).mean() * 1.315 + 0.0012242 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_242_struct_v242_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=371, w3=191, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.329375 + 0.0012243 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_243_struct_v243_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=382, w3=204, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(115)
    rank = change.rolling(382, min_periods=max(382//3, 2)).rank(pct=True)
    persistence = change.rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 0.0012244 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_244_struct_v244_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=393, w3=217, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(393, min_periods=max(393//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.358125 + 0.0012245 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_245_struct_v245_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=404, w3=230, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(404, min_periods=max(404//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1262 * slope + 0.0012246 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_246_struct_v246_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=415, w3=243, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(415, min_periods=max(415//3, 2)).mean()
    noise = impulse.abs().rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.386875 + 0.0012247 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_247_struct_v247_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=426, w3=256, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 426)
    curvature = _rolling_slope(acceleration, 256)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1414 * acceleration + 0.0012248 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_248_struct_v248_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=437, w3=269, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(437, min_periods=max(437//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.415625 + 0.0012249 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_249_struct_v249_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=448, w3=282, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(448, min_periods=max(448//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1566 * _rolling_slope(draw, 282) + 0.001225 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_250_struct_v250_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=459, w3=295, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(459, min_periods=max(459//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.444375 + 0.0012251 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_251_struct_v251_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=470, w3=308, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 470)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.45875 + 0.0012252 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_252_struct_v252_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=481, w3=321, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(481, min_periods=max(481//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.473125 + 0.0012253 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_253_struct_v253_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=492, w3=334, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(492, min_periods=max(492//3, 2)).rank(pct=True)
    persistence = change.rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.187 * persistence + 0.0012254 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_254_struct_v254_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=503, w3=347, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(503, min_periods=max(503//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.501875 + 0.0012255 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_255_struct_v255_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=11, w3=360, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(11, min_periods=max(11//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2022 * slope + 0.0012256 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_256_struct_v256_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=22, w3=373, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(22, min_periods=max(22//3, 2)).mean()
    noise = impulse.abs().rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.530625 + 0.0012257 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_257_struct_v257_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=213, w2=33, w3=386, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 33)
    curvature = _rolling_slope(acceleration, 386)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2174 * acceleration + 0.0012258 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_258_struct_v258_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=220, w2=44, w3=399, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(44, min_periods=max(44//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.559375 + 0.0012259 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_259_struct_v259_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=227, w2=55, w3=412, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(55, min_periods=max(55//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2326 * _rolling_slope(draw, 412) + 0.001226 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_260_struct_v260_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=234, w2=66, w3=425, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.588125 + 0.0012261 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_261_struct_v261_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=241, w2=77, w3=438, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 77)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.6025 + 0.0012262 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_262_struct_v262_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=248, w2=88, w3=451, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(88, min_periods=max(88//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.616875 + 0.0012263 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_263_struct_v263_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=255, w2=99, w3=464, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(99, min_periods=max(99//3, 2)).rank(pct=True)
    persistence = change.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.263 * persistence + 0.0012264 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_264_struct_v264_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=11, w2=110, w3=477, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(11, min_periods=max(11//3, 2)).std()
    vol_slow = ret.rolling(110, min_periods=max(110//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8725 + 0.0012265 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_265_struct_v265_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=18, w2=121, w3=490, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(121, min_periods=max(121//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 18)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2782 * slope + 0.0012266 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_266_struct_v266_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=25, w2=132, w3=503, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(25)
    drag = impulse.rolling(132, min_periods=max(132//3, 2)).mean()
    noise = impulse.abs().rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.90125 + 0.0012267 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_267_struct_v267_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=32, w2=143, w3=516, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 32)
    acceleration = _rolling_slope(velocity, 143)
    curvature = _rolling_slope(acceleration, 516)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2934 * acceleration + 0.0012268 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_268_struct_v268_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=39, w2=154, w3=529, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(154, min_periods=max(154//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93 + 0.0012269 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_269_struct_v269_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=46, w2=165, w3=542, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(165, min_periods=max(165//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3086 * _rolling_slope(draw, 542) + 0.001227 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_270_struct_v270_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=53, w2=176, w3=555, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(176, min_periods=max(176//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.95875 + 0.0012271 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_271_struct_v271_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=60, w2=187, w3=568, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 187)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.973125 + 0.0012272 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_272_struct_v272_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=67, w2=198, w3=581, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(198, min_periods=max(198//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9875 + 0.0012273 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_273_struct_v273_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=74, w2=209, w3=594, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(74)
    rank = change.rolling(209, min_periods=max(209//3, 2)).rank(pct=True)
    persistence = change.rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.339 * persistence + 0.0012274 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_274_struct_v274_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=81, w2=220, w3=607, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(220, min_periods=max(220//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01625 + 0.0012275 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_275_struct_v275_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=88, w2=231, w3=620, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(231, min_periods=max(231//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3542 * slope + 0.0012276 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_276_struct_v276_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=95, w2=242, w3=633, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(95)
    drag = impulse.rolling(242, min_periods=max(242//3, 2)).mean()
    noise = impulse.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.045 + 0.0012277 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_277_struct_v277_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=102, w2=253, w3=646, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 253)
    curvature = _rolling_slope(acceleration, 646)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3694 * acceleration + 0.0012278 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_278_struct_v278_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=109, w2=264, w3=659, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(264, min_periods=max(264//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.07375 + 0.0012279 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_279_struct_v279_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=116, w2=275, w3=672, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(275, min_periods=max(275//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3846 * _rolling_slope(draw, 672) + 0.001228 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_280_struct_v280_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=123, w2=286, w3=685, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 123)
    baseline = trend.rolling(286, min_periods=max(286//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1025 + 0.0012281 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_281_struct_v281_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=130, w2=297, w3=698, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 130)
    slow = _rolling_slope(x, 297)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.116875 + 0.0012282 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_282_struct_v282_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=137, w2=308, w3=711, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(308, min_periods=max(308//3, 2)).max()
    trough = x.rolling(137, min_periods=max(137//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.13125 + 0.0012283 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_283_struct_v283_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=144, w2=319, w3=724, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(319, min_periods=max(319//3, 2)).rank(pct=True)
    persistence = change.rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0386 * persistence + 0.0012284 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_284_struct_v284_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=151, w2=330, w3=737, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(151, min_periods=max(151//3, 2)).std()
    vol_slow = ret.rolling(330, min_periods=max(330//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16 + 0.0012285 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_285_struct_v285_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=158, w2=341, w3=750, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(341, min_periods=max(341//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 158)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0538 * slope + 0.0012286 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_286_struct_v286_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=165, w2=352, w3=763, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(352, min_periods=max(352//3, 2)).mean()
    noise = impulse.abs().rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.18875 + 0.0012287 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_287_struct_v287_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=172, w2=363, w3=19, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 172)
    acceleration = _rolling_slope(velocity, 363)
    curvature = _rolling_slope(acceleration, 19)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.069 * acceleration + 0.0012288 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_288_struct_v288_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=179, w2=374, w3=32, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(374, min_periods=max(374//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(32) * 1.2175 + 0.0012289 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_289_struct_v289_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=186, w2=385, w3=45, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(385, min_periods=max(385//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0842 * _rolling_slope(draw, 45) + 0.001229 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_290_struct_v290_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=193, w2=396, w3=58, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 193)
    baseline = trend.rolling(396, min_periods=max(396//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24625 + 0.0012291 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_291_struct_v291_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=200, w2=407, w3=71, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 407)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=71, adjust=False).mean() * 1.260625 + 0.0012292 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_292_struct_v292_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=207, w2=418, w3=84, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(418, min_periods=max(418//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.275 + 0.0012293 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_293_struct_v293_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=214, w2=429, w3=97, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(429, min_periods=max(429//3, 2)).rank(pct=True)
    persistence = change.rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1146 * persistence + 0.0012294 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_294_struct_v294_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=221, w2=440, w3=110, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(440, min_periods=max(440//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30375 + 0.0012295 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_295_struct_v295_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=228, w2=451, w3=123, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(451, min_periods=max(451//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1298 * slope + 0.0012296 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_296_struct_v296_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=235, w2=462, w3=136, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(462, min_periods=max(462//3, 2)).mean()
    noise = impulse.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3325 + 0.0012297 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_297_struct_v297_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=242, w2=473, w3=149, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 473)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.145 * acceleration + 0.0012298 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_298_struct_v298_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=249, w2=484, w3=162, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(484, min_periods=max(484//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.36125 + 0.0012299 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_299_struct_v299_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=5, w2=495, w3=175, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(495, min_periods=max(495//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1602 * _rolling_slope(draw, 175) + 0.00123 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_300_struct_v300_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=12, w2=506, w3=188, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(506, min_periods=max(506//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.39 + 0.0012301 * anchor
    return base_signal.diff().diff().diff()
