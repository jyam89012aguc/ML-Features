"""71 altman z distress kinetics d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f71_zscr_376_struct_v376_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=56, w2=322, w3=765, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(56)
    drag = impulse.rolling(322, min_periods=max(322//3, 2)).mean()
    noise = impulse.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.243125 + 0.0036977 * anchor
    return base_signal.diff()

def f71_zscr_377_struct_v377_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=63, w2=333, w3=21, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 21)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2658 * acceleration + 0.0036978 * anchor
    return base_signal.diff()

def f71_zscr_378_struct_v378_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=70, w2=344, w3=34, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(344, min_periods=max(344//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(34) * 1.271875 + 0.0036979 * anchor
    return base_signal.diff()

def f71_zscr_379_struct_v379_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=77, w2=355, w3=47, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(355, min_periods=max(355//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.281 * _rolling_slope(draw, 47) + 0.003698 * anchor
    return base_signal.diff()

def f71_zscr_380_struct_v380_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=84, w2=366, w3=60, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(366, min_periods=max(366//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.300625 + 0.0036981 * anchor
    return base_signal.diff()

def f71_zscr_381_struct_v381_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=91, w2=377, w3=73, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=73, adjust=False).mean() * 1.315 + 0.0036982 * anchor
    return base_signal.diff()

def f71_zscr_382_struct_v382_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=98, w2=388, w3=86, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(388, min_periods=max(388//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.329375 + 0.0036983 * anchor
    return base_signal.diff()

def f71_zscr_383_struct_v383_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=105, w2=399, w3=99, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(105)
    rank = change.rolling(399, min_periods=max(399//3, 2)).rank(pct=True)
    persistence = change.rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3114 * persistence + 0.0036984 * anchor
    return base_signal.diff()

def f71_zscr_384_struct_v384_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=112, w2=410, w3=112, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(410, min_periods=max(410//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.358125 + 0.0036985 * anchor
    return base_signal.diff()

def f71_zscr_385_struct_v385_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=119, w2=421, w3=125, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3266 * slope + 0.0036986 * anchor
    return base_signal.diff()

def f71_zscr_386_struct_v386_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=126, w2=432, w3=138, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(432, min_periods=max(432//3, 2)).mean()
    noise = impulse.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.386875 + 0.0036987 * anchor
    return base_signal.diff()

def f71_zscr_387_struct_v387_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=133, w2=443, w3=151, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 151)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3418 * acceleration + 0.0036988 * anchor
    return base_signal.diff()

def f71_zscr_388_struct_v388_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=140, w2=454, w3=164, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(454, min_periods=max(454//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.415625 + 0.0036989 * anchor
    return base_signal.diff()

def f71_zscr_389_struct_v389_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=147, w2=465, w3=177, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(465, min_periods=max(465//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.357 * _rolling_slope(draw, 177) + 0.003699 * anchor
    return base_signal.diff()

def f71_zscr_390_struct_v390_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=154, w2=476, w3=190, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(476, min_periods=max(476//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.444375 + 0.0036991 * anchor
    return base_signal.diff()

def f71_zscr_391_struct_v391_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=161, w2=487, w3=203, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 487)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=203, adjust=False).mean() * 1.45875 + 0.0036992 * anchor
    return base_signal.diff()

def f71_zscr_392_struct_v392_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=498, w3=216, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(498, min_periods=max(498//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.473125 + 0.0036993 * anchor
    return base_signal.diff()

def f71_zscr_393_struct_v393_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=509, w3=229, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3874 * persistence + 0.0036994 * anchor
    return base_signal.diff()

def f71_zscr_394_struct_v394_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=17, w3=242, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(17, min_periods=max(17//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.501875 + 0.0036995 * anchor
    return base_signal.diff()

def f71_zscr_395_struct_v395_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=28, w3=255, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4026 * slope + 0.0036996 * anchor
    return base_signal.diff()

def f71_zscr_396_struct_v396_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=39, w3=268, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(39, min_periods=max(39//3, 2)).mean()
    noise = impulse.abs().rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.530625 + 0.0036997 * anchor
    return base_signal.diff()

def f71_zscr_397_struct_v397_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=50, w3=281, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 50)
    curvature = _rolling_slope(acceleration, 281)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0414 * acceleration + 0.0036998 * anchor
    return base_signal.diff()

def f71_zscr_398_struct_v398_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=61, w3=294, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(61, min_periods=max(61//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.559375 + 0.0036999 * anchor
    return base_signal.diff()

def f71_zscr_399_struct_v399_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=72, w3=307, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(72, min_periods=max(72//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0566 * _rolling_slope(draw, 307) + 0.0037 * anchor
    return base_signal.diff()

def f71_zscr_400_struct_v400_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=83, w3=320, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.588125 + 0.0037001 * anchor
    return base_signal.diff()

def f71_zscr_401_struct_v401_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=94, w3=333, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.6025 + 0.0037002 * anchor
    return base_signal.diff()

def f71_zscr_402_struct_v402_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=105, w3=346, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.616875 + 0.0037003 * anchor
    return base_signal.diff()

def f71_zscr_403_struct_v403_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=116, w3=359, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(116, min_periods=max(116//3, 2)).rank(pct=True)
    persistence = change.rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087 * persistence + 0.0037004 * anchor
    return base_signal.diff()

def f71_zscr_404_struct_v404_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=127, w3=372, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(252, min_periods=max(252//3, 2)).std()
    vol_slow = ret.rolling(127, min_periods=max(127//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8725 + 0.0037005 * anchor
    return base_signal.diff()

def f71_zscr_405_struct_v405_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=138, w3=385, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(138, min_periods=max(138//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1022 * slope + 0.0037006 * anchor
    return base_signal.diff()

def f71_zscr_406_struct_v406_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=149, w3=398, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(15)
    drag = impulse.rolling(149, min_periods=max(149//3, 2)).mean()
    noise = impulse.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.90125 + 0.0037007 * anchor
    return base_signal.diff()

def f71_zscr_407_struct_v407_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=160, w3=411, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 160)
    curvature = _rolling_slope(acceleration, 411)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1174 * acceleration + 0.0037008 * anchor
    return base_signal.diff()

def f71_zscr_408_struct_v408_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=171, w3=424, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93 + 0.0037009 * anchor
    return base_signal.diff()

def f71_zscr_409_struct_v409_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=182, w3=437, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(182, min_periods=max(182//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1326 * _rolling_slope(draw, 437) + 0.003701 * anchor
    return base_signal.diff()

def f71_zscr_410_struct_v410_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=193, w3=450, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(193, min_periods=max(193//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.95875 + 0.0037011 * anchor
    return base_signal.diff()

def f71_zscr_411_struct_v411_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=204, w3=463, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 204)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.973125 + 0.0037012 * anchor
    return base_signal.diff()

def f71_zscr_412_struct_v412_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=215, w3=476, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(215, min_periods=max(215//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9875 + 0.0037013 * anchor
    return base_signal.diff()

def f71_zscr_413_struct_v413_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=226, w3=489, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(64)
    rank = change.rolling(226, min_periods=max(226//3, 2)).rank(pct=True)
    persistence = change.rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.163 * persistence + 0.0037014 * anchor
    return base_signal.diff()

def f71_zscr_414_struct_v414_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=237, w3=502, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(237, min_periods=max(237//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01625 + 0.0037015 * anchor
    return base_signal.diff()

def f71_zscr_415_struct_v415_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=248, w3=515, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(248, min_periods=max(248//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1782 * slope + 0.0037016 * anchor
    return base_signal.diff()

def f71_zscr_416_struct_v416_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=259, w3=528, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(85)
    drag = impulse.rolling(259, min_periods=max(259//3, 2)).mean()
    noise = impulse.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.045 + 0.0037017 * anchor
    return base_signal.diff()

def f71_zscr_417_struct_v417_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=270, w3=541, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 541)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1934 * acceleration + 0.0037018 * anchor
    return base_signal.diff()

def f71_zscr_418_struct_v418_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=281, w3=554, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(281, min_periods=max(281//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.07375 + 0.0037019 * anchor
    return base_signal.diff()

def f71_zscr_419_struct_v419_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=292, w3=567, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(106, min_periods=max(106//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2086 * _rolling_slope(draw, 567) + 0.003702 * anchor
    return base_signal.diff()

def f71_zscr_420_struct_v420_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=303, w3=580, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 113)
    baseline = trend.rolling(303, min_periods=max(303//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(580, min_periods=max(580//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1025 + 0.0037021 * anchor
    return base_signal.diff()

def f71_zscr_421_struct_v421_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=314, w3=593, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 314)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.116875 + 0.0037022 * anchor
    return base_signal.diff()

def f71_zscr_422_struct_v422_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=325, w3=606, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(325, min_periods=max(325//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.13125 + 0.0037023 * anchor
    return base_signal.diff()

def f71_zscr_423_struct_v423_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=336, w3=619, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(336, min_periods=max(336//3, 2)).rank(pct=True)
    persistence = change.rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.239 * persistence + 0.0037024 * anchor
    return base_signal.diff()

def f71_zscr_424_struct_v424_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=347, w3=632, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(347, min_periods=max(347//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16 + 0.0037025 * anchor
    return base_signal.diff()

def f71_zscr_425_struct_v425_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=358, w3=645, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(358, min_periods=max(358//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2542 * slope + 0.0037026 * anchor
    return base_signal.diff()

def f71_zscr_426_struct_v426_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=369, w3=658, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(369, min_periods=max(369//3, 2)).mean()
    noise = impulse.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.18875 + 0.0037027 * anchor
    return base_signal.diff()

def f71_zscr_427_struct_v427_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=380, w3=671, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 380)
    curvature = _rolling_slope(acceleration, 671)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2694 * acceleration + 0.0037028 * anchor
    return base_signal.diff()

def f71_zscr_428_struct_v428_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=391, w3=684, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(391, min_periods=max(391//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2175 + 0.0037029 * anchor
    return base_signal.diff()

def f71_zscr_429_struct_v429_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=402, w3=697, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(402, min_periods=max(402//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2846 * _rolling_slope(draw, 697) + 0.003703 * anchor
    return base_signal.diff()

def f71_zscr_430_struct_v430_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=413, w3=710, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(413, min_periods=max(413//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24625 + 0.0037031 * anchor
    return base_signal.diff()

def f71_zscr_431_struct_v431_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=424, w3=723, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 424)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.260625 + 0.0037032 * anchor
    return base_signal.diff()

def f71_zscr_432_struct_v432_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=435, w3=736, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(435, min_periods=max(435//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.275 + 0.0037033 * anchor
    return base_signal.diff()

def f71_zscr_433_struct_v433_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=446, w3=749, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(446, min_periods=max(446//3, 2)).rank(pct=True)
    persistence = change.rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.315 * persistence + 0.0037034 * anchor
    return base_signal.diff()

def f71_zscr_434_struct_v434_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=457, w3=762, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(457, min_periods=max(457//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30375 + 0.0037035 * anchor
    return base_signal.diff()

def f71_zscr_435_struct_v435_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=468, w3=18, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(468, min_periods=max(468//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3302 * slope + 0.0037036 * anchor
    return base_signal.diff()

def f71_zscr_436_struct_v436_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=479, w3=31, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(479, min_periods=max(479//3, 2)).mean()
    noise = impulse.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3325 + 0.0037037 * anchor
    return base_signal.diff()

def f71_zscr_437_struct_v437_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=490, w3=44, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 490)
    curvature = _rolling_slope(acceleration, 44)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3454 * acceleration + 0.0037038 * anchor
    return base_signal.diff()

def f71_zscr_438_struct_v438_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=501, w3=57, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(501, min_periods=max(501//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(57) * 1.36125 + 0.0037039 * anchor
    return base_signal.diff()

def f71_zscr_439_struct_v439_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=512, w3=70, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(512, min_periods=max(512//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3606 * _rolling_slope(draw, 70) + 0.003704 * anchor
    return base_signal.diff()

def f71_zscr_440_struct_v440_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=20, w3=83, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(20, min_periods=max(20//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.39 + 0.0037041 * anchor
    return base_signal.diff()

def f71_zscr_441_struct_v441_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=31, w3=96, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 31)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=96, adjust=False).mean() * 1.404375 + 0.0037042 * anchor
    return base_signal.diff()

def f71_zscr_442_struct_v442_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=42, w3=109, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(42, min_periods=max(42//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.41875 + 0.0037043 * anchor
    return base_signal.diff()

def f71_zscr_443_struct_v443_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=53, w3=122, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(23)
    rank = change.rolling(53, min_periods=max(53//3, 2)).rank(pct=True)
    persistence = change.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.391 * persistence + 0.0037044 * anchor
    return base_signal.diff()

def f71_zscr_444_struct_v444_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=64, w3=135, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(64, min_periods=max(64//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4475 + 0.0037045 * anchor
    return base_signal.diff()

def f71_zscr_445_struct_v445_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=75, w3=148, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(75, min_periods=max(75//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4062 * slope + 0.0037046 * anchor
    return base_signal.diff()

def f71_zscr_446_struct_v446_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=86, w3=161, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(44)
    drag = impulse.rolling(86, min_periods=max(86//3, 2)).mean()
    noise = impulse.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47625 + 0.0037047 * anchor
    return base_signal.diff()

def f71_zscr_447_struct_v447_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=97, w3=174, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 97)
    curvature = _rolling_slope(acceleration, 174)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045 * acceleration + 0.0037048 * anchor
    return base_signal.diff()

def f71_zscr_448_struct_v448_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=108, w3=187, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(108, min_periods=max(108//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.505 + 0.0037049 * anchor
    return base_signal.diff()

def f71_zscr_449_struct_v449_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=119, w3=200, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(119, min_periods=max(119//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0602 * _rolling_slope(draw, 200) + 0.003705 * anchor
    return base_signal.diff()

def f71_zscr_450_struct_v450_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=130, w3=213, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.53375 + 0.0037051 * anchor
    return base_signal.diff()
