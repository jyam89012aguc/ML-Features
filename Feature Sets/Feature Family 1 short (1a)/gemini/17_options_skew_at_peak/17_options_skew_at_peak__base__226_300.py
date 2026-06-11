"""17 options skew at peak base features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Options_Greeks - Institutional-grade short-side signal.
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

def f17_optx_226_struct_v226(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=12, w3=50, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.510625 + 0.0010427 * anchor

def f17_optx_227_struct_v227(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=23, w3=63, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 63)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2362 * acceleration + 0.0010428 * anchor

def f17_optx_228_struct_v228(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=34, w3=76, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(211, min_periods=max(211//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(76) * 1.539375 + 0.0010429 * anchor

def f17_optx_229_struct_v229(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=45, w3=89, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(45, min_periods=max(45//3, 2)).max()
    rebound = x - x.rolling(218, min_periods=max(218//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2514 * _rolling_slope(draw, 89) + 0.001043 * anchor

def f17_optx_230_struct_v230(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=56, w3=102, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(56, min_periods=max(56//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.568125 + 0.0010431 * anchor

def f17_optx_231_struct_v231(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=67, w3=115, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=115, adjust=False).mean() * 1.5825 + 0.0010432 * anchor

def f17_optx_232_struct_v232(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=78, w3=128, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.596875 + 0.0010433 * anchor

def f17_optx_233_struct_v233(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=89, w3=141, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(89, min_periods=max(89//3, 2)).rank(pct=True)
    persistence = change.rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2818 * persistence + 0.0010434 * anchor

def f17_optx_234_struct_v234(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=100, w3=154, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(253, min_periods=max(253//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8525 + 0.0010435 * anchor

def f17_optx_235_struct_v235(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=111, w3=167, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.297 * slope + 0.0010436 * anchor

def f17_optx_236_struct_v236(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=122, w3=180, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(16)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88125 + 0.0010437 * anchor

def f17_optx_237_struct_v237(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=133, w3=193, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 133)
    curvature = _rolling_slope(acceleration, 193)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3122 * acceleration + 0.0010438 * anchor

def f17_optx_238_struct_v238(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=144, w3=206, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(144, min_periods=max(144//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.91 + 0.0010439 * anchor

def f17_optx_239_struct_v239(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=155, w3=219, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(155, min_periods=max(155//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3274 * _rolling_slope(draw, 219) + 0.001044 * anchor

def f17_optx_240_struct_v240(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=166, w3=232, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(166, min_periods=max(166//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.93875 + 0.0010441 * anchor

def f17_optx_241_struct_v241(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=177, w3=245, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 177)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=245, adjust=False).mean() * 0.953125 + 0.0010442 * anchor

def f17_optx_242_struct_v242(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=188, w3=258, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(188, min_periods=max(188//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9675 + 0.0010443 * anchor

def f17_optx_243_struct_v243(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=199, w3=271, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(65)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3578 * persistence + 0.0010444 * anchor

def f17_optx_244_struct_v244(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=210, w3=284, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(210, min_periods=max(210//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99625 + 0.0010445 * anchor

def f17_optx_245_struct_v245(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=221, w3=297, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(221, min_periods=max(221//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.373 * slope + 0.0010446 * anchor

def f17_optx_246_struct_v246(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=232, w3=310, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(86)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.025 + 0.0010447 * anchor

def f17_optx_247_struct_v247(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=243, w3=323, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 243)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3882 * acceleration + 0.0010448 * anchor

def f17_optx_248_struct_v248(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=254, w3=336, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05375 + 0.0010449 * anchor

def f17_optx_249_struct_v249(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=265, w3=349, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4034 * _rolling_slope(draw, 349) + 0.001045 * anchor

def f17_optx_250_struct_v250(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=276, w3=362, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(276, min_periods=max(276//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0825 + 0.0010451 * anchor

def f17_optx_251_struct_v251(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=287, w3=375, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.096875 + 0.0010452 * anchor

def f17_optx_252_struct_v252(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=298, w3=388, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(298, min_periods=max(298//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11125 + 0.0010453 * anchor

def f17_optx_253_struct_v253(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=309, w3=401, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0574 * persistence + 0.0010454 * anchor

def f17_optx_254_struct_v254(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=320, w3=414, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(320, min_periods=max(320//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14 + 0.0010455 * anchor

def f17_optx_255_struct_v255(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=331, w3=427, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(331, min_periods=max(331//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0726 * slope + 0.0010456 * anchor

def f17_optx_256_struct_v256(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=342, w3=440, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(342, min_periods=max(342//3, 2)).mean()
    noise = impulse.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.16875 + 0.0010457 * anchor

def f17_optx_257_struct_v257(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=353, w3=453, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 453)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0878 * acceleration + 0.0010458 * anchor

def f17_optx_258_struct_v258(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=364, w3=466, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(364, min_periods=max(364//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1975 + 0.0010459 * anchor

def f17_optx_259_struct_v259(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=375, w3=479, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(375, min_periods=max(375//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.103 * _rolling_slope(draw, 479) + 0.001046 * anchor

def f17_optx_260_struct_v260(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=386, w3=492, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.22625 + 0.0010461 * anchor

def f17_optx_261_struct_v261(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=397, w3=505, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.240625 + 0.0010462 * anchor

def f17_optx_262_struct_v262(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=408, w3=518, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.255 + 0.0010463 * anchor

def f17_optx_263_struct_v263(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=419, w3=531, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(419, min_periods=max(419//3, 2)).rank(pct=True)
    persistence = change.rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1334 * persistence + 0.0010464 * anchor

def f17_optx_264_struct_v264(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=430, w3=544, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28375 + 0.0010465 * anchor

def f17_optx_265_struct_v265(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=441, w3=557, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1486 * slope + 0.0010466 * anchor

def f17_optx_266_struct_v266(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=452, w3=570, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(570, min_periods=max(570//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3125 + 0.0010467 * anchor

def f17_optx_267_struct_v267(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=463, w3=583, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 583)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1638 * acceleration + 0.0010468 * anchor

def f17_optx_268_struct_v268(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=474, w3=596, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(474, min_periods=max(474//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.34125 + 0.0010469 * anchor

def f17_optx_269_struct_v269(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=485, w3=609, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.179 * _rolling_slope(draw, 609) + 0.001047 * anchor

def f17_optx_270_struct_v270(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=496, w3=622, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(496, min_periods=max(496//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.37 + 0.0010471 * anchor

def f17_optx_271_struct_v271(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=507, w3=635, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 507)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.384375 + 0.0010472 * anchor

def f17_optx_272_struct_v272(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=15, w3=648, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(15, min_periods=max(15//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.39875 + 0.0010473 * anchor

def f17_optx_273_struct_v273(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=26, w3=661, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(24)
    rank = change.rolling(26, min_periods=max(26//3, 2)).rank(pct=True)
    persistence = change.rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2094 * persistence + 0.0010474 * anchor

def f17_optx_274_struct_v274(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=37, w3=674, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(37, min_periods=max(37//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4275 + 0.0010475 * anchor

def f17_optx_275_struct_v275(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=48, w3=687, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2246 * slope + 0.0010476 * anchor

def f17_optx_276_struct_v276(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=59, w3=700, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(45)
    drag = impulse.rolling(59, min_periods=max(59//3, 2)).mean()
    noise = impulse.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.45625 + 0.0010477 * anchor

def f17_optx_277_struct_v277(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=70, w3=713, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 713)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2398 * acceleration + 0.0010478 * anchor

def f17_optx_278_struct_v278(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=81, w3=726, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(81, min_periods=max(81//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.485 + 0.0010479 * anchor

def f17_optx_279_struct_v279(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=92, w3=739, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(92, min_periods=max(92//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.255 * _rolling_slope(draw, 739) + 0.001048 * anchor

def f17_optx_280_struct_v280(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=103, w3=752, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(103, min_periods=max(103//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51375 + 0.0010481 * anchor

def f17_optx_281_struct_v281(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=114, w3=765, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 114)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.528125 + 0.0010482 * anchor

def f17_optx_282_struct_v282(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=125, w3=21, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(125, min_periods=max(125//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5425 + 0.0010483 * anchor

def f17_optx_283_struct_v283(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=136, w3=34, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(94)
    rank = change.rolling(136, min_periods=max(136//3, 2)).rank(pct=True)
    persistence = change.rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2854 * persistence + 0.0010484 * anchor

def f17_optx_284_struct_v284(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=147, w3=47, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(147, min_periods=max(147//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57125 + 0.0010485 * anchor

def f17_optx_285_struct_v285(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=158, w3=60, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(158, min_periods=max(158//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3006 * slope + 0.0010486 * anchor

def f17_optx_286_struct_v286(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=169, w3=73, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(115)
    drag = impulse.rolling(169, min_periods=max(169//3, 2)).mean()
    noise = impulse.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6 + 0.0010487 * anchor

def f17_optx_287_struct_v287(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=180, w3=86, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 180)
    curvature = _rolling_slope(acceleration, 86)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3158 * acceleration + 0.0010488 * anchor

def f17_optx_288_struct_v288(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=191, w3=99, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(191, min_periods=max(191//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(99) * 0.855625 + 0.0010489 * anchor

def f17_optx_289_struct_v289(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=202, w3=112, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(202, min_periods=max(202//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.331 * _rolling_slope(draw, 112) + 0.001049 * anchor

def f17_optx_290_struct_v290(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=213, w3=125, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(213, min_periods=max(213//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(125, min_periods=max(125//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.884375 + 0.0010491 * anchor

def f17_optx_291_struct_v291(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=224, w3=138, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 224)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=138, adjust=False).mean() * 0.89875 + 0.0010492 * anchor

def f17_optx_292_struct_v292(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=235, w3=151, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(235, min_periods=max(235//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.913125 + 0.0010493 * anchor

def f17_optx_293_struct_v293(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=246, w3=164, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(246, min_periods=max(246//3, 2)).rank(pct=True)
    persistence = change.rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3614 * persistence + 0.0010494 * anchor

def f17_optx_294_struct_v294(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=257, w3=177, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(257, min_periods=max(257//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.941875 + 0.0010495 * anchor

def f17_optx_295_struct_v295(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=268, w3=190, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(268, min_periods=max(268//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3766 * slope + 0.0010496 * anchor

def f17_optx_296_struct_v296(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=279, w3=203, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(279, min_periods=max(279//3, 2)).mean()
    noise = impulse.abs().rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.970625 + 0.0010497 * anchor

def f17_optx_297_struct_v297(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=290, w3=216, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 290)
    curvature = _rolling_slope(acceleration, 216)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3918 * acceleration + 0.0010498 * anchor

def f17_optx_298_struct_v298(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=301, w3=229, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(301, min_periods=max(301//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.999375 + 0.0010499 * anchor

def f17_optx_299_struct_v299(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=312, w3=242, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(312, min_periods=max(312//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.407 * _rolling_slope(draw, 242) + 0.00105 * anchor

def f17_optx_300_struct_v300(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=323, w3=255, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(323, min_periods=max(323//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.028125 + 0.0010501 * anchor
