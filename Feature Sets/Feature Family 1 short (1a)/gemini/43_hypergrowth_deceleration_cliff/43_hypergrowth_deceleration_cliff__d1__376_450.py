"""43 hypergrowth deceleration cliff d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f43_hdc_376_struct_v376_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=291, w3=640, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(291, min_periods=max(291//3, 2)).mean()
    noise = impulse.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.511875 + 0.0026777 * anchor
    return base_signal.diff()

def f43_hdc_377_struct_v377_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=302, w3=653, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 302)
    curvature = _rolling_slope(acceleration, 653)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2842 * acceleration + 0.0026778 * anchor
    return base_signal.diff()

def f43_hdc_378_struct_v378_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=313, w3=666, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.540625 + 0.0026779 * anchor
    return base_signal.diff()

def f43_hdc_379_struct_v379_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=324, w3=679, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(324, min_periods=max(324//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2994 * _rolling_slope(draw, 679) + 0.002678 * anchor
    return base_signal.diff()

def f43_hdc_380_struct_v380_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=335, w3=692, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.569375 + 0.0026781 * anchor
    return base_signal.diff()

def f43_hdc_381_struct_v381_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=346, w3=705, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 346)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.58375 + 0.0026782 * anchor
    return base_signal.diff()

def f43_hdc_382_struct_v382_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=357, w3=718, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.598125 + 0.0026783 * anchor
    return base_signal.diff()

def f43_hdc_383_struct_v383_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=368, w3=731, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3298 * persistence + 0.0026784 * anchor
    return base_signal.diff()

def f43_hdc_384_struct_v384_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=379, w3=744, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85375 + 0.0026785 * anchor
    return base_signal.diff()

def f43_hdc_385_struct_v385_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=390, w3=757, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.345 * slope + 0.0026786 * anchor
    return base_signal.diff()

def f43_hdc_386_struct_v386_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=401, w3=770, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(10)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8825 + 0.0026787 * anchor
    return base_signal.diff()

def f43_hdc_387_struct_v387_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=412, w3=26, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 26)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3602 * acceleration + 0.0026788 * anchor
    return base_signal.diff()

def f43_hdc_388_struct_v388_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=423, w3=39, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(423, min_periods=max(423//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(39) * 0.91125 + 0.0026789 * anchor
    return base_signal.diff()

def f43_hdc_389_struct_v389_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=434, w3=52, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(434, min_periods=max(434//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3754 * _rolling_slope(draw, 52) + 0.002679 * anchor
    return base_signal.diff()

def f43_hdc_390_struct_v390_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=445, w3=65, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(445, min_periods=max(445//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.94 + 0.0026791 * anchor
    return base_signal.diff()

def f43_hdc_391_struct_v391_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=456, w3=78, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 456)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=78, adjust=False).mean() * 0.954375 + 0.0026792 * anchor
    return base_signal.diff()

def f43_hdc_392_struct_v392_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=467, w3=91, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(467, min_periods=max(467//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.96875 + 0.0026793 * anchor
    return base_signal.diff()

def f43_hdc_393_struct_v393_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=478, w3=104, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(59)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4058 * persistence + 0.0026794 * anchor
    return base_signal.diff()

def f43_hdc_394_struct_v394_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=489, w3=117, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(489, min_periods=max(489//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9975 + 0.0026795 * anchor
    return base_signal.diff()

def f43_hdc_395_struct_v395_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=500, w3=130, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0446 * slope + 0.0026796 * anchor
    return base_signal.diff()

def f43_hdc_396_struct_v396_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=511, w3=143, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(80)
    drag = impulse.rolling(511, min_periods=max(511//3, 2)).mean()
    noise = impulse.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02625 + 0.0026797 * anchor
    return base_signal.diff()

def f43_hdc_397_struct_v397_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=19, w3=156, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 19)
    curvature = _rolling_slope(acceleration, 156)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0598 * acceleration + 0.0026798 * anchor
    return base_signal.diff()

def f43_hdc_398_struct_v398_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=30, w3=169, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(30, min_periods=max(30//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.055 + 0.0026799 * anchor
    return base_signal.diff()

def f43_hdc_399_struct_v399_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=41, w3=182, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(41, min_periods=max(41//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.075 * _rolling_slope(draw, 182) + 0.00268 * anchor
    return base_signal.diff()

def f43_hdc_400_struct_v400_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=52, w3=195, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(52, min_periods=max(52//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.08375 + 0.0026801 * anchor
    return base_signal.diff()

def f43_hdc_401_struct_v401_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=63, w3=208, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 63)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=208, adjust=False).mean() * 1.098125 + 0.0026802 * anchor
    return base_signal.diff()

def f43_hdc_402_struct_v402_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=74, w3=221, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(74, min_periods=max(74//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1125 + 0.0026803 * anchor
    return base_signal.diff()

def f43_hdc_403_struct_v403_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=85, w3=234, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(85, min_periods=max(85//3, 2)).rank(pct=True)
    persistence = change.rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1054 * persistence + 0.0026804 * anchor
    return base_signal.diff()

def f43_hdc_404_struct_v404_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=96, w3=247, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(96, min_periods=max(96//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14125 + 0.0026805 * anchor
    return base_signal.diff()

def f43_hdc_405_struct_v405_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=107, w3=260, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(107, min_periods=max(107//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1206 * slope + 0.0026806 * anchor
    return base_signal.diff()

def f43_hdc_406_struct_v406_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=118, w3=273, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(118, min_periods=max(118//3, 2)).mean()
    noise = impulse.abs().rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.17 + 0.0026807 * anchor
    return base_signal.diff()

def f43_hdc_407_struct_v407_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=129, w3=286, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 129)
    curvature = _rolling_slope(acceleration, 286)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1358 * acceleration + 0.0026808 * anchor
    return base_signal.diff()

def f43_hdc_408_struct_v408_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=140, w3=299, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.19875 + 0.0026809 * anchor
    return base_signal.diff()

def f43_hdc_409_struct_v409_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=151, w3=312, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(151, min_periods=max(151//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.151 * _rolling_slope(draw, 312) + 0.002681 * anchor
    return base_signal.diff()

def f43_hdc_410_struct_v410_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=162, w3=325, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(162, min_periods=max(162//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2275 + 0.0026811 * anchor
    return base_signal.diff()

def f43_hdc_411_struct_v411_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=173, w3=338, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 173)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.241875 + 0.0026812 * anchor
    return base_signal.diff()

def f43_hdc_412_struct_v412_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=184, w3=351, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(184, min_periods=max(184//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.25625 + 0.0026813 * anchor
    return base_signal.diff()

def f43_hdc_413_struct_v413_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=195, w3=364, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(195, min_periods=max(195//3, 2)).rank(pct=True)
    persistence = change.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1814 * persistence + 0.0026814 * anchor
    return base_signal.diff()

def f43_hdc_414_struct_v414_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=206, w3=377, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(206, min_periods=max(206//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.285 + 0.0026815 * anchor
    return base_signal.diff()

def f43_hdc_415_struct_v415_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=217, w3=390, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(217, min_periods=max(217//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1966 * slope + 0.0026816 * anchor
    return base_signal.diff()

def f43_hdc_416_struct_v416_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=228, w3=403, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(228, min_periods=max(228//3, 2)).mean()
    noise = impulse.abs().rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31375 + 0.0026817 * anchor
    return base_signal.diff()

def f43_hdc_417_struct_v417_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=239, w3=416, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 239)
    curvature = _rolling_slope(acceleration, 416)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2118 * acceleration + 0.0026818 * anchor
    return base_signal.diff()

def f43_hdc_418_struct_v418_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=250, w3=429, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(250, min_periods=max(250//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3425 + 0.0026819 * anchor
    return base_signal.diff()

def f43_hdc_419_struct_v419_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=261, w3=442, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(261, min_periods=max(261//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227 * _rolling_slope(draw, 442) + 0.002682 * anchor
    return base_signal.diff()

def f43_hdc_420_struct_v420_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=272, w3=455, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(272, min_periods=max(272//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.37125 + 0.0026821 * anchor
    return base_signal.diff()

def f43_hdc_421_struct_v421_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=283, w3=468, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 255)
    slow = _rolling_slope(x, 283)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.385625 + 0.0026822 * anchor
    return base_signal.diff()

def f43_hdc_422_struct_v422_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=294, w3=481, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(294, min_periods=max(294//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4 + 0.0026823 * anchor
    return base_signal.diff()

def f43_hdc_423_struct_v423_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=305, w3=494, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(18)
    rank = change.rolling(305, min_periods=max(305//3, 2)).rank(pct=True)
    persistence = change.rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2574 * persistence + 0.0026824 * anchor
    return base_signal.diff()

def f43_hdc_424_struct_v424_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=316, w3=507, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(316, min_periods=max(316//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.42875 + 0.0026825 * anchor
    return base_signal.diff()

def f43_hdc_425_struct_v425_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=327, w3=520, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(327, min_periods=max(327//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2726 * slope + 0.0026826 * anchor
    return base_signal.diff()

def f43_hdc_426_struct_v426_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=338, w3=533, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(39)
    drag = impulse.rolling(338, min_periods=max(338//3, 2)).mean()
    noise = impulse.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4575 + 0.0026827 * anchor
    return base_signal.diff()

def f43_hdc_427_struct_v427_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=349, w3=546, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 349)
    curvature = _rolling_slope(acceleration, 546)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2878 * acceleration + 0.0026828 * anchor
    return base_signal.diff()

def f43_hdc_428_struct_v428_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=360, w3=559, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(360, min_periods=max(360//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.48625 + 0.0026829 * anchor
    return base_signal.diff()

def f43_hdc_429_struct_v429_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=371, w3=572, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(371, min_periods=max(371//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.303 * _rolling_slope(draw, 572) + 0.002683 * anchor
    return base_signal.diff()

def f43_hdc_430_struct_v430_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=382, w3=585, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(382, min_periods=max(382//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.515 + 0.0026831 * anchor
    return base_signal.diff()

def f43_hdc_431_struct_v431_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=393, w3=598, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 393)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.529375 + 0.0026832 * anchor
    return base_signal.diff()

def f43_hdc_432_struct_v432_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=404, w3=611, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(404, min_periods=max(404//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.54375 + 0.0026833 * anchor
    return base_signal.diff()

def f43_hdc_433_struct_v433_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=415, w3=624, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(88)
    rank = change.rolling(415, min_periods=max(415//3, 2)).rank(pct=True)
    persistence = change.rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3334 * persistence + 0.0026834 * anchor
    return base_signal.diff()

def f43_hdc_434_struct_v434_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=426, w3=637, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5725 + 0.0026835 * anchor
    return base_signal.diff()

def f43_hdc_435_struct_v435_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=437, w3=650, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3486 * slope + 0.0026836 * anchor
    return base_signal.diff()

def f43_hdc_436_struct_v436_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=448, w3=663, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(109)
    drag = impulse.rolling(448, min_periods=max(448//3, 2)).mean()
    noise = impulse.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.60125 + 0.0026837 * anchor
    return base_signal.diff()

def f43_hdc_437_struct_v437_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=459, w3=676, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 459)
    curvature = _rolling_slope(acceleration, 676)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3638 * acceleration + 0.0026838 * anchor
    return base_signal.diff()

def f43_hdc_438_struct_v438_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=470, w3=689, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(470, min_periods=max(470//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.856875 + 0.0026839 * anchor
    return base_signal.diff()

def f43_hdc_439_struct_v439_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=481, w3=702, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(481, min_periods=max(481//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.379 * _rolling_slope(draw, 702) + 0.002684 * anchor
    return base_signal.diff()

def f43_hdc_440_struct_v440_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=492, w3=715, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(492, min_periods=max(492//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.885625 + 0.0026841 * anchor
    return base_signal.diff()

def f43_hdc_441_struct_v441_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=503, w3=728, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 503)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9 + 0.0026842 * anchor
    return base_signal.diff()

def f43_hdc_442_struct_v442_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=11, w3=741, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(11, min_periods=max(11//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.914375 + 0.0026843 * anchor
    return base_signal.diff()

def f43_hdc_443_struct_v443_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=22, w3=754, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(22, min_periods=max(22//3, 2)).rank(pct=True)
    persistence = change.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4094 * persistence + 0.0026844 * anchor
    return base_signal.diff()

def f43_hdc_444_struct_v444_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=33, w3=767, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(33, min_periods=max(33//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.943125 + 0.0026845 * anchor
    return base_signal.diff()

def f43_hdc_445_struct_v445_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=44, w3=23, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(44, min_periods=max(44//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0482 * slope + 0.0026846 * anchor
    return base_signal.diff()

def f43_hdc_446_struct_v446_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=55, w3=36, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(55, min_periods=max(55//3, 2)).mean()
    noise = impulse.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.971875 + 0.0026847 * anchor
    return base_signal.diff()

def f43_hdc_447_struct_v447_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=66, w3=49, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 66)
    curvature = _rolling_slope(acceleration, 49)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0634 * acceleration + 0.0026848 * anchor
    return base_signal.diff()

def f43_hdc_448_struct_v448_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=77, w3=62, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(77, min_periods=max(77//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(62) * 1.000625 + 0.0026849 * anchor
    return base_signal.diff()

def f43_hdc_449_struct_v449_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=88, w3=75, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(88, min_periods=max(88//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0786 * _rolling_slope(draw, 75) + 0.002685 * anchor
    return base_signal.diff()

def f43_hdc_450_struct_v450_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=99, w3=88, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(99, min_periods=max(99//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.029375 + 0.0026851 * anchor
    return base_signal.diff()
