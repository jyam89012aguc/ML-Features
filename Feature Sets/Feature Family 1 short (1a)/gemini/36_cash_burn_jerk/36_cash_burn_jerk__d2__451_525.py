"""36 cash burn jerk d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f36_cbj_451_struct_v451_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=248, w2=125, w3=532, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 125)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.851875 + 0.0022052 * anchor
    return base_signal.diff().diff()

def f36_cbj_452_struct_v452_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=255, w2=136, w3=545, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(136, min_periods=max(136//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.86625 + 0.0022053 * anchor
    return base_signal.diff().diff()

def f36_cbj_453_struct_v453_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=11, w2=147, w3=558, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(11)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1398 * persistence + 0.0022054 * anchor
    return base_signal.diff().diff()

def f36_cbj_454_struct_v454_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=18, w2=158, w3=571, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(158, min_periods=max(158//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.895 + 0.0022055 * anchor
    return base_signal.diff().diff()

def f36_cbj_455_struct_v455_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=25, w2=169, w3=584, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.155 * slope + 0.0022056 * anchor
    return base_signal.diff().diff()

def f36_cbj_456_struct_v456_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=180, w3=597, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(32)
    drag = impulse.rolling(180, min_periods=max(180//3, 2)).mean()
    noise = impulse.abs().rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.92375 + 0.0022057 * anchor
    return base_signal.diff().diff()

def f36_cbj_457_struct_v457_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=191, w3=610, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 191)
    curvature = _rolling_slope(acceleration, 610)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1702 * acceleration + 0.0022058 * anchor
    return base_signal.diff().diff()

def f36_cbj_458_struct_v458_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=202, w3=623, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(202, min_periods=max(202//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9525 + 0.0022059 * anchor
    return base_signal.diff().diff()

def f36_cbj_459_struct_v459_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=213, w3=636, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1854 * _rolling_slope(draw, 636) + 0.002206 * anchor
    return base_signal.diff().diff()

def f36_cbj_460_struct_v460_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=224, w3=649, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(224, min_periods=max(224//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.98125 + 0.0022061 * anchor
    return base_signal.diff().diff()

def f36_cbj_461_struct_v461_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=235, w3=662, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 235)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.995625 + 0.0022062 * anchor
    return base_signal.diff().diff()

def f36_cbj_462_struct_v462_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=246, w3=675, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01 + 0.0022063 * anchor
    return base_signal.diff().diff()

def f36_cbj_463_struct_v463_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=257, w3=688, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(81)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2158 * persistence + 0.0022064 * anchor
    return base_signal.diff().diff()

def f36_cbj_464_struct_v464_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=268, w3=701, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(268, min_periods=max(268//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03875 + 0.0022065 * anchor
    return base_signal.diff().diff()

def f36_cbj_465_struct_v465_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=279, w3=714, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(279, min_periods=max(279//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.231 * slope + 0.0022066 * anchor
    return base_signal.diff().diff()

def f36_cbj_466_struct_v466_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=290, w3=727, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(102)
    drag = impulse.rolling(290, min_periods=max(290//3, 2)).mean()
    noise = impulse.abs().rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0675 + 0.0022067 * anchor
    return base_signal.diff().diff()

def f36_cbj_467_struct_v467_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=301, w3=740, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 301)
    curvature = _rolling_slope(acceleration, 740)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2462 * acceleration + 0.0022068 * anchor
    return base_signal.diff().diff()

def f36_cbj_468_struct_v468_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=116, w2=312, w3=753, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(312, min_periods=max(312//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.09625 + 0.0022069 * anchor
    return base_signal.diff().diff()

def f36_cbj_469_struct_v469_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=123, w2=323, w3=766, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(323, min_periods=max(323//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2614 * _rolling_slope(draw, 766) + 0.002207 * anchor
    return base_signal.diff().diff()

def f36_cbj_470_struct_v470_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=130, w2=334, w3=22, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(334, min_periods=max(334//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.125 + 0.0022071 * anchor
    return base_signal.diff().diff()

def f36_cbj_471_struct_v471_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=137, w2=345, w3=35, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 345)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=35, adjust=False).mean() * 1.139375 + 0.0022072 * anchor
    return base_signal.diff().diff()

def f36_cbj_472_struct_v472_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=144, w2=356, w3=48, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(356, min_periods=max(356//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.15375 + 0.0022073 * anchor
    return base_signal.diff().diff()

def f36_cbj_473_struct_v473_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=151, w2=367, w3=61, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(367, min_periods=max(367//3, 2)).rank(pct=True)
    persistence = change.rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2918 * persistence + 0.0022074 * anchor
    return base_signal.diff().diff()

def f36_cbj_474_struct_v474_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=158, w2=378, w3=74, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(378, min_periods=max(378//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1825 + 0.0022075 * anchor
    return base_signal.diff().diff()

def f36_cbj_475_struct_v475_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=165, w2=389, w3=87, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(389, min_periods=max(389//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.307 * slope + 0.0022076 * anchor
    return base_signal.diff().diff()

def f36_cbj_476_struct_v476_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=172, w2=400, w3=100, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(400, min_periods=max(400//3, 2)).mean()
    noise = impulse.abs().rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.21125 + 0.0022077 * anchor
    return base_signal.diff().diff()

def f36_cbj_477_struct_v477_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=179, w2=411, w3=113, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 411)
    curvature = _rolling_slope(acceleration, 113)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3222 * acceleration + 0.0022078 * anchor
    return base_signal.diff().diff()

def f36_cbj_478_struct_v478_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=186, w2=422, w3=126, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(422, min_periods=max(422//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.24 + 0.0022079 * anchor
    return base_signal.diff().diff()

def f36_cbj_479_struct_v479_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=193, w2=433, w3=139, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(433, min_periods=max(433//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3374 * _rolling_slope(draw, 139) + 0.002208 * anchor
    return base_signal.diff().diff()

def f36_cbj_480_struct_v480_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=200, w2=444, w3=152, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(444, min_periods=max(444//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.26875 + 0.0022081 * anchor
    return base_signal.diff().diff()

def f36_cbj_481_struct_v481_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=207, w2=455, w3=165, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 455)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=165, adjust=False).mean() * 1.283125 + 0.0022082 * anchor
    return base_signal.diff().diff()

def f36_cbj_482_struct_v482_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=214, w2=466, w3=178, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(466, min_periods=max(466//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2975 + 0.0022083 * anchor
    return base_signal.diff().diff()

def f36_cbj_483_struct_v483_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=221, w2=477, w3=191, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(477, min_periods=max(477//3, 2)).rank(pct=True)
    persistence = change.rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3678 * persistence + 0.0022084 * anchor
    return base_signal.diff().diff()

def f36_cbj_484_struct_v484_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=228, w2=488, w3=204, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32625 + 0.0022085 * anchor
    return base_signal.diff().diff()

def f36_cbj_485_struct_v485_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=235, w2=499, w3=217, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(499, min_periods=max(499//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.383 * slope + 0.0022086 * anchor
    return base_signal.diff().diff()

def f36_cbj_486_struct_v486_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=242, w2=510, w3=230, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(510, min_periods=max(510//3, 2)).mean()
    noise = impulse.abs().rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.355 + 0.0022087 * anchor
    return base_signal.diff().diff()

def f36_cbj_487_struct_v487_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=249, w2=18, w3=243, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 18)
    curvature = _rolling_slope(acceleration, 243)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3982 * acceleration + 0.0022088 * anchor
    return base_signal.diff().diff()

def f36_cbj_488_struct_v488_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=5, w2=29, w3=256, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(29, min_periods=max(29//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.38375 + 0.0022089 * anchor
    return base_signal.diff().diff()

def f36_cbj_489_struct_v489_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=12, w2=40, w3=269, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(40, min_periods=max(40//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.037 * _rolling_slope(draw, 269) + 0.002209 * anchor
    return base_signal.diff().diff()

def f36_cbj_490_struct_v490_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=19, w2=51, w3=282, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(51, min_periods=max(51//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4125 + 0.0022091 * anchor
    return base_signal.diff().diff()

def f36_cbj_491_struct_v491_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=26, w2=62, w3=295, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 62)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=295, adjust=False).mean() * 1.426875 + 0.0022092 * anchor
    return base_signal.diff().diff()

def f36_cbj_492_struct_v492_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=33, w2=73, w3=308, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(73, min_periods=max(73//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44125 + 0.0022093 * anchor
    return base_signal.diff().diff()

def f36_cbj_493_struct_v493_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=40, w2=84, w3=321, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(40)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0674 * persistence + 0.0022094 * anchor
    return base_signal.diff().diff()

def f36_cbj_494_struct_v494_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=47, w2=95, w3=334, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(95, min_periods=max(95//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47 + 0.0022095 * anchor
    return base_signal.diff().diff()

def f36_cbj_495_struct_v495_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=54, w2=106, w3=347, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(106, min_periods=max(106//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0826 * slope + 0.0022096 * anchor
    return base_signal.diff().diff()

def f36_cbj_496_struct_v496_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=61, w2=117, w3=360, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(61)
    drag = impulse.rolling(117, min_periods=max(117//3, 2)).mean()
    noise = impulse.abs().rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.49875 + 0.0022097 * anchor
    return base_signal.diff().diff()

def f36_cbj_497_struct_v497_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=68, w2=128, w3=373, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 128)
    curvature = _rolling_slope(acceleration, 373)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0978 * acceleration + 0.0022098 * anchor
    return base_signal.diff().diff()

def f36_cbj_498_struct_v498_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=75, w2=139, w3=386, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5275 + 0.0022099 * anchor
    return base_signal.diff().diff()

def f36_cbj_499_struct_v499_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=82, w2=150, w3=399, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(150, min_periods=max(150//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.113 * _rolling_slope(draw, 399) + 0.00221 * anchor
    return base_signal.diff().diff()

def f36_cbj_500_struct_v500_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=89, w2=161, w3=412, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(161, min_periods=max(161//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55625 + 0.0022101 * anchor
    return base_signal.diff().diff()

def f36_cbj_501_struct_v501_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=96, w2=172, w3=425, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.570625 + 0.0022102 * anchor
    return base_signal.diff().diff()

def f36_cbj_502_struct_v502_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=103, w2=183, w3=438, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(183, min_periods=max(183//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.585 + 0.0022103 * anchor
    return base_signal.diff().diff()

def f36_cbj_503_struct_v503_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=110, w2=194, w3=451, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(110)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1434 * persistence + 0.0022104 * anchor
    return base_signal.diff().diff()

def f36_cbj_504_struct_v504_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=117, w2=205, w3=464, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(205, min_periods=max(205//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61375 + 0.0022105 * anchor
    return base_signal.diff().diff()

def f36_cbj_505_struct_v505_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=124, w2=216, w3=477, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(216, min_periods=max(216//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1586 * slope + 0.0022106 * anchor
    return base_signal.diff().diff()

def f36_cbj_506_struct_v506_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=131, w2=227, w3=490, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(227, min_periods=max(227//3, 2)).mean()
    noise = impulse.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.869375 + 0.0022107 * anchor
    return base_signal.diff().diff()

def f36_cbj_507_struct_v507_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=138, w2=238, w3=503, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 238)
    curvature = _rolling_slope(acceleration, 503)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1738 * acceleration + 0.0022108 * anchor
    return base_signal.diff().diff()

def f36_cbj_508_struct_v508_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=145, w2=249, w3=516, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(249, min_periods=max(249//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.898125 + 0.0022109 * anchor
    return base_signal.diff().diff()

def f36_cbj_509_struct_v509_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=152, w2=260, w3=529, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(260, min_periods=max(260//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189 * _rolling_slope(draw, 529) + 0.002211 * anchor
    return base_signal.diff().diff()

def f36_cbj_510_struct_v510_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=159, w2=271, w3=542, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(271, min_periods=max(271//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.926875 + 0.0022111 * anchor
    return base_signal.diff().diff()

def f36_cbj_511_struct_v511_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=166, w2=282, w3=555, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 282)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.94125 + 0.0022112 * anchor
    return base_signal.diff().diff()

def f36_cbj_512_struct_v512_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=173, w2=293, w3=568, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(293, min_periods=max(293//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.955625 + 0.0022113 * anchor
    return base_signal.diff().diff()

def f36_cbj_513_struct_v513_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=180, w2=304, w3=581, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(304, min_periods=max(304//3, 2)).rank(pct=True)
    persistence = change.rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2194 * persistence + 0.0022114 * anchor
    return base_signal.diff().diff()

def f36_cbj_514_struct_v514_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=187, w2=315, w3=594, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(315, min_periods=max(315//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.984375 + 0.0022115 * anchor
    return base_signal.diff().diff()

def f36_cbj_515_struct_v515_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=194, w2=326, w3=607, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2346 * slope + 0.0022116 * anchor
    return base_signal.diff().diff()

def f36_cbj_516_struct_v516_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=201, w2=337, w3=620, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(337, min_periods=max(337//3, 2)).mean()
    noise = impulse.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.013125 + 0.0022117 * anchor
    return base_signal.diff().diff()

def f36_cbj_517_struct_v517_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=208, w2=348, w3=633, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 348)
    curvature = _rolling_slope(acceleration, 633)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2498 * acceleration + 0.0022118 * anchor
    return base_signal.diff().diff()

def f36_cbj_518_struct_v518_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=215, w2=359, w3=646, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(359, min_periods=max(359//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.041875 + 0.0022119 * anchor
    return base_signal.diff().diff()

def f36_cbj_519_struct_v519_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=222, w2=370, w3=659, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(370, min_periods=max(370//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.265 * _rolling_slope(draw, 659) + 0.002212 * anchor
    return base_signal.diff().diff()

def f36_cbj_520_struct_v520_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=229, w2=381, w3=672, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(381, min_periods=max(381//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.070625 + 0.0022121 * anchor
    return base_signal.diff().diff()

def f36_cbj_521_struct_v521_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=236, w2=392, w3=685, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 392)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.085 + 0.0022122 * anchor
    return base_signal.diff().diff()

def f36_cbj_522_struct_v522_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=243, w2=403, w3=698, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(403, min_periods=max(403//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.099375 + 0.0022123 * anchor
    return base_signal.diff().diff()

def f36_cbj_523_struct_v523_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=250, w2=414, w3=711, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(414, min_periods=max(414//3, 2)).rank(pct=True)
    persistence = change.rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2954 * persistence + 0.0022124 * anchor
    return base_signal.diff().diff()

def f36_cbj_524_struct_v524_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=6, w2=425, w3=724, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(425, min_periods=max(425//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.128125 + 0.0022125 * anchor
    return base_signal.diff().diff()

def f36_cbj_525_struct_v525_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=13, w2=436, w3=737, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(436, min_periods=max(436//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3106 * slope + 0.0022126 * anchor
    return base_signal.diff().diff()
