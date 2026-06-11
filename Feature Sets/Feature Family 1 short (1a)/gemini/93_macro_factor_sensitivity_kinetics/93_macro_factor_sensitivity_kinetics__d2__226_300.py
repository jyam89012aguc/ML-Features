"""93 macro factor sensitivity kinetics d2 second derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Macro_Factor - Institutional-grade short-side signal.
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

def f93_mcf_226_struct_v226_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=93, w2=288, w3=358, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(93)
    drag = impulse.rolling(288, min_periods=max(288//3, 2)).mean()
    noise = impulse.abs().rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.06625 + 0.0042827 * anchor
    return base_signal.diff().diff()

def f93_mcf_227_struct_v227_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=100, w2=299, w3=371, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 299)
    curvature = _rolling_slope(acceleration, 371)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3106 * acceleration + 0.0042828 * anchor
    return base_signal.diff().diff()

def f93_mcf_228_struct_v228_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=107, w2=310, w3=384, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(310, min_periods=max(310//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.095 + 0.0042829 * anchor
    return base_signal.diff().diff()

def f93_mcf_229_struct_v229_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=114, w2=321, w3=397, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(321, min_periods=max(321//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3258 * _rolling_slope(draw, 397) + 0.004283 * anchor
    return base_signal.diff().diff()

def f93_mcf_230_struct_v230_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=121, w2=332, w3=410, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(332, min_periods=max(332//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.12375 + 0.0042831 * anchor
    return base_signal.diff().diff()

def f93_mcf_231_struct_v231_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=128, w2=343, w3=423, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 343)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.138125 + 0.0042832 * anchor
    return base_signal.diff().diff()

def f93_mcf_232_struct_v232_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=135, w2=354, w3=436, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(354, min_periods=max(354//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1525 + 0.0042833 * anchor
    return base_signal.diff().diff()

def f93_mcf_233_struct_v233_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=142, w2=365, w3=449, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(365, min_periods=max(365//3, 2)).rank(pct=True)
    persistence = change.rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3562 * persistence + 0.0042834 * anchor
    return base_signal.diff().diff()

def f93_mcf_234_struct_v234_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=149, w2=376, w3=462, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(376, min_periods=max(376//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18125 + 0.0042835 * anchor
    return base_signal.diff().diff()

def f93_mcf_235_struct_v235_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=156, w2=387, w3=475, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(387, min_periods=max(387//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3714 * slope + 0.0042836 * anchor
    return base_signal.diff().diff()

def f93_mcf_236_struct_v236_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=163, w2=398, w3=488, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(398, min_periods=max(398//3, 2)).mean()
    noise = impulse.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.21 + 0.0042837 * anchor
    return base_signal.diff().diff()

def f93_mcf_237_struct_v237_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=170, w2=409, w3=501, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 409)
    curvature = _rolling_slope(acceleration, 501)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3866 * acceleration + 0.0042838 * anchor
    return base_signal.diff().diff()

def f93_mcf_238_struct_v238_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=177, w2=420, w3=514, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(420, min_periods=max(420//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.23875 + 0.0042839 * anchor
    return base_signal.diff().diff()

def f93_mcf_239_struct_v239_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=184, w2=431, w3=527, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(431, min_periods=max(431//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4018 * _rolling_slope(draw, 527) + 0.004284 * anchor
    return base_signal.diff().diff()

def f93_mcf_240_struct_v240_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=191, w2=442, w3=540, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(442, min_periods=max(442//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2675 + 0.0042841 * anchor
    return base_signal.diff().diff()

def f93_mcf_241_struct_v241_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=198, w2=453, w3=553, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.281875 + 0.0042842 * anchor
    return base_signal.diff().diff()

def f93_mcf_242_struct_v242_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=205, w2=464, w3=566, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(464, min_periods=max(464//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.29625 + 0.0042843 * anchor
    return base_signal.diff().diff()

def f93_mcf_243_struct_v243_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=212, w2=475, w3=579, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0558 * persistence + 0.0042844 * anchor
    return base_signal.diff().diff()

def f93_mcf_244_struct_v244_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=219, w2=486, w3=592, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(486, min_periods=max(486//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.325 + 0.0042845 * anchor
    return base_signal.diff().diff()

def f93_mcf_245_struct_v245_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=226, w2=497, w3=605, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(497, min_periods=max(497//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.071 * slope + 0.0042846 * anchor
    return base_signal.diff().diff()

def f93_mcf_246_struct_v246_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=233, w2=508, w3=618, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(508, min_periods=max(508//3, 2)).mean()
    noise = impulse.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.35375 + 0.0042847 * anchor
    return base_signal.diff().diff()

def f93_mcf_247_struct_v247_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=240, w2=16, w3=631, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 16)
    curvature = _rolling_slope(acceleration, 631)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0862 * acceleration + 0.0042848 * anchor
    return base_signal.diff().diff()

def f93_mcf_248_struct_v248_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=247, w2=27, w3=644, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(27, min_periods=max(27//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3825 + 0.0042849 * anchor
    return base_signal.diff().diff()

def f93_mcf_249_struct_v249_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=254, w2=38, w3=657, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(38, min_periods=max(38//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1014 * _rolling_slope(draw, 657) + 0.004285 * anchor
    return base_signal.diff().diff()

def f93_mcf_250_struct_v250_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=10, w2=49, w3=670, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(49, min_periods=max(49//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41125 + 0.0042851 * anchor
    return base_signal.diff().diff()

def f93_mcf_251_struct_v251_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=17, w2=60, w3=683, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 60)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.425625 + 0.0042852 * anchor
    return base_signal.diff().diff()

def f93_mcf_252_struct_v252_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=24, w2=71, w3=696, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44 + 0.0042853 * anchor
    return base_signal.diff().diff()

def f93_mcf_253_struct_v253_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=31, w2=82, w3=709, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(31)
    rank = change.rolling(82, min_periods=max(82//3, 2)).rank(pct=True)
    persistence = change.rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1318 * persistence + 0.0042854 * anchor
    return base_signal.diff().diff()

def f93_mcf_254_struct_v254_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=38, w2=93, w3=722, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(93, min_periods=max(93//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46875 + 0.0042855 * anchor
    return base_signal.diff().diff()

def f93_mcf_255_struct_v255_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=45, w2=104, w3=735, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(104, min_periods=max(104//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147 * slope + 0.0042856 * anchor
    return base_signal.diff().diff()

def f93_mcf_256_struct_v256_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=52, w2=115, w3=748, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(52)
    drag = impulse.rolling(115, min_periods=max(115//3, 2)).mean()
    noise = impulse.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4975 + 0.0042857 * anchor
    return base_signal.diff().diff()

def f93_mcf_257_struct_v257_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=59, w2=126, w3=761, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 126)
    curvature = _rolling_slope(acceleration, 761)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1622 * acceleration + 0.0042858 * anchor
    return base_signal.diff().diff()

def f93_mcf_258_struct_v258_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=66, w2=137, w3=17, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(137, min_periods=max(137//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(17) * 1.52625 + 0.0042859 * anchor
    return base_signal.diff().diff()

def f93_mcf_259_struct_v259_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=73, w2=148, w3=30, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(148, min_periods=max(148//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1774 * _rolling_slope(draw, 30) + 0.004286 * anchor
    return base_signal.diff().diff()

def f93_mcf_260_struct_v260_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=80, w2=159, w3=43, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.555 + 0.0042861 * anchor
    return base_signal.diff().diff()

def f93_mcf_261_struct_v261_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=87, w2=170, w3=56, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 170)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=56, adjust=False).mean() * 1.569375 + 0.0042862 * anchor
    return base_signal.diff().diff()

def f93_mcf_262_struct_v262_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=94, w2=181, w3=69, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.58375 + 0.0042863 * anchor
    return base_signal.diff().diff()

def f93_mcf_263_struct_v263_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=101, w2=192, w3=82, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(101)
    rank = change.rolling(192, min_periods=max(192//3, 2)).rank(pct=True)
    persistence = change.rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2078 * persistence + 0.0042864 * anchor
    return base_signal.diff().diff()

def f93_mcf_264_struct_v264_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=108, w2=203, w3=95, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(203, min_periods=max(203//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6125 + 0.0042865 * anchor
    return base_signal.diff().diff()

def f93_mcf_265_struct_v265_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=115, w2=214, w3=108, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.223 * slope + 0.0042866 * anchor
    return base_signal.diff().diff()

def f93_mcf_266_struct_v266_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=122, w2=225, w3=121, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(122)
    drag = impulse.rolling(225, min_periods=max(225//3, 2)).mean()
    noise = impulse.abs().rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.868125 + 0.0042867 * anchor
    return base_signal.diff().diff()

def f93_mcf_267_struct_v267_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=129, w2=236, w3=134, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 236)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2382 * acceleration + 0.0042868 * anchor
    return base_signal.diff().diff()

def f93_mcf_268_struct_v268_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=136, w2=247, w3=147, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(247, min_periods=max(247//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.896875 + 0.0042869 * anchor
    return base_signal.diff().diff()

def f93_mcf_269_struct_v269_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=143, w2=258, w3=160, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(258, min_periods=max(258//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2534 * _rolling_slope(draw, 160) + 0.004287 * anchor
    return base_signal.diff().diff()

def f93_mcf_270_struct_v270_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=150, w2=269, w3=173, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(269, min_periods=max(269//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.925625 + 0.0042871 * anchor
    return base_signal.diff().diff()

def f93_mcf_271_struct_v271_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=157, w2=280, w3=186, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 280)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=186, adjust=False).mean() * 0.94 + 0.0042872 * anchor
    return base_signal.diff().diff()

def f93_mcf_272_struct_v272_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=164, w2=291, w3=199, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(291, min_periods=max(291//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.954375 + 0.0042873 * anchor
    return base_signal.diff().diff()

def f93_mcf_273_struct_v273_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=171, w2=302, w3=212, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(302, min_periods=max(302//3, 2)).rank(pct=True)
    persistence = change.rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2838 * persistence + 0.0042874 * anchor
    return base_signal.diff().diff()

def f93_mcf_274_struct_v274_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=178, w2=313, w3=225, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.983125 + 0.0042875 * anchor
    return base_signal.diff().diff()

def f93_mcf_275_struct_v275_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=185, w2=324, w3=238, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(324, min_periods=max(324//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.299 * slope + 0.0042876 * anchor
    return base_signal.diff().diff()

def f93_mcf_276_struct_v276_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=192, w2=335, w3=251, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(335, min_periods=max(335//3, 2)).mean()
    noise = impulse.abs().rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.011875 + 0.0042877 * anchor
    return base_signal.diff().diff()

def f93_mcf_277_struct_v277_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=199, w2=346, w3=264, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 346)
    curvature = _rolling_slope(acceleration, 264)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3142 * acceleration + 0.0042878 * anchor
    return base_signal.diff().diff()

def f93_mcf_278_struct_v278_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=206, w2=357, w3=277, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(357, min_periods=max(357//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.040625 + 0.0042879 * anchor
    return base_signal.diff().diff()

def f93_mcf_279_struct_v279_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=213, w2=368, w3=290, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(368, min_periods=max(368//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3294 * _rolling_slope(draw, 290) + 0.004288 * anchor
    return base_signal.diff().diff()

def f93_mcf_280_struct_v280_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=220, w2=379, w3=303, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(379, min_periods=max(379//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.069375 + 0.0042881 * anchor
    return base_signal.diff().diff()

def f93_mcf_281_struct_v281_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=227, w2=390, w3=316, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 390)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.08375 + 0.0042882 * anchor
    return base_signal.diff().diff()

def f93_mcf_282_struct_v282_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=234, w2=401, w3=329, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(401, min_periods=max(401//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.098125 + 0.0042883 * anchor
    return base_signal.diff().diff()

def f93_mcf_283_struct_v283_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=241, w2=412, w3=342, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(412, min_periods=max(412//3, 2)).rank(pct=True)
    persistence = change.rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3598 * persistence + 0.0042884 * anchor
    return base_signal.diff().diff()

def f93_mcf_284_struct_v284_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=248, w2=423, w3=355, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(423, min_periods=max(423//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.126875 + 0.0042885 * anchor
    return base_signal.diff().diff()

def f93_mcf_285_struct_v285_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=255, w2=434, w3=368, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(434, min_periods=max(434//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 255)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.375 * slope + 0.0042886 * anchor
    return base_signal.diff().diff()

def f93_mcf_286_struct_v286_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=11, w2=445, w3=381, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(11)
    drag = impulse.rolling(445, min_periods=max(445//3, 2)).mean()
    noise = impulse.abs().rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.155625 + 0.0042887 * anchor
    return base_signal.diff().diff()

def f93_mcf_287_struct_v287_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=18, w2=456, w3=394, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 456)
    curvature = _rolling_slope(acceleration, 394)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3902 * acceleration + 0.0042888 * anchor
    return base_signal.diff().diff()

def f93_mcf_288_struct_v288_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=25, w2=467, w3=407, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(467, min_periods=max(467//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.184375 + 0.0042889 * anchor
    return base_signal.diff().diff()

def f93_mcf_289_struct_v289_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=478, w3=420, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(478, min_periods=max(478//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4054 * _rolling_slope(draw, 420) + 0.004289 * anchor
    return base_signal.diff().diff()

def f93_mcf_290_struct_v290_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=489, w3=433, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(489, min_periods=max(489//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.213125 + 0.0042891 * anchor
    return base_signal.diff().diff()

def f93_mcf_291_struct_v291_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=500, w3=446, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 500)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2275 + 0.0042892 * anchor
    return base_signal.diff().diff()

def f93_mcf_292_struct_v292_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=511, w3=459, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(511, min_periods=max(511//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.241875 + 0.0042893 * anchor
    return base_signal.diff().diff()

def f93_mcf_293_struct_v293_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=19, w3=472, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(60)
    rank = change.rolling(19, min_periods=max(19//3, 2)).rank(pct=True)
    persistence = change.rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0594 * persistence + 0.0042894 * anchor
    return base_signal.diff().diff()

def f93_mcf_294_struct_v294_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=30, w3=485, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(30, min_periods=max(30//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.270625 + 0.0042895 * anchor
    return base_signal.diff().diff()

def f93_mcf_295_struct_v295_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=41, w3=498, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(41, min_periods=max(41//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0746 * slope + 0.0042896 * anchor
    return base_signal.diff().diff()

def f93_mcf_296_struct_v296_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=52, w3=511, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(81)
    drag = impulse.rolling(52, min_periods=max(52//3, 2)).mean()
    noise = impulse.abs().rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.299375 + 0.0042897 * anchor
    return base_signal.diff().diff()

def f93_mcf_297_struct_v297_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=63, w3=524, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 63)
    curvature = _rolling_slope(acceleration, 524)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0898 * acceleration + 0.0042898 * anchor
    return base_signal.diff().diff()

def f93_mcf_298_struct_v298_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=74, w3=537, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(74, min_periods=max(74//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.328125 + 0.0042899 * anchor
    return base_signal.diff().diff()

def f93_mcf_299_struct_v299_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=85, w3=550, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(85, min_periods=max(85//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.105 * _rolling_slope(draw, 550) + 0.00429 * anchor
    return base_signal.diff().diff()

def f93_mcf_300_struct_v300_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=96, w3=563, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(96, min_periods=max(96//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.356875 + 0.0042901 * anchor
    return base_signal.diff().diff()
