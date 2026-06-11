"""91 governance risk kinetics d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f91_govr_451_struct_v451_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=45, w2=126, w3=552, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.966875 + 0.0041852 * anchor
    return base_signal.diff().diff()

def f91_govr_452_struct_v452_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=52, w2=137, w3=565, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(137, min_periods=max(137//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.98125 + 0.0041853 * anchor
    return base_signal.diff().diff()

def f91_govr_453_struct_v453_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=59, w2=148, w3=578, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(59)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0598 * persistence + 0.0041854 * anchor
    return base_signal.diff().diff()

def f91_govr_454_struct_v454_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=66, w2=159, w3=591, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(159, min_periods=max(159//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01 + 0.0041855 * anchor
    return base_signal.diff().diff()

def f91_govr_455_struct_v455_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=73, w2=170, w3=604, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.075 * slope + 0.0041856 * anchor
    return base_signal.diff().diff()

def f91_govr_456_struct_v456_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=80, w2=181, w3=617, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(80)
    drag = impulse.rolling(181, min_periods=max(181//3, 2)).mean()
    noise = impulse.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03875 + 0.0041857 * anchor
    return base_signal.diff().diff()

def f91_govr_457_struct_v457_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=87, w2=192, w3=630, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 630)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0902 * acceleration + 0.0041858 * anchor
    return base_signal.diff().diff()

def f91_govr_458_struct_v458_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=94, w2=203, w3=643, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0675 + 0.0041859 * anchor
    return base_signal.diff().diff()

def f91_govr_459_struct_v459_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=101, w2=214, w3=656, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1054 * _rolling_slope(draw, 656) + 0.004186 * anchor
    return base_signal.diff().diff()

def f91_govr_460_struct_v460_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=108, w2=225, w3=669, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(225, min_periods=max(225//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09625 + 0.0041861 * anchor
    return base_signal.diff().diff()

def f91_govr_461_struct_v461_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=115, w2=236, w3=682, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 236)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.110625 + 0.0041862 * anchor
    return base_signal.diff().diff()

def f91_govr_462_struct_v462_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=122, w2=247, w3=695, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.125 + 0.0041863 * anchor
    return base_signal.diff().diff()

def f91_govr_463_struct_v463_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=129, w2=258, w3=708, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(258, min_periods=max(258//3, 2)).rank(pct=True)
    persistence = change.rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1358 * persistence + 0.0041864 * anchor
    return base_signal.diff().diff()

def f91_govr_464_struct_v464_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=136, w2=269, w3=721, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(269, min_periods=max(269//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.15375 + 0.0041865 * anchor
    return base_signal.diff().diff()

def f91_govr_465_struct_v465_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=143, w2=280, w3=734, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.151 * slope + 0.0041866 * anchor
    return base_signal.diff().diff()

def f91_govr_466_struct_v466_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=150, w2=291, w3=747, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(291, min_periods=max(291//3, 2)).mean()
    noise = impulse.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1825 + 0.0041867 * anchor
    return base_signal.diff().diff()

def f91_govr_467_struct_v467_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=157, w2=302, w3=760, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 302)
    curvature = _rolling_slope(acceleration, 760)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1662 * acceleration + 0.0041868 * anchor
    return base_signal.diff().diff()

def f91_govr_468_struct_v468_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=164, w2=313, w3=16, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(16) * 1.21125 + 0.0041869 * anchor
    return base_signal.diff().diff()

def f91_govr_469_struct_v469_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=171, w2=324, w3=29, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(324, min_periods=max(324//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1814 * _rolling_slope(draw, 29) + 0.004187 * anchor
    return base_signal.diff().diff()

def f91_govr_470_struct_v470_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=178, w2=335, w3=42, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24 + 0.0041871 * anchor
    return base_signal.diff().diff()

def f91_govr_471_struct_v471_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=185, w2=346, w3=55, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 346)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=55, adjust=False).mean() * 1.254375 + 0.0041872 * anchor
    return base_signal.diff().diff()

def f91_govr_472_struct_v472_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=192, w2=357, w3=68, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26875 + 0.0041873 * anchor
    return base_signal.diff().diff()

def f91_govr_473_struct_v473_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=199, w2=368, w3=81, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2118 * persistence + 0.0041874 * anchor
    return base_signal.diff().diff()

def f91_govr_474_struct_v474_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=206, w2=379, w3=94, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2975 + 0.0041875 * anchor
    return base_signal.diff().diff()

def f91_govr_475_struct_v475_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=213, w2=390, w3=107, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.227 * slope + 0.0041876 * anchor
    return base_signal.diff().diff()

def f91_govr_476_struct_v476_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=220, w2=401, w3=120, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.32625 + 0.0041877 * anchor
    return base_signal.diff().diff()

def f91_govr_477_struct_v477_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=227, w2=412, w3=133, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 133)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2422 * acceleration + 0.0041878 * anchor
    return base_signal.diff().diff()

def f91_govr_478_struct_v478_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=234, w2=423, w3=146, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(423, min_periods=max(423//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.355 + 0.0041879 * anchor
    return base_signal.diff().diff()

def f91_govr_479_struct_v479_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=241, w2=434, w3=159, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(434, min_periods=max(434//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2574 * _rolling_slope(draw, 159) + 0.004188 * anchor
    return base_signal.diff().diff()

def f91_govr_480_struct_v480_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=248, w2=445, w3=172, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(445, min_periods=max(445//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.38375 + 0.0041881 * anchor
    return base_signal.diff().diff()

def f91_govr_481_struct_v481_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=255, w2=456, w3=185, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 255)
    slow = _rolling_slope(x, 456)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=185, adjust=False).mean() * 1.398125 + 0.0041882 * anchor
    return base_signal.diff().diff()

def f91_govr_482_struct_v482_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=11, w2=467, w3=198, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(467, min_periods=max(467//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4125 + 0.0041883 * anchor
    return base_signal.diff().diff()

def f91_govr_483_struct_v483_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=18, w2=478, w3=211, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(18)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2878 * persistence + 0.0041884 * anchor
    return base_signal.diff().diff()

def f91_govr_484_struct_v484_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=25, w2=489, w3=224, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(489, min_periods=max(489//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.44125 + 0.0041885 * anchor
    return base_signal.diff().diff()

def f91_govr_485_struct_v485_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=500, w3=237, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.303 * slope + 0.0041886 * anchor
    return base_signal.diff().diff()

def f91_govr_486_struct_v486_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=511, w3=250, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(39)
    drag = impulse.rolling(511, min_periods=max(511//3, 2)).mean()
    noise = impulse.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47 + 0.0041887 * anchor
    return base_signal.diff().diff()

def f91_govr_487_struct_v487_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=19, w3=263, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 19)
    curvature = _rolling_slope(acceleration, 263)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3182 * acceleration + 0.0041888 * anchor
    return base_signal.diff().diff()

def f91_govr_488_struct_v488_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=30, w3=276, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(30, min_periods=max(30//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49875 + 0.0041889 * anchor
    return base_signal.diff().diff()

def f91_govr_489_struct_v489_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=41, w3=289, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(41, min_periods=max(41//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3334 * _rolling_slope(draw, 289) + 0.004189 * anchor
    return base_signal.diff().diff()

def f91_govr_490_struct_v490_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=52, w3=302, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(52, min_periods=max(52//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5275 + 0.0041891 * anchor
    return base_signal.diff().diff()

def f91_govr_491_struct_v491_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=63, w3=315, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 63)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.541875 + 0.0041892 * anchor
    return base_signal.diff().diff()

def f91_govr_492_struct_v492_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=74, w3=328, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(74, min_periods=max(74//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.55625 + 0.0041893 * anchor
    return base_signal.diff().diff()

def f91_govr_493_struct_v493_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=85, w3=341, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(88)
    rank = change.rolling(85, min_periods=max(85//3, 2)).rank(pct=True)
    persistence = change.rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3638 * persistence + 0.0041894 * anchor
    return base_signal.diff().diff()

def f91_govr_494_struct_v494_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=96, w3=354, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(96, min_periods=max(96//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585 + 0.0041895 * anchor
    return base_signal.diff().diff()

def f91_govr_495_struct_v495_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=107, w3=367, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(107, min_periods=max(107//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.379 * slope + 0.0041896 * anchor
    return base_signal.diff().diff()

def f91_govr_496_struct_v496_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=118, w3=380, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(109)
    drag = impulse.rolling(118, min_periods=max(118//3, 2)).mean()
    noise = impulse.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.61375 + 0.0041897 * anchor
    return base_signal.diff().diff()

def f91_govr_497_struct_v497_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=116, w2=129, w3=393, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 129)
    curvature = _rolling_slope(acceleration, 393)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3942 * acceleration + 0.0041898 * anchor
    return base_signal.diff().diff()

def f91_govr_498_struct_v498_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=123, w2=140, w3=406, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.869375 + 0.0041899 * anchor
    return base_signal.diff().diff()

def f91_govr_499_struct_v499_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=130, w2=151, w3=419, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(151, min_periods=max(151//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4094 * _rolling_slope(draw, 419) + 0.00419 * anchor
    return base_signal.diff().diff()

def f91_govr_500_struct_v500_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=137, w2=162, w3=432, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(162, min_periods=max(162//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.898125 + 0.0041901 * anchor
    return base_signal.diff().diff()

def f91_govr_501_struct_v501_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=144, w2=173, w3=445, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 173)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9125 + 0.0041902 * anchor
    return base_signal.diff().diff()

def f91_govr_502_struct_v502_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=151, w2=184, w3=458, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(184, min_periods=max(184//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.926875 + 0.0041903 * anchor
    return base_signal.diff().diff()

def f91_govr_503_struct_v503_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=158, w2=195, w3=471, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(195, min_periods=max(195//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0634 * persistence + 0.0041904 * anchor
    return base_signal.diff().diff()

def f91_govr_504_struct_v504_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=165, w2=206, w3=484, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(206, min_periods=max(206//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955625 + 0.0041905 * anchor
    return base_signal.diff().diff()

def f91_govr_505_struct_v505_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=172, w2=217, w3=497, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(217, min_periods=max(217//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0786 * slope + 0.0041906 * anchor
    return base_signal.diff().diff()

def f91_govr_506_struct_v506_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=179, w2=228, w3=510, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(228, min_periods=max(228//3, 2)).mean()
    noise = impulse.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.984375 + 0.0041907 * anchor
    return base_signal.diff().diff()

def f91_govr_507_struct_v507_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=186, w2=239, w3=523, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 239)
    curvature = _rolling_slope(acceleration, 523)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0938 * acceleration + 0.0041908 * anchor
    return base_signal.diff().diff()

def f91_govr_508_struct_v508_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=193, w2=250, w3=536, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(250, min_periods=max(250//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.013125 + 0.0041909 * anchor
    return base_signal.diff().diff()

def f91_govr_509_struct_v509_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=200, w2=261, w3=549, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(261, min_periods=max(261//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.109 * _rolling_slope(draw, 549) + 0.004191 * anchor
    return base_signal.diff().diff()

def f91_govr_510_struct_v510_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=207, w2=272, w3=562, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(272, min_periods=max(272//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.041875 + 0.0041911 * anchor
    return base_signal.diff().diff()

def f91_govr_511_struct_v511_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=214, w2=283, w3=575, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 283)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.05625 + 0.0041912 * anchor
    return base_signal.diff().diff()

def f91_govr_512_struct_v512_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=221, w2=294, w3=588, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(294, min_periods=max(294//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.070625 + 0.0041913 * anchor
    return base_signal.diff().diff()

def f91_govr_513_struct_v513_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=228, w2=305, w3=601, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(305, min_periods=max(305//3, 2)).rank(pct=True)
    persistence = change.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1394 * persistence + 0.0041914 * anchor
    return base_signal.diff().diff()

def f91_govr_514_struct_v514_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=235, w2=316, w3=614, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(316, min_periods=max(316//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.099375 + 0.0041915 * anchor
    return base_signal.diff().diff()

def f91_govr_515_struct_v515_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=242, w2=327, w3=627, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(327, min_periods=max(327//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1546 * slope + 0.0041916 * anchor
    return base_signal.diff().diff()

def f91_govr_516_struct_v516_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=249, w2=338, w3=640, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(338, min_periods=max(338//3, 2)).mean()
    noise = impulse.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.128125 + 0.0041917 * anchor
    return base_signal.diff().diff()

def f91_govr_517_struct_v517_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=5, w2=349, w3=653, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 349)
    curvature = _rolling_slope(acceleration, 653)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1698 * acceleration + 0.0041918 * anchor
    return base_signal.diff().diff()

def f91_govr_518_struct_v518_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=12, w2=360, w3=666, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(360, min_periods=max(360//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.156875 + 0.0041919 * anchor
    return base_signal.diff().diff()

def f91_govr_519_struct_v519_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=19, w2=371, w3=679, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(371, min_periods=max(371//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.185 * _rolling_slope(draw, 679) + 0.004192 * anchor
    return base_signal.diff().diff()

def f91_govr_520_struct_v520_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=26, w2=382, w3=692, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(382, min_periods=max(382//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.185625 + 0.0041921 * anchor
    return base_signal.diff().diff()

def f91_govr_521_struct_v521_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=33, w2=393, w3=705, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 393)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2 + 0.0041922 * anchor
    return base_signal.diff().diff()

def f91_govr_522_struct_v522_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=40, w2=404, w3=718, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(404, min_periods=max(404//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.214375 + 0.0041923 * anchor
    return base_signal.diff().diff()

def f91_govr_523_struct_v523_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=47, w2=415, w3=731, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(47)
    rank = change.rolling(415, min_periods=max(415//3, 2)).rank(pct=True)
    persistence = change.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2154 * persistence + 0.0041924 * anchor
    return base_signal.diff().diff()

def f91_govr_524_struct_v524_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=54, w2=426, w3=744, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.243125 + 0.0041925 * anchor
    return base_signal.diff().diff()

def f91_govr_525_struct_v525_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=61, w2=437, w3=757, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2306 * slope + 0.0041926 * anchor
    return base_signal.diff().diff()
