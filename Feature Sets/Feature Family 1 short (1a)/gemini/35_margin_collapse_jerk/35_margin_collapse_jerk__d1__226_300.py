"""35 margin collapse jerk d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f35_mcj_226_struct_v226_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=104, w3=405, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3625 + 0.0021227 * anchor
    return base_signal.diff()

def f35_mcj_227_struct_v227_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=115, w3=418, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 253)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 418)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.261 * acceleration + 0.0021228 * anchor
    return base_signal.diff()

def f35_mcj_228_struct_v228_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=126, w3=431, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.39125 + 0.0021229 * anchor
    return base_signal.diff()

def f35_mcj_229_struct_v229_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=137, w3=444, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2762 * _rolling_slope(draw, 444) + 0.002123 * anchor
    return base_signal.diff()

def f35_mcj_230_struct_v230_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=148, w3=457, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.42 + 0.0021231 * anchor
    return base_signal.diff()

def f35_mcj_231_struct_v231_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=159, w3=470, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.434375 + 0.0021232 * anchor
    return base_signal.diff()

def f35_mcj_232_struct_v232_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=170, w3=483, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44875 + 0.0021233 * anchor
    return base_signal.diff()

def f35_mcj_233_struct_v233_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=181, w3=496, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(44)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3066 * persistence + 0.0021234 * anchor
    return base_signal.diff()

def f35_mcj_234_struct_v234_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=192, w3=509, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(192, min_periods=max(192//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4775 + 0.0021235 * anchor
    return base_signal.diff()

def f35_mcj_235_struct_v235_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=203, w3=522, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3218 * slope + 0.0021236 * anchor
    return base_signal.diff()

def f35_mcj_236_struct_v236_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=214, w3=535, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(65)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.50625 + 0.0021237 * anchor
    return base_signal.diff()

def f35_mcj_237_struct_v237_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=225, w3=548, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 548)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.337 * acceleration + 0.0021238 * anchor
    return base_signal.diff()

def f35_mcj_238_struct_v238_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=236, w3=561, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.535 + 0.0021239 * anchor
    return base_signal.diff()

def f35_mcj_239_struct_v239_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=247, w3=574, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(247, min_periods=max(247//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3522 * _rolling_slope(draw, 574) + 0.002124 * anchor
    return base_signal.diff()

def f35_mcj_240_struct_v240_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=258, w3=587, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(258, min_periods=max(258//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.56375 + 0.0021241 * anchor
    return base_signal.diff()

def f35_mcj_241_struct_v241_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=269, w3=600, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.578125 + 0.0021242 * anchor
    return base_signal.diff()

def f35_mcj_242_struct_v242_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=280, w3=613, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5925 + 0.0021243 * anchor
    return base_signal.diff()

def f35_mcj_243_struct_v243_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=291, w3=626, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(114)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3826 * persistence + 0.0021244 * anchor
    return base_signal.diff()

def f35_mcj_244_struct_v244_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=302, w3=639, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(302, min_periods=max(302//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.62125 + 0.0021245 * anchor
    return base_signal.diff()

def f35_mcj_245_struct_v245_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=313, w3=652, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(313, min_periods=max(313//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3978 * slope + 0.0021246 * anchor
    return base_signal.diff()

def f35_mcj_246_struct_v246_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=324, w3=665, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(324, min_periods=max(324//3, 2)).mean()
    noise = impulse.abs().rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.876875 + 0.0021247 * anchor
    return base_signal.diff()

def f35_mcj_247_struct_v247_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=335, w3=678, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 335)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0366 * acceleration + 0.0021248 * anchor
    return base_signal.diff()

def f35_mcj_248_struct_v248_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=346, w3=691, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.905625 + 0.0021249 * anchor
    return base_signal.diff()

def f35_mcj_249_struct_v249_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=357, w3=704, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(357, min_periods=max(357//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0518 * _rolling_slope(draw, 704) + 0.002125 * anchor
    return base_signal.diff()

def f35_mcj_250_struct_v250_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=368, w3=717, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.934375 + 0.0021251 * anchor
    return base_signal.diff()

def f35_mcj_251_struct_v251_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=379, w3=730, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 379)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.94875 + 0.0021252 * anchor
    return base_signal.diff()

def f35_mcj_252_struct_v252_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=390, w3=743, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.963125 + 0.0021253 * anchor
    return base_signal.diff()

def f35_mcj_253_struct_v253_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=401, w3=756, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(401, min_periods=max(401//3, 2)).rank(pct=True)
    persistence = change.rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0822 * persistence + 0.0021254 * anchor
    return base_signal.diff()

def f35_mcj_254_struct_v254_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=412, w3=769, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(412, min_periods=max(412//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.991875 + 0.0021255 * anchor
    return base_signal.diff()

def f35_mcj_255_struct_v255_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=423, w3=25, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(423, min_periods=max(423//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0974 * slope + 0.0021256 * anchor
    return base_signal.diff()

def f35_mcj_256_struct_v256_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=434, w3=38, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.020625 + 0.0021257 * anchor
    return base_signal.diff()

def f35_mcj_257_struct_v257_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=445, w3=51, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 445)
    curvature = _rolling_slope(acceleration, 51)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1126 * acceleration + 0.0021258 * anchor
    return base_signal.diff()

def f35_mcj_258_struct_v258_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=456, w3=64, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(456, min_periods=max(456//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(64) * 1.049375 + 0.0021259 * anchor
    return base_signal.diff()

def f35_mcj_259_struct_v259_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=467, w3=77, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(467, min_periods=max(467//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1278 * _rolling_slope(draw, 77) + 0.002126 * anchor
    return base_signal.diff()

def f35_mcj_260_struct_v260_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=478, w3=90, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.078125 + 0.0021261 * anchor
    return base_signal.diff()

def f35_mcj_261_struct_v261_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=489, w3=103, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 489)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=103, adjust=False).mean() * 1.0925 + 0.0021262 * anchor
    return base_signal.diff()

def f35_mcj_262_struct_v262_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=500, w3=116, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(500, min_periods=max(500//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.106875 + 0.0021263 * anchor
    return base_signal.diff()

def f35_mcj_263_struct_v263_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=511, w3=129, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(511, min_periods=max(511//3, 2)).rank(pct=True)
    persistence = change.rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1582 * persistence + 0.0021264 * anchor
    return base_signal.diff()

def f35_mcj_264_struct_v264_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=19, w3=142, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(19, min_periods=max(19//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.135625 + 0.0021265 * anchor
    return base_signal.diff()

def f35_mcj_265_struct_v265_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=30, w3=155, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(30, min_periods=max(30//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1734 * slope + 0.0021266 * anchor
    return base_signal.diff()

def f35_mcj_266_struct_v266_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=41, w3=168, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(24)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.164375 + 0.0021267 * anchor
    return base_signal.diff()

def f35_mcj_267_struct_v267_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=52, w3=181, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 52)
    curvature = _rolling_slope(acceleration, 181)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1886 * acceleration + 0.0021268 * anchor
    return base_signal.diff()

def f35_mcj_268_struct_v268_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=63, w3=194, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(63, min_periods=max(63//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.193125 + 0.0021269 * anchor
    return base_signal.diff()

def f35_mcj_269_struct_v269_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=74, w3=207, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(74, min_periods=max(74//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2038 * _rolling_slope(draw, 207) + 0.002127 * anchor
    return base_signal.diff()

def f35_mcj_270_struct_v270_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=85, w3=220, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(85, min_periods=max(85//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.221875 + 0.0021271 * anchor
    return base_signal.diff()

def f35_mcj_271_struct_v271_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=96, w3=233, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=233, adjust=False).mean() * 1.23625 + 0.0021272 * anchor
    return base_signal.diff()

def f35_mcj_272_struct_v272_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=107, w3=246, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(107, min_periods=max(107//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.250625 + 0.0021273 * anchor
    return base_signal.diff()

def f35_mcj_273_struct_v273_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=118, w3=259, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(73)
    rank = change.rolling(118, min_periods=max(118//3, 2)).rank(pct=True)
    persistence = change.rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2342 * persistence + 0.0021274 * anchor
    return base_signal.diff()

def f35_mcj_274_struct_v274_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=129, w3=272, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(129, min_periods=max(129//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.279375 + 0.0021275 * anchor
    return base_signal.diff()

def f35_mcj_275_struct_v275_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=140, w3=285, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(140, min_periods=max(140//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2494 * slope + 0.0021276 * anchor
    return base_signal.diff()

def f35_mcj_276_struct_v276_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=151, w3=298, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(94)
    drag = impulse.rolling(151, min_periods=max(151//3, 2)).mean()
    noise = impulse.abs().rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.308125 + 0.0021277 * anchor
    return base_signal.diff()

def f35_mcj_277_struct_v277_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=162, w3=311, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 162)
    curvature = _rolling_slope(acceleration, 311)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2646 * acceleration + 0.0021278 * anchor
    return base_signal.diff()

def f35_mcj_278_struct_v278_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=173, w3=324, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.336875 + 0.0021279 * anchor
    return base_signal.diff()

def f35_mcj_279_struct_v279_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=184, w3=337, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2798 * _rolling_slope(draw, 337) + 0.002128 * anchor
    return base_signal.diff()

def f35_mcj_280_struct_v280_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=195, w3=350, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(195, min_periods=max(195//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.365625 + 0.0021281 * anchor
    return base_signal.diff()

def f35_mcj_281_struct_v281_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=206, w3=363, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 206)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.38 + 0.0021282 * anchor
    return base_signal.diff()

def f35_mcj_282_struct_v282_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=217, w3=376, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.394375 + 0.0021283 * anchor
    return base_signal.diff()

def f35_mcj_283_struct_v283_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=228, w3=389, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(228, min_periods=max(228//3, 2)).rank(pct=True)
    persistence = change.rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3102 * persistence + 0.0021284 * anchor
    return base_signal.diff()

def f35_mcj_284_struct_v284_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=239, w3=402, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.423125 + 0.0021285 * anchor
    return base_signal.diff()

def f35_mcj_285_struct_v285_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=250, w3=415, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(250, min_periods=max(250//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3254 * slope + 0.0021286 * anchor
    return base_signal.diff()

def f35_mcj_286_struct_v286_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=261, w3=428, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(261, min_periods=max(261//3, 2)).mean()
    noise = impulse.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.451875 + 0.0021287 * anchor
    return base_signal.diff()

def f35_mcj_287_struct_v287_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=272, w3=441, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 272)
    curvature = _rolling_slope(acceleration, 441)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3406 * acceleration + 0.0021288 * anchor
    return base_signal.diff()

def f35_mcj_288_struct_v288_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=283, w3=454, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(283, min_periods=max(283//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.480625 + 0.0021289 * anchor
    return base_signal.diff()

def f35_mcj_289_struct_v289_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=294, w3=467, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(294, min_periods=max(294//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3558 * _rolling_slope(draw, 467) + 0.002129 * anchor
    return base_signal.diff()

def f35_mcj_290_struct_v290_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=305, w3=480, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.509375 + 0.0021291 * anchor
    return base_signal.diff()

def f35_mcj_291_struct_v291_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=316, w3=493, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 316)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.52375 + 0.0021292 * anchor
    return base_signal.diff()

def f35_mcj_292_struct_v292_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=327, w3=506, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(327, min_periods=max(327//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.538125 + 0.0021293 * anchor
    return base_signal.diff()

def f35_mcj_293_struct_v293_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=338, w3=519, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(338, min_periods=max(338//3, 2)).rank(pct=True)
    persistence = change.rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3862 * persistence + 0.0021294 * anchor
    return base_signal.diff()

def f35_mcj_294_struct_v294_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=349, w3=532, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(349, min_periods=max(349//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.566875 + 0.0021295 * anchor
    return base_signal.diff()

def f35_mcj_295_struct_v295_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=360, w3=545, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(360, min_periods=max(360//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4014 * slope + 0.0021296 * anchor
    return base_signal.diff()

def f35_mcj_296_struct_v296_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=371, w3=558, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(371, min_periods=max(371//3, 2)).mean()
    noise = impulse.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.595625 + 0.0021297 * anchor
    return base_signal.diff()

def f35_mcj_297_struct_v297_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=382, w3=571, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 382)
    curvature = _rolling_slope(acceleration, 571)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0402 * acceleration + 0.0021298 * anchor
    return base_signal.diff()

def f35_mcj_298_struct_v298_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=393, w3=584, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(393, min_periods=max(393//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.85125 + 0.0021299 * anchor
    return base_signal.diff()

def f35_mcj_299_struct_v299_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=404, w3=597, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(404, min_periods=max(404//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0554 * _rolling_slope(draw, 597) + 0.00213 * anchor
    return base_signal.diff()

def f35_mcj_300_struct_v300_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=415, w3=610, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(415, min_periods=max(415//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.88 + 0.0021301 * anchor
    return base_signal.diff()
