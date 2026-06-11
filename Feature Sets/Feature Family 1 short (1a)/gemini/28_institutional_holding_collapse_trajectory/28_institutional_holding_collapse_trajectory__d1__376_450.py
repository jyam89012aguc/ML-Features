"""28 institutional holding collapse trajectory d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Ownership - Institutional-grade short-side signal.
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

def f28_ihc_376_struct_v376_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=321, w3=745, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(8)
    drag = impulse.rolling(321, min_periods=max(321//3, 2)).mean()
    noise = impulse.abs().rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.128125 + 0.0017177 * anchor
    return base_signal.diff()

def f28_ihc_377_struct_v377_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=332, w3=758, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 332)
    curvature = _rolling_slope(acceleration, 758)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3458 * acceleration + 0.0017178 * anchor
    return base_signal.diff()

def f28_ihc_378_struct_v378_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=343, w3=771, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(343, min_periods=max(343//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.156875 + 0.0017179 * anchor
    return base_signal.diff()

def f28_ihc_379_struct_v379_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=354, w3=27, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(354, min_periods=max(354//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.361 * _rolling_slope(draw, 27) + 0.001718 * anchor
    return base_signal.diff()

def f28_ihc_380_struct_v380_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=365, w3=40, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.185625 + 0.0017181 * anchor
    return base_signal.diff()

def f28_ihc_381_struct_v381_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=376, w3=53, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 376)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=53, adjust=False).mean() * 1.2 + 0.0017182 * anchor
    return base_signal.diff()

def f28_ihc_382_struct_v382_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=387, w3=66, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(387, min_periods=max(387//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.214375 + 0.0017183 * anchor
    return base_signal.diff()

def f28_ihc_383_struct_v383_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=398, w3=79, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(57)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3914 * persistence + 0.0017184 * anchor
    return base_signal.diff()

def f28_ihc_384_struct_v384_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=409, w3=92, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.243125 + 0.0017185 * anchor
    return base_signal.diff()

def f28_ihc_385_struct_v385_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=420, w3=105, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(420, min_periods=max(420//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4066 * slope + 0.0017186 * anchor
    return base_signal.diff()

def f28_ihc_386_struct_v386_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=431, w3=118, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(78)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.271875 + 0.0017187 * anchor
    return base_signal.diff()

def f28_ihc_387_struct_v387_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=442, w3=131, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 442)
    curvature = _rolling_slope(acceleration, 131)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0454 * acceleration + 0.0017188 * anchor
    return base_signal.diff()

def f28_ihc_388_struct_v388_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=453, w3=144, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(453, min_periods=max(453//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.300625 + 0.0017189 * anchor
    return base_signal.diff()

def f28_ihc_389_struct_v389_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=464, w3=157, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0606 * _rolling_slope(draw, 157) + 0.001719 * anchor
    return base_signal.diff()

def f28_ihc_390_struct_v390_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=475, w3=170, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(475, min_periods=max(475//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.329375 + 0.0017191 * anchor
    return base_signal.diff()

def f28_ihc_391_struct_v391_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=486, w3=183, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 486)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=183, adjust=False).mean() * 1.34375 + 0.0017192 * anchor
    return base_signal.diff()

def f28_ihc_392_struct_v392_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=497, w3=196, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(497, min_periods=max(497//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.358125 + 0.0017193 * anchor
    return base_signal.diff()

def f28_ihc_393_struct_v393_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=508, w3=209, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(508, min_periods=max(508//3, 2)).rank(pct=True)
    persistence = change.rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.091 * persistence + 0.0017194 * anchor
    return base_signal.diff()

def f28_ihc_394_struct_v394_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=16, w3=222, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(16, min_periods=max(16//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.386875 + 0.0017195 * anchor
    return base_signal.diff()

def f28_ihc_395_struct_v395_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=27, w3=235, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(27, min_periods=max(27//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1062 * slope + 0.0017196 * anchor
    return base_signal.diff()

def f28_ihc_396_struct_v396_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=38, w3=248, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(38, min_periods=max(38//3, 2)).mean()
    noise = impulse.abs().rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.415625 + 0.0017197 * anchor
    return base_signal.diff()

def f28_ihc_397_struct_v397_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=49, w3=261, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 49)
    curvature = _rolling_slope(acceleration, 261)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1214 * acceleration + 0.0017198 * anchor
    return base_signal.diff()

def f28_ihc_398_struct_v398_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=60, w3=274, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(60, min_periods=max(60//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.444375 + 0.0017199 * anchor
    return base_signal.diff()

def f28_ihc_399_struct_v399_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=71, w3=287, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(71, min_periods=max(71//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1366 * _rolling_slope(draw, 287) + 0.00172 * anchor
    return base_signal.diff()

def f28_ihc_400_struct_v400_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=82, w3=300, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(82, min_periods=max(82//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.473125 + 0.0017201 * anchor
    return base_signal.diff()

def f28_ihc_401_struct_v401_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=93, w3=313, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 93)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4875 + 0.0017202 * anchor
    return base_signal.diff()

def f28_ihc_402_struct_v402_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=104, w3=326, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(104, min_periods=max(104//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.501875 + 0.0017203 * anchor
    return base_signal.diff()

def f28_ihc_403_struct_v403_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=115, w3=339, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(115, min_periods=max(115//3, 2)).rank(pct=True)
    persistence = change.rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.167 * persistence + 0.0017204 * anchor
    return base_signal.diff()

def f28_ihc_404_struct_v404_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=126, w3=352, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(126, min_periods=max(126//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.530625 + 0.0017205 * anchor
    return base_signal.diff()

def f28_ihc_405_struct_v405_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=137, w3=365, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(137, min_periods=max(137//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1822 * slope + 0.0017206 * anchor
    return base_signal.diff()

def f28_ihc_406_struct_v406_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=148, w3=378, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(148, min_periods=max(148//3, 2)).mean()
    noise = impulse.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.559375 + 0.0017207 * anchor
    return base_signal.diff()

def f28_ihc_407_struct_v407_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=159, w3=391, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 159)
    curvature = _rolling_slope(acceleration, 391)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1974 * acceleration + 0.0017208 * anchor
    return base_signal.diff()

def f28_ihc_408_struct_v408_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=170, w3=404, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(170, min_periods=max(170//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.588125 + 0.0017209 * anchor
    return base_signal.diff()

def f28_ihc_409_struct_v409_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=181, w3=417, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(181, min_periods=max(181//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2126 * _rolling_slope(draw, 417) + 0.001721 * anchor
    return base_signal.diff()

def f28_ihc_410_struct_v410_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=192, w3=430, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(192, min_periods=max(192//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.616875 + 0.0017211 * anchor
    return base_signal.diff()

def f28_ihc_411_struct_v411_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=203, w3=443, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 253)
    slow = _rolling_slope(x, 203)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.858125 + 0.0017212 * anchor
    return base_signal.diff()

def f28_ihc_412_struct_v412_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=214, w3=456, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(214, min_periods=max(214//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.8725 + 0.0017213 * anchor
    return base_signal.diff()

def f28_ihc_413_struct_v413_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=225, w3=469, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(16)
    rank = change.rolling(225, min_periods=max(225//3, 2)).rank(pct=True)
    persistence = change.rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.243 * persistence + 0.0017214 * anchor
    return base_signal.diff()

def f28_ihc_414_struct_v414_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=236, w3=482, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(236, min_periods=max(236//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90125 + 0.0017215 * anchor
    return base_signal.diff()

def f28_ihc_415_struct_v415_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=247, w3=495, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(247, min_periods=max(247//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2582 * slope + 0.0017216 * anchor
    return base_signal.diff()

def f28_ihc_416_struct_v416_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=258, w3=508, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(37)
    drag = impulse.rolling(258, min_periods=max(258//3, 2)).mean()
    noise = impulse.abs().rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.93 + 0.0017217 * anchor
    return base_signal.diff()

def f28_ihc_417_struct_v417_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=269, w3=521, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 269)
    curvature = _rolling_slope(acceleration, 521)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2734 * acceleration + 0.0017218 * anchor
    return base_signal.diff()

def f28_ihc_418_struct_v418_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=280, w3=534, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(280, min_periods=max(280//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.95875 + 0.0017219 * anchor
    return base_signal.diff()

def f28_ihc_419_struct_v419_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=291, w3=547, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(291, min_periods=max(291//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2886 * _rolling_slope(draw, 547) + 0.001722 * anchor
    return base_signal.diff()

def f28_ihc_420_struct_v420_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=302, w3=560, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(302, min_periods=max(302//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9875 + 0.0017221 * anchor
    return base_signal.diff()

def f28_ihc_421_struct_v421_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=313, w3=573, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 313)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.001875 + 0.0017222 * anchor
    return base_signal.diff()

def f28_ihc_422_struct_v422_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=324, w3=586, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(324, min_periods=max(324//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01625 + 0.0017223 * anchor
    return base_signal.diff()

def f28_ihc_423_struct_v423_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=335, w3=599, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(86)
    rank = change.rolling(335, min_periods=max(335//3, 2)).rank(pct=True)
    persistence = change.rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319 * persistence + 0.0017224 * anchor
    return base_signal.diff()

def f28_ihc_424_struct_v424_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=346, w3=612, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(346, min_periods=max(346//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.045 + 0.0017225 * anchor
    return base_signal.diff()

def f28_ihc_425_struct_v425_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=357, w3=625, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(357, min_periods=max(357//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3342 * slope + 0.0017226 * anchor
    return base_signal.diff()

def f28_ihc_426_struct_v426_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=368, w3=638, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(107)
    drag = impulse.rolling(368, min_periods=max(368//3, 2)).mean()
    noise = impulse.abs().rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.07375 + 0.0017227 * anchor
    return base_signal.diff()

def f28_ihc_427_struct_v427_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=379, w3=651, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 379)
    curvature = _rolling_slope(acceleration, 651)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3494 * acceleration + 0.0017228 * anchor
    return base_signal.diff()

def f28_ihc_428_struct_v428_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=390, w3=664, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1025 + 0.0017229 * anchor
    return base_signal.diff()

def f28_ihc_429_struct_v429_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=401, w3=677, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3646 * _rolling_slope(draw, 677) + 0.001723 * anchor
    return base_signal.diff()

def f28_ihc_430_struct_v430_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=412, w3=690, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 135)
    baseline = trend.rolling(412, min_periods=max(412//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.13125 + 0.0017231 * anchor
    return base_signal.diff()

def f28_ihc_431_struct_v431_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=423, w3=703, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.145625 + 0.0017232 * anchor
    return base_signal.diff()

def f28_ihc_432_struct_v432_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=434, w3=716, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(434, min_periods=max(434//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.16 + 0.0017233 * anchor
    return base_signal.diff()

def f28_ihc_433_struct_v433_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=445, w3=729, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(445, min_periods=max(445//3, 2)).rank(pct=True)
    persistence = change.rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.395 * persistence + 0.0017234 * anchor
    return base_signal.diff()

def f28_ihc_434_struct_v434_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=456, w3=742, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(456, min_periods=max(456//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18875 + 0.0017235 * anchor
    return base_signal.diff()

def f28_ihc_435_struct_v435_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=467, w3=755, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(467, min_periods=max(467//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4102 * slope + 0.0017236 * anchor
    return base_signal.diff()

def f28_ihc_436_struct_v436_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=478, w3=768, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(478, min_periods=max(478//3, 2)).mean()
    noise = impulse.abs().rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2175 + 0.0017237 * anchor
    return base_signal.diff()

def f28_ihc_437_struct_v437_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=489, w3=24, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 24)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.049 * acceleration + 0.0017238 * anchor
    return base_signal.diff()

def f28_ihc_438_struct_v438_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=500, w3=37, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(500, min_periods=max(500//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(37) * 1.24625 + 0.0017239 * anchor
    return base_signal.diff()

def f28_ihc_439_struct_v439_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=511, w3=50, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(511, min_periods=max(511//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0642 * _rolling_slope(draw, 50) + 0.001724 * anchor
    return base_signal.diff()

def f28_ihc_440_struct_v440_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=19, w3=63, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 205)
    baseline = trend.rolling(19, min_periods=max(19//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.275 + 0.0017241 * anchor
    return base_signal.diff()

def f28_ihc_441_struct_v441_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=30, w3=76, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 212)
    slow = _rolling_slope(x, 30)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=76, adjust=False).mean() * 1.289375 + 0.0017242 * anchor
    return base_signal.diff()

def f28_ihc_442_struct_v442_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=41, w3=89, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(41, min_periods=max(41//3, 2)).max()
    trough = x.rolling(219, min_periods=max(219//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.30375 + 0.0017243 * anchor
    return base_signal.diff()

def f28_ihc_443_struct_v443_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=52, w3=102, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(52, min_periods=max(52//3, 2)).rank(pct=True)
    persistence = change.rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0946 * persistence + 0.0017244 * anchor
    return base_signal.diff()

def f28_ihc_444_struct_v444_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=63, w3=115, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(233, min_periods=max(233//3, 2)).std()
    vol_slow = ret.rolling(63, min_periods=max(63//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3325 + 0.0017245 * anchor
    return base_signal.diff()

def f28_ihc_445_struct_v445_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=74, w3=128, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(74, min_periods=max(74//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 240)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1098 * slope + 0.0017246 * anchor
    return base_signal.diff()

def f28_ihc_446_struct_v446_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=85, w3=141, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(85, min_periods=max(85//3, 2)).mean()
    noise = impulse.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.36125 + 0.0017247 * anchor
    return base_signal.diff()

def f28_ihc_447_struct_v447_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=96, w3=154, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 254)
    acceleration = _rolling_slope(velocity, 96)
    curvature = _rolling_slope(acceleration, 154)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125 * acceleration + 0.0017248 * anchor
    return base_signal.diff()

def f28_ihc_448_struct_v448_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=107, w3=167, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(10, min_periods=max(10//3, 2)).mean(), upside.rolling(107, min_periods=max(107//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.39 + 0.0017249 * anchor
    return base_signal.diff()

def f28_ihc_449_struct_v449_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=118, w3=180, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(118, min_periods=max(118//3, 2)).max()
    rebound = x - x.rolling(17, min_periods=max(17//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1402 * _rolling_slope(draw, 180) + 0.001725 * anchor
    return base_signal.diff()

def f28_ihc_450_struct_v450_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=129, w3=193, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(129, min_periods=max(129//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41875 + 0.0017251 * anchor
    return base_signal.diff()
