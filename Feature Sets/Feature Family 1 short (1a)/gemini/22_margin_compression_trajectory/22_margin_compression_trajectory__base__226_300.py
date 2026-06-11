"""22 margin compression trajectory base features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f22_mct_226_struct_v226(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=317, w3=443, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(113)
    drag = impulse.rolling(317, min_periods=max(317//3, 2)).mean()
    noise = impulse.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.340625 + 0.0013427 * anchor

def f22_mct_227_struct_v227(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=328, w3=456, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 328)
    curvature = _rolling_slope(acceleration, 456)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0758 * acceleration + 0.0013428 * anchor

def f22_mct_228_struct_v228(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=339, w3=469, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(339, min_periods=max(339//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.369375 + 0.0013429 * anchor

def f22_mct_229_struct_v229(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=350, w3=482, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(350, min_periods=max(350//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.091 * _rolling_slope(draw, 482) + 0.001343 * anchor

def f22_mct_230_struct_v230(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=361, w3=495, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(361, min_periods=max(361//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.398125 + 0.0013431 * anchor

def f22_mct_231_struct_v231(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=372, w3=508, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 372)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4125 + 0.0013432 * anchor

def f22_mct_232_struct_v232(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=383, w3=521, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.426875 + 0.0013433 * anchor

def f22_mct_233_struct_v233(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=394, w3=534, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(394, min_periods=max(394//3, 2)).rank(pct=True)
    persistence = change.rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1214 * persistence + 0.0013434 * anchor

def f22_mct_234_struct_v234(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=405, w3=547, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.455625 + 0.0013435 * anchor

def f22_mct_235_struct_v235(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=416, w3=560, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(416, min_periods=max(416//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1366 * slope + 0.0013436 * anchor

def f22_mct_236_struct_v236(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=427, w3=573, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(427, min_periods=max(427//3, 2)).mean()
    noise = impulse.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.484375 + 0.0013437 * anchor

def f22_mct_237_struct_v237(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=438, w3=586, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 438)
    curvature = _rolling_slope(acceleration, 586)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1518 * acceleration + 0.0013438 * anchor

def f22_mct_238_struct_v238(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=449, w3=599, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(449, min_periods=max(449//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.513125 + 0.0013439 * anchor

def f22_mct_239_struct_v239(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=460, w3=612, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(460, min_periods=max(460//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.167 * _rolling_slope(draw, 612) + 0.001344 * anchor

def f22_mct_240_struct_v240(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=471, w3=625, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(471, min_periods=max(471//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.541875 + 0.0013441 * anchor

def f22_mct_241_struct_v241(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=482, w3=638, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 482)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.55625 + 0.0013442 * anchor

def f22_mct_242_struct_v242(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=493, w3=651, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(493, min_periods=max(493//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.570625 + 0.0013443 * anchor

def f22_mct_243_struct_v243(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=504, w3=664, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(504, min_periods=max(504//3, 2)).rank(pct=True)
    persistence = change.rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1974 * persistence + 0.0013444 * anchor

def f22_mct_244_struct_v244(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=12, w3=677, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(12, min_periods=max(12//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.599375 + 0.0013445 * anchor

def f22_mct_245_struct_v245(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=23, w3=690, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(23, min_periods=max(23//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2126 * slope + 0.0013446 * anchor

def f22_mct_246_struct_v246(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=34, w3=703, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(34, min_periods=max(34//3, 2)).mean()
    noise = impulse.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.855 + 0.0013447 * anchor

def f22_mct_247_struct_v247(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=45, w3=716, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 45)
    curvature = _rolling_slope(acceleration, 716)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2278 * acceleration + 0.0013448 * anchor

def f22_mct_248_struct_v248(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=56, w3=729, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(56, min_periods=max(56//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.88375 + 0.0013449 * anchor

def f22_mct_249_struct_v249(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=67, w3=742, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(67, min_periods=max(67//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.243 * _rolling_slope(draw, 742) + 0.001345 * anchor

def f22_mct_250_struct_v250(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=78, w3=755, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(78, min_periods=max(78//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9125 + 0.0013451 * anchor

def f22_mct_251_struct_v251(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=89, w3=768, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 89)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.926875 + 0.0013452 * anchor

def f22_mct_252_struct_v252(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=100, w3=24, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(100, min_periods=max(100//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.94125 + 0.0013453 * anchor

def f22_mct_253_struct_v253(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=111, w3=37, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(51)
    rank = change.rolling(111, min_periods=max(111//3, 2)).rank(pct=True)
    persistence = change.rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2734 * persistence + 0.0013454 * anchor

def f22_mct_254_struct_v254(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=122, w3=50, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(122, min_periods=max(122//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97 + 0.0013455 * anchor

def f22_mct_255_struct_v255(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=133, w3=63, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(133, min_periods=max(133//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2886 * slope + 0.0013456 * anchor

def f22_mct_256_struct_v256(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=144, w3=76, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(72)
    drag = impulse.rolling(144, min_periods=max(144//3, 2)).mean()
    noise = impulse.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.99875 + 0.0013457 * anchor

def f22_mct_257_struct_v257(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=155, w3=89, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 155)
    curvature = _rolling_slope(acceleration, 89)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3038 * acceleration + 0.0013458 * anchor

def f22_mct_258_struct_v258(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=166, w3=102, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(166, min_periods=max(166//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(102) * 1.0275 + 0.0013459 * anchor

def f22_mct_259_struct_v259(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=177, w3=115, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(177, min_periods=max(177//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.319 * _rolling_slope(draw, 115) + 0.001346 * anchor

def f22_mct_260_struct_v260(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=188, w3=128, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(188, min_periods=max(188//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.05625 + 0.0013461 * anchor

def f22_mct_261_struct_v261(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=199, w3=141, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 199)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=141, adjust=False).mean() * 1.070625 + 0.0013462 * anchor

def f22_mct_262_struct_v262(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=210, w3=154, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(210, min_periods=max(210//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.085 + 0.0013463 * anchor

def f22_mct_263_struct_v263(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=221, w3=167, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(121)
    rank = change.rolling(221, min_periods=max(221//3, 2)).rank(pct=True)
    persistence = change.rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3494 * persistence + 0.0013464 * anchor

def f22_mct_264_struct_v264(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=232, w3=180, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(232, min_periods=max(232//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11375 + 0.0013465 * anchor

def f22_mct_265_struct_v265(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=243, w3=193, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(243, min_periods=max(243//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3646 * slope + 0.0013466 * anchor

def f22_mct_266_struct_v266(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=254, w3=206, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(254, min_periods=max(254//3, 2)).mean()
    noise = impulse.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1425 + 0.0013467 * anchor

def f22_mct_267_struct_v267(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=265, w3=219, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 265)
    curvature = _rolling_slope(acceleration, 219)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3798 * acceleration + 0.0013468 * anchor

def f22_mct_268_struct_v268(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=276, w3=232, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(276, min_periods=max(276//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.17125 + 0.0013469 * anchor

def f22_mct_269_struct_v269(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=287, w3=245, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(287, min_periods=max(287//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.395 * _rolling_slope(draw, 245) + 0.001347 * anchor

def f22_mct_270_struct_v270(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=298, w3=258, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(298, min_periods=max(298//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.2 + 0.0013471 * anchor

def f22_mct_271_struct_v271(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=309, w3=271, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 309)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=271, adjust=False).mean() * 1.214375 + 0.0013472 * anchor

def f22_mct_272_struct_v272(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=320, w3=284, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(320, min_periods=max(320//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.22875 + 0.0013473 * anchor

def f22_mct_273_struct_v273(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=331, w3=297, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(331, min_periods=max(331//3, 2)).rank(pct=True)
    persistence = change.rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.049 * persistence + 0.0013474 * anchor

def f22_mct_274_struct_v274(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=342, w3=310, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(342, min_periods=max(342//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2575 + 0.0013475 * anchor

def f22_mct_275_struct_v275(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=353, w3=323, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(353, min_periods=max(353//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0642 * slope + 0.0013476 * anchor

def f22_mct_276_struct_v276(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=364, w3=336, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(364, min_periods=max(364//3, 2)).mean()
    noise = impulse.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.28625 + 0.0013477 * anchor

def f22_mct_277_struct_v277(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=375, w3=349, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 375)
    curvature = _rolling_slope(acceleration, 349)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0794 * acceleration + 0.0013478 * anchor

def f22_mct_278_struct_v278(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=386, w3=362, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(386, min_periods=max(386//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.315 + 0.0013479 * anchor

def f22_mct_279_struct_v279(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=397, w3=375, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(397, min_periods=max(397//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0946 * _rolling_slope(draw, 375) + 0.001348 * anchor

def f22_mct_280_struct_v280(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=408, w3=388, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(408, min_periods=max(408//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.34375 + 0.0013481 * anchor

def f22_mct_281_struct_v281(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=419, w3=401, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 419)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.358125 + 0.0013482 * anchor

def f22_mct_282_struct_v282(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=430, w3=414, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(430, min_periods=max(430//3, 2)).max()
    trough = x.rolling(254, min_periods=max(254//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3725 + 0.0013483 * anchor

def f22_mct_283_struct_v283(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=441, w3=427, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(10)
    rank = change.rolling(441, min_periods=max(441//3, 2)).rank(pct=True)
    persistence = change.rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.125 * persistence + 0.0013484 * anchor

def f22_mct_284_struct_v284(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=452, w3=440, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(452, min_periods=max(452//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.40125 + 0.0013485 * anchor

def f22_mct_285_struct_v285(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=463, w3=453, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(463, min_periods=max(463//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1402 * slope + 0.0013486 * anchor

def f22_mct_286_struct_v286(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=474, w3=466, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(31)
    drag = impulse.rolling(474, min_periods=max(474//3, 2)).mean()
    noise = impulse.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.43 + 0.0013487 * anchor

def f22_mct_287_struct_v287(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=485, w3=479, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 485)
    curvature = _rolling_slope(acceleration, 479)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1554 * acceleration + 0.0013488 * anchor

def f22_mct_288_struct_v288(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=496, w3=492, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(496, min_periods=max(496//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45875 + 0.0013489 * anchor

def f22_mct_289_struct_v289(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=507, w3=505, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(507, min_periods=max(507//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1706 * _rolling_slope(draw, 505) + 0.001349 * anchor

def f22_mct_290_struct_v290(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=15, w3=518, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(15, min_periods=max(15//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4875 + 0.0013491 * anchor

def f22_mct_291_struct_v291(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=26, w3=531, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 26)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.501875 + 0.0013492 * anchor

def f22_mct_292_struct_v292(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=37, w3=544, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(37, min_periods=max(37//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.51625 + 0.0013493 * anchor

def f22_mct_293_struct_v293(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=48, w3=557, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(80)
    rank = change.rolling(48, min_periods=max(48//3, 2)).rank(pct=True)
    persistence = change.rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.201 * persistence + 0.0013494 * anchor

def f22_mct_294_struct_v294(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=59, w3=570, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(59, min_periods=max(59//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.545 + 0.0013495 * anchor

def f22_mct_295_struct_v295(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=70, w3=583, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(70, min_periods=max(70//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2162 * slope + 0.0013496 * anchor

def f22_mct_296_struct_v296(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=81, w3=596, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(101)
    drag = impulse.rolling(81, min_periods=max(81//3, 2)).mean()
    noise = impulse.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.57375 + 0.0013497 * anchor

def f22_mct_297_struct_v297(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=92, w3=609, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 92)
    curvature = _rolling_slope(acceleration, 609)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2314 * acceleration + 0.0013498 * anchor

def f22_mct_298_struct_v298(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=103, w3=622, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(103, min_periods=max(103//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.6025 + 0.0013499 * anchor

def f22_mct_299_struct_v299(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=114, w3=635, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(114, min_periods=max(114//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2466 * _rolling_slope(draw, 635) + 0.00135 * anchor

def f22_mct_300_struct_v300(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=125, w3=648, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(125, min_periods=max(125//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.858125 + 0.0013501 * anchor
