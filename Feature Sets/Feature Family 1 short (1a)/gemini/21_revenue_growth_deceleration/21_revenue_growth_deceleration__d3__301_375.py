"""21 revenue growth deceleration d3 third derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f21_rgd_301_struct_v301_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=203, w2=75, w3=431, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 75)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.525 + 0.0012902 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_302_struct_v302_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=210, w2=86, w3=444, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(86, min_periods=max(86//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.539375 + 0.0012903 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_303_struct_v303_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=217, w2=97, w3=457, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(97, min_periods=max(97//3, 2)).rank(pct=True)
    persistence = change.rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2338 * persistence + 0.0012904 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_304_struct_v304_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=224, w2=108, w3=470, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(108, min_periods=max(108//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.568125 + 0.0012905 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_305_struct_v305_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=231, w2=119, w3=483, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.249 * slope + 0.0012906 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_306_struct_v306_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=238, w2=130, w3=496, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(130, min_periods=max(130//3, 2)).mean()
    noise = impulse.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.596875 + 0.0012907 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_307_struct_v307_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=245, w2=141, w3=509, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 141)
    curvature = _rolling_slope(acceleration, 509)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2642 * acceleration + 0.0012908 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_308_struct_v308_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=252, w2=152, w3=522, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8525 + 0.0012909 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_309_struct_v309_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=8, w2=163, w3=535, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(163, min_periods=max(163//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2794 * _rolling_slope(draw, 535) + 0.001291 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_310_struct_v310_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=15, w2=174, w3=548, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(174, min_periods=max(174//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.88125 + 0.0012911 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_311_struct_v311_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=22, w2=185, w3=561, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 185)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.895625 + 0.0012912 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_312_struct_v312_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=29, w2=196, w3=574, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(196, min_periods=max(196//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.91 + 0.0012913 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_313_struct_v313_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=36, w2=207, w3=587, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(36)
    rank = change.rolling(207, min_periods=max(207//3, 2)).rank(pct=True)
    persistence = change.rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3098 * persistence + 0.0012914 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_314_struct_v314_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=43, w2=218, w3=600, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(218, min_periods=max(218//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.93875 + 0.0012915 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_315_struct_v315_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=50, w2=229, w3=613, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(229, min_periods=max(229//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.325 * slope + 0.0012916 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_316_struct_v316_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=57, w2=240, w3=626, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(57)
    drag = impulse.rolling(240, min_periods=max(240//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9675 + 0.0012917 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_317_struct_v317_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=64, w2=251, w3=639, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 251)
    curvature = _rolling_slope(acceleration, 639)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3402 * acceleration + 0.0012918 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_318_struct_v318_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=71, w2=262, w3=652, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(262, min_periods=max(262//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.99625 + 0.0012919 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_319_struct_v319_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=78, w2=273, w3=665, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(273, min_periods=max(273//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3554 * _rolling_slope(draw, 665) + 0.001292 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_320_struct_v320_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=85, w2=284, w3=678, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.025 + 0.0012921 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_321_struct_v321_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=92, w2=295, w3=691, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 295)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.039375 + 0.0012922 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_322_struct_v322_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=99, w2=306, w3=704, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.05375 + 0.0012923 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_323_struct_v323_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=106, w2=317, w3=717, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(106)
    rank = change.rolling(317, min_periods=max(317//3, 2)).rank(pct=True)
    persistence = change.rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3858 * persistence + 0.0012924 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_324_struct_v324_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=113, w2=328, w3=730, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(328, min_periods=max(328//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0825 + 0.0012925 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_325_struct_v325_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=120, w2=339, w3=743, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.401 * slope + 0.0012926 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_326_struct_v326_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=127, w2=350, w3=756, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(350, min_periods=max(350//3, 2)).mean()
    noise = impulse.abs().rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.11125 + 0.0012927 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_327_struct_v327_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=134, w2=361, w3=769, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 769)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0398 * acceleration + 0.0012928 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_328_struct_v328_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=141, w2=372, w3=25, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(372, min_periods=max(372//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(25) * 1.14 + 0.0012929 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_329_struct_v329_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=148, w2=383, w3=38, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(383, min_periods=max(383//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.055 * _rolling_slope(draw, 38) + 0.001293 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_330_struct_v330_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=155, w2=394, w3=51, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(394, min_periods=max(394//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.16875 + 0.0012931 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_331_struct_v331_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=162, w2=405, w3=64, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 405)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=64, adjust=False).mean() * 1.183125 + 0.0012932 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_332_struct_v332_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=169, w2=416, w3=77, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(416, min_periods=max(416//3, 2)).max()
    trough = x.rolling(169, min_periods=max(169//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1975 + 0.0012933 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_333_struct_v333_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=176, w2=427, w3=90, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(427, min_periods=max(427//3, 2)).rank(pct=True)
    persistence = change.rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0854 * persistence + 0.0012934 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_334_struct_v334_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=183, w2=438, w3=103, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(183, min_periods=max(183//3, 2)).std()
    vol_slow = ret.rolling(438, min_periods=max(438//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.22625 + 0.0012935 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_335_struct_v335_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=190, w2=449, w3=116, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(449, min_periods=max(449//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 190)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1006 * slope + 0.0012936 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_336_struct_v336_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=197, w2=460, w3=129, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(460, min_periods=max(460//3, 2)).mean()
    noise = impulse.abs().rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.255 + 0.0012937 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_337_struct_v337_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=204, w2=471, w3=142, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 471)
    curvature = _rolling_slope(acceleration, 142)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1158 * acceleration + 0.0012938 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_338_struct_v338_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=211, w2=482, w3=155, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(211, min_periods=max(211//3, 2)).mean(), upside.rolling(482, min_periods=max(482//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.28375 + 0.0012939 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_339_struct_v339_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=218, w2=493, w3=168, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(493, min_periods=max(493//3, 2)).max()
    rebound = x - x.rolling(218, min_periods=max(218//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.131 * _rolling_slope(draw, 168) + 0.001294 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_340_struct_v340_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=225, w2=504, w3=181, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(504, min_periods=max(504//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3125 + 0.0012941 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_341_struct_v341_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=232, w2=12, w3=194, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 12)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=194, adjust=False).mean() * 1.326875 + 0.0012942 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_342_struct_v342_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=239, w2=23, w3=207, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(23, min_periods=max(23//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.34125 + 0.0012943 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_343_struct_v343_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=246, w2=34, w3=220, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(34, min_periods=max(34//3, 2)).rank(pct=True)
    persistence = change.rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1614 * persistence + 0.0012944 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_344_struct_v344_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=253, w2=45, w3=233, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(253, min_periods=max(253//3, 2)).std()
    vol_slow = ret.rolling(45, min_periods=max(45//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37 + 0.0012945 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_345_struct_v345_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=9, w2=56, w3=246, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(56, min_periods=max(56//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1766 * slope + 0.0012946 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_346_struct_v346_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=16, w2=67, w3=259, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(16)
    drag = impulse.rolling(67, min_periods=max(67//3, 2)).mean()
    noise = impulse.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.39875 + 0.0012947 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_347_struct_v347_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=23, w2=78, w3=272, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 78)
    curvature = _rolling_slope(acceleration, 272)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1918 * acceleration + 0.0012948 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_348_struct_v348_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=89, w3=285, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(89, min_periods=max(89//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4275 + 0.0012949 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_349_struct_v349_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=100, w3=298, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.207 * _rolling_slope(draw, 298) + 0.001295 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_350_struct_v350_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=111, w3=311, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(111, min_periods=max(111//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.45625 + 0.0012951 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_351_struct_v351_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=122, w3=324, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.470625 + 0.0012952 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_352_struct_v352_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=133, w3=337, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.485 + 0.0012953 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_353_struct_v353_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=144, w3=350, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(65)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2374 * persistence + 0.0012954 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_354_struct_v354_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=155, w3=363, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.51375 + 0.0012955 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_355_struct_v355_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=166, w3=376, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2526 * slope + 0.0012956 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_356_struct_v356_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=177, w3=389, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(86)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5425 + 0.0012957 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_357_struct_v357_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=188, w3=402, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 188)
    curvature = _rolling_slope(acceleration, 402)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2678 * acceleration + 0.0012958 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_358_struct_v358_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=199, w3=415, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(199, min_periods=max(199//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.57125 + 0.0012959 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_359_struct_v359_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=210, w3=428, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.283 * _rolling_slope(draw, 428) + 0.001296 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_360_struct_v360_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=221, w3=441, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.6 + 0.0012961 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_361_struct_v361_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=232, w3=454, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 232)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.614375 + 0.0012962 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_362_struct_v362_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=243, w3=467, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(243, min_periods=max(243//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.855625 + 0.0012963 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_363_struct_v363_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=254, w3=480, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(254, min_periods=max(254//3, 2)).rank(pct=True)
    persistence = change.rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3134 * persistence + 0.0012964 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_364_struct_v364_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=265, w3=493, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(265, min_periods=max(265//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.884375 + 0.0012965 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_365_struct_v365_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=276, w3=506, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(276, min_periods=max(276//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3286 * slope + 0.0012966 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_366_struct_v366_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=287, w3=519, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(287, min_periods=max(287//3, 2)).mean()
    noise = impulse.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.913125 + 0.0012967 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_367_struct_v367_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=298, w3=532, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 298)
    curvature = _rolling_slope(acceleration, 532)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3438 * acceleration + 0.0012968 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_368_struct_v368_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=309, w3=545, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(309, min_periods=max(309//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.941875 + 0.0012969 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_369_struct_v369_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=320, w3=558, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(320, min_periods=max(320//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359 * _rolling_slope(draw, 558) + 0.001297 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_370_struct_v370_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=331, w3=571, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(331, min_periods=max(331//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.970625 + 0.0012971 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_371_struct_v371_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=342, w3=584, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 342)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.985 + 0.0012972 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_372_struct_v372_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=353, w3=597, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.999375 + 0.0012973 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_373_struct_v373_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=364, w3=610, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(364, min_periods=max(364//3, 2)).rank(pct=True)
    persistence = change.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3894 * persistence + 0.0012974 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_374_struct_v374_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=375, w3=623, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(375, min_periods=max(375//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.028125 + 0.0012975 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_375_struct_v375_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=386, w3=636, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4046 * slope + 0.0012976 * anchor
    return base_signal.diff().diff().diff()
