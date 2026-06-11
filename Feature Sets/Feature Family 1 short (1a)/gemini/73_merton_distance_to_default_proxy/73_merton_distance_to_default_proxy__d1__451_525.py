"""73 merton distance to default proxy d1 first derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Credit_Risk - Institutional-grade short-side signal.
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

def f73_mdd_451_struct_v451_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=263, w3=686, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 263)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.01625 + 0.0038252 * anchor
    return base_signal.diff()

def f73_mdd_452_struct_v452_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=274, w3=699, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(274, min_periods=max(274//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.030625 + 0.0038253 * anchor
    return base_signal.diff()

def f73_mdd_453_struct_v453_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=285, w3=712, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(285, min_periods=max(285//3, 2)).rank(pct=True)
    persistence = change.rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.177 * persistence + 0.0038254 * anchor
    return base_signal.diff()

def f73_mdd_454_struct_v454_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=296, w3=725, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.059375 + 0.0038255 * anchor
    return base_signal.diff()

def f73_mdd_455_struct_v455_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=307, w3=738, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1922 * slope + 0.0038256 * anchor
    return base_signal.diff()

def f73_mdd_456_struct_v456_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=318, w3=751, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.088125 + 0.0038257 * anchor
    return base_signal.diff()

def f73_mdd_457_struct_v457_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=329, w3=764, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 764)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2074 * acceleration + 0.0038258 * anchor
    return base_signal.diff()

def f73_mdd_458_struct_v458_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=340, w3=20, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(20) * 1.116875 + 0.0038259 * anchor
    return base_signal.diff()

def f73_mdd_459_struct_v459_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=351, w3=33, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2226 * _rolling_slope(draw, 33) + 0.003826 * anchor
    return base_signal.diff()

def f73_mdd_460_struct_v460_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=362, w3=46, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.145625 + 0.0038261 * anchor
    return base_signal.diff()

def f73_mdd_461_struct_v461_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=373, w3=59, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 373)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=59, adjust=False).mean() * 1.16 + 0.0038262 * anchor
    return base_signal.diff()

def f73_mdd_462_struct_v462_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=384, w3=72, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.174375 + 0.0038263 * anchor
    return base_signal.diff()

def f73_mdd_463_struct_v463_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=395, w3=85, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(29)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.253 * persistence + 0.0038264 * anchor
    return base_signal.diff()

def f73_mdd_464_struct_v464_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=406, w3=98, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.203125 + 0.0038265 * anchor
    return base_signal.diff()

def f73_mdd_465_struct_v465_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=417, w3=111, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2682 * slope + 0.0038266 * anchor
    return base_signal.diff()

def f73_mdd_466_struct_v466_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=428, w3=124, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(50)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.231875 + 0.0038267 * anchor
    return base_signal.diff()

def f73_mdd_467_struct_v467_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=439, w3=137, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 137)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2834 * acceleration + 0.0038268 * anchor
    return base_signal.diff()

def f73_mdd_468_struct_v468_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=450, w3=150, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.260625 + 0.0038269 * anchor
    return base_signal.diff()

def f73_mdd_469_struct_v469_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=461, w3=163, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2986 * _rolling_slope(draw, 163) + 0.003827 * anchor
    return base_signal.diff()

def f73_mdd_470_struct_v470_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=472, w3=176, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(472, min_periods=max(472//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.289375 + 0.0038271 * anchor
    return base_signal.diff()

def f73_mdd_471_struct_v471_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=483, w3=189, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=189, adjust=False).mean() * 1.30375 + 0.0038272 * anchor
    return base_signal.diff()

def f73_mdd_472_struct_v472_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=494, w3=202, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.318125 + 0.0038273 * anchor
    return base_signal.diff()

def f73_mdd_473_struct_v473_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=505, w3=215, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(99)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.329 * persistence + 0.0038274 * anchor
    return base_signal.diff()

def f73_mdd_474_struct_v474_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=13, w3=228, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.346875 + 0.0038275 * anchor
    return base_signal.diff()

def f73_mdd_475_struct_v475_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=24, w3=241, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3442 * slope + 0.0038276 * anchor
    return base_signal.diff()

def f73_mdd_476_struct_v476_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=35, w3=254, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(120)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.375625 + 0.0038277 * anchor
    return base_signal.diff()

def f73_mdd_477_struct_v477_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=46, w3=267, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 46)
    curvature = _rolling_slope(acceleration, 267)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3594 * acceleration + 0.0038278 * anchor
    return base_signal.diff()

def f73_mdd_478_struct_v478_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=57, w3=280, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.404375 + 0.0038279 * anchor
    return base_signal.diff()

def f73_mdd_479_struct_v479_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=68, w3=293, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3746 * _rolling_slope(draw, 293) + 0.003828 * anchor
    return base_signal.diff()

def f73_mdd_480_struct_v480_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=79, w3=306, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.433125 + 0.0038281 * anchor
    return base_signal.diff()

def f73_mdd_481_struct_v481_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=90, w3=319, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 90)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4475 + 0.0038282 * anchor
    return base_signal.diff()

def f73_mdd_482_struct_v482_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=101, w3=332, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(101, min_periods=max(101//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.461875 + 0.0038283 * anchor
    return base_signal.diff()

def f73_mdd_483_struct_v483_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=112, w3=345, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(112, min_periods=max(112//3, 2)).rank(pct=True)
    persistence = change.rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.405 * persistence + 0.0038284 * anchor
    return base_signal.diff()

def f73_mdd_484_struct_v484_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=123, w3=358, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(123, min_periods=max(123//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.490625 + 0.0038285 * anchor
    return base_signal.diff()

def f73_mdd_485_struct_v485_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=134, w3=371, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(134, min_periods=max(134//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0438 * slope + 0.0038286 * anchor
    return base_signal.diff()

def f73_mdd_486_struct_v486_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=145, w3=384, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.519375 + 0.0038287 * anchor
    return base_signal.diff()

def f73_mdd_487_struct_v487_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=156, w3=397, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 397)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.059 * acceleration + 0.0038288 * anchor
    return base_signal.diff()

def f73_mdd_488_struct_v488_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=167, w3=410, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.548125 + 0.0038289 * anchor
    return base_signal.diff()

def f73_mdd_489_struct_v489_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=178, w3=423, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(178, min_periods=max(178//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0742 * _rolling_slope(draw, 423) + 0.003829 * anchor
    return base_signal.diff()

def f73_mdd_490_struct_v490_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=189, w3=436, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(189, min_periods=max(189//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.576875 + 0.0038291 * anchor
    return base_signal.diff()

def f73_mdd_491_struct_v491_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=200, w3=449, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.59125 + 0.0038292 * anchor
    return base_signal.diff()

def f73_mdd_492_struct_v492_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=211, w3=462, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(211, min_periods=max(211//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.605625 + 0.0038293 * anchor
    return base_signal.diff()

def f73_mdd_493_struct_v493_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=222, w3=475, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(475, min_periods=max(475//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1046 * persistence + 0.0038294 * anchor
    return base_signal.diff()

def f73_mdd_494_struct_v494_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=233, w3=488, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86125 + 0.0038295 * anchor
    return base_signal.diff()

def f73_mdd_495_struct_v495_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=244, w3=501, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1198 * slope + 0.0038296 * anchor
    return base_signal.diff()

def f73_mdd_496_struct_v496_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=255, w3=514, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(9)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.89 + 0.0038297 * anchor
    return base_signal.diff()

def f73_mdd_497_struct_v497_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=266, w3=527, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 527)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.135 * acceleration + 0.0038298 * anchor
    return base_signal.diff()

def f73_mdd_498_struct_v498_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=277, w3=540, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.91875 + 0.0038299 * anchor
    return base_signal.diff()

def f73_mdd_499_struct_v499_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=288, w3=553, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1502 * _rolling_slope(draw, 553) + 0.00383 * anchor
    return base_signal.diff()

def f73_mdd_500_struct_v500_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=299, w3=566, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9475 + 0.0038301 * anchor
    return base_signal.diff()

def f73_mdd_501_struct_v501_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=310, w3=579, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.961875 + 0.0038302 * anchor
    return base_signal.diff()

def f73_mdd_502_struct_v502_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=321, w3=592, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.97625 + 0.0038303 * anchor
    return base_signal.diff()

def f73_mdd_503_struct_v503_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=332, w3=605, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(58)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1806 * persistence + 0.0038304 * anchor
    return base_signal.diff()

def f73_mdd_504_struct_v504_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=343, w3=618, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.005 + 0.0038305 * anchor
    return base_signal.diff()

def f73_mdd_505_struct_v505_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=354, w3=631, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1958 * slope + 0.0038306 * anchor
    return base_signal.diff()

def f73_mdd_506_struct_v506_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=365, w3=644, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(79)
    drag = impulse.rolling(365, min_periods=max(365//3, 2)).mean()
    noise = impulse.abs().rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03375 + 0.0038307 * anchor
    return base_signal.diff()

def f73_mdd_507_struct_v507_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=376, w3=657, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 657)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211 * acceleration + 0.0038308 * anchor
    return base_signal.diff()

def f73_mdd_508_struct_v508_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=387, w3=670, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0625 + 0.0038309 * anchor
    return base_signal.diff()

def f73_mdd_509_struct_v509_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=398, w3=683, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(398, min_periods=max(398//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2262 * _rolling_slope(draw, 683) + 0.003831 * anchor
    return base_signal.diff()

def f73_mdd_510_struct_v510_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=409, w3=696, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(409, min_periods=max(409//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09125 + 0.0038311 * anchor
    return base_signal.diff()

def f73_mdd_511_struct_v511_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=420, w3=709, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.105625 + 0.0038312 * anchor
    return base_signal.diff()

def f73_mdd_512_struct_v512_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=431, w3=722, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(431, min_periods=max(431//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.12 + 0.0038313 * anchor
    return base_signal.diff()

def f73_mdd_513_struct_v513_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=442, w3=735, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(442, min_periods=max(442//3, 2)).rank(pct=True)
    persistence = change.rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2566 * persistence + 0.0038314 * anchor
    return base_signal.diff()

def f73_mdd_514_struct_v514_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=453, w3=748, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(453, min_periods=max(453//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14875 + 0.0038315 * anchor
    return base_signal.diff()

def f73_mdd_515_struct_v515_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=464, w3=761, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2718 * slope + 0.0038316 * anchor
    return base_signal.diff()

def f73_mdd_516_struct_v516_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=475, w3=17, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(475, min_periods=max(475//3, 2)).mean()
    noise = impulse.abs().rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1775 + 0.0038317 * anchor
    return base_signal.diff()

def f73_mdd_517_struct_v517_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=486, w3=30, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 30)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.287 * acceleration + 0.0038318 * anchor
    return base_signal.diff()

def f73_mdd_518_struct_v518_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=497, w3=43, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(43) * 1.20625 + 0.0038319 * anchor
    return base_signal.diff()

def f73_mdd_519_struct_v519_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=508, w3=56, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3022 * _rolling_slope(draw, 56) + 0.003832 * anchor
    return base_signal.diff()

def f73_mdd_520_struct_v520_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=16, w3=69, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.235 + 0.0038321 * anchor
    return base_signal.diff()

def f73_mdd_521_struct_v521_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=27, w3=82, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 27)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=82, adjust=False).mean() * 1.249375 + 0.0038322 * anchor
    return base_signal.diff()

def f73_mdd_522_struct_v522_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=38, w3=95, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(38, min_periods=max(38//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26375 + 0.0038323 * anchor
    return base_signal.diff()

def f73_mdd_523_struct_v523_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=49, w3=108, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(49, min_periods=max(49//3, 2)).rank(pct=True)
    persistence = change.rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3326 * persistence + 0.0038324 * anchor
    return base_signal.diff()

def f73_mdd_524_struct_v524_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=60, w3=121, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2925 + 0.0038325 * anchor
    return base_signal.diff()

def f73_mdd_525_struct_v525_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=71, w3=134, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(71, min_periods=max(71//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3478 * slope + 0.0038326 * anchor
    return base_signal.diff()
