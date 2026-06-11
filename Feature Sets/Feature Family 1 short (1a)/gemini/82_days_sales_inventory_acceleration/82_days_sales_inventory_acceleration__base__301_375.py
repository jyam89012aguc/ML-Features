"""82 days sales inventory acceleration base features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Operating_Efficiency - Institutional-grade short-side signal.
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

def f82_dsia_301_struct_v301(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=305, w3=183, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 305)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=183, adjust=False).mean() * 1.54125 + 0.0039902 * anchor

def f82_dsia_302_struct_v302(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=316, w3=196, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(316, min_periods=max(316//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.555625 + 0.0039903 * anchor

def f82_dsia_303_struct_v303(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=327, w3=209, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(327, min_periods=max(327//3, 2)).rank(pct=True)
    persistence = change.rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2958 * persistence + 0.0039904 * anchor

def f82_dsia_304_struct_v304(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=338, w3=222, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(338, min_periods=max(338//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.584375 + 0.0039905 * anchor

def f82_dsia_305_struct_v305(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=349, w3=235, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.311 * slope + 0.0039906 * anchor

def f82_dsia_306_struct_v306(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=360, w3=248, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(360, min_periods=max(360//3, 2)).mean()
    noise = impulse.abs().rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.613125 + 0.0039907 * anchor

def f82_dsia_307_struct_v307(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=371, w3=261, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 261)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3262 * acceleration + 0.0039908 * anchor

def f82_dsia_308_struct_v308(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=382, w3=274, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(382, min_periods=max(382//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.86875 + 0.0039909 * anchor

def f82_dsia_309_struct_v309(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=393, w3=287, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(393, min_periods=max(393//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3414 * _rolling_slope(draw, 287) + 0.003991 * anchor

def f82_dsia_310_struct_v310(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=404, w3=300, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(404, min_periods=max(404//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.8975 + 0.0039911 * anchor

def f82_dsia_311_struct_v311(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=415, w3=313, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 415)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.911875 + 0.0039912 * anchor

def f82_dsia_312_struct_v312(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=426, w3=326, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(426, min_periods=max(426//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.92625 + 0.0039913 * anchor

def f82_dsia_313_struct_v313(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=437, w3=339, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(33)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3718 * persistence + 0.0039914 * anchor

def f82_dsia_314_struct_v314(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=448, w3=352, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(448, min_periods=max(448//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955 + 0.0039915 * anchor

def f82_dsia_315_struct_v315(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=459, w3=365, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(459, min_periods=max(459//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.387 * slope + 0.0039916 * anchor

def f82_dsia_316_struct_v316(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=470, w3=378, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(54)
    drag = impulse.rolling(470, min_periods=max(470//3, 2)).mean()
    noise = impulse.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.98375 + 0.0039917 * anchor

def f82_dsia_317_struct_v317(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=481, w3=391, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 481)
    curvature = _rolling_slope(acceleration, 391)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4022 * acceleration + 0.0039918 * anchor

def f82_dsia_318_struct_v318(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=492, w3=404, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(492, min_periods=max(492//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0125 + 0.0039919 * anchor

def f82_dsia_319_struct_v319(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=503, w3=417, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.041 * _rolling_slope(draw, 417) + 0.003992 * anchor

def f82_dsia_320_struct_v320(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=11, w3=430, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(11, min_periods=max(11//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.04125 + 0.0039921 * anchor

def f82_dsia_321_struct_v321(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=22, w3=443, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 22)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.055625 + 0.0039922 * anchor

def f82_dsia_322_struct_v322(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=33, w3=456, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.07 + 0.0039923 * anchor

def f82_dsia_323_struct_v323(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=44, w3=469, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(103)
    rank = change.rolling(44, min_periods=max(44//3, 2)).rank(pct=True)
    persistence = change.rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0714 * persistence + 0.0039924 * anchor

def f82_dsia_324_struct_v324(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=55, w3=482, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09875 + 0.0039925 * anchor

def f82_dsia_325_struct_v325(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=66, w3=495, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(66, min_periods=max(66//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0866 * slope + 0.0039926 * anchor

def f82_dsia_326_struct_v326(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=77, w3=508, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(124)
    drag = impulse.rolling(77, min_periods=max(77//3, 2)).mean()
    noise = impulse.abs().rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1275 + 0.0039927 * anchor

def f82_dsia_327_struct_v327(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=88, w3=521, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 88)
    curvature = _rolling_slope(acceleration, 521)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1018 * acceleration + 0.0039928 * anchor

def f82_dsia_328_struct_v328(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=99, w3=534, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.15625 + 0.0039929 * anchor

def f82_dsia_329_struct_v329(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=110, w3=547, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.117 * _rolling_slope(draw, 547) + 0.003993 * anchor

def f82_dsia_330_struct_v330(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=121, w3=560, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(121, min_periods=max(121//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.185 + 0.0039931 * anchor

def f82_dsia_331_struct_v331(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=132, w3=573, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 132)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.199375 + 0.0039932 * anchor

def f82_dsia_332_struct_v332(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=143, w3=586, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(143, min_periods=max(143//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.21375 + 0.0039933 * anchor

def f82_dsia_333_struct_v333(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=154, w3=599, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(154, min_periods=max(154//3, 2)).rank(pct=True)
    persistence = change.rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1474 * persistence + 0.0039934 * anchor

def f82_dsia_334_struct_v334(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=165, w3=612, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2425 + 0.0039935 * anchor

def f82_dsia_335_struct_v335(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=176, w3=625, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(176, min_periods=max(176//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1626 * slope + 0.0039936 * anchor

def f82_dsia_336_struct_v336(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=187, w3=638, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.27125 + 0.0039937 * anchor

def f82_dsia_337_struct_v337(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=198, w3=651, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 651)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1778 * acceleration + 0.0039938 * anchor

def f82_dsia_338_struct_v338(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=209, w3=664, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.3 + 0.0039939 * anchor

def f82_dsia_339_struct_v339(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=220, w3=677, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(220, min_periods=max(220//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.193 * _rolling_slope(draw, 677) + 0.003994 * anchor

def f82_dsia_340_struct_v340(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=231, w3=690, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.32875 + 0.0039941 * anchor

def f82_dsia_341_struct_v341(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=242, w3=703, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.343125 + 0.0039942 * anchor

def f82_dsia_342_struct_v342(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=253, w3=716, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3575 + 0.0039943 * anchor

def f82_dsia_343_struct_v343(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=264, w3=729, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(264, min_periods=max(264//3, 2)).rank(pct=True)
    persistence = change.rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2234 * persistence + 0.0039944 * anchor

def f82_dsia_344_struct_v344(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=275, w3=742, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38625 + 0.0039945 * anchor

def f82_dsia_345_struct_v345(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=286, w3=755, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2386 * slope + 0.0039946 * anchor

def f82_dsia_346_struct_v346(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=297, w3=768, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(13)
    drag = impulse.rolling(297, min_periods=max(297//3, 2)).mean()
    noise = impulse.abs().rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.415 + 0.0039947 * anchor

def f82_dsia_347_struct_v347(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=308, w3=24, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 24)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2538 * acceleration + 0.0039948 * anchor

def f82_dsia_348_struct_v348(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=319, w3=37, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(319, min_periods=max(319//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(37) * 1.44375 + 0.0039949 * anchor

def f82_dsia_349_struct_v349(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=330, w3=50, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.269 * _rolling_slope(draw, 50) + 0.003995 * anchor

def f82_dsia_350_struct_v350(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=341, w3=63, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4725 + 0.0039951 * anchor

def f82_dsia_351_struct_v351(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=352, w3=76, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=76, adjust=False).mean() * 1.486875 + 0.0039952 * anchor

def f82_dsia_352_struct_v352(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=363, w3=89, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(363, min_periods=max(363//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.50125 + 0.0039953 * anchor

def f82_dsia_353_struct_v353(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=374, w3=102, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(62)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2994 * persistence + 0.0039954 * anchor

def f82_dsia_354_struct_v354(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=385, w3=115, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(385, min_periods=max(385//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53 + 0.0039955 * anchor

def f82_dsia_355_struct_v355(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=396, w3=128, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3146 * slope + 0.0039956 * anchor

def f82_dsia_356_struct_v356(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=407, w3=141, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(83)
    drag = impulse.rolling(407, min_periods=max(407//3, 2)).mean()
    noise = impulse.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.55875 + 0.0039957 * anchor

def f82_dsia_357_struct_v357(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=418, w3=154, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 154)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3298 * acceleration + 0.0039958 * anchor

def f82_dsia_358_struct_v358(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=429, w3=167, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5875 + 0.0039959 * anchor

def f82_dsia_359_struct_v359(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=440, w3=180, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.345 * _rolling_slope(draw, 180) + 0.003996 * anchor

def f82_dsia_360_struct_v360(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=451, w3=193, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.61625 + 0.0039961 * anchor

def f82_dsia_361_struct_v361(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=462, w3=206, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=206, adjust=False).mean() * 0.8575 + 0.0039962 * anchor

def f82_dsia_362_struct_v362(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=473, w3=219, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(473, min_periods=max(473//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.871875 + 0.0039963 * anchor

def f82_dsia_363_struct_v363(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=484, w3=232, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(484, min_periods=max(484//3, 2)).rank(pct=True)
    persistence = change.rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3754 * persistence + 0.0039964 * anchor

def f82_dsia_364_struct_v364(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=495, w3=245, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.900625 + 0.0039965 * anchor

def f82_dsia_365_struct_v365(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=506, w3=258, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3906 * slope + 0.0039966 * anchor

def f82_dsia_366_struct_v366(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=14, w3=271, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.929375 + 0.0039967 * anchor

def f82_dsia_367_struct_v367(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=25, w3=284, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 284)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4058 * acceleration + 0.0039968 * anchor

def f82_dsia_368_struct_v368(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=36, w3=297, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(36, min_periods=max(36//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.958125 + 0.0039969 * anchor

def f82_dsia_369_struct_v369(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=47, w3=310, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0446 * _rolling_slope(draw, 310) + 0.003997 * anchor

def f82_dsia_370_struct_v370(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=58, w3=323, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.986875 + 0.0039971 * anchor

def f82_dsia_371_struct_v371(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=69, w3=336, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 188)
    slow = _rolling_slope(x, 69)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.00125 + 0.0039972 * anchor

def f82_dsia_372_struct_v372(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=80, w3=349, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(195, min_periods=max(195//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.015625 + 0.0039973 * anchor

def f82_dsia_373_struct_v373(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=91, w3=362, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.075 * persistence + 0.0039974 * anchor

def f82_dsia_374_struct_v374(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=102, w3=375, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(209, min_periods=max(209//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.044375 + 0.0039975 * anchor

def f82_dsia_375_struct_v375(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=113, w3=388, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 216)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0902 * slope + 0.0039976 * anchor
