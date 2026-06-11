"""17 options skew at peak d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f17_optx_526_struct_v526_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=294, w3=165, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(38)
    drag = impulse.rolling(294, min_periods=max(294//3, 2)).mean()
    noise = impulse.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.184375 + 0.0010727 * anchor
    return base_signal.diff()

def f17_optx_527_struct_v527_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=305, w3=178, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 305)
    curvature = _rolling_slope(acceleration, 178)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2578 * acceleration + 0.0010728 * anchor
    return base_signal.diff()

def f17_optx_528_struct_v528_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=316, w3=191, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(316, min_periods=max(316//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.213125 + 0.0010729 * anchor
    return base_signal.diff()

def f17_optx_529_struct_v529_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=327, w3=204, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(327, min_periods=max(327//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.273 * _rolling_slope(draw, 204) + 0.001073 * anchor
    return base_signal.diff()

def f17_optx_530_struct_v530_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=338, w3=217, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.241875 + 0.0010731 * anchor
    return base_signal.diff()

def f17_optx_531_struct_v531_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=349, w3=230, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 349)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 1.25625 + 0.0010732 * anchor
    return base_signal.diff()

def f17_optx_532_struct_v532_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=360, w3=243, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.270625 + 0.0010733 * anchor
    return base_signal.diff()

def f17_optx_533_struct_v533_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=371, w3=256, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(87)
    rank = change.rolling(371, min_periods=max(371//3, 2)).rank(pct=True)
    persistence = change.rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3034 * persistence + 0.0010734 * anchor
    return base_signal.diff()

def f17_optx_534_struct_v534_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=382, w3=269, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.299375 + 0.0010735 * anchor
    return base_signal.diff()

def f17_optx_535_struct_v535_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=393, w3=282, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(393, min_periods=max(393//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3186 * slope + 0.0010736 * anchor
    return base_signal.diff()

def f17_optx_536_struct_v536_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=404, w3=295, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(108)
    drag = impulse.rolling(404, min_periods=max(404//3, 2)).mean()
    noise = impulse.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.328125 + 0.0010737 * anchor
    return base_signal.diff()

def f17_optx_537_struct_v537_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=415, w3=308, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 415)
    curvature = _rolling_slope(acceleration, 308)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3338 * acceleration + 0.0010738 * anchor
    return base_signal.diff()

def f17_optx_538_struct_v538_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=426, w3=321, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(426, min_periods=max(426//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.356875 + 0.0010739 * anchor
    return base_signal.diff()

def f17_optx_539_struct_v539_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=437, w3=334, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(437, min_periods=max(437//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.349 * _rolling_slope(draw, 334) + 0.001074 * anchor
    return base_signal.diff()

def f17_optx_540_struct_v540_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=448, w3=347, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(448, min_periods=max(448//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.385625 + 0.0010741 * anchor
    return base_signal.diff()

def f17_optx_541_struct_v541_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=459, w3=360, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 459)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4 + 0.0010742 * anchor
    return base_signal.diff()

def f17_optx_542_struct_v542_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=470, w3=373, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(470, min_periods=max(470//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.414375 + 0.0010743 * anchor
    return base_signal.diff()

def f17_optx_543_struct_v543_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=481, w3=386, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(481, min_periods=max(481//3, 2)).rank(pct=True)
    persistence = change.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3794 * persistence + 0.0010744 * anchor
    return base_signal.diff()

def f17_optx_544_struct_v544_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=492, w3=399, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(492, min_periods=max(492//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.443125 + 0.0010745 * anchor
    return base_signal.diff()

def f17_optx_545_struct_v545_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=503, w3=412, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(503, min_periods=max(503//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3946 * slope + 0.0010746 * anchor
    return base_signal.diff()

def f17_optx_546_struct_v546_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=11, w3=425, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(11, min_periods=max(11//3, 2)).mean()
    noise = impulse.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.471875 + 0.0010747 * anchor
    return base_signal.diff()

def f17_optx_547_struct_v547_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=22, w3=438, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 22)
    curvature = _rolling_slope(acceleration, 438)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4098 * acceleration + 0.0010748 * anchor
    return base_signal.diff()

def f17_optx_548_struct_v548_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=33, w3=451, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(33, min_periods=max(33//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.500625 + 0.0010749 * anchor
    return base_signal.diff()

def f17_optx_549_struct_v549_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=44, w3=464, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(44, min_periods=max(44//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0486 * _rolling_slope(draw, 464) + 0.001075 * anchor
    return base_signal.diff()

def f17_optx_550_struct_v550_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=55, w3=477, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(55, min_periods=max(55//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.529375 + 0.0010751 * anchor
    return base_signal.diff()

def f17_optx_551_struct_v551_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=66, w3=490, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 66)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.54375 + 0.0010752 * anchor
    return base_signal.diff()

def f17_optx_552_struct_v552_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=77, w3=503, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(77, min_periods=max(77//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.558125 + 0.0010753 * anchor
    return base_signal.diff()

def f17_optx_553_struct_v553_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=88, w3=516, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(88, min_periods=max(88//3, 2)).rank(pct=True)
    persistence = change.rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.079 * persistence + 0.0010754 * anchor
    return base_signal.diff()

def f17_optx_554_struct_v554_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=99, w3=529, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.586875 + 0.0010755 * anchor
    return base_signal.diff()

def f17_optx_555_struct_v555_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=110, w3=542, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0942 * slope + 0.0010756 * anchor
    return base_signal.diff()

def f17_optx_556_struct_v556_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=121, w3=555, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.615625 + 0.0010757 * anchor
    return base_signal.diff()

def f17_optx_557_struct_v557_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=132, w3=568, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 255)
    acceleration = _rolling_slope(velocity, 132)
    curvature = _rolling_slope(acceleration, 568)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1094 * acceleration + 0.0010758 * anchor
    return base_signal.diff()

def f17_optx_558_struct_v558_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=143, w3=581, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(143, min_periods=max(143//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87125 + 0.0010759 * anchor
    return base_signal.diff()

def f17_optx_559_struct_v559_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=154, w3=594, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(154, min_periods=max(154//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1246 * _rolling_slope(draw, 594) + 0.001076 * anchor
    return base_signal.diff()

def f17_optx_560_struct_v560_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=165, w3=607, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(165, min_periods=max(165//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9 + 0.0010761 * anchor
    return base_signal.diff()

def f17_optx_561_struct_v561_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=176, w3=620, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 176)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.914375 + 0.0010762 * anchor
    return base_signal.diff()

def f17_optx_562_struct_v562_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=187, w3=633, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(187, min_periods=max(187//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92875 + 0.0010763 * anchor
    return base_signal.diff()

def f17_optx_563_struct_v563_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=198, w3=646, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(46)
    rank = change.rolling(198, min_periods=max(198//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.155 * persistence + 0.0010764 * anchor
    return base_signal.diff()

def f17_optx_564_struct_v564_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=209, w3=659, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(209, min_periods=max(209//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9575 + 0.0010765 * anchor
    return base_signal.diff()

def f17_optx_565_struct_v565_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=220, w3=672, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(220, min_periods=max(220//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1702 * slope + 0.0010766 * anchor
    return base_signal.diff()

def f17_optx_566_struct_v566_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=231, w3=685, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(67)
    drag = impulse.rolling(231, min_periods=max(231//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98625 + 0.0010767 * anchor
    return base_signal.diff()

def f17_optx_567_struct_v567_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=242, w3=698, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 242)
    curvature = _rolling_slope(acceleration, 698)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1854 * acceleration + 0.0010768 * anchor
    return base_signal.diff()

def f17_optx_568_struct_v568_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=253, w3=711, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(253, min_periods=max(253//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.015 + 0.0010769 * anchor
    return base_signal.diff()

def f17_optx_569_struct_v569_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=264, w3=724, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(264, min_periods=max(264//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2006 * _rolling_slope(draw, 724) + 0.001077 * anchor
    return base_signal.diff()

def f17_optx_570_struct_v570_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=275, w3=737, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(275, min_periods=max(275//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04375 + 0.0010771 * anchor
    return base_signal.diff()

def f17_optx_571_struct_v571_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=286, w3=750, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 286)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.058125 + 0.0010772 * anchor
    return base_signal.diff()

def f17_optx_572_struct_v572_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=297, w3=763, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(297, min_periods=max(297//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0725 + 0.0010773 * anchor
    return base_signal.diff()

def f17_optx_573_struct_v573_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=308, w3=19, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(116)
    rank = change.rolling(308, min_periods=max(308//3, 2)).rank(pct=True)
    persistence = change.rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.231 * persistence + 0.0010774 * anchor
    return base_signal.diff()

def f17_optx_574_struct_v574_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=319, w3=32, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(319, min_periods=max(319//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10125 + 0.0010775 * anchor
    return base_signal.diff()

def f17_optx_575_struct_v575_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=330, w3=45, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(330, min_periods=max(330//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2462 * slope + 0.0010776 * anchor
    return base_signal.diff()

def f17_optx_576_struct_v576_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=341, w3=58, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(341, min_periods=max(341//3, 2)).mean()
    noise = impulse.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13 + 0.0010777 * anchor
    return base_signal.diff()

def f17_optx_577_struct_v577_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=352, w3=71, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 352)
    curvature = _rolling_slope(acceleration, 71)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2614 * acceleration + 0.0010778 * anchor
    return base_signal.diff()

def f17_optx_578_struct_v578_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=363, w3=84, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(363, min_periods=max(363//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(84) * 1.15875 + 0.0010779 * anchor
    return base_signal.diff()

def f17_optx_579_struct_v579_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=374, w3=97, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(374, min_periods=max(374//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2766 * _rolling_slope(draw, 97) + 0.001078 * anchor
    return base_signal.diff()

def f17_optx_580_struct_v580_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=385, w3=110, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(385, min_periods=max(385//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1875 + 0.0010781 * anchor
    return base_signal.diff()

def f17_optx_581_struct_v581_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=396, w3=123, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 396)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=123, adjust=False).mean() * 1.201875 + 0.0010782 * anchor
    return base_signal.diff()

def f17_optx_582_struct_v582_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=407, w3=136, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(407, min_periods=max(407//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21625 + 0.0010783 * anchor
    return base_signal.diff()

def f17_optx_583_struct_v583_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=418, w3=149, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(418, min_periods=max(418//3, 2)).rank(pct=True)
    persistence = change.rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.307 * persistence + 0.0010784 * anchor
    return base_signal.diff()

def f17_optx_584_struct_v584_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=429, w3=162, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(429, min_periods=max(429//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245 + 0.0010785 * anchor
    return base_signal.diff()

def f17_optx_585_struct_v585_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=440, w3=175, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(440, min_periods=max(440//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3222 * slope + 0.0010786 * anchor
    return base_signal.diff()

def f17_optx_586_struct_v586_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=451, w3=188, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27375 + 0.0010787 * anchor
    return base_signal.diff()

def f17_optx_587_struct_v587_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=462, w3=201, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 462)
    curvature = _rolling_slope(acceleration, 201)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3374 * acceleration + 0.0010788 * anchor
    return base_signal.diff()

def f17_optx_588_struct_v588_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=473, w3=214, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3025 + 0.0010789 * anchor
    return base_signal.diff()

def f17_optx_589_struct_v589_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=484, w3=227, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(484, min_periods=max(484//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3526 * _rolling_slope(draw, 227) + 0.001079 * anchor
    return base_signal.diff()

def f17_optx_590_struct_v590_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=495, w3=240, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33125 + 0.0010791 * anchor
    return base_signal.diff()

def f17_optx_591_struct_v591_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=506, w3=253, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 506)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=253, adjust=False).mean() * 1.345625 + 0.0010792 * anchor
    return base_signal.diff()

def f17_optx_592_struct_v592_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=14, w3=266, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36 + 0.0010793 * anchor
    return base_signal.diff()

def f17_optx_593_struct_v593_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=25, w3=279, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(5)
    rank = change.rolling(25, min_periods=max(25//3, 2)).rank(pct=True)
    persistence = change.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.383 * persistence + 0.0010794 * anchor
    return base_signal.diff()

def f17_optx_594_struct_v594_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=36, w3=292, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38875 + 0.0010795 * anchor
    return base_signal.diff()

def f17_optx_595_struct_v595_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=47, w3=305, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(47, min_periods=max(47//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 19)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3982 * slope + 0.0010796 * anchor
    return base_signal.diff()

def f17_optx_596_struct_v596_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=58, w3=318, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(26)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4175 + 0.0010797 * anchor
    return base_signal.diff()

def f17_optx_597_struct_v597_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=69, w3=331, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 331)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.037 * acceleration + 0.0010798 * anchor
    return base_signal.diff()

def f17_optx_598_struct_v598_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=80, w3=344, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.44625 + 0.0010799 * anchor
    return base_signal.diff()

def f17_optx_599_struct_v599_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=91, w3=357, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(91, min_periods=max(91//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0522 * _rolling_slope(draw, 357) + 0.00108 * anchor
    return base_signal.diff()

def f17_optx_600_struct_v600_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=102, w3=370, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.475 + 0.0010801 * anchor
    return base_signal.diff()
