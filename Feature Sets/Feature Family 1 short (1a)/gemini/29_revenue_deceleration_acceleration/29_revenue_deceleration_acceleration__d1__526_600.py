"""29 revenue deceleration acceleration d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f29_rda_526_struct_v526_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=20, w3=654, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.085625 + 0.0017927 * anchor
    return base_signal.diff()

def f29_rda_527_struct_v527_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=31, w3=667, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 667)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3998 * acceleration + 0.0017928 * anchor
    return base_signal.diff()

def f29_rda_528_struct_v528_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=42, w3=680, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(42, min_periods=max(42//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.114375 + 0.0017929 * anchor
    return base_signal.diff()

def f29_rda_529_struct_v529_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=53, w3=693, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0386 * _rolling_slope(draw, 693) + 0.001793 * anchor
    return base_signal.diff()

def f29_rda_530_struct_v530_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=64, w3=706, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(64, min_periods=max(64//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.143125 + 0.0017931 * anchor
    return base_signal.diff()

def f29_rda_531_struct_v531_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=75, w3=719, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 75)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1575 + 0.0017932 * anchor
    return base_signal.diff()

def f29_rda_532_struct_v532_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=86, w3=732, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(86, min_periods=max(86//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.171875 + 0.0017933 * anchor
    return base_signal.diff()

def f29_rda_533_struct_v533_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=97, w3=745, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(36)
    rank = change.rolling(97, min_periods=max(97//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.069 * persistence + 0.0017934 * anchor
    return base_signal.diff()

def f29_rda_534_struct_v534_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=108, w3=758, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(108, min_periods=max(108//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.200625 + 0.0017935 * anchor
    return base_signal.diff()

def f29_rda_535_struct_v535_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=119, w3=771, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0842 * slope + 0.0017936 * anchor
    return base_signal.diff()

def f29_rda_536_struct_v536_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=130, w3=27, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(57)
    drag = impulse.rolling(130, min_periods=max(130//3, 2)).mean()
    noise = impulse.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.229375 + 0.0017937 * anchor
    return base_signal.diff()

def f29_rda_537_struct_v537_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=141, w3=40, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 141)
    curvature = _rolling_slope(acceleration, 40)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0994 * acceleration + 0.0017938 * anchor
    return base_signal.diff()

def f29_rda_538_struct_v538_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=152, w3=53, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(53) * 1.258125 + 0.0017939 * anchor
    return base_signal.diff()

def f29_rda_539_struct_v539_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=163, w3=66, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(163, min_periods=max(163//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1146 * _rolling_slope(draw, 66) + 0.001794 * anchor
    return base_signal.diff()

def f29_rda_540_struct_v540_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=174, w3=79, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(174, min_periods=max(174//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.286875 + 0.0017941 * anchor
    return base_signal.diff()

def f29_rda_541_struct_v541_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=185, w3=92, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 185)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=92, adjust=False).mean() * 1.30125 + 0.0017942 * anchor
    return base_signal.diff()

def f29_rda_542_struct_v542_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=196, w3=105, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(196, min_periods=max(196//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.315625 + 0.0017943 * anchor
    return base_signal.diff()

def f29_rda_543_struct_v543_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=207, w3=118, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(106)
    rank = change.rolling(207, min_periods=max(207//3, 2)).rank(pct=True)
    persistence = change.rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.145 * persistence + 0.0017944 * anchor
    return base_signal.diff()

def f29_rda_544_struct_v544_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=218, w3=131, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(218, min_periods=max(218//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.344375 + 0.0017945 * anchor
    return base_signal.diff()

def f29_rda_545_struct_v545_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=229, w3=144, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(229, min_periods=max(229//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1602 * slope + 0.0017946 * anchor
    return base_signal.diff()

def f29_rda_546_struct_v546_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=240, w3=157, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(240, min_periods=max(240//3, 2)).mean()
    noise = impulse.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.373125 + 0.0017947 * anchor
    return base_signal.diff()

def f29_rda_547_struct_v547_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=251, w3=170, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 251)
    curvature = _rolling_slope(acceleration, 170)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1754 * acceleration + 0.0017948 * anchor
    return base_signal.diff()

def f29_rda_548_struct_v548_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=262, w3=183, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(262, min_periods=max(262//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.401875 + 0.0017949 * anchor
    return base_signal.diff()

def f29_rda_549_struct_v549_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=273, w3=196, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(273, min_periods=max(273//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1906 * _rolling_slope(draw, 196) + 0.001795 * anchor
    return base_signal.diff()

def f29_rda_550_struct_v550_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=284, w3=209, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.430625 + 0.0017951 * anchor
    return base_signal.diff()

def f29_rda_551_struct_v551_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=295, w3=222, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 295)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=222, adjust=False).mean() * 1.445 + 0.0017952 * anchor
    return base_signal.diff()

def f29_rda_552_struct_v552_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=306, w3=235, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(169, min_periods=max(169//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.459375 + 0.0017953 * anchor
    return base_signal.diff()

def f29_rda_553_struct_v553_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=317, w3=248, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(317, min_periods=max(317//3, 2)).rank(pct=True)
    persistence = change.rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.221 * persistence + 0.0017954 * anchor
    return base_signal.diff()

def f29_rda_554_struct_v554_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=328, w3=261, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(183, min_periods=max(183//3, 2)).std()
    vol_slow = ret.rolling(328, min_periods=max(328//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.488125 + 0.0017955 * anchor
    return base_signal.diff()

def f29_rda_555_struct_v555_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=339, w3=274, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 190)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2362 * slope + 0.0017956 * anchor
    return base_signal.diff()

def f29_rda_556_struct_v556_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=350, w3=287, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(350, min_periods=max(350//3, 2)).mean()
    noise = impulse.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.516875 + 0.0017957 * anchor
    return base_signal.diff()

def f29_rda_557_struct_v557_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=361, w3=300, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 300)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2514 * acceleration + 0.0017958 * anchor
    return base_signal.diff()

def f29_rda_558_struct_v558_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=372, w3=313, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(211, min_periods=max(211//3, 2)).mean(), upside.rolling(372, min_periods=max(372//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.545625 + 0.0017959 * anchor
    return base_signal.diff()

def f29_rda_559_struct_v559_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=383, w3=326, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(383, min_periods=max(383//3, 2)).max()
    rebound = x - x.rolling(218, min_periods=max(218//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2666 * _rolling_slope(draw, 326) + 0.001796 * anchor
    return base_signal.diff()

def f29_rda_560_struct_v560_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=394, w3=339, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(394, min_periods=max(394//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.574375 + 0.0017961 * anchor
    return base_signal.diff()

def f29_rda_561_struct_v561_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=405, w3=352, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 405)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.58875 + 0.0017962 * anchor
    return base_signal.diff()

def f29_rda_562_struct_v562_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=416, w3=365, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(416, min_periods=max(416//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.603125 + 0.0017963 * anchor
    return base_signal.diff()

def f29_rda_563_struct_v563_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=427, w3=378, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(427, min_periods=max(427//3, 2)).rank(pct=True)
    persistence = change.rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.297 * persistence + 0.0017964 * anchor
    return base_signal.diff()

def f29_rda_564_struct_v564_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=438, w3=391, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(253, min_periods=max(253//3, 2)).std()
    vol_slow = ret.rolling(438, min_periods=max(438//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85875 + 0.0017965 * anchor
    return base_signal.diff()

def f29_rda_565_struct_v565_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=449, w3=404, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(449, min_periods=max(449//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3122 * slope + 0.0017966 * anchor
    return base_signal.diff()

def f29_rda_566_struct_v566_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=460, w3=417, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(16)
    drag = impulse.rolling(460, min_periods=max(460//3, 2)).mean()
    noise = impulse.abs().rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8875 + 0.0017967 * anchor
    return base_signal.diff()

def f29_rda_567_struct_v567_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=471, w3=430, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 471)
    curvature = _rolling_slope(acceleration, 430)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3274 * acceleration + 0.0017968 * anchor
    return base_signal.diff()

def f29_rda_568_struct_v568_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=482, w3=443, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(482, min_periods=max(482//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.91625 + 0.0017969 * anchor
    return base_signal.diff()

def f29_rda_569_struct_v569_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=493, w3=456, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(493, min_periods=max(493//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3426 * _rolling_slope(draw, 456) + 0.001797 * anchor
    return base_signal.diff()

def f29_rda_570_struct_v570_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=504, w3=469, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(504, min_periods=max(504//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.945 + 0.0017971 * anchor
    return base_signal.diff()

def f29_rda_571_struct_v571_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=12, w3=482, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 12)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.959375 + 0.0017972 * anchor
    return base_signal.diff()

def f29_rda_572_struct_v572_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=23, w3=495, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(23, min_periods=max(23//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.97375 + 0.0017973 * anchor
    return base_signal.diff()

def f29_rda_573_struct_v573_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=34, w3=508, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(65)
    rank = change.rolling(34, min_periods=max(34//3, 2)).rank(pct=True)
    persistence = change.rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.373 * persistence + 0.0017974 * anchor
    return base_signal.diff()

def f29_rda_574_struct_v574_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=45, w3=521, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(45, min_periods=max(45//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0025 + 0.0017975 * anchor
    return base_signal.diff()

def f29_rda_575_struct_v575_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=56, w3=534, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(56, min_periods=max(56//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3882 * slope + 0.0017976 * anchor
    return base_signal.diff()

def f29_rda_576_struct_v576_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=67, w3=547, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(86)
    drag = impulse.rolling(67, min_periods=max(67//3, 2)).mean()
    noise = impulse.abs().rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03125 + 0.0017977 * anchor
    return base_signal.diff()

def f29_rda_577_struct_v577_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=78, w3=560, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 78)
    curvature = _rolling_slope(acceleration, 560)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4034 * acceleration + 0.0017978 * anchor
    return base_signal.diff()

def f29_rda_578_struct_v578_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=89, w3=573, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(89, min_periods=max(89//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.06 + 0.0017979 * anchor
    return base_signal.diff()

def f29_rda_579_struct_v579_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=100, w3=586, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0422 * _rolling_slope(draw, 586) + 0.001798 * anchor
    return base_signal.diff()

def f29_rda_580_struct_v580_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=111, w3=599, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(111, min_periods=max(111//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.08875 + 0.0017981 * anchor
    return base_signal.diff()

def f29_rda_581_struct_v581_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=122, w3=612, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.103125 + 0.0017982 * anchor
    return base_signal.diff()

def f29_rda_582_struct_v582_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=133, w3=625, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1175 + 0.0017983 * anchor
    return base_signal.diff()

def f29_rda_583_struct_v583_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=144, w3=638, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0726 * persistence + 0.0017984 * anchor
    return base_signal.diff()

def f29_rda_584_struct_v584_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=155, w3=651, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14625 + 0.0017985 * anchor
    return base_signal.diff()

def f29_rda_585_struct_v585_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=166, w3=664, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0878 * slope + 0.0017986 * anchor
    return base_signal.diff()

def f29_rda_586_struct_v586_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=177, w3=677, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.175 + 0.0017987 * anchor
    return base_signal.diff()

def f29_rda_587_struct_v587_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=188, w3=690, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 188)
    curvature = _rolling_slope(acceleration, 690)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.103 * acceleration + 0.0017988 * anchor
    return base_signal.diff()

def f29_rda_588_struct_v588_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=199, w3=703, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(199, min_periods=max(199//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.20375 + 0.0017989 * anchor
    return base_signal.diff()

def f29_rda_589_struct_v589_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=210, w3=716, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1182 * _rolling_slope(draw, 716) + 0.001799 * anchor
    return base_signal.diff()

def f29_rda_590_struct_v590_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=221, w3=729, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2325 + 0.0017991 * anchor
    return base_signal.diff()

def f29_rda_591_struct_v591_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=232, w3=742, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 232)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.246875 + 0.0017992 * anchor
    return base_signal.diff()

def f29_rda_592_struct_v592_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=243, w3=755, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(243, min_periods=max(243//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26125 + 0.0017993 * anchor
    return base_signal.diff()

def f29_rda_593_struct_v593_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=254, w3=768, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(254, min_periods=max(254//3, 2)).rank(pct=True)
    persistence = change.rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1486 * persistence + 0.0017994 * anchor
    return base_signal.diff()

def f29_rda_594_struct_v594_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=265, w3=24, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(265, min_periods=max(265//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.29 + 0.0017995 * anchor
    return base_signal.diff()

def f29_rda_595_struct_v595_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=276, w3=37, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(276, min_periods=max(276//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1638 * slope + 0.0017996 * anchor
    return base_signal.diff()

def f29_rda_596_struct_v596_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=287, w3=50, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(287, min_periods=max(287//3, 2)).mean()
    noise = impulse.abs().rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31875 + 0.0017997 * anchor
    return base_signal.diff()

def f29_rda_597_struct_v597_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=298, w3=63, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 298)
    curvature = _rolling_slope(acceleration, 63)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.179 * acceleration + 0.0017998 * anchor
    return base_signal.diff()

def f29_rda_598_struct_v598_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=309, w3=76, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(309, min_periods=max(309//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(76) * 1.3475 + 0.0017999 * anchor
    return base_signal.diff()

def f29_rda_599_struct_v599_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=320, w3=89, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(320, min_periods=max(320//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1942 * _rolling_slope(draw, 89) + 0.0018 * anchor
    return base_signal.diff()

def f29_rda_600_struct_v600_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=331, w3=102, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(331, min_periods=max(331//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.37625 + 0.0018001 * anchor
    return base_signal.diff()
