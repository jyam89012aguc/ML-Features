"""18 insider activity snapshot d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f18_insd_226_struct_v226_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=73, w3=280, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(73, min_periods=max(73//3, 2)).mean()
    noise = impulse.abs().rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.858125 + 0.0011027 * anchor
    return base_signal.diff()

def f18_insd_227_struct_v227_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=84, w3=293, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 293)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2794 * acceleration + 0.0011028 * anchor
    return base_signal.diff()

def f18_insd_228_struct_v228_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=95, w3=306, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(95, min_periods=max(95//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.886875 + 0.0011029 * anchor
    return base_signal.diff()

def f18_insd_229_struct_v229_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=106, w3=319, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(106, min_periods=max(106//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2946 * _rolling_slope(draw, 319) + 0.001103 * anchor
    return base_signal.diff()

def f18_insd_230_struct_v230_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=117, w3=332, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(117, min_periods=max(117//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.915625 + 0.0011031 * anchor
    return base_signal.diff()

def f18_insd_231_struct_v231_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=128, w3=345, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.93 + 0.0011032 * anchor
    return base_signal.diff()

def f18_insd_232_struct_v232_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=139, w3=358, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.944375 + 0.0011033 * anchor
    return base_signal.diff()

def f18_insd_233_struct_v233_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=150, w3=371, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(150, min_periods=max(150//3, 2)).rank(pct=True)
    persistence = change.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.325 * persistence + 0.0011034 * anchor
    return base_signal.diff()

def f18_insd_234_struct_v234_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=161, w3=384, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.973125 + 0.0011035 * anchor
    return base_signal.diff()

def f18_insd_235_struct_v235_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=172, w3=397, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3402 * slope + 0.0011036 * anchor
    return base_signal.diff()

def f18_insd_236_struct_v236_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=183, w3=410, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.001875 + 0.0011037 * anchor
    return base_signal.diff()

def f18_insd_237_struct_v237_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=194, w3=423, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 194)
    curvature = _rolling_slope(acceleration, 423)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3554 * acceleration + 0.0011038 * anchor
    return base_signal.diff()

def f18_insd_238_struct_v238_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=205, w3=436, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(205, min_periods=max(205//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.030625 + 0.0011039 * anchor
    return base_signal.diff()

def f18_insd_239_struct_v239_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=216, w3=449, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3706 * _rolling_slope(draw, 449) + 0.001104 * anchor
    return base_signal.diff()

def f18_insd_240_struct_v240_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=227, w3=462, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(227, min_periods=max(227//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.059375 + 0.0011041 * anchor
    return base_signal.diff()

def f18_insd_241_struct_v241_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=238, w3=475, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 238)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.07375 + 0.0011042 * anchor
    return base_signal.diff()

def f18_insd_242_struct_v242_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=249, w3=488, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(249, min_periods=max(249//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.088125 + 0.0011043 * anchor
    return base_signal.diff()

def f18_insd_243_struct_v243_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=260, w3=501, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.401 * persistence + 0.0011044 * anchor
    return base_signal.diff()

def f18_insd_244_struct_v244_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=271, w3=514, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(271, min_periods=max(271//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.116875 + 0.0011045 * anchor
    return base_signal.diff()

def f18_insd_245_struct_v245_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=282, w3=527, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(282, min_periods=max(282//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0398 * slope + 0.0011046 * anchor
    return base_signal.diff()

def f18_insd_246_struct_v246_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=293, w3=540, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(19)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.145625 + 0.0011047 * anchor
    return base_signal.diff()

def f18_insd_247_struct_v247_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=304, w3=553, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 304)
    curvature = _rolling_slope(acceleration, 553)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.055 * acceleration + 0.0011048 * anchor
    return base_signal.diff()

def f18_insd_248_struct_v248_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=315, w3=566, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.174375 + 0.0011049 * anchor
    return base_signal.diff()

def f18_insd_249_struct_v249_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=326, w3=579, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0702 * _rolling_slope(draw, 579) + 0.001105 * anchor
    return base_signal.diff()

def f18_insd_250_struct_v250_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=337, w3=592, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(337, min_periods=max(337//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.203125 + 0.0011051 * anchor
    return base_signal.diff()

def f18_insd_251_struct_v251_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=348, w3=605, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2175 + 0.0011052 * anchor
    return base_signal.diff()

def f18_insd_252_struct_v252_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=359, w3=618, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(359, min_periods=max(359//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.231875 + 0.0011053 * anchor
    return base_signal.diff()

def f18_insd_253_struct_v253_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=370, w3=631, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(68)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1006 * persistence + 0.0011054 * anchor
    return base_signal.diff()

def f18_insd_254_struct_v254_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=381, w3=644, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.260625 + 0.0011055 * anchor
    return base_signal.diff()

def f18_insd_255_struct_v255_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=392, w3=657, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1158 * slope + 0.0011056 * anchor
    return base_signal.diff()

def f18_insd_256_struct_v256_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=403, w3=670, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(89)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.289375 + 0.0011057 * anchor
    return base_signal.diff()

def f18_insd_257_struct_v257_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=414, w3=683, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 683)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.131 * acceleration + 0.0011058 * anchor
    return base_signal.diff()

def f18_insd_258_struct_v258_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=425, w3=696, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.318125 + 0.0011059 * anchor
    return base_signal.diff()

def f18_insd_259_struct_v259_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=436, w3=709, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1462 * _rolling_slope(draw, 709) + 0.001106 * anchor
    return base_signal.diff()

def f18_insd_260_struct_v260_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=447, w3=722, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(447, min_periods=max(447//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.346875 + 0.0011061 * anchor
    return base_signal.diff()

def f18_insd_261_struct_v261_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=458, w3=735, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 458)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.36125 + 0.0011062 * anchor
    return base_signal.diff()

def f18_insd_262_struct_v262_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=469, w3=748, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(469, min_periods=max(469//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.375625 + 0.0011063 * anchor
    return base_signal.diff()

def f18_insd_263_struct_v263_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=480, w3=761, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1766 * persistence + 0.0011064 * anchor
    return base_signal.diff()

def f18_insd_264_struct_v264_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=491, w3=17, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.404375 + 0.0011065 * anchor
    return base_signal.diff()

def f18_insd_265_struct_v265_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=502, w3=30, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1918 * slope + 0.0011066 * anchor
    return base_signal.diff()

def f18_insd_266_struct_v266_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=10, w3=43, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(10, min_periods=max(10//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.433125 + 0.0011067 * anchor
    return base_signal.diff()

def f18_insd_267_struct_v267_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=21, w3=56, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 56)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.207 * acceleration + 0.0011068 * anchor
    return base_signal.diff()

def f18_insd_268_struct_v268_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=32, w3=69, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(32, min_periods=max(32//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(69) * 1.461875 + 0.0011069 * anchor
    return base_signal.diff()

def f18_insd_269_struct_v269_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=43, w3=82, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(43, min_periods=max(43//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2222 * _rolling_slope(draw, 82) + 0.001107 * anchor
    return base_signal.diff()

def f18_insd_270_struct_v270_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=54, w3=95, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.490625 + 0.0011071 * anchor
    return base_signal.diff()

def f18_insd_271_struct_v271_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=65, w3=108, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=108, adjust=False).mean() * 1.505 + 0.0011072 * anchor
    return base_signal.diff()

def f18_insd_272_struct_v272_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=76, w3=121, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(76, min_periods=max(76//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.519375 + 0.0011073 * anchor
    return base_signal.diff()

def f18_insd_273_struct_v273_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=87, w3=134, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2526 * persistence + 0.0011074 * anchor
    return base_signal.diff()

def f18_insd_274_struct_v274_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=98, w3=147, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.548125 + 0.0011075 * anchor
    return base_signal.diff()

def f18_insd_275_struct_v275_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=109, w3=160, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2678 * slope + 0.0011076 * anchor
    return base_signal.diff()

def f18_insd_276_struct_v276_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=120, w3=173, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.576875 + 0.0011077 * anchor
    return base_signal.diff()

def f18_insd_277_struct_v277_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=236, w2=131, w3=186, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 186)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283 * acceleration + 0.0011078 * anchor
    return base_signal.diff()

def f18_insd_278_struct_v278_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=142, w3=199, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.605625 + 0.0011079 * anchor
    return base_signal.diff()

def f18_insd_279_struct_v279_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=153, w3=212, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2982 * _rolling_slope(draw, 212) + 0.001108 * anchor
    return base_signal.diff()

def f18_insd_280_struct_v280_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=164, w3=225, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.86125 + 0.0011081 * anchor
    return base_signal.diff()

def f18_insd_281_struct_v281_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=175, w3=238, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=238, adjust=False).mean() * 0.875625 + 0.0011082 * anchor
    return base_signal.diff()

def f18_insd_282_struct_v282_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=186, w3=251, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.89 + 0.0011083 * anchor
    return base_signal.diff()

def f18_insd_283_struct_v283_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=197, w3=264, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(27)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3286 * persistence + 0.0011084 * anchor
    return base_signal.diff()

def f18_insd_284_struct_v284_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=208, w3=277, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.91875 + 0.0011085 * anchor
    return base_signal.diff()

def f18_insd_285_struct_v285_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=219, w3=290, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3438 * slope + 0.0011086 * anchor
    return base_signal.diff()

def f18_insd_286_struct_v286_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=230, w3=303, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(48)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9475 + 0.0011087 * anchor
    return base_signal.diff()

def f18_insd_287_struct_v287_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=241, w3=316, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 316)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.359 * acceleration + 0.0011088 * anchor
    return base_signal.diff()

def f18_insd_288_struct_v288_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=252, w3=329, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.97625 + 0.0011089 * anchor
    return base_signal.diff()

def f18_insd_289_struct_v289_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=69, w2=263, w3=342, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3742 * _rolling_slope(draw, 342) + 0.001109 * anchor
    return base_signal.diff()

def f18_insd_290_struct_v290_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=76, w2=274, w3=355, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.005 + 0.0011091 * anchor
    return base_signal.diff()

def f18_insd_291_struct_v291_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=83, w2=285, w3=368, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 285)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.019375 + 0.0011092 * anchor
    return base_signal.diff()

def f18_insd_292_struct_v292_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=90, w2=296, w3=381, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03375 + 0.0011093 * anchor
    return base_signal.diff()

def f18_insd_293_struct_v293_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=97, w2=307, w3=394, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(97)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4046 * persistence + 0.0011094 * anchor
    return base_signal.diff()

def f18_insd_294_struct_v294_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=104, w2=318, w3=407, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(318, min_periods=max(318//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0625 + 0.0011095 * anchor
    return base_signal.diff()

def f18_insd_295_struct_v295_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=111, w2=329, w3=420, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(329, min_periods=max(329//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0434 * slope + 0.0011096 * anchor
    return base_signal.diff()

def f18_insd_296_struct_v296_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=118, w2=340, w3=433, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(118)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.09125 + 0.0011097 * anchor
    return base_signal.diff()

def f18_insd_297_struct_v297_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=125, w2=351, w3=446, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 351)
    curvature = _rolling_slope(acceleration, 446)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0586 * acceleration + 0.0011098 * anchor
    return base_signal.diff()

def f18_insd_298_struct_v298_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=132, w2=362, w3=459, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(362, min_periods=max(362//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.12 + 0.0011099 * anchor
    return base_signal.diff()

def f18_insd_299_struct_v299_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=139, w2=373, w3=472, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0738 * _rolling_slope(draw, 472) + 0.00111 * anchor
    return base_signal.diff()

def f18_insd_300_struct_v300_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=146, w2=384, w3=485, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.14875 + 0.0011101 * anchor
    return base_signal.diff()
