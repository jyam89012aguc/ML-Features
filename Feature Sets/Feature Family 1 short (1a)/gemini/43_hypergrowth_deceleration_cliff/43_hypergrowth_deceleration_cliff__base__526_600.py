"""43 hypergrowth deceleration cliff base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f43_hdc_526_struct_v526(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=432, w3=319, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(432, min_periods=max(432//3, 2)).mean()
    noise = impulse.abs().rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.34875 + 0.0026927 * anchor

def f43_hdc_527_struct_v527(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=443, w3=332, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.295 * acceleration + 0.0026928 * anchor

def f43_hdc_528_struct_v528(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=454, w3=345, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(454, min_periods=max(454//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.3775 + 0.0026929 * anchor

def f43_hdc_529_struct_v529(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=465, w3=358, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(465, min_periods=max(465//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3102 * _rolling_slope(draw, 358) + 0.002693 * anchor

def f43_hdc_530_struct_v530(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=476, w3=371, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(476, min_periods=max(476//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.40625 + 0.0026931 * anchor

def f43_hdc_531_struct_v531(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=487, w3=384, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 487)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.420625 + 0.0026932 * anchor

def f43_hdc_532_struct_v532(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=498, w3=397, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(498, min_periods=max(498//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.435 + 0.0026933 * anchor

def f43_hdc_533_struct_v533(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=509, w3=410, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(35)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3406 * persistence + 0.0026934 * anchor

def f43_hdc_534_struct_v534(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=17, w3=423, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(17, min_periods=max(17//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46375 + 0.0026935 * anchor

def f43_hdc_535_struct_v535(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=28, w3=436, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3558 * slope + 0.0026936 * anchor

def f43_hdc_536_struct_v536(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=39, w3=449, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(56)
    drag = impulse.rolling(39, min_periods=max(39//3, 2)).mean()
    noise = impulse.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4925 + 0.0026937 * anchor

def f43_hdc_537_struct_v537(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=50, w3=462, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 50)
    curvature = _rolling_slope(acceleration, 462)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.371 * acceleration + 0.0026938 * anchor

def f43_hdc_538_struct_v538(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=61, w3=475, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(61, min_periods=max(61//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.52125 + 0.0026939 * anchor

def f43_hdc_539_struct_v539(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=72, w3=488, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(72, min_periods=max(72//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3862 * _rolling_slope(draw, 488) + 0.002694 * anchor

def f43_hdc_540_struct_v540(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=83, w3=501, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.55 + 0.0026941 * anchor

def f43_hdc_541_struct_v541(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=94, w3=514, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.564375 + 0.0026942 * anchor

def f43_hdc_542_struct_v542(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=105, w3=527, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.57875 + 0.0026943 * anchor

def f43_hdc_543_struct_v543(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=116, w3=540, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(105)
    rank = change.rolling(116, min_periods=max(116//3, 2)).rank(pct=True)
    persistence = change.rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0402 * persistence + 0.0026944 * anchor

def f43_hdc_544_struct_v544(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=127, w3=553, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(127, min_periods=max(127//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6075 + 0.0026945 * anchor

def f43_hdc_545_struct_v545(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=138, w3=566, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(138, min_periods=max(138//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0554 * slope + 0.0026946 * anchor

def f43_hdc_546_struct_v546(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=149, w3=579, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(149, min_periods=max(149//3, 2)).mean()
    noise = impulse.abs().rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.863125 + 0.0026947 * anchor

def f43_hdc_547_struct_v547(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=160, w3=592, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 160)
    curvature = _rolling_slope(acceleration, 592)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0706 * acceleration + 0.0026948 * anchor

def f43_hdc_548_struct_v548(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=171, w3=605, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.891875 + 0.0026949 * anchor

def f43_hdc_549_struct_v549(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=182, w3=618, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(182, min_periods=max(182//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0858 * _rolling_slope(draw, 618) + 0.002695 * anchor

def f43_hdc_550_struct_v550(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=193, w3=631, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(193, min_periods=max(193//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.920625 + 0.0026951 * anchor

def f43_hdc_551_struct_v551(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=204, w3=644, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 204)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.935 + 0.0026952 * anchor

def f43_hdc_552_struct_v552(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=215, w3=657, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(215, min_periods=max(215//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.949375 + 0.0026953 * anchor

def f43_hdc_553_struct_v553(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=226, w3=670, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(226, min_periods=max(226//3, 2)).rank(pct=True)
    persistence = change.rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1162 * persistence + 0.0026954 * anchor

def f43_hdc_554_struct_v554(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=237, w3=683, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(237, min_periods=max(237//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.978125 + 0.0026955 * anchor

def f43_hdc_555_struct_v555(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=248, w3=696, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(248, min_periods=max(248//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1314 * slope + 0.0026956 * anchor

def f43_hdc_556_struct_v556(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=259, w3=709, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(259, min_periods=max(259//3, 2)).mean()
    noise = impulse.abs().rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.006875 + 0.0026957 * anchor

def f43_hdc_557_struct_v557(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=270, w3=722, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 722)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1466 * acceleration + 0.0026958 * anchor

def f43_hdc_558_struct_v558(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=281, w3=735, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(281, min_periods=max(281//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.035625 + 0.0026959 * anchor

def f43_hdc_559_struct_v559(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=292, w3=748, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1618 * _rolling_slope(draw, 748) + 0.002696 * anchor

def f43_hdc_560_struct_v560(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=303, w3=761, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(303, min_periods=max(303//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.064375 + 0.0026961 * anchor

def f43_hdc_561_struct_v561(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=314, w3=17, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 314)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=17, adjust=False).mean() * 1.07875 + 0.0026962 * anchor

def f43_hdc_562_struct_v562(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=325, w3=30, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(325, min_periods=max(325//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.093125 + 0.0026963 * anchor

def f43_hdc_563_struct_v563(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=336, w3=43, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(336, min_periods=max(336//3, 2)).rank(pct=True)
    persistence = change.rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1922 * persistence + 0.0026964 * anchor

def f43_hdc_564_struct_v564(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=347, w3=56, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(252, min_periods=max(252//3, 2)).std()
    vol_slow = ret.rolling(347, min_periods=max(347//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.121875 + 0.0026965 * anchor

def f43_hdc_565_struct_v565(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=358, w3=69, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(358, min_periods=max(358//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2074 * slope + 0.0026966 * anchor

def f43_hdc_566_struct_v566(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=369, w3=82, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(15)
    drag = impulse.rolling(369, min_periods=max(369//3, 2)).mean()
    noise = impulse.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.150625 + 0.0026967 * anchor

def f43_hdc_567_struct_v567(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=380, w3=95, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 380)
    curvature = _rolling_slope(acceleration, 95)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2226 * acceleration + 0.0026968 * anchor

def f43_hdc_568_struct_v568(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=391, w3=108, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(391, min_periods=max(391//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(108) * 1.179375 + 0.0026969 * anchor

def f43_hdc_569_struct_v569(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=402, w3=121, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(402, min_periods=max(402//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2378 * _rolling_slope(draw, 121) + 0.002697 * anchor

def f43_hdc_570_struct_v570(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=413, w3=134, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(413, min_periods=max(413//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.208125 + 0.0026971 * anchor

def f43_hdc_571_struct_v571(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=424, w3=147, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 424)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=147, adjust=False).mean() * 1.2225 + 0.0026972 * anchor

def f43_hdc_572_struct_v572(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=435, w3=160, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(435, min_periods=max(435//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.236875 + 0.0026973 * anchor

def f43_hdc_573_struct_v573(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=446, w3=173, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(64)
    rank = change.rolling(446, min_periods=max(446//3, 2)).rank(pct=True)
    persistence = change.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2682 * persistence + 0.0026974 * anchor

def f43_hdc_574_struct_v574(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=457, w3=186, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(457, min_periods=max(457//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.265625 + 0.0026975 * anchor

def f43_hdc_575_struct_v575(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=468, w3=199, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(468, min_periods=max(468//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2834 * slope + 0.0026976 * anchor

def f43_hdc_576_struct_v576(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=479, w3=212, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(85)
    drag = impulse.rolling(479, min_periods=max(479//3, 2)).mean()
    noise = impulse.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.294375 + 0.0026977 * anchor

def f43_hdc_577_struct_v577(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=490, w3=225, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 490)
    curvature = _rolling_slope(acceleration, 225)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2986 * acceleration + 0.0026978 * anchor

def f43_hdc_578_struct_v578(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=501, w3=238, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(501, min_periods=max(501//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.323125 + 0.0026979 * anchor

def f43_hdc_579_struct_v579(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=512, w3=251, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(512, min_periods=max(512//3, 2)).max()
    rebound = x - x.rolling(106, min_periods=max(106//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3138 * _rolling_slope(draw, 251) + 0.002698 * anchor

def f43_hdc_580_struct_v580(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=20, w3=264, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 113)
    baseline = trend.rolling(20, min_periods=max(20//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.351875 + 0.0026981 * anchor

def f43_hdc_581_struct_v581(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=31, w3=277, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 31)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=277, adjust=False).mean() * 1.36625 + 0.0026982 * anchor

def f43_hdc_582_struct_v582(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=42, w3=290, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(42, min_periods=max(42//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.380625 + 0.0026983 * anchor

def f43_hdc_583_struct_v583(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=53, w3=303, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(53, min_periods=max(53//3, 2)).rank(pct=True)
    persistence = change.rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3442 * persistence + 0.0026984 * anchor

def f43_hdc_584_struct_v584(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=64, w3=316, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(64, min_periods=max(64//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.409375 + 0.0026985 * anchor

def f43_hdc_585_struct_v585(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=75, w3=329, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(75, min_periods=max(75//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3594 * slope + 0.0026986 * anchor

def f43_hdc_586_struct_v586(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=86, w3=342, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(86, min_periods=max(86//3, 2)).mean()
    noise = impulse.abs().rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.438125 + 0.0026987 * anchor

def f43_hdc_587_struct_v587(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=97, w3=355, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 97)
    curvature = _rolling_slope(acceleration, 355)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3746 * acceleration + 0.0026988 * anchor

def f43_hdc_588_struct_v588(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=108, w3=368, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(108, min_periods=max(108//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.466875 + 0.0026989 * anchor

def f43_hdc_589_struct_v589(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=119, w3=381, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(119, min_periods=max(119//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3898 * _rolling_slope(draw, 381) + 0.002699 * anchor

def f43_hdc_590_struct_v590(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=130, w3=394, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.495625 + 0.0026991 * anchor

def f43_hdc_591_struct_v591(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=141, w3=407, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 141)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.51 + 0.0026992 * anchor

def f43_hdc_592_struct_v592(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=152, w3=420, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(152, min_periods=max(152//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.524375 + 0.0026993 * anchor

def f43_hdc_593_struct_v593(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=163, w3=433, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(163, min_periods=max(163//3, 2)).rank(pct=True)
    persistence = change.rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0438 * persistence + 0.0026994 * anchor

def f43_hdc_594_struct_v594(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=174, w3=446, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(174, min_periods=max(174//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.553125 + 0.0026995 * anchor

def f43_hdc_595_struct_v595(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=185, w3=459, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(185, min_periods=max(185//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.059 * slope + 0.0026996 * anchor

def f43_hdc_596_struct_v596(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=196, w3=472, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(196, min_periods=max(196//3, 2)).mean()
    noise = impulse.abs().rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.581875 + 0.0026997 * anchor

def f43_hdc_597_struct_v597(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=207, w3=485, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 207)
    curvature = _rolling_slope(acceleration, 485)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0742 * acceleration + 0.0026998 * anchor

def f43_hdc_598_struct_v598(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=218, w3=498, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(218, min_periods=max(218//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.610625 + 0.0026999 * anchor

def f43_hdc_599_struct_v599(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=229, w3=511, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(229, min_periods=max(229//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0894 * _rolling_slope(draw, 511) + 0.0027 * anchor

def f43_hdc_600_struct_v600(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=240, w3=524, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(240, min_periods=max(240//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.86625 + 0.0027001 * anchor
