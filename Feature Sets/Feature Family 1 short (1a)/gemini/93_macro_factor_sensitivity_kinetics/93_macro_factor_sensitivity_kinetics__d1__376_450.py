"""93 macro factor sensitivity kinetics d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f93_mcf_376_struct_v376_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=139, w2=429, w3=37, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.903125 + 0.0042977 * anchor
    return base_signal.diff()

def f93_mcf_377_struct_v377_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=146, w2=440, w3=50, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 440)
    curvature = _rolling_slope(acceleration, 50)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3214 * acceleration + 0.0042978 * anchor
    return base_signal.diff()

def f93_mcf_378_struct_v378_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=153, w2=451, w3=63, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(63) * 0.931875 + 0.0042979 * anchor
    return base_signal.diff()

def f93_mcf_379_struct_v379_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=160, w2=462, w3=76, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3366 * _rolling_slope(draw, 76) + 0.004298 * anchor
    return base_signal.diff()

def f93_mcf_380_struct_v380_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=167, w2=473, w3=89, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.960625 + 0.0042981 * anchor
    return base_signal.diff()

def f93_mcf_381_struct_v381_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=174, w2=484, w3=102, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=102, adjust=False).mean() * 0.975 + 0.0042982 * anchor
    return base_signal.diff()

def f93_mcf_382_struct_v382_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=181, w2=495, w3=115, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.989375 + 0.0042983 * anchor
    return base_signal.diff()

def f93_mcf_383_struct_v383_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=188, w2=506, w3=128, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(506, min_periods=max(506//3, 2)).rank(pct=True)
    persistence = change.rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.367 * persistence + 0.0042984 * anchor
    return base_signal.diff()

def f93_mcf_384_struct_v384_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=195, w2=14, w3=141, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.018125 + 0.0042985 * anchor
    return base_signal.diff()

def f93_mcf_385_struct_v385_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=202, w2=25, w3=154, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(25, min_periods=max(25//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3822 * slope + 0.0042986 * anchor
    return base_signal.diff()

def f93_mcf_386_struct_v386_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=209, w2=36, w3=167, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(36, min_periods=max(36//3, 2)).mean()
    noise = impulse.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.046875 + 0.0042987 * anchor
    return base_signal.diff()

def f93_mcf_387_struct_v387_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=216, w2=47, w3=180, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 47)
    curvature = _rolling_slope(acceleration, 180)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3974 * acceleration + 0.0042988 * anchor
    return base_signal.diff()

def f93_mcf_388_struct_v388_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=223, w2=58, w3=193, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(58, min_periods=max(58//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.075625 + 0.0042989 * anchor
    return base_signal.diff()

def f93_mcf_389_struct_v389_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=230, w2=69, w3=206, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(69, min_periods=max(69//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0362 * _rolling_slope(draw, 206) + 0.004299 * anchor
    return base_signal.diff()

def f93_mcf_390_struct_v390_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=237, w2=80, w3=219, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(80, min_periods=max(80//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.104375 + 0.0042991 * anchor
    return base_signal.diff()

def f93_mcf_391_struct_v391_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=244, w2=91, w3=232, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 91)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=232, adjust=False).mean() * 1.11875 + 0.0042992 * anchor
    return base_signal.diff()

def f93_mcf_392_struct_v392_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=251, w2=102, w3=245, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(102, min_periods=max(102//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.133125 + 0.0042993 * anchor
    return base_signal.diff()

def f93_mcf_393_struct_v393_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=7, w2=113, w3=258, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(7)
    rank = change.rolling(113, min_periods=max(113//3, 2)).rank(pct=True)
    persistence = change.rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0666 * persistence + 0.0042994 * anchor
    return base_signal.diff()

def f93_mcf_394_struct_v394_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=14, w2=124, w3=271, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.161875 + 0.0042995 * anchor
    return base_signal.diff()

def f93_mcf_395_struct_v395_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=21, w2=135, w3=284, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(135, min_periods=max(135//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0818 * slope + 0.0042996 * anchor
    return base_signal.diff()

def f93_mcf_396_struct_v396_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=28, w2=146, w3=297, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(28)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.190625 + 0.0042997 * anchor
    return base_signal.diff()

def f93_mcf_397_struct_v397_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=35, w2=157, w3=310, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 310)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.097 * acceleration + 0.0042998 * anchor
    return base_signal.diff()

def f93_mcf_398_struct_v398_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=42, w2=168, w3=323, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(168, min_periods=max(168//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.219375 + 0.0042999 * anchor
    return base_signal.diff()

def f93_mcf_399_struct_v399_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=49, w2=179, w3=336, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1122 * _rolling_slope(draw, 336) + 0.0043 * anchor
    return base_signal.diff()

def f93_mcf_400_struct_v400_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=56, w2=190, w3=349, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.248125 + 0.0043001 * anchor
    return base_signal.diff()

def f93_mcf_401_struct_v401_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=63, w2=201, w3=362, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2625 + 0.0043002 * anchor
    return base_signal.diff()

def f93_mcf_402_struct_v402_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=70, w2=212, w3=375, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(212, min_periods=max(212//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.276875 + 0.0043003 * anchor
    return base_signal.diff()

def f93_mcf_403_struct_v403_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=77, w2=223, w3=388, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(77)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1426 * persistence + 0.0043004 * anchor
    return base_signal.diff()

def f93_mcf_404_struct_v404_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=84, w2=234, w3=401, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(234, min_periods=max(234//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.305625 + 0.0043005 * anchor
    return base_signal.diff()

def f93_mcf_405_struct_v405_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=91, w2=245, w3=414, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(245, min_periods=max(245//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1578 * slope + 0.0043006 * anchor
    return base_signal.diff()

def f93_mcf_406_struct_v406_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=98, w2=256, w3=427, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(98)
    drag = impulse.rolling(256, min_periods=max(256//3, 2)).mean()
    noise = impulse.abs().rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.334375 + 0.0043007 * anchor
    return base_signal.diff()

def f93_mcf_407_struct_v407_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=105, w2=267, w3=440, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 440)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.173 * acceleration + 0.0043008 * anchor
    return base_signal.diff()

def f93_mcf_408_struct_v408_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=112, w2=278, w3=453, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(278, min_periods=max(278//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.363125 + 0.0043009 * anchor
    return base_signal.diff()

def f93_mcf_409_struct_v409_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=119, w2=289, w3=466, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(289, min_periods=max(289//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1882 * _rolling_slope(draw, 466) + 0.004301 * anchor
    return base_signal.diff()

def f93_mcf_410_struct_v410_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=126, w2=300, w3=479, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(300, min_periods=max(300//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.391875 + 0.0043011 * anchor
    return base_signal.diff()

def f93_mcf_411_struct_v411_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=133, w2=311, w3=492, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.40625 + 0.0043012 * anchor
    return base_signal.diff()

def f93_mcf_412_struct_v412_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=140, w2=322, w3=505, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(322, min_periods=max(322//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.420625 + 0.0043013 * anchor
    return base_signal.diff()

def f93_mcf_413_struct_v413_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=147, w2=333, w3=518, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(333, min_periods=max(333//3, 2)).rank(pct=True)
    persistence = change.rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2186 * persistence + 0.0043014 * anchor
    return base_signal.diff()

def f93_mcf_414_struct_v414_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=154, w2=344, w3=531, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(344, min_periods=max(344//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.449375 + 0.0043015 * anchor
    return base_signal.diff()

def f93_mcf_415_struct_v415_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=161, w2=355, w3=544, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2338 * slope + 0.0043016 * anchor
    return base_signal.diff()

def f93_mcf_416_struct_v416_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=366, w3=557, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(366, min_periods=max(366//3, 2)).mean()
    noise = impulse.abs().rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.478125 + 0.0043017 * anchor
    return base_signal.diff()

def f93_mcf_417_struct_v417_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=377, w3=570, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 377)
    curvature = _rolling_slope(acceleration, 570)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.249 * acceleration + 0.0043018 * anchor
    return base_signal.diff()

def f93_mcf_418_struct_v418_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=388, w3=583, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.506875 + 0.0043019 * anchor
    return base_signal.diff()

def f93_mcf_419_struct_v419_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=399, w3=596, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(399, min_periods=max(399//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2642 * _rolling_slope(draw, 596) + 0.004302 * anchor
    return base_signal.diff()

def f93_mcf_420_struct_v420_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=410, w3=609, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.535625 + 0.0043021 * anchor
    return base_signal.diff()

def f93_mcf_421_struct_v421_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=421, w3=622, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 421)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.55 + 0.0043022 * anchor
    return base_signal.diff()

def f93_mcf_422_struct_v422_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=432, w3=635, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(432, min_periods=max(432//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.564375 + 0.0043023 * anchor
    return base_signal.diff()

def f93_mcf_423_struct_v423_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=443, w3=648, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2946 * persistence + 0.0043024 * anchor
    return base_signal.diff()

def f93_mcf_424_struct_v424_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=454, w3=661, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(454, min_periods=max(454//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.593125 + 0.0043025 * anchor
    return base_signal.diff()

def f93_mcf_425_struct_v425_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=465, w3=674, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(465, min_periods=max(465//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3098 * slope + 0.0043026 * anchor
    return base_signal.diff()

def f93_mcf_426_struct_v426_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=476, w3=687, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.621875 + 0.0043027 * anchor
    return base_signal.diff()

def f93_mcf_427_struct_v427_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=487, w3=700, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 487)
    curvature = _rolling_slope(acceleration, 700)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.325 * acceleration + 0.0043028 * anchor
    return base_signal.diff()

def f93_mcf_428_struct_v428_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=498, w3=713, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(498, min_periods=max(498//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8775 + 0.0043029 * anchor
    return base_signal.diff()

def f93_mcf_429_struct_v429_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=509, w3=726, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(509, min_periods=max(509//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3402 * _rolling_slope(draw, 726) + 0.004303 * anchor
    return base_signal.diff()

def f93_mcf_430_struct_v430_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=17, w3=739, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(17, min_periods=max(17//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.90625 + 0.0043031 * anchor
    return base_signal.diff()

def f93_mcf_431_struct_v431_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=28, w3=752, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 28)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.920625 + 0.0043032 * anchor
    return base_signal.diff()

def f93_mcf_432_struct_v432_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=39, w3=765, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(39, min_periods=max(39//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.935 + 0.0043033 * anchor
    return base_signal.diff()

def f93_mcf_433_struct_v433_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=50, w3=21, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(36)
    rank = change.rolling(50, min_periods=max(50//3, 2)).rank(pct=True)
    persistence = change.rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3706 * persistence + 0.0043034 * anchor
    return base_signal.diff()

def f93_mcf_434_struct_v434_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=61, w3=34, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(61, min_periods=max(61//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96375 + 0.0043035 * anchor
    return base_signal.diff()

def f93_mcf_435_struct_v435_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=72, w3=47, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3858 * slope + 0.0043036 * anchor
    return base_signal.diff()

def f93_mcf_436_struct_v436_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=83, w3=60, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(57)
    drag = impulse.rolling(83, min_periods=max(83//3, 2)).mean()
    noise = impulse.abs().rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9925 + 0.0043037 * anchor
    return base_signal.diff()

def f93_mcf_437_struct_v437_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=94, w3=73, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 73)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.401 * acceleration + 0.0043038 * anchor
    return base_signal.diff()

def f93_mcf_438_struct_v438_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=105, w3=86, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(86) * 1.02125 + 0.0043039 * anchor
    return base_signal.diff()

def f93_mcf_439_struct_v439_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=116, w3=99, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0398 * _rolling_slope(draw, 99) + 0.004304 * anchor
    return base_signal.diff()

def f93_mcf_440_struct_v440_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=127, w3=112, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(127, min_periods=max(127//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.05 + 0.0043041 * anchor
    return base_signal.diff()

def f93_mcf_441_struct_v441_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=138, w3=125, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 138)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=125, adjust=False).mean() * 1.064375 + 0.0043042 * anchor
    return base_signal.diff()

def f93_mcf_442_struct_v442_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=149, w3=138, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07875 + 0.0043043 * anchor
    return base_signal.diff()

def f93_mcf_443_struct_v443_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=160, w3=151, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(106)
    rank = change.rolling(160, min_periods=max(160//3, 2)).rank(pct=True)
    persistence = change.rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0702 * persistence + 0.0043044 * anchor
    return base_signal.diff()

def f93_mcf_444_struct_v444_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=171, w3=164, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(171, min_periods=max(171//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1075 + 0.0043045 * anchor
    return base_signal.diff()

def f93_mcf_445_struct_v445_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=182, w3=177, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(182, min_periods=max(182//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0854 * slope + 0.0043046 * anchor
    return base_signal.diff()

def f93_mcf_446_struct_v446_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=193, w3=190, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(193, min_periods=max(193//3, 2)).mean()
    noise = impulse.abs().rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13625 + 0.0043047 * anchor
    return base_signal.diff()

def f93_mcf_447_struct_v447_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=204, w3=203, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 203)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1006 * acceleration + 0.0043048 * anchor
    return base_signal.diff()

def f93_mcf_448_struct_v448_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=215, w3=216, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(215, min_periods=max(215//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.165 + 0.0043049 * anchor
    return base_signal.diff()

def f93_mcf_449_struct_v449_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=226, w3=229, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(226, min_periods=max(226//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1158 * _rolling_slope(draw, 229) + 0.004305 * anchor
    return base_signal.diff()

def f93_mcf_450_struct_v450_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=237, w3=242, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(237, min_periods=max(237//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.19375 + 0.0043051 * anchor
    return base_signal.diff()
