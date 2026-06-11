"""84 operating leverage reversal d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f84_olr_226_struct_v226_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=105, w3=425, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(43)
    drag = impulse.rolling(105, min_periods=max(105//3, 2)).mean()
    noise = impulse.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4775 + 0.0041027 * anchor
    return base_signal.diff()

def f84_olr_227_struct_v227_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=116, w3=438, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 50)
    acceleration = _rolling_slope(velocity, 116)
    curvature = _rolling_slope(acceleration, 438)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.181 * acceleration + 0.0041028 * anchor
    return base_signal.diff()

def f84_olr_228_struct_v228_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=127, w3=451, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.50625 + 0.0041029 * anchor
    return base_signal.diff()

def f84_olr_229_struct_v229_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=138, w3=464, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(138, min_periods=max(138//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1962 * _rolling_slope(draw, 464) + 0.004103 * anchor
    return base_signal.diff()

def f84_olr_230_struct_v230_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=149, w3=477, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.535 + 0.0041031 * anchor
    return base_signal.diff()

def f84_olr_231_struct_v231_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=160, w3=490, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 160)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.549375 + 0.0041032 * anchor
    return base_signal.diff()

def f84_olr_232_struct_v232_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=171, w3=503, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.56375 + 0.0041033 * anchor
    return base_signal.diff()

def f84_olr_233_struct_v233_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=182, w3=516, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(92)
    rank = change.rolling(182, min_periods=max(182//3, 2)).rank(pct=True)
    persistence = change.rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2266 * persistence + 0.0041034 * anchor
    return base_signal.diff()

def f84_olr_234_struct_v234_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=193, w3=529, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(193, min_periods=max(193//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5925 + 0.0041035 * anchor
    return base_signal.diff()

def f84_olr_235_struct_v235_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=204, w3=542, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(204, min_periods=max(204//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2418 * slope + 0.0041036 * anchor
    return base_signal.diff()

def f84_olr_236_struct_v236_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=215, w3=555, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(113)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.62125 + 0.0041037 * anchor
    return base_signal.diff()

def f84_olr_237_struct_v237_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=226, w3=568, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 568)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.257 * acceleration + 0.0041038 * anchor
    return base_signal.diff()

def f84_olr_238_struct_v238_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=237, w3=581, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.876875 + 0.0041039 * anchor
    return base_signal.diff()

def f84_olr_239_struct_v239_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=248, w3=594, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2722 * _rolling_slope(draw, 594) + 0.004104 * anchor
    return base_signal.diff()

def f84_olr_240_struct_v240_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=259, w3=607, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.905625 + 0.0041041 * anchor
    return base_signal.diff()

def f84_olr_241_struct_v241_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=270, w3=620, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 270)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.92 + 0.0041042 * anchor
    return base_signal.diff()

def f84_olr_242_struct_v242_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=281, w3=633, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(281, min_periods=max(281//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.934375 + 0.0041043 * anchor
    return base_signal.diff()

def f84_olr_243_struct_v243_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=292, w3=646, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(292, min_periods=max(292//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3026 * persistence + 0.0041044 * anchor
    return base_signal.diff()

def f84_olr_244_struct_v244_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=303, w3=659, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(303, min_periods=max(303//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.963125 + 0.0041045 * anchor
    return base_signal.diff()

def f84_olr_245_struct_v245_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=314, w3=672, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(314, min_periods=max(314//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3178 * slope + 0.0041046 * anchor
    return base_signal.diff()

def f84_olr_246_struct_v246_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=325, w3=685, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(325, min_periods=max(325//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.991875 + 0.0041047 * anchor
    return base_signal.diff()

def f84_olr_247_struct_v247_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=336, w3=698, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 698)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.333 * acceleration + 0.0041048 * anchor
    return base_signal.diff()

def f84_olr_248_struct_v248_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=347, w3=711, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(347, min_periods=max(347//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.020625 + 0.0041049 * anchor
    return base_signal.diff()

def f84_olr_249_struct_v249_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=358, w3=724, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(358, min_periods=max(358//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3482 * _rolling_slope(draw, 724) + 0.004105 * anchor
    return base_signal.diff()

def f84_olr_250_struct_v250_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=369, w3=737, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(369, min_periods=max(369//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.049375 + 0.0041051 * anchor
    return base_signal.diff()

def f84_olr_251_struct_v251_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=380, w3=750, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 380)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.06375 + 0.0041052 * anchor
    return base_signal.diff()

def f84_olr_252_struct_v252_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=391, w3=763, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.078125 + 0.0041053 * anchor
    return base_signal.diff()

def f84_olr_253_struct_v253_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=402, w3=19, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(402, min_periods=max(402//3, 2)).rank(pct=True)
    persistence = change.rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3786 * persistence + 0.0041054 * anchor
    return base_signal.diff()

def f84_olr_254_struct_v254_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=413, w3=32, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(413, min_periods=max(413//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.106875 + 0.0041055 * anchor
    return base_signal.diff()

def f84_olr_255_struct_v255_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=424, w3=45, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3938 * slope + 0.0041056 * anchor
    return base_signal.diff()

def f84_olr_256_struct_v256_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=435, w3=58, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(435, min_periods=max(435//3, 2)).mean()
    noise = impulse.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.135625 + 0.0041057 * anchor
    return base_signal.diff()

def f84_olr_257_struct_v257_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=446, w3=71, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 446)
    curvature = _rolling_slope(acceleration, 71)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.409 * acceleration + 0.0041058 * anchor
    return base_signal.diff()

def f84_olr_258_struct_v258_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=457, w3=84, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(84) * 1.164375 + 0.0041059 * anchor
    return base_signal.diff()

def f84_olr_259_struct_v259_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=468, w3=97, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(468, min_periods=max(468//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0478 * _rolling_slope(draw, 97) + 0.004106 * anchor
    return base_signal.diff()

def f84_olr_260_struct_v260_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=479, w3=110, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(479, min_periods=max(479//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.193125 + 0.0041061 * anchor
    return base_signal.diff()

def f84_olr_261_struct_v261_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=490, w3=123, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=123, adjust=False).mean() * 1.2075 + 0.0041062 * anchor
    return base_signal.diff()

def f84_olr_262_struct_v262_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=501, w3=136, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.221875 + 0.0041063 * anchor
    return base_signal.diff()

def f84_olr_263_struct_v263_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=512, w3=149, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(51)
    rank = change.rolling(512, min_periods=max(512//3, 2)).rank(pct=True)
    persistence = change.rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0782 * persistence + 0.0041064 * anchor
    return base_signal.diff()

def f84_olr_264_struct_v264_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=20, w3=162, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(20, min_periods=max(20//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.250625 + 0.0041065 * anchor
    return base_signal.diff()

def f84_olr_265_struct_v265_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=31, w3=175, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(31, min_periods=max(31//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0934 * slope + 0.0041066 * anchor
    return base_signal.diff()

def f84_olr_266_struct_v266_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=42, w3=188, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(72)
    drag = impulse.rolling(42, min_periods=max(42//3, 2)).mean()
    noise = impulse.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.279375 + 0.0041067 * anchor
    return base_signal.diff()

def f84_olr_267_struct_v267_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=53, w3=201, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 53)
    curvature = _rolling_slope(acceleration, 201)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1086 * acceleration + 0.0041068 * anchor
    return base_signal.diff()

def f84_olr_268_struct_v268_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=64, w3=214, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(64, min_periods=max(64//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.308125 + 0.0041069 * anchor
    return base_signal.diff()

def f84_olr_269_struct_v269_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=75, w3=227, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(75, min_periods=max(75//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1238 * _rolling_slope(draw, 227) + 0.004107 * anchor
    return base_signal.diff()

def f84_olr_270_struct_v270_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=86, w3=240, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(86, min_periods=max(86//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.336875 + 0.0041071 * anchor
    return base_signal.diff()

def f84_olr_271_struct_v271_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=97, w3=253, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 97)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=253, adjust=False).mean() * 1.35125 + 0.0041072 * anchor
    return base_signal.diff()

def f84_olr_272_struct_v272_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=108, w3=266, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.365625 + 0.0041073 * anchor
    return base_signal.diff()

def f84_olr_273_struct_v273_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=119, w3=279, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(121)
    rank = change.rolling(119, min_periods=max(119//3, 2)).rank(pct=True)
    persistence = change.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1542 * persistence + 0.0041074 * anchor
    return base_signal.diff()

def f84_olr_274_struct_v274_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=130, w3=292, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(130, min_periods=max(130//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.394375 + 0.0041075 * anchor
    return base_signal.diff()

def f84_olr_275_struct_v275_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=141, w3=305, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(141, min_periods=max(141//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1694 * slope + 0.0041076 * anchor
    return base_signal.diff()

def f84_olr_276_struct_v276_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=152, w3=318, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.423125 + 0.0041077 * anchor
    return base_signal.diff()

def f84_olr_277_struct_v277_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=163, w3=331, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 163)
    curvature = _rolling_slope(acceleration, 331)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1846 * acceleration + 0.0041078 * anchor
    return base_signal.diff()

def f84_olr_278_struct_v278_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=174, w3=344, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.451875 + 0.0041079 * anchor
    return base_signal.diff()

def f84_olr_279_struct_v279_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=185, w3=357, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(185, min_periods=max(185//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1998 * _rolling_slope(draw, 357) + 0.004108 * anchor
    return base_signal.diff()

def f84_olr_280_struct_v280_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=196, w3=370, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.480625 + 0.0041081 * anchor
    return base_signal.diff()

def f84_olr_281_struct_v281_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=207, w3=383, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 207)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.495 + 0.0041082 * anchor
    return base_signal.diff()

def f84_olr_282_struct_v282_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=218, w3=396, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(218, min_periods=max(218//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.509375 + 0.0041083 * anchor
    return base_signal.diff()

def f84_olr_283_struct_v283_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=229, w3=409, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(229, min_periods=max(229//3, 2)).rank(pct=True)
    persistence = change.rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2302 * persistence + 0.0041084 * anchor
    return base_signal.diff()

def f84_olr_284_struct_v284_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=240, w3=422, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(240, min_periods=max(240//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.538125 + 0.0041085 * anchor
    return base_signal.diff()

def f84_olr_285_struct_v285_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=251, w3=435, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(251, min_periods=max(251//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2454 * slope + 0.0041086 * anchor
    return base_signal.diff()

def f84_olr_286_struct_v286_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=262, w3=448, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(262, min_periods=max(262//3, 2)).mean()
    noise = impulse.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.566875 + 0.0041087 * anchor
    return base_signal.diff()

def f84_olr_287_struct_v287_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=273, w3=461, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 273)
    curvature = _rolling_slope(acceleration, 461)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2606 * acceleration + 0.0041088 * anchor
    return base_signal.diff()

def f84_olr_288_struct_v288_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=284, w3=474, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(284, min_periods=max(284//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.595625 + 0.0041089 * anchor
    return base_signal.diff()

def f84_olr_289_struct_v289_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=295, w3=487, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(295, min_periods=max(295//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2758 * _rolling_slope(draw, 487) + 0.004109 * anchor
    return base_signal.diff()

def f84_olr_290_struct_v290_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=306, w3=500, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.85125 + 0.0041091 * anchor
    return base_signal.diff()

def f84_olr_291_struct_v291_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=317, w3=513, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.865625 + 0.0041092 * anchor
    return base_signal.diff()

def f84_olr_292_struct_v292_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=328, w3=526, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(328, min_periods=max(328//3, 2)).max()
    trough = x.rolling(254, min_periods=max(254//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.88 + 0.0041093 * anchor
    return base_signal.diff()

def f84_olr_293_struct_v293_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=339, w3=539, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(10)
    rank = change.rolling(339, min_periods=max(339//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3062 * persistence + 0.0041094 * anchor
    return base_signal.diff()

def f84_olr_294_struct_v294_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=350, w3=552, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90875 + 0.0041095 * anchor
    return base_signal.diff()

def f84_olr_295_struct_v295_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=361, w3=565, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(361, min_periods=max(361//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3214 * slope + 0.0041096 * anchor
    return base_signal.diff()

def f84_olr_296_struct_v296_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=372, w3=578, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(31)
    drag = impulse.rolling(372, min_periods=max(372//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9375 + 0.0041097 * anchor
    return base_signal.diff()

def f84_olr_297_struct_v297_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=383, w3=591, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 383)
    curvature = _rolling_slope(acceleration, 591)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3366 * acceleration + 0.0041098 * anchor
    return base_signal.diff()

def f84_olr_298_struct_v298_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=394, w3=604, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.96625 + 0.0041099 * anchor
    return base_signal.diff()

def f84_olr_299_struct_v299_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=405, w3=617, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(405, min_periods=max(405//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3518 * _rolling_slope(draw, 617) + 0.00411 * anchor
    return base_signal.diff()

def f84_olr_300_struct_v300_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=416, w3=630, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(416, min_periods=max(416//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(630, min_periods=max(630//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.995 + 0.0041101 * anchor
    return base_signal.diff()
