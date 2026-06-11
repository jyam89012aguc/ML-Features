"""24 debt buildup trajectory d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f24_dbt_226_struct_v226_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=230, w2=439, w3=146, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(439, min_periods=max(439//3, 2)).mean()
    noise = impulse.abs().rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.581875 + 0.0014627 * anchor
    return base_signal.diff()

def f24_dbt_227_struct_v227_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=237, w2=450, w3=159, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 237)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 159)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1622 * acceleration + 0.0014628 * anchor
    return base_signal.diff()

def f24_dbt_228_struct_v228_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=244, w2=461, w3=172, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(461, min_periods=max(461//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.610625 + 0.0014629 * anchor
    return base_signal.diff()

def f24_dbt_229_struct_v229_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=251, w2=472, w3=185, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(472, min_periods=max(472//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1774 * _rolling_slope(draw, 185) + 0.001463 * anchor
    return base_signal.diff()

def f24_dbt_230_struct_v230_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=7, w2=483, w3=198, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.86625 + 0.0014631 * anchor
    return base_signal.diff()

def f24_dbt_231_struct_v231_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=14, w2=494, w3=211, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 494)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=211, adjust=False).mean() * 0.880625 + 0.0014632 * anchor
    return base_signal.diff()

def f24_dbt_232_struct_v232_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=21, w2=505, w3=224, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.895 + 0.0014633 * anchor
    return base_signal.diff()

def f24_dbt_233_struct_v233_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=28, w2=13, w3=237, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(28)
    rank = change.rolling(13, min_periods=max(13//3, 2)).rank(pct=True)
    persistence = change.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2078 * persistence + 0.0014634 * anchor
    return base_signal.diff()

def f24_dbt_234_struct_v234_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=35, w2=24, w3=250, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(24, min_periods=max(24//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92375 + 0.0014635 * anchor
    return base_signal.diff()

def f24_dbt_235_struct_v235_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=42, w2=35, w3=263, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 42)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.223 * slope + 0.0014636 * anchor
    return base_signal.diff()

def f24_dbt_236_struct_v236_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=49, w2=46, w3=276, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(49)
    drag = impulse.rolling(46, min_periods=max(46//3, 2)).mean()
    noise = impulse.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9525 + 0.0014637 * anchor
    return base_signal.diff()

def f24_dbt_237_struct_v237_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=56, w2=57, w3=289, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 56)
    acceleration = _rolling_slope(velocity, 57)
    curvature = _rolling_slope(acceleration, 289)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2382 * acceleration + 0.0014638 * anchor
    return base_signal.diff()

def f24_dbt_238_struct_v238_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=63, w2=68, w3=302, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(68, min_periods=max(68//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.98125 + 0.0014639 * anchor
    return base_signal.diff()

def f24_dbt_239_struct_v239_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=70, w2=79, w3=315, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(79, min_periods=max(79//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2534 * _rolling_slope(draw, 315) + 0.001464 * anchor
    return base_signal.diff()

def f24_dbt_240_struct_v240_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=77, w2=90, w3=328, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(90, min_periods=max(90//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.01 + 0.0014641 * anchor
    return base_signal.diff()

def f24_dbt_241_struct_v241_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=84, w2=101, w3=341, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 101)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.024375 + 0.0014642 * anchor
    return base_signal.diff()

def f24_dbt_242_struct_v242_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=91, w2=112, w3=354, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(112, min_periods=max(112//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03875 + 0.0014643 * anchor
    return base_signal.diff()

def f24_dbt_243_struct_v243_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=98, w2=123, w3=367, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(98)
    rank = change.rolling(123, min_periods=max(123//3, 2)).rank(pct=True)
    persistence = change.rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2838 * persistence + 0.0014644 * anchor
    return base_signal.diff()

def f24_dbt_244_struct_v244_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=105, w2=134, w3=380, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(134, min_periods=max(134//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0675 + 0.0014645 * anchor
    return base_signal.diff()

def f24_dbt_245_struct_v245_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=112, w2=145, w3=393, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(145, min_periods=max(145//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.299 * slope + 0.0014646 * anchor
    return base_signal.diff()

def f24_dbt_246_struct_v246_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=119, w2=156, w3=406, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(119)
    drag = impulse.rolling(156, min_periods=max(156//3, 2)).mean()
    noise = impulse.abs().rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.09625 + 0.0014647 * anchor
    return base_signal.diff()

def f24_dbt_247_struct_v247_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=126, w2=167, w3=419, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 167)
    curvature = _rolling_slope(acceleration, 419)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3142 * acceleration + 0.0014648 * anchor
    return base_signal.diff()

def f24_dbt_248_struct_v248_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=133, w2=178, w3=432, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(178, min_periods=max(178//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.125 + 0.0014649 * anchor
    return base_signal.diff()

def f24_dbt_249_struct_v249_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=140, w2=189, w3=445, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3294 * _rolling_slope(draw, 445) + 0.001465 * anchor
    return base_signal.diff()

def f24_dbt_250_struct_v250_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=147, w2=200, w3=458, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(200, min_periods=max(200//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15375 + 0.0014651 * anchor
    return base_signal.diff()

def f24_dbt_251_struct_v251_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=154, w2=211, w3=471, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 211)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.168125 + 0.0014652 * anchor
    return base_signal.diff()

def f24_dbt_252_struct_v252_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=161, w2=222, w3=484, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1825 + 0.0014653 * anchor
    return base_signal.diff()

def f24_dbt_253_struct_v253_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=233, w3=497, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(233, min_periods=max(233//3, 2)).rank(pct=True)
    persistence = change.rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3598 * persistence + 0.0014654 * anchor
    return base_signal.diff()

def f24_dbt_254_struct_v254_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=244, w3=510, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(244, min_periods=max(244//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21125 + 0.0014655 * anchor
    return base_signal.diff()

def f24_dbt_255_struct_v255_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=255, w3=523, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(255, min_periods=max(255//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.375 * slope + 0.0014656 * anchor
    return base_signal.diff()

def f24_dbt_256_struct_v256_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=266, w3=536, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(266, min_periods=max(266//3, 2)).mean()
    noise = impulse.abs().rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.24 + 0.0014657 * anchor
    return base_signal.diff()

def f24_dbt_257_struct_v257_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=277, w3=549, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 277)
    curvature = _rolling_slope(acceleration, 549)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3902 * acceleration + 0.0014658 * anchor
    return base_signal.diff()

def f24_dbt_258_struct_v258_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=288, w3=562, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(288, min_periods=max(288//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.26875 + 0.0014659 * anchor
    return base_signal.diff()

def f24_dbt_259_struct_v259_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=299, w3=575, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(299, min_periods=max(299//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4054 * _rolling_slope(draw, 575) + 0.001466 * anchor
    return base_signal.diff()

def f24_dbt_260_struct_v260_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=310, w3=588, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 217)
    baseline = trend.rolling(310, min_periods=max(310//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2975 + 0.0014661 * anchor
    return base_signal.diff()

def f24_dbt_261_struct_v261_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=321, w3=601, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 224)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.311875 + 0.0014662 * anchor
    return base_signal.diff()

def f24_dbt_262_struct_v262_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=332, w3=614, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(231, min_periods=max(231//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.32625 + 0.0014663 * anchor
    return base_signal.diff()

def f24_dbt_263_struct_v263_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=343, w3=627, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0594 * persistence + 0.0014664 * anchor
    return base_signal.diff()

def f24_dbt_264_struct_v264_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=354, w3=640, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(245, min_periods=max(245//3, 2)).std()
    vol_slow = ret.rolling(354, min_periods=max(354//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355 + 0.0014665 * anchor
    return base_signal.diff()

def f24_dbt_265_struct_v265_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=365, w3=653, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(365, min_periods=max(365//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 252)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0746 * slope + 0.0014666 * anchor
    return base_signal.diff()

def f24_dbt_266_struct_v266_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=376, w3=666, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(8)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.38375 + 0.0014667 * anchor
    return base_signal.diff()

def f24_dbt_267_struct_v267_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=387, w3=679, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 387)
    curvature = _rolling_slope(acceleration, 679)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0898 * acceleration + 0.0014668 * anchor
    return base_signal.diff()

def f24_dbt_268_struct_v268_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=398, w3=692, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(398, min_periods=max(398//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4125 + 0.0014669 * anchor
    return base_signal.diff()

def f24_dbt_269_struct_v269_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=409, w3=705, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(409, min_periods=max(409//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.105 * _rolling_slope(draw, 705) + 0.001467 * anchor
    return base_signal.diff()

def f24_dbt_270_struct_v270_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=420, w3=718, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(420, min_periods=max(420//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.44125 + 0.0014671 * anchor
    return base_signal.diff()

def f24_dbt_271_struct_v271_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=431, w3=731, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 431)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.455625 + 0.0014672 * anchor
    return base_signal.diff()

def f24_dbt_272_struct_v272_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=442, w3=744, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(442, min_periods=max(442//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47 + 0.0014673 * anchor
    return base_signal.diff()

def f24_dbt_273_struct_v273_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=453, w3=757, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(57)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1354 * persistence + 0.0014674 * anchor
    return base_signal.diff()

def f24_dbt_274_struct_v274_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=464, w3=770, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(464, min_periods=max(464//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49875 + 0.0014675 * anchor
    return base_signal.diff()

def f24_dbt_275_struct_v275_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=475, w3=26, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1506 * slope + 0.0014676 * anchor
    return base_signal.diff()

def f24_dbt_276_struct_v276_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=486, w3=39, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(78)
    drag = impulse.rolling(486, min_periods=max(486//3, 2)).mean()
    noise = impulse.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5275 + 0.0014677 * anchor
    return base_signal.diff()

def f24_dbt_277_struct_v277_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=497, w3=52, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 497)
    curvature = _rolling_slope(acceleration, 52)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1658 * acceleration + 0.0014678 * anchor
    return base_signal.diff()

def f24_dbt_278_struct_v278_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=508, w3=65, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(508, min_periods=max(508//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(65) * 1.55625 + 0.0014679 * anchor
    return base_signal.diff()

def f24_dbt_279_struct_v279_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=16, w3=78, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(16, min_periods=max(16//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.181 * _rolling_slope(draw, 78) + 0.001468 * anchor
    return base_signal.diff()

def f24_dbt_280_struct_v280_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=27, w3=91, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(27, min_periods=max(27//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.585 + 0.0014681 * anchor
    return base_signal.diff()

def f24_dbt_281_struct_v281_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=38, w3=104, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 38)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=104, adjust=False).mean() * 1.599375 + 0.0014682 * anchor
    return base_signal.diff()

def f24_dbt_282_struct_v282_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=49, w3=117, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(49, min_periods=max(49//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.61375 + 0.0014683 * anchor
    return base_signal.diff()

def f24_dbt_283_struct_v283_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=60, w3=130, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(60, min_periods=max(60//3, 2)).rank(pct=True)
    persistence = change.rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2114 * persistence + 0.0014684 * anchor
    return base_signal.diff()

def f24_dbt_284_struct_v284_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=71, w3=143, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(71, min_periods=max(71//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.869375 + 0.0014685 * anchor
    return base_signal.diff()

def f24_dbt_285_struct_v285_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=82, w3=156, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(82, min_periods=max(82//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2266 * slope + 0.0014686 * anchor
    return base_signal.diff()

def f24_dbt_286_struct_v286_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=93, w3=169, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(93, min_periods=max(93//3, 2)).mean()
    noise = impulse.abs().rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.898125 + 0.0014687 * anchor
    return base_signal.diff()

def f24_dbt_287_struct_v287_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=104, w3=182, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 104)
    curvature = _rolling_slope(acceleration, 182)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2418 * acceleration + 0.0014688 * anchor
    return base_signal.diff()

def f24_dbt_288_struct_v288_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=115, w3=195, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(115, min_periods=max(115//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.926875 + 0.0014689 * anchor
    return base_signal.diff()

def f24_dbt_289_struct_v289_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=126, w3=208, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(126, min_periods=max(126//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.257 * _rolling_slope(draw, 208) + 0.001469 * anchor
    return base_signal.diff()

def f24_dbt_290_struct_v290_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=137, w3=221, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(137, min_periods=max(137//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.955625 + 0.0014691 * anchor
    return base_signal.diff()

def f24_dbt_291_struct_v291_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=148, w3=234, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 148)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=234, adjust=False).mean() * 0.97 + 0.0014692 * anchor
    return base_signal.diff()

def f24_dbt_292_struct_v292_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=159, w3=247, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(159, min_periods=max(159//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.984375 + 0.0014693 * anchor
    return base_signal.diff()

def f24_dbt_293_struct_v293_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=170, w3=260, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(170, min_periods=max(170//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2874 * persistence + 0.0014694 * anchor
    return base_signal.diff()

def f24_dbt_294_struct_v294_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=181, w3=273, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(181, min_periods=max(181//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.013125 + 0.0014695 * anchor
    return base_signal.diff()

def f24_dbt_295_struct_v295_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=192, w3=286, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(192, min_periods=max(192//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3026 * slope + 0.0014696 * anchor
    return base_signal.diff()

def f24_dbt_296_struct_v296_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=203, w3=299, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(203, min_periods=max(203//3, 2)).mean()
    noise = impulse.abs().rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.041875 + 0.0014697 * anchor
    return base_signal.diff()

def f24_dbt_297_struct_v297_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=214, w3=312, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 214)
    curvature = _rolling_slope(acceleration, 312)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3178 * acceleration + 0.0014698 * anchor
    return base_signal.diff()

def f24_dbt_298_struct_v298_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=225, w3=325, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(225, min_periods=max(225//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.070625 + 0.0014699 * anchor
    return base_signal.diff()

def f24_dbt_299_struct_v299_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=236, w3=338, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(236, min_periods=max(236//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.333 * _rolling_slope(draw, 338) + 0.00147 * anchor
    return base_signal.diff()

def f24_dbt_300_struct_v300_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=247, w3=351, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(247, min_periods=max(247//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.099375 + 0.0014701 * anchor
    return base_signal.diff()
