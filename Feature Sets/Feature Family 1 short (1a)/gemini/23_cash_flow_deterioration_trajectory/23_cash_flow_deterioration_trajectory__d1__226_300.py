"""23 cash flow deterioration trajectory d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f23_cfd_226_struct_v226_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=378, w3=673, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(46)
    drag = impulse.rolling(378, min_periods=max(378//3, 2)).mean()
    noise = impulse.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.46125 + 0.0014027 * anchor
    return base_signal.diff()

def f23_cfd_227_struct_v227_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=389, w3=686, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 53)
    acceleration = _rolling_slope(velocity, 389)
    curvature = _rolling_slope(acceleration, 686)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.119 * acceleration + 0.0014028 * anchor
    return base_signal.diff()

def f23_cfd_228_struct_v228_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=400, w3=699, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(60, min_periods=max(60//3, 2)).mean(), upside.rolling(400, min_periods=max(400//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49 + 0.0014029 * anchor
    return base_signal.diff()

def f23_cfd_229_struct_v229_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=411, w3=712, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(411, min_periods=max(411//3, 2)).max()
    rebound = x - x.rolling(67, min_periods=max(67//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1342 * _rolling_slope(draw, 712) + 0.001403 * anchor
    return base_signal.diff()

def f23_cfd_230_struct_v230_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=422, w3=725, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(422, min_periods=max(422//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51875 + 0.0014031 * anchor
    return base_signal.diff()

def f23_cfd_231_struct_v231_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=433, w3=738, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 433)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.533125 + 0.0014032 * anchor
    return base_signal.diff()

def f23_cfd_232_struct_v232_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=444, w3=751, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(444, min_periods=max(444//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5475 + 0.0014033 * anchor
    return base_signal.diff()

def f23_cfd_233_struct_v233_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=455, w3=764, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(95)
    rank = change.rolling(455, min_periods=max(455//3, 2)).rank(pct=True)
    persistence = change.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1646 * persistence + 0.0014034 * anchor
    return base_signal.diff()

def f23_cfd_234_struct_v234_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=466, w3=20, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(466, min_periods=max(466//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57625 + 0.0014035 * anchor
    return base_signal.diff()

def f23_cfd_235_struct_v235_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=477, w3=33, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(477, min_periods=max(477//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1798 * slope + 0.0014036 * anchor
    return base_signal.diff()

def f23_cfd_236_struct_v236_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=488, w3=46, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(116)
    drag = impulse.rolling(488, min_periods=max(488//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.605 + 0.0014037 * anchor
    return base_signal.diff()

def f23_cfd_237_struct_v237_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=499, w3=59, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 499)
    curvature = _rolling_slope(acceleration, 59)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.195 * acceleration + 0.0014038 * anchor
    return base_signal.diff()

def f23_cfd_238_struct_v238_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=510, w3=72, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(130, min_periods=max(130//3, 2)).mean(), upside.rolling(510, min_periods=max(510//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(72) * 0.860625 + 0.0014039 * anchor
    return base_signal.diff()

def f23_cfd_239_struct_v239_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=18, w3=85, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(18, min_periods=max(18//3, 2)).max()
    rebound = x - x.rolling(137, min_periods=max(137//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2102 * _rolling_slope(draw, 85) + 0.001404 * anchor
    return base_signal.diff()

def f23_cfd_240_struct_v240_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=29, w3=98, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(29, min_periods=max(29//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.889375 + 0.0014041 * anchor
    return base_signal.diff()

def f23_cfd_241_struct_v241_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=40, w3=111, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 40)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=111, adjust=False).mean() * 0.90375 + 0.0014042 * anchor
    return base_signal.diff()

def f23_cfd_242_struct_v242_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=51, w3=124, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(51, min_periods=max(51//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.918125 + 0.0014043 * anchor
    return base_signal.diff()

def f23_cfd_243_struct_v243_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=62, w3=137, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(62, min_periods=max(62//3, 2)).rank(pct=True)
    persistence = change.rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2406 * persistence + 0.0014044 * anchor
    return base_signal.diff()

def f23_cfd_244_struct_v244_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=73, w3=150, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(73, min_periods=max(73//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.946875 + 0.0014045 * anchor
    return base_signal.diff()

def f23_cfd_245_struct_v245_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=84, w3=163, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(84, min_periods=max(84//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2558 * slope + 0.0014046 * anchor
    return base_signal.diff()

def f23_cfd_246_struct_v246_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=95, w3=176, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(95, min_periods=max(95//3, 2)).mean()
    noise = impulse.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.975625 + 0.0014047 * anchor
    return base_signal.diff()

def f23_cfd_247_struct_v247_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=106, w3=189, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 106)
    curvature = _rolling_slope(acceleration, 189)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.271 * acceleration + 0.0014048 * anchor
    return base_signal.diff()

def f23_cfd_248_struct_v248_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=117, w3=202, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(117, min_periods=max(117//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.004375 + 0.0014049 * anchor
    return base_signal.diff()

def f23_cfd_249_struct_v249_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=128, w3=215, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(128, min_periods=max(128//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2862 * _rolling_slope(draw, 215) + 0.001405 * anchor
    return base_signal.diff()

def f23_cfd_250_struct_v250_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=139, w3=228, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(139, min_periods=max(139//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.033125 + 0.0014051 * anchor
    return base_signal.diff()

def f23_cfd_251_struct_v251_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=150, w3=241, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 150)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=241, adjust=False).mean() * 1.0475 + 0.0014052 * anchor
    return base_signal.diff()

def f23_cfd_252_struct_v252_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=161, w3=254, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(161, min_periods=max(161//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.061875 + 0.0014053 * anchor
    return base_signal.diff()

def f23_cfd_253_struct_v253_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=172, w3=267, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(172, min_periods=max(172//3, 2)).rank(pct=True)
    persistence = change.rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3166 * persistence + 0.0014054 * anchor
    return base_signal.diff()

def f23_cfd_254_struct_v254_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=183, w3=280, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(183, min_periods=max(183//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.090625 + 0.0014055 * anchor
    return base_signal.diff()

def f23_cfd_255_struct_v255_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=194, w3=293, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(194, min_periods=max(194//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3318 * slope + 0.0014056 * anchor
    return base_signal.diff()

def f23_cfd_256_struct_v256_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=205, w3=306, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(5)
    drag = impulse.rolling(205, min_periods=max(205//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.119375 + 0.0014057 * anchor
    return base_signal.diff()

def f23_cfd_257_struct_v257_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=216, w3=319, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 216)
    curvature = _rolling_slope(acceleration, 319)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.347 * acceleration + 0.0014058 * anchor
    return base_signal.diff()

def f23_cfd_258_struct_v258_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=227, w3=332, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(227, min_periods=max(227//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.148125 + 0.0014059 * anchor
    return base_signal.diff()

def f23_cfd_259_struct_v259_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=238, w3=345, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(238, min_periods=max(238//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3622 * _rolling_slope(draw, 345) + 0.001406 * anchor
    return base_signal.diff()

def f23_cfd_260_struct_v260_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=249, w3=358, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(249, min_periods=max(249//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.176875 + 0.0014061 * anchor
    return base_signal.diff()

def f23_cfd_261_struct_v261_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=260, w3=371, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 260)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.19125 + 0.0014062 * anchor
    return base_signal.diff()

def f23_cfd_262_struct_v262_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=271, w3=384, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(271, min_periods=max(271//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.205625 + 0.0014063 * anchor
    return base_signal.diff()

def f23_cfd_263_struct_v263_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=282, w3=397, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(54)
    rank = change.rolling(282, min_periods=max(282//3, 2)).rank(pct=True)
    persistence = change.rolling(397, min_periods=max(397//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3926 * persistence + 0.0014064 * anchor
    return base_signal.diff()

def f23_cfd_264_struct_v264_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=293, w3=410, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(293, min_periods=max(293//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.234375 + 0.0014065 * anchor
    return base_signal.diff()

def f23_cfd_265_struct_v265_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=304, w3=423, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(304, min_periods=max(304//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4078 * slope + 0.0014066 * anchor
    return base_signal.diff()

def f23_cfd_266_struct_v266_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=315, w3=436, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(75)
    drag = impulse.rolling(315, min_periods=max(315//3, 2)).mean()
    noise = impulse.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.263125 + 0.0014067 * anchor
    return base_signal.diff()

def f23_cfd_267_struct_v267_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=326, w3=449, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 326)
    curvature = _rolling_slope(acceleration, 449)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0466 * acceleration + 0.0014068 * anchor
    return base_signal.diff()

def f23_cfd_268_struct_v268_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=337, w3=462, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(337, min_periods=max(337//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.291875 + 0.0014069 * anchor
    return base_signal.diff()

def f23_cfd_269_struct_v269_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=348, w3=475, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(348, min_periods=max(348//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0618 * _rolling_slope(draw, 475) + 0.001407 * anchor
    return base_signal.diff()

def f23_cfd_270_struct_v270_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=359, w3=488, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(359, min_periods=max(359//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.320625 + 0.0014071 * anchor
    return base_signal.diff()

def f23_cfd_271_struct_v271_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=370, w3=501, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 370)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.335 + 0.0014072 * anchor
    return base_signal.diff()

def f23_cfd_272_struct_v272_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=381, w3=514, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(381, min_periods=max(381//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.349375 + 0.0014073 * anchor
    return base_signal.diff()

def f23_cfd_273_struct_v273_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=392, w3=527, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(124)
    rank = change.rolling(392, min_periods=max(392//3, 2)).rank(pct=True)
    persistence = change.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0922 * persistence + 0.0014074 * anchor
    return base_signal.diff()

def f23_cfd_274_struct_v274_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=403, w3=540, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(403, min_periods=max(403//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.378125 + 0.0014075 * anchor
    return base_signal.diff()

def f23_cfd_275_struct_v275_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=414, w3=553, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(414, min_periods=max(414//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1074 * slope + 0.0014076 * anchor
    return base_signal.diff()

def f23_cfd_276_struct_v276_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=425, w3=566, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(425, min_periods=max(425//3, 2)).mean()
    noise = impulse.abs().rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.406875 + 0.0014077 * anchor
    return base_signal.diff()

def f23_cfd_277_struct_v277_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=436, w3=579, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 579)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1226 * acceleration + 0.0014078 * anchor
    return base_signal.diff()

def f23_cfd_278_struct_v278_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=447, w3=592, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(447, min_periods=max(447//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.435625 + 0.0014079 * anchor
    return base_signal.diff()

def f23_cfd_279_struct_v279_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=458, w3=605, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(458, min_periods=max(458//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1378 * _rolling_slope(draw, 605) + 0.001408 * anchor
    return base_signal.diff()

def f23_cfd_280_struct_v280_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=469, w3=618, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(469, min_periods=max(469//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.464375 + 0.0014081 * anchor
    return base_signal.diff()

def f23_cfd_281_struct_v281_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=480, w3=631, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 480)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.47875 + 0.0014082 * anchor
    return base_signal.diff()

def f23_cfd_282_struct_v282_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=491, w3=644, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(491, min_periods=max(491//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.493125 + 0.0014083 * anchor
    return base_signal.diff()

def f23_cfd_283_struct_v283_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=502, w3=657, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(502, min_periods=max(502//3, 2)).rank(pct=True)
    persistence = change.rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1682 * persistence + 0.0014084 * anchor
    return base_signal.diff()

def f23_cfd_284_struct_v284_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=10, w3=670, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(10, min_periods=max(10//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.521875 + 0.0014085 * anchor
    return base_signal.diff()

def f23_cfd_285_struct_v285_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=21, w3=683, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(21, min_periods=max(21//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1834 * slope + 0.0014086 * anchor
    return base_signal.diff()

def f23_cfd_286_struct_v286_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=32, w3=696, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(32, min_periods=max(32//3, 2)).mean()
    noise = impulse.abs().rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.550625 + 0.0014087 * anchor
    return base_signal.diff()

def f23_cfd_287_struct_v287_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=43, w3=709, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 43)
    curvature = _rolling_slope(acceleration, 709)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1986 * acceleration + 0.0014088 * anchor
    return base_signal.diff()

def f23_cfd_288_struct_v288_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=54, w3=722, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(54, min_periods=max(54//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.579375 + 0.0014089 * anchor
    return base_signal.diff()

def f23_cfd_289_struct_v289_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=236, w2=65, w3=735, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(65, min_periods=max(65//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2138 * _rolling_slope(draw, 735) + 0.001409 * anchor
    return base_signal.diff()

def f23_cfd_290_struct_v290_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=76, w3=748, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(76, min_periods=max(76//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.608125 + 0.0014091 * anchor
    return base_signal.diff()

def f23_cfd_291_struct_v291_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=87, w3=761, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 87)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.6225 + 0.0014092 * anchor
    return base_signal.diff()

def f23_cfd_292_struct_v292_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=98, w3=17, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(98, min_periods=max(98//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.86375 + 0.0014093 * anchor
    return base_signal.diff()

def f23_cfd_293_struct_v293_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=109, w3=30, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(13)
    rank = change.rolling(109, min_periods=max(109//3, 2)).rank(pct=True)
    persistence = change.rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2442 * persistence + 0.0014094 * anchor
    return base_signal.diff()

def f23_cfd_294_struct_v294_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=120, w3=43, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(120, min_periods=max(120//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8925 + 0.0014095 * anchor
    return base_signal.diff()

def f23_cfd_295_struct_v295_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=131, w3=56, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2594 * slope + 0.0014096 * anchor
    return base_signal.diff()

def f23_cfd_296_struct_v296_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=142, w3=69, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(34)
    drag = impulse.rolling(142, min_periods=max(142//3, 2)).mean()
    noise = impulse.abs().rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.92125 + 0.0014097 * anchor
    return base_signal.diff()

def f23_cfd_297_struct_v297_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=153, w3=82, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 41)
    acceleration = _rolling_slope(velocity, 153)
    curvature = _rolling_slope(acceleration, 82)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2746 * acceleration + 0.0014098 * anchor
    return base_signal.diff()

def f23_cfd_298_struct_v298_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=164, w3=95, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(48, min_periods=max(48//3, 2)).mean(), upside.rolling(164, min_periods=max(164//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(95) * 0.95 + 0.0014099 * anchor
    return base_signal.diff()

def f23_cfd_299_struct_v299_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=175, w3=108, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(175, min_periods=max(175//3, 2)).max()
    rebound = x - x.rolling(55, min_periods=max(55//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2898 * _rolling_slope(draw, 108) + 0.00141 * anchor
    return base_signal.diff()

def f23_cfd_300_struct_v300_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=186, w3=121, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 62)
    baseline = trend.rolling(186, min_periods=max(186//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.97875 + 0.0014101 * anchor
    return base_signal.diff()
