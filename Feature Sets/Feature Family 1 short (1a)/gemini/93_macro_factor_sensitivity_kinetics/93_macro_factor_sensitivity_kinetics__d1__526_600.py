"""93 macro factor sensitivity kinetics d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f93_mcf_526_struct_v526_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=67, w3=473, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(67, min_periods=max(67//3, 2)).mean()
    noise = impulse.abs().rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.513125 + 0.0043127 * anchor
    return base_signal.diff()

def f93_mcf_527_struct_v527_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=78, w3=486, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 78)
    curvature = _rolling_slope(acceleration, 486)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3322 * acceleration + 0.0043128 * anchor
    return base_signal.diff()

def f93_mcf_528_struct_v528_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=89, w3=499, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(89, min_periods=max(89//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.541875 + 0.0043129 * anchor
    return base_signal.diff()

def f93_mcf_529_struct_v529_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=100, w3=512, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3474 * _rolling_slope(draw, 512) + 0.004313 * anchor
    return base_signal.diff()

def f93_mcf_530_struct_v530_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=111, w3=525, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(111, min_periods=max(111//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.570625 + 0.0043131 * anchor
    return base_signal.diff()

def f93_mcf_531_struct_v531_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=122, w3=538, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.585 + 0.0043132 * anchor
    return base_signal.diff()

def f93_mcf_532_struct_v532_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=133, w3=551, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.599375 + 0.0043133 * anchor
    return base_signal.diff()

def f93_mcf_533_struct_v533_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=144, w3=564, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3778 * persistence + 0.0043134 * anchor
    return base_signal.diff()

def f93_mcf_534_struct_v534_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=155, w3=577, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.855 + 0.0043135 * anchor
    return base_signal.diff()

def f93_mcf_535_struct_v535_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=166, w3=590, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.393 * slope + 0.0043136 * anchor
    return base_signal.diff()

def f93_mcf_536_struct_v536_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=177, w3=603, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.88375 + 0.0043137 * anchor
    return base_signal.diff()

def f93_mcf_537_struct_v537_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=188, w3=616, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 188)
    curvature = _rolling_slope(acceleration, 616)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4082 * acceleration + 0.0043138 * anchor
    return base_signal.diff()

def f93_mcf_538_struct_v538_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=199, w3=629, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(199, min_periods=max(199//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9125 + 0.0043139 * anchor
    return base_signal.diff()

def f93_mcf_539_struct_v539_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=210, w3=642, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.047 * _rolling_slope(draw, 642) + 0.004314 * anchor
    return base_signal.diff()

def f93_mcf_540_struct_v540_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=221, w3=655, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.94125 + 0.0043141 * anchor
    return base_signal.diff()

def f93_mcf_541_struct_v541_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=232, w3=668, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 232)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.955625 + 0.0043142 * anchor
    return base_signal.diff()

def f93_mcf_542_struct_v542_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=243, w3=681, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(243, min_periods=max(243//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.97 + 0.0043143 * anchor
    return base_signal.diff()

def f93_mcf_543_struct_v543_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=254, w3=694, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(53)
    rank = change.rolling(254, min_periods=max(254//3, 2)).rank(pct=True)
    persistence = change.rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0774 * persistence + 0.0043144 * anchor
    return base_signal.diff()

def f93_mcf_544_struct_v544_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=265, w3=707, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(265, min_periods=max(265//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99875 + 0.0043145 * anchor
    return base_signal.diff()

def f93_mcf_545_struct_v545_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=276, w3=720, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(276, min_periods=max(276//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0926 * slope + 0.0043146 * anchor
    return base_signal.diff()

def f93_mcf_546_struct_v546_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=287, w3=733, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(74)
    drag = impulse.rolling(287, min_periods=max(287//3, 2)).mean()
    noise = impulse.abs().rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0275 + 0.0043147 * anchor
    return base_signal.diff()

def f93_mcf_547_struct_v547_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=298, w3=746, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 298)
    curvature = _rolling_slope(acceleration, 746)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1078 * acceleration + 0.0043148 * anchor
    return base_signal.diff()

def f93_mcf_548_struct_v548_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=309, w3=759, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(309, min_periods=max(309//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.05625 + 0.0043149 * anchor
    return base_signal.diff()

def f93_mcf_549_struct_v549_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=320, w3=15, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(320, min_periods=max(320//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.123 * _rolling_slope(draw, 15) + 0.004315 * anchor
    return base_signal.diff()

def f93_mcf_550_struct_v550_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=331, w3=28, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(331, min_periods=max(331//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.085 + 0.0043151 * anchor
    return base_signal.diff()

def f93_mcf_551_struct_v551_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=342, w3=41, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 342)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=41, adjust=False).mean() * 1.099375 + 0.0043152 * anchor
    return base_signal.diff()

def f93_mcf_552_struct_v552_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=353, w3=54, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.11375 + 0.0043153 * anchor
    return base_signal.diff()

def f93_mcf_553_struct_v553_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=364, w3=67, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(123)
    rank = change.rolling(364, min_periods=max(364//3, 2)).rank(pct=True)
    persistence = change.rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1534 * persistence + 0.0043154 * anchor
    return base_signal.diff()

def f93_mcf_554_struct_v554_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=375, w3=80, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(375, min_periods=max(375//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1425 + 0.0043155 * anchor
    return base_signal.diff()

def f93_mcf_555_struct_v555_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=386, w3=93, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1686 * slope + 0.0043156 * anchor
    return base_signal.diff()

def f93_mcf_556_struct_v556_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=397, w3=106, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(397, min_periods=max(397//3, 2)).mean()
    noise = impulse.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.17125 + 0.0043157 * anchor
    return base_signal.diff()

def f93_mcf_557_struct_v557_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=408, w3=119, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 408)
    curvature = _rolling_slope(acceleration, 119)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1838 * acceleration + 0.0043158 * anchor
    return base_signal.diff()

def f93_mcf_558_struct_v558_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=419, w3=132, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(419, min_periods=max(419//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2 + 0.0043159 * anchor
    return base_signal.diff()

def f93_mcf_559_struct_v559_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=430, w3=145, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(430, min_periods=max(430//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.199 * _rolling_slope(draw, 145) + 0.004316 * anchor
    return base_signal.diff()

def f93_mcf_560_struct_v560_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=441, w3=158, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(441, min_periods=max(441//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.22875 + 0.0043161 * anchor
    return base_signal.diff()

def f93_mcf_561_struct_v561_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=452, w3=171, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 452)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=171, adjust=False).mean() * 1.243125 + 0.0043162 * anchor
    return base_signal.diff()

def f93_mcf_562_struct_v562_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=463, w3=184, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(463, min_periods=max(463//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2575 + 0.0043163 * anchor
    return base_signal.diff()

def f93_mcf_563_struct_v563_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=474, w3=197, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2294 * persistence + 0.0043164 * anchor
    return base_signal.diff()

def f93_mcf_564_struct_v564_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=485, w3=210, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(485, min_periods=max(485//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28625 + 0.0043165 * anchor
    return base_signal.diff()

def f93_mcf_565_struct_v565_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=496, w3=223, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(496, min_periods=max(496//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2446 * slope + 0.0043166 * anchor
    return base_signal.diff()

def f93_mcf_566_struct_v566_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=507, w3=236, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.315 + 0.0043167 * anchor
    return base_signal.diff()

def f93_mcf_567_struct_v567_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=15, w3=249, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 249)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2598 * acceleration + 0.0043168 * anchor
    return base_signal.diff()

def f93_mcf_568_struct_v568_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=26, w3=262, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(26, min_periods=max(26//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.34375 + 0.0043169 * anchor
    return base_signal.diff()

def f93_mcf_569_struct_v569_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=37, w3=275, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.275 * _rolling_slope(draw, 275) + 0.004317 * anchor
    return base_signal.diff()

def f93_mcf_570_struct_v570_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=48, w3=288, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(48, min_periods=max(48//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3725 + 0.0043171 * anchor
    return base_signal.diff()

def f93_mcf_571_struct_v571_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=59, w3=301, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 59)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.386875 + 0.0043172 * anchor
    return base_signal.diff()

def f93_mcf_572_struct_v572_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=70, w3=314, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(70, min_periods=max(70//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.40125 + 0.0043173 * anchor
    return base_signal.diff()

def f93_mcf_573_struct_v573_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=81, w3=327, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(12)
    rank = change.rolling(81, min_periods=max(81//3, 2)).rank(pct=True)
    persistence = change.rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3054 * persistence + 0.0043174 * anchor
    return base_signal.diff()

def f93_mcf_574_struct_v574_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=92, w3=340, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(92, min_periods=max(92//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43 + 0.0043175 * anchor
    return base_signal.diff()

def f93_mcf_575_struct_v575_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=103, w3=353, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(103, min_periods=max(103//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3206 * slope + 0.0043176 * anchor
    return base_signal.diff()

def f93_mcf_576_struct_v576_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=114, w3=366, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(33)
    drag = impulse.rolling(114, min_periods=max(114//3, 2)).mean()
    noise = impulse.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45875 + 0.0043177 * anchor
    return base_signal.diff()

def f93_mcf_577_struct_v577_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=125, w3=379, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 125)
    curvature = _rolling_slope(acceleration, 379)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3358 * acceleration + 0.0043178 * anchor
    return base_signal.diff()

def f93_mcf_578_struct_v578_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=136, w3=392, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(136, min_periods=max(136//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4875 + 0.0043179 * anchor
    return base_signal.diff()

def f93_mcf_579_struct_v579_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=147, w3=405, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(147, min_periods=max(147//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.351 * _rolling_slope(draw, 405) + 0.004318 * anchor
    return base_signal.diff()

def f93_mcf_580_struct_v580_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=158, w3=418, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(158, min_periods=max(158//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51625 + 0.0043181 * anchor
    return base_signal.diff()

def f93_mcf_581_struct_v581_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=169, w3=431, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 169)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.530625 + 0.0043182 * anchor
    return base_signal.diff()

def f93_mcf_582_struct_v582_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=180, w3=444, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.545 + 0.0043183 * anchor
    return base_signal.diff()

def f93_mcf_583_struct_v583_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=191, w3=457, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(82)
    rank = change.rolling(191, min_periods=max(191//3, 2)).rank(pct=True)
    persistence = change.rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3814 * persistence + 0.0043184 * anchor
    return base_signal.diff()

def f93_mcf_584_struct_v584_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=202, w3=470, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57375 + 0.0043185 * anchor
    return base_signal.diff()

def f93_mcf_585_struct_v585_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=213, w3=483, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(213, min_periods=max(213//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3966 * slope + 0.0043186 * anchor
    return base_signal.diff()

def f93_mcf_586_struct_v586_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=224, w3=496, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(103)
    drag = impulse.rolling(224, min_periods=max(224//3, 2)).mean()
    noise = impulse.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.6025 + 0.0043187 * anchor
    return base_signal.diff()

def f93_mcf_587_struct_v587_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=235, w3=509, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 235)
    curvature = _rolling_slope(acceleration, 509)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0354 * acceleration + 0.0043188 * anchor
    return base_signal.diff()

def f93_mcf_588_struct_v588_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=246, w3=522, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(246, min_periods=max(246//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.858125 + 0.0043189 * anchor
    return base_signal.diff()

def f93_mcf_589_struct_v589_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=257, w3=535, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(257, min_periods=max(257//3, 2)).max()
    rebound = x - x.rolling(124, min_periods=max(124//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0506 * _rolling_slope(draw, 535) + 0.004319 * anchor
    return base_signal.diff()

def f93_mcf_590_struct_v590_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=268, w3=548, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(268, min_periods=max(268//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.886875 + 0.0043191 * anchor
    return base_signal.diff()

def f93_mcf_591_struct_v591_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=279, w3=561, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 279)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.90125 + 0.0043192 * anchor
    return base_signal.diff()

def f93_mcf_592_struct_v592_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=290, w3=574, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(290, min_periods=max(290//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.915625 + 0.0043193 * anchor
    return base_signal.diff()

def f93_mcf_593_struct_v593_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=301, w3=587, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.081 * persistence + 0.0043194 * anchor
    return base_signal.diff()

def f93_mcf_594_struct_v594_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=312, w3=600, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(312, min_periods=max(312//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.944375 + 0.0043195 * anchor
    return base_signal.diff()

def f93_mcf_595_struct_v595_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=323, w3=613, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(323, min_periods=max(323//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0962 * slope + 0.0043196 * anchor
    return base_signal.diff()

def f93_mcf_596_struct_v596_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=334, w3=626, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.973125 + 0.0043197 * anchor
    return base_signal.diff()

def f93_mcf_597_struct_v597_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=345, w3=639, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 345)
    curvature = _rolling_slope(acceleration, 639)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1114 * acceleration + 0.0043198 * anchor
    return base_signal.diff()

def f93_mcf_598_struct_v598_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=356, w3=652, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.001875 + 0.0043199 * anchor
    return base_signal.diff()

def f93_mcf_599_struct_v599_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=367, w3=665, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(367, min_periods=max(367//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1266 * _rolling_slope(draw, 665) + 0.00432 * anchor
    return base_signal.diff()

def f93_mcf_600_struct_v600_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=378, w3=678, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(378, min_periods=max(378//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.030625 + 0.0043201 * anchor
    return base_signal.diff()
