"""27 insider selling trajectory d2 second derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f27_ist_226_struct_v226_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=29, w2=119, w3=79, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(29)
    drag = impulse.rolling(119, min_periods=max(119//3, 2)).mean()
    noise = impulse.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.170625 + 0.0016427 * anchor
    return base_signal.diff().diff()

def f27_ist_227_struct_v227_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=36, w2=130, w3=92, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 130)
    curvature = _rolling_slope(acceleration, 92)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2918 * acceleration + 0.0016428 * anchor
    return base_signal.diff().diff()

def f27_ist_228_struct_v228_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=43, w2=141, w3=105, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(141, min_periods=max(141//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(105) * 1.199375 + 0.0016429 * anchor
    return base_signal.diff().diff()

def f27_ist_229_struct_v229_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=50, w2=152, w3=118, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(152, min_periods=max(152//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.307 * _rolling_slope(draw, 118) + 0.001643 * anchor
    return base_signal.diff().diff()

def f27_ist_230_struct_v230_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=57, w2=163, w3=131, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(163, min_periods=max(163//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.228125 + 0.0016431 * anchor
    return base_signal.diff().diff()

def f27_ist_231_struct_v231_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=64, w2=174, w3=144, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 174)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=144, adjust=False).mean() * 1.2425 + 0.0016432 * anchor
    return base_signal.diff().diff()

def f27_ist_232_struct_v232_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=71, w2=185, w3=157, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(71, min_periods=max(71//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.256875 + 0.0016433 * anchor
    return base_signal.diff().diff()

def f27_ist_233_struct_v233_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=78, w2=196, w3=170, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(78)
    rank = change.rolling(196, min_periods=max(196//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3374 * persistence + 0.0016434 * anchor
    return base_signal.diff().diff()

def f27_ist_234_struct_v234_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=85, w2=207, w3=183, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(85, min_periods=max(85//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.285625 + 0.0016435 * anchor
    return base_signal.diff().diff()

def f27_ist_235_struct_v235_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=92, w2=218, w3=196, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(218, min_periods=max(218//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3526 * slope + 0.0016436 * anchor
    return base_signal.diff().diff()

def f27_ist_236_struct_v236_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=99, w2=229, w3=209, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(99)
    drag = impulse.rolling(229, min_periods=max(229//3, 2)).mean()
    noise = impulse.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.314375 + 0.0016437 * anchor
    return base_signal.diff().diff()

def f27_ist_237_struct_v237_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=106, w2=240, w3=222, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 222)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3678 * acceleration + 0.0016438 * anchor
    return base_signal.diff().diff()

def f27_ist_238_struct_v238_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=113, w2=251, w3=235, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.343125 + 0.0016439 * anchor
    return base_signal.diff().diff()

def f27_ist_239_struct_v239_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=120, w2=262, w3=248, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.383 * _rolling_slope(draw, 248) + 0.001644 * anchor
    return base_signal.diff().diff()

def f27_ist_240_struct_v240_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=127, w2=273, w3=261, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 127)
    baseline = trend.rolling(273, min_periods=max(273//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.371875 + 0.0016441 * anchor
    return base_signal.diff().diff()

def f27_ist_241_struct_v241_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=134, w2=284, w3=274, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 134)
    slow = _rolling_slope(x, 284)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=274, adjust=False).mean() * 1.38625 + 0.0016442 * anchor
    return base_signal.diff().diff()

def f27_ist_242_struct_v242_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=141, w2=295, w3=287, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(141, min_periods=max(141//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.400625 + 0.0016443 * anchor
    return base_signal.diff().diff()

def f27_ist_243_struct_v243_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=148, w2=306, w3=300, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(306, min_periods=max(306//3, 2)).rank(pct=True)
    persistence = change.rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.037 * persistence + 0.0016444 * anchor
    return base_signal.diff().diff()

def f27_ist_244_struct_v244_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=155, w2=317, w3=313, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(155, min_periods=max(155//3, 2)).std()
    vol_slow = ret.rolling(317, min_periods=max(317//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.429375 + 0.0016445 * anchor
    return base_signal.diff().diff()

def f27_ist_245_struct_v245_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=162, w2=328, w3=326, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(328, min_periods=max(328//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 162)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0522 * slope + 0.0016446 * anchor
    return base_signal.diff().diff()

def f27_ist_246_struct_v246_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=169, w2=339, w3=339, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.458125 + 0.0016447 * anchor
    return base_signal.diff().diff()

def f27_ist_247_struct_v247_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=176, w2=350, w3=352, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 352)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0674 * acceleration + 0.0016448 * anchor
    return base_signal.diff().diff()

def f27_ist_248_struct_v248_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=183, w2=361, w3=365, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(361, min_periods=max(361//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.486875 + 0.0016449 * anchor
    return base_signal.diff().diff()

def f27_ist_249_struct_v249_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=190, w2=372, w3=378, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(372, min_periods=max(372//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0826 * _rolling_slope(draw, 378) + 0.001645 * anchor
    return base_signal.diff().diff()

def f27_ist_250_struct_v250_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=197, w2=383, w3=391, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 197)
    baseline = trend.rolling(383, min_periods=max(383//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.515625 + 0.0016451 * anchor
    return base_signal.diff().diff()

def f27_ist_251_struct_v251_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=204, w2=394, w3=404, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 204)
    slow = _rolling_slope(x, 394)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.53 + 0.0016452 * anchor
    return base_signal.diff().diff()

def f27_ist_252_struct_v252_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=211, w2=405, w3=417, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(405, min_periods=max(405//3, 2)).max()
    trough = x.rolling(211, min_periods=max(211//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.544375 + 0.0016453 * anchor
    return base_signal.diff().diff()

def f27_ist_253_struct_v253_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=218, w2=416, w3=430, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(416, min_periods=max(416//3, 2)).rank(pct=True)
    persistence = change.rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.113 * persistence + 0.0016454 * anchor
    return base_signal.diff().diff()

def f27_ist_254_struct_v254_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=225, w2=427, w3=443, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(225, min_periods=max(225//3, 2)).std()
    vol_slow = ret.rolling(427, min_periods=max(427//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.573125 + 0.0016455 * anchor
    return base_signal.diff().diff()

def f27_ist_255_struct_v255_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=232, w2=438, w3=456, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 232)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1282 * slope + 0.0016456 * anchor
    return base_signal.diff().diff()

def f27_ist_256_struct_v256_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=239, w2=449, w3=469, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(449, min_periods=max(449//3, 2)).mean()
    noise = impulse.abs().rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.601875 + 0.0016457 * anchor
    return base_signal.diff().diff()

def f27_ist_257_struct_v257_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=246, w2=460, w3=482, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 246)
    acceleration = _rolling_slope(velocity, 460)
    curvature = _rolling_slope(acceleration, 482)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1434 * acceleration + 0.0016458 * anchor
    return base_signal.diff().diff()

def f27_ist_258_struct_v258_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=253, w2=471, w3=495, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(471, min_periods=max(471//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8575 + 0.0016459 * anchor
    return base_signal.diff().diff()

def f27_ist_259_struct_v259_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=9, w2=482, w3=508, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(482, min_periods=max(482//3, 2)).max()
    rebound = x - x.rolling(9, min_periods=max(9//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1586 * _rolling_slope(draw, 508) + 0.001646 * anchor
    return base_signal.diff().diff()

def f27_ist_260_struct_v260_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=16, w2=493, w3=521, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(493, min_periods=max(493//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.88625 + 0.0016461 * anchor
    return base_signal.diff().diff()

def f27_ist_261_struct_v261_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=23, w2=504, w3=534, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 504)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.900625 + 0.0016462 * anchor
    return base_signal.diff().diff()

def f27_ist_262_struct_v262_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=30, w2=12, w3=547, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(12, min_periods=max(12//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.915 + 0.0016463 * anchor
    return base_signal.diff().diff()

def f27_ist_263_struct_v263_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=37, w2=23, w3=560, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(37)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189 * persistence + 0.0016464 * anchor
    return base_signal.diff().diff()

def f27_ist_264_struct_v264_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=44, w2=34, w3=573, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(34, min_periods=max(34//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.94375 + 0.0016465 * anchor
    return base_signal.diff().diff()

def f27_ist_265_struct_v265_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=51, w2=45, w3=586, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(45, min_periods=max(45//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2042 * slope + 0.0016466 * anchor
    return base_signal.diff().diff()

def f27_ist_266_struct_v266_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=58, w2=56, w3=599, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(58)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9725 + 0.0016467 * anchor
    return base_signal.diff().diff()

def f27_ist_267_struct_v267_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=65, w2=67, w3=612, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 67)
    curvature = _rolling_slope(acceleration, 612)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2194 * acceleration + 0.0016468 * anchor
    return base_signal.diff().diff()

def f27_ist_268_struct_v268_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=72, w2=78, w3=625, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(72, min_periods=max(72//3, 2)).mean(), upside.rolling(78, min_periods=max(78//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.00125 + 0.0016469 * anchor
    return base_signal.diff().diff()

def f27_ist_269_struct_v269_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=79, w2=89, w3=638, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(79, min_periods=max(79//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2346 * _rolling_slope(draw, 638) + 0.001647 * anchor
    return base_signal.diff().diff()

def f27_ist_270_struct_v270_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=86, w2=100, w3=651, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(100, min_periods=max(100//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.03 + 0.0016471 * anchor
    return base_signal.diff().diff()

def f27_ist_271_struct_v271_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=93, w2=111, w3=664, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 111)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.044375 + 0.0016472 * anchor
    return base_signal.diff().diff()

def f27_ist_272_struct_v272_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=100, w2=122, w3=677, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.05875 + 0.0016473 * anchor
    return base_signal.diff().diff()

def f27_ist_273_struct_v273_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=107, w2=133, w3=690, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(107)
    rank = change.rolling(133, min_periods=max(133//3, 2)).rank(pct=True)
    persistence = change.rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265 * persistence + 0.0016474 * anchor
    return base_signal.diff().diff()

def f27_ist_274_struct_v274_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=114, w2=144, w3=703, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(144, min_periods=max(144//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0875 + 0.0016475 * anchor
    return base_signal.diff().diff()

def f27_ist_275_struct_v275_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=121, w2=155, w3=716, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(155, min_periods=max(155//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2802 * slope + 0.0016476 * anchor
    return base_signal.diff().diff()

def f27_ist_276_struct_v276_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=128, w2=166, w3=729, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(166, min_periods=max(166//3, 2)).mean()
    noise = impulse.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.11625 + 0.0016477 * anchor
    return base_signal.diff().diff()

def f27_ist_277_struct_v277_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=135, w2=177, w3=742, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 177)
    curvature = _rolling_slope(acceleration, 742)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2954 * acceleration + 0.0016478 * anchor
    return base_signal.diff().diff()

def f27_ist_278_struct_v278_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=142, w2=188, w3=755, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(188, min_periods=max(188//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.145 + 0.0016479 * anchor
    return base_signal.diff().diff()

def f27_ist_279_struct_v279_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=149, w2=199, w3=768, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(199, min_periods=max(199//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3106 * _rolling_slope(draw, 768) + 0.001648 * anchor
    return base_signal.diff().diff()

def f27_ist_280_struct_v280_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=156, w2=210, w3=24, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(210, min_periods=max(210//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.17375 + 0.0016481 * anchor
    return base_signal.diff().diff()

def f27_ist_281_struct_v281_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=163, w2=221, w3=37, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 221)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=37, adjust=False).mean() * 1.188125 + 0.0016482 * anchor
    return base_signal.diff().diff()

def f27_ist_282_struct_v282_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=170, w2=232, w3=50, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(232, min_periods=max(232//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2025 + 0.0016483 * anchor
    return base_signal.diff().diff()

def f27_ist_283_struct_v283_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=177, w2=243, w3=63, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(243, min_periods=max(243//3, 2)).rank(pct=True)
    persistence = change.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341 * persistence + 0.0016484 * anchor
    return base_signal.diff().diff()

def f27_ist_284_struct_v284_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=184, w2=254, w3=76, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(254, min_periods=max(254//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.23125 + 0.0016485 * anchor
    return base_signal.diff().diff()

def f27_ist_285_struct_v285_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=191, w2=265, w3=89, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(265, min_periods=max(265//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3562 * slope + 0.0016486 * anchor
    return base_signal.diff().diff()

def f27_ist_286_struct_v286_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=198, w2=276, w3=102, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(276, min_periods=max(276//3, 2)).mean()
    noise = impulse.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.26 + 0.0016487 * anchor
    return base_signal.diff().diff()

def f27_ist_287_struct_v287_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=205, w2=287, w3=115, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 115)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3714 * acceleration + 0.0016488 * anchor
    return base_signal.diff().diff()

def f27_ist_288_struct_v288_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=212, w2=298, w3=128, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(298, min_periods=max(298//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.28875 + 0.0016489 * anchor
    return base_signal.diff().diff()

def f27_ist_289_struct_v289_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=219, w2=309, w3=141, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(309, min_periods=max(309//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3866 * _rolling_slope(draw, 141) + 0.001649 * anchor
    return base_signal.diff().diff()

def f27_ist_290_struct_v290_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=226, w2=320, w3=154, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(320, min_periods=max(320//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3175 + 0.0016491 * anchor
    return base_signal.diff().diff()

def f27_ist_291_struct_v291_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=233, w2=331, w3=167, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 331)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=167, adjust=False).mean() * 1.331875 + 0.0016492 * anchor
    return base_signal.diff().diff()

def f27_ist_292_struct_v292_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=240, w2=342, w3=180, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(342, min_periods=max(342//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.34625 + 0.0016493 * anchor
    return base_signal.diff().diff()

def f27_ist_293_struct_v293_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=247, w2=353, w3=193, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(353, min_periods=max(353//3, 2)).rank(pct=True)
    persistence = change.rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0406 * persistence + 0.0016494 * anchor
    return base_signal.diff().diff()

def f27_ist_294_struct_v294_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=254, w2=364, w3=206, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(364, min_periods=max(364//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.375 + 0.0016495 * anchor
    return base_signal.diff().diff()

def f27_ist_295_struct_v295_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=10, w2=375, w3=219, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(375, min_periods=max(375//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0558 * slope + 0.0016496 * anchor
    return base_signal.diff().diff()

def f27_ist_296_struct_v296_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=17, w2=386, w3=232, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(17)
    drag = impulse.rolling(386, min_periods=max(386//3, 2)).mean()
    noise = impulse.abs().rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.40375 + 0.0016497 * anchor
    return base_signal.diff().diff()

def f27_ist_297_struct_v297_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=24, w2=397, w3=245, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 397)
    curvature = _rolling_slope(acceleration, 245)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.071 * acceleration + 0.0016498 * anchor
    return base_signal.diff().diff()

def f27_ist_298_struct_v298_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=31, w2=408, w3=258, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(408, min_periods=max(408//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4325 + 0.0016499 * anchor
    return base_signal.diff().diff()

def f27_ist_299_struct_v299_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=38, w2=419, w3=271, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(419, min_periods=max(419//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0862 * _rolling_slope(draw, 271) + 0.00165 * anchor
    return base_signal.diff().diff()

def f27_ist_300_struct_v300_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=45, w2=430, w3=284, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(430, min_periods=max(430//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46125 + 0.0016501 * anchor
    return base_signal.diff().diff()
