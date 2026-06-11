"""92 executive turnover signals d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Governance - Institutional-grade short-side signal.
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

def f92_exec_526_struct_v526_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=509, w3=243, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(509, min_periods=max(509//3, 2)).mean()
    noise = impulse.abs().rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3925 + 0.0042527 * anchor
    return base_signal.diff()

def f92_exec_527_struct_v527_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=17, w3=256, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 17)
    curvature = _rolling_slope(acceleration, 256)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.289 * acceleration + 0.0042528 * anchor
    return base_signal.diff()

def f92_exec_528_struct_v528_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=28, w3=269, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(28, min_periods=max(28//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.42125 + 0.0042529 * anchor
    return base_signal.diff()

def f92_exec_529_struct_v529_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=39, w3=282, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(39, min_periods=max(39//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3042 * _rolling_slope(draw, 282) + 0.004253 * anchor
    return base_signal.diff()

def f92_exec_530_struct_v530_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=50, w3=295, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(50, min_periods=max(50//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.45 + 0.0042531 * anchor
    return base_signal.diff()

def f92_exec_531_struct_v531_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=61, w3=308, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 61)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.464375 + 0.0042532 * anchor
    return base_signal.diff()

def f92_exec_532_struct_v532_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=72, w3=321, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(72, min_periods=max(72//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47875 + 0.0042533 * anchor
    return base_signal.diff()

def f92_exec_533_struct_v533_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=83, w3=334, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(50)
    rank = change.rolling(83, min_periods=max(83//3, 2)).rank(pct=True)
    persistence = change.rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3346 * persistence + 0.0042534 * anchor
    return base_signal.diff()

def f92_exec_534_struct_v534_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=94, w3=347, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(94, min_periods=max(94//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5075 + 0.0042535 * anchor
    return base_signal.diff()

def f92_exec_535_struct_v535_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=105, w3=360, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(105, min_periods=max(105//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3498 * slope + 0.0042536 * anchor
    return base_signal.diff()

def f92_exec_536_struct_v536_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=116, w3=373, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(71)
    drag = impulse.rolling(116, min_periods=max(116//3, 2)).mean()
    noise = impulse.abs().rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.53625 + 0.0042537 * anchor
    return base_signal.diff()

def f92_exec_537_struct_v537_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=127, w3=386, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 127)
    curvature = _rolling_slope(acceleration, 386)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.365 * acceleration + 0.0042538 * anchor
    return base_signal.diff()

def f92_exec_538_struct_v538_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=138, w3=399, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(138, min_periods=max(138//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.565 + 0.0042539 * anchor
    return base_signal.diff()

def f92_exec_539_struct_v539_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=149, w3=412, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(149, min_periods=max(149//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3802 * _rolling_slope(draw, 412) + 0.004254 * anchor
    return base_signal.diff()

def f92_exec_540_struct_v540_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=160, w3=425, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59375 + 0.0042541 * anchor
    return base_signal.diff()

def f92_exec_541_struct_v541_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=171, w3=438, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 106)
    slow = _rolling_slope(x, 171)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.608125 + 0.0042542 * anchor
    return base_signal.diff()

def f92_exec_542_struct_v542_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=182, w3=451, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(182, min_periods=max(182//3, 2)).max()
    trough = x.rolling(113, min_periods=max(113//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6225 + 0.0042543 * anchor
    return base_signal.diff()

def f92_exec_543_struct_v543_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=193, w3=464, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(120)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4106 * persistence + 0.0042544 * anchor
    return base_signal.diff()

def f92_exec_544_struct_v544_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=204, w3=477, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(127, min_periods=max(127//3, 2)).std()
    vol_slow = ret.rolling(204, min_periods=max(204//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.878125 + 0.0042545 * anchor
    return base_signal.diff()

def f92_exec_545_struct_v545_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=215, w3=490, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 134)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0494 * slope + 0.0042546 * anchor
    return base_signal.diff()

def f92_exec_546_struct_v546_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=226, w3=503, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(226, min_periods=max(226//3, 2)).mean()
    noise = impulse.abs().rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.906875 + 0.0042547 * anchor
    return base_signal.diff()

def f92_exec_547_struct_v547_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=237, w3=516, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 148)
    acceleration = _rolling_slope(velocity, 237)
    curvature = _rolling_slope(acceleration, 516)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0646 * acceleration + 0.0042548 * anchor
    return base_signal.diff()

def f92_exec_548_struct_v548_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=248, w3=529, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(248, min_periods=max(248//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.935625 + 0.0042549 * anchor
    return base_signal.diff()

def f92_exec_549_struct_v549_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=259, w3=542, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(259, min_periods=max(259//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0798 * _rolling_slope(draw, 542) + 0.004255 * anchor
    return base_signal.diff()

def f92_exec_550_struct_v550_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=270, w3=555, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 169)
    baseline = trend.rolling(270, min_periods=max(270//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.964375 + 0.0042551 * anchor
    return base_signal.diff()

def f92_exec_551_struct_v551_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=281, w3=568, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 281)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.97875 + 0.0042552 * anchor
    return base_signal.diff()

def f92_exec_552_struct_v552_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=292, w3=581, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(292, min_periods=max(292//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.993125 + 0.0042553 * anchor
    return base_signal.diff()

def f92_exec_553_struct_v553_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=303, w3=594, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(303, min_periods=max(303//3, 2)).rank(pct=True)
    persistence = change.rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1102 * persistence + 0.0042554 * anchor
    return base_signal.diff()

def f92_exec_554_struct_v554_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=314, w3=607, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(314, min_periods=max(314//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.021875 + 0.0042555 * anchor
    return base_signal.diff()

def f92_exec_555_struct_v555_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=325, w3=620, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(325, min_periods=max(325//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1254 * slope + 0.0042556 * anchor
    return base_signal.diff()

def f92_exec_556_struct_v556_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=336, w3=633, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(336, min_periods=max(336//3, 2)).mean()
    noise = impulse.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.050625 + 0.0042557 * anchor
    return base_signal.diff()

def f92_exec_557_struct_v557_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=347, w3=646, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 347)
    curvature = _rolling_slope(acceleration, 646)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1406 * acceleration + 0.0042558 * anchor
    return base_signal.diff()

def f92_exec_558_struct_v558_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=358, w3=659, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(358, min_periods=max(358//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.079375 + 0.0042559 * anchor
    return base_signal.diff()

def f92_exec_559_struct_v559_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=369, w3=672, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1558 * _rolling_slope(draw, 672) + 0.004256 * anchor
    return base_signal.diff()

def f92_exec_560_struct_v560_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=380, w3=685, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(380, min_periods=max(380//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.108125 + 0.0042561 * anchor
    return base_signal.diff()

def f92_exec_561_struct_v561_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=391, w3=698, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 391)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1225 + 0.0042562 * anchor
    return base_signal.diff()

def f92_exec_562_struct_v562_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=402, w3=711, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(402, min_periods=max(402//3, 2)).max()
    trough = x.rolling(253, min_periods=max(253//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.136875 + 0.0042563 * anchor
    return base_signal.diff()

def f92_exec_563_struct_v563_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=413, w3=724, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(9)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1862 * persistence + 0.0042564 * anchor
    return base_signal.diff()

def f92_exec_564_struct_v564_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=424, w3=737, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(424, min_periods=max(424//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.165625 + 0.0042565 * anchor
    return base_signal.diff()

def f92_exec_565_struct_v565_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=435, w3=750, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(435, min_periods=max(435//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2014 * slope + 0.0042566 * anchor
    return base_signal.diff()

def f92_exec_566_struct_v566_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=446, w3=763, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(30)
    drag = impulse.rolling(446, min_periods=max(446//3, 2)).mean()
    noise = impulse.abs().rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.194375 + 0.0042567 * anchor
    return base_signal.diff()

def f92_exec_567_struct_v567_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=457, w3=19, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 457)
    curvature = _rolling_slope(acceleration, 19)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2166 * acceleration + 0.0042568 * anchor
    return base_signal.diff()

def f92_exec_568_struct_v568_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=468, w3=32, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(468, min_periods=max(468//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(32) * 1.223125 + 0.0042569 * anchor
    return base_signal.diff()

def f92_exec_569_struct_v569_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=479, w3=45, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(479, min_periods=max(479//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2318 * _rolling_slope(draw, 45) + 0.004257 * anchor
    return base_signal.diff()

def f92_exec_570_struct_v570_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=490, w3=58, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(490, min_periods=max(490//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.251875 + 0.0042571 * anchor
    return base_signal.diff()

def f92_exec_571_struct_v571_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=501, w3=71, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 501)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=71, adjust=False).mean() * 1.26625 + 0.0042572 * anchor
    return base_signal.diff()

def f92_exec_572_struct_v572_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=512, w3=84, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(512, min_periods=max(512//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.280625 + 0.0042573 * anchor
    return base_signal.diff()

def f92_exec_573_struct_v573_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=20, w3=97, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(79)
    rank = change.rolling(20, min_periods=max(20//3, 2)).rank(pct=True)
    persistence = change.rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2622 * persistence + 0.0042574 * anchor
    return base_signal.diff()

def f92_exec_574_struct_v574_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=31, w3=110, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.309375 + 0.0042575 * anchor
    return base_signal.diff()

def f92_exec_575_struct_v575_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=42, w3=123, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(42, min_periods=max(42//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2774 * slope + 0.0042576 * anchor
    return base_signal.diff()

def f92_exec_576_struct_v576_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=53, w3=136, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(100)
    drag = impulse.rolling(53, min_periods=max(53//3, 2)).mean()
    noise = impulse.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.338125 + 0.0042577 * anchor
    return base_signal.diff()

def f92_exec_577_struct_v577_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=64, w3=149, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 64)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2926 * acceleration + 0.0042578 * anchor
    return base_signal.diff()

def f92_exec_578_struct_v578_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=75, w3=162, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(75, min_periods=max(75//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.366875 + 0.0042579 * anchor
    return base_signal.diff()

def f92_exec_579_struct_v579_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=86, w3=175, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3078 * _rolling_slope(draw, 175) + 0.004258 * anchor
    return base_signal.diff()

def f92_exec_580_struct_v580_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=97, w3=188, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(97, min_periods=max(97//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.395625 + 0.0042581 * anchor
    return base_signal.diff()

def f92_exec_581_struct_v581_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=108, w3=201, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 108)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=201, adjust=False).mean() * 1.41 + 0.0042582 * anchor
    return base_signal.diff()

def f92_exec_582_struct_v582_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=119, w3=214, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.424375 + 0.0042583 * anchor
    return base_signal.diff()

def f92_exec_583_struct_v583_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=130, w3=227, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(130, min_periods=max(130//3, 2)).rank(pct=True)
    persistence = change.rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3382 * persistence + 0.0042584 * anchor
    return base_signal.diff()

def f92_exec_584_struct_v584_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=141, w3=240, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(141, min_periods=max(141//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.453125 + 0.0042585 * anchor
    return base_signal.diff()

def f92_exec_585_struct_v585_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=152, w3=253, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(152, min_periods=max(152//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3534 * slope + 0.0042586 * anchor
    return base_signal.diff()

def f92_exec_586_struct_v586_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=163, w3=266, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(163, min_periods=max(163//3, 2)).mean()
    noise = impulse.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.481875 + 0.0042587 * anchor
    return base_signal.diff()

def f92_exec_587_struct_v587_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=174, w3=279, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 279)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3686 * acceleration + 0.0042588 * anchor
    return base_signal.diff()

def f92_exec_588_struct_v588_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=185, w3=292, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(185, min_periods=max(185//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.510625 + 0.0042589 * anchor
    return base_signal.diff()

def f92_exec_589_struct_v589_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=196, w3=305, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(196, min_periods=max(196//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3838 * _rolling_slope(draw, 305) + 0.004259 * anchor
    return base_signal.diff()

def f92_exec_590_struct_v590_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=207, w3=318, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(207, min_periods=max(207//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.539375 + 0.0042591 * anchor
    return base_signal.diff()

def f92_exec_591_struct_v591_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=218, w3=331, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.55375 + 0.0042592 * anchor
    return base_signal.diff()

def f92_exec_592_struct_v592_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=229, w3=344, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(229, min_periods=max(229//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.568125 + 0.0042593 * anchor
    return base_signal.diff()

def f92_exec_593_struct_v593_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=240, w3=357, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(240, min_periods=max(240//3, 2)).rank(pct=True)
    persistence = change.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0378 * persistence + 0.0042594 * anchor
    return base_signal.diff()

def f92_exec_594_struct_v594_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=251, w3=370, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.596875 + 0.0042595 * anchor
    return base_signal.diff()

def f92_exec_595_struct_v595_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=262, w3=383, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.053 * slope + 0.0042596 * anchor
    return base_signal.diff()

def f92_exec_596_struct_v596_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=273, w3=396, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(273, min_periods=max(273//3, 2)).mean()
    noise = impulse.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8525 + 0.0042597 * anchor
    return base_signal.diff()

def f92_exec_597_struct_v597_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=284, w3=409, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 284)
    curvature = _rolling_slope(acceleration, 409)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0682 * acceleration + 0.0042598 * anchor
    return base_signal.diff()

def f92_exec_598_struct_v598_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=295, w3=422, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(295, min_periods=max(295//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.88125 + 0.0042599 * anchor
    return base_signal.diff()

def f92_exec_599_struct_v599_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=306, w3=435, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(306, min_periods=max(306//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0834 * _rolling_slope(draw, 435) + 0.00426 * anchor
    return base_signal.diff()

def f92_exec_600_struct_v600_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=317, w3=448, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(317, min_periods=max(317//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.91 + 0.0042601 * anchor
    return base_signal.diff()
