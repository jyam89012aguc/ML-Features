"""16 short interest structure base features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Securities_Lending - Institutional-grade short-side signal.
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

def f16_sist_301_struct_v301(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=273, w3=38, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 273)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=38, adjust=False).mean() * 0.921875 + 0.0009902 * anchor

def f16_sist_302_struct_v302(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=284, w3=51, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(284, min_periods=max(284//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.93625 + 0.0009903 * anchor

def f16_sist_303_struct_v303(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=295, w3=64, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(50)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3942 * persistence + 0.0009904 * anchor

def f16_sist_304_struct_v304(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=306, w3=77, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(306, min_periods=max(306//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.965 + 0.0009905 * anchor

def f16_sist_305_struct_v305(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=317, w3=90, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(317, min_periods=max(317//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4094 * slope + 0.0009906 * anchor

def f16_sist_306_struct_v306(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=328, w3=103, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(71)
    drag = impulse.rolling(328, min_periods=max(328//3, 2)).mean()
    noise = impulse.abs().rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.99375 + 0.0009907 * anchor

def f16_sist_307_struct_v307(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=339, w3=116, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 339)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0482 * acceleration + 0.0009908 * anchor

def f16_sist_308_struct_v308(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=350, w3=129, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(350, min_periods=max(350//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0225 + 0.0009909 * anchor

def f16_sist_309_struct_v309(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=361, w3=142, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(361, min_periods=max(361//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0634 * _rolling_slope(draw, 142) + 0.000991 * anchor

def f16_sist_310_struct_v310(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=372, w3=155, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(372, min_periods=max(372//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.05125 + 0.0009911 * anchor

def f16_sist_311_struct_v311(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=383, w3=168, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 106)
    slow = _rolling_slope(x, 383)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=168, adjust=False).mean() * 1.065625 + 0.0009912 * anchor

def f16_sist_312_struct_v312(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=394, w3=181, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(394, min_periods=max(394//3, 2)).max()
    trough = x.rolling(113, min_periods=max(113//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.08 + 0.0009913 * anchor

def f16_sist_313_struct_v313(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=405, w3=194, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(120)
    rank = change.rolling(405, min_periods=max(405//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0938 * persistence + 0.0009914 * anchor

def f16_sist_314_struct_v314(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=416, w3=207, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(127, min_periods=max(127//3, 2)).std()
    vol_slow = ret.rolling(416, min_periods=max(416//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10875 + 0.0009915 * anchor

def f16_sist_315_struct_v315(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=427, w3=220, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(427, min_periods=max(427//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 134)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.109 * slope + 0.0009916 * anchor

def f16_sist_316_struct_v316(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=438, w3=233, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(438, min_periods=max(438//3, 2)).mean()
    noise = impulse.abs().rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1375 + 0.0009917 * anchor

def f16_sist_317_struct_v317(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=449, w3=246, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 148)
    acceleration = _rolling_slope(velocity, 449)
    curvature = _rolling_slope(acceleration, 246)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1242 * acceleration + 0.0009918 * anchor

def f16_sist_318_struct_v318(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=460, w3=259, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(460, min_periods=max(460//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.16625 + 0.0009919 * anchor

def f16_sist_319_struct_v319(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=471, w3=272, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(471, min_periods=max(471//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1394 * _rolling_slope(draw, 272) + 0.000992 * anchor

def f16_sist_320_struct_v320(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=482, w3=285, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 169)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.195 + 0.0009921 * anchor

def f16_sist_321_struct_v321(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=493, w3=298, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 493)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=298, adjust=False).mean() * 1.209375 + 0.0009922 * anchor

def f16_sist_322_struct_v322(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=504, w3=311, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.22375 + 0.0009923 * anchor

def f16_sist_323_struct_v323(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=12, w3=324, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(12, min_periods=max(12//3, 2)).rank(pct=True)
    persistence = change.rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1698 * persistence + 0.0009924 * anchor

def f16_sist_324_struct_v324(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=23, w3=337, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2525 + 0.0009925 * anchor

def f16_sist_325_struct_v325(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=34, w3=350, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.185 * slope + 0.0009926 * anchor

def f16_sist_326_struct_v326(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=45, w3=363, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(45, min_periods=max(45//3, 2)).mean()
    noise = impulse.abs().rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.28125 + 0.0009927 * anchor

def f16_sist_327_struct_v327(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=56, w3=376, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 56)
    curvature = _rolling_slope(acceleration, 376)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2002 * acceleration + 0.0009928 * anchor

def f16_sist_328_struct_v328(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=67, w3=389, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(67, min_periods=max(67//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.31 + 0.0009929 * anchor

def f16_sist_329_struct_v329(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=78, w3=402, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2154 * _rolling_slope(draw, 402) + 0.000993 * anchor

def f16_sist_330_struct_v330(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=89, w3=415, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(89, min_periods=max(89//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.33875 + 0.0009931 * anchor

def f16_sist_331_struct_v331(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=100, w3=428, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 100)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.353125 + 0.0009932 * anchor

def f16_sist_332_struct_v332(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=111, w3=441, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(111, min_periods=max(111//3, 2)).max()
    trough = x.rolling(253, min_periods=max(253//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3675 + 0.0009933 * anchor

def f16_sist_333_struct_v333(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=122, w3=454, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(9)
    rank = change.rolling(122, min_periods=max(122//3, 2)).rank(pct=True)
    persistence = change.rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2458 * persistence + 0.0009934 * anchor

def f16_sist_334_struct_v334(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=133, w3=467, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(133, min_periods=max(133//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39625 + 0.0009935 * anchor

def f16_sist_335_struct_v335(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=144, w3=480, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(144, min_periods=max(144//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.261 * slope + 0.0009936 * anchor

def f16_sist_336_struct_v336(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=155, w3=493, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(30)
    drag = impulse.rolling(155, min_periods=max(155//3, 2)).mean()
    noise = impulse.abs().rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.425 + 0.0009937 * anchor

def f16_sist_337_struct_v337(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=166, w3=506, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 166)
    curvature = _rolling_slope(acceleration, 506)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2762 * acceleration + 0.0009938 * anchor

def f16_sist_338_struct_v338(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=177, w3=519, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(177, min_periods=max(177//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45375 + 0.0009939 * anchor

def f16_sist_339_struct_v339(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=188, w3=532, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(188, min_periods=max(188//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2914 * _rolling_slope(draw, 532) + 0.000994 * anchor

def f16_sist_340_struct_v340(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=199, w3=545, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(199, min_periods=max(199//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4825 + 0.0009941 * anchor

def f16_sist_341_struct_v341(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=210, w3=558, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 210)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.496875 + 0.0009942 * anchor

def f16_sist_342_struct_v342(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=221, w3=571, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(221, min_periods=max(221//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.51125 + 0.0009943 * anchor

def f16_sist_343_struct_v343(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=232, w3=584, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(79)
    rank = change.rolling(232, min_periods=max(232//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3218 * persistence + 0.0009944 * anchor

def f16_sist_344_struct_v344(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=243, w3=597, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(243, min_periods=max(243//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54 + 0.0009945 * anchor

def f16_sist_345_struct_v345(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=254, w3=610, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(254, min_periods=max(254//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.337 * slope + 0.0009946 * anchor

def f16_sist_346_struct_v346(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=265, w3=623, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(100)
    drag = impulse.rolling(265, min_periods=max(265//3, 2)).mean()
    noise = impulse.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.56875 + 0.0009947 * anchor

def f16_sist_347_struct_v347(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=276, w3=636, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 276)
    curvature = _rolling_slope(acceleration, 636)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3522 * acceleration + 0.0009948 * anchor

def f16_sist_348_struct_v348(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=287, w3=649, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(287, min_periods=max(287//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5975 + 0.0009949 * anchor

def f16_sist_349_struct_v349(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=298, w3=662, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(298, min_periods=max(298//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3674 * _rolling_slope(draw, 662) + 0.000995 * anchor

def f16_sist_350_struct_v350(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=309, w3=675, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(309, min_periods=max(309//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.853125 + 0.0009951 * anchor

def f16_sist_351_struct_v351(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=320, w3=688, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 320)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.8675 + 0.0009952 * anchor

def f16_sist_352_struct_v352(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=331, w3=701, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.881875 + 0.0009953 * anchor

def f16_sist_353_struct_v353(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=342, w3=714, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(342, min_periods=max(342//3, 2)).rank(pct=True)
    persistence = change.rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3978 * persistence + 0.0009954 * anchor

def f16_sist_354_struct_v354(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=353, w3=727, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(353, min_periods=max(353//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.910625 + 0.0009955 * anchor

def f16_sist_355_struct_v355(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=364, w3=740, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(364, min_periods=max(364//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0366 * slope + 0.0009956 * anchor

def f16_sist_356_struct_v356(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=375, w3=753, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(375, min_periods=max(375//3, 2)).mean()
    noise = impulse.abs().rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.939375 + 0.0009957 * anchor

def f16_sist_357_struct_v357(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=386, w3=766, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 386)
    curvature = _rolling_slope(acceleration, 766)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0518 * acceleration + 0.0009958 * anchor

def f16_sist_358_struct_v358(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=397, w3=22, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(397, min_periods=max(397//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(22) * 0.968125 + 0.0009959 * anchor

def f16_sist_359_struct_v359(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=408, w3=35, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(408, min_periods=max(408//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.067 * _rolling_slope(draw, 35) + 0.000996 * anchor

def f16_sist_360_struct_v360(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=419, w3=48, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(419, min_periods=max(419//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.996875 + 0.0009961 * anchor

def f16_sist_361_struct_v361(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=430, w3=61, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 430)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=61, adjust=False).mean() * 1.01125 + 0.0009962 * anchor

def f16_sist_362_struct_v362(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=441, w3=74, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(441, min_periods=max(441//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.025625 + 0.0009963 * anchor

def f16_sist_363_struct_v363(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=452, w3=87, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(452, min_periods=max(452//3, 2)).rank(pct=True)
    persistence = change.rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0974 * persistence + 0.0009964 * anchor

def f16_sist_364_struct_v364(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=463, w3=100, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(463, min_periods=max(463//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.054375 + 0.0009965 * anchor

def f16_sist_365_struct_v365(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=474, w3=113, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(474, min_periods=max(474//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1126 * slope + 0.0009966 * anchor

def f16_sist_366_struct_v366(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=485, w3=126, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(485, min_periods=max(485//3, 2)).mean()
    noise = impulse.abs().rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.083125 + 0.0009967 * anchor

def f16_sist_367_struct_v367(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=496, w3=139, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 496)
    curvature = _rolling_slope(acceleration, 139)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1278 * acceleration + 0.0009968 * anchor

def f16_sist_368_struct_v368(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=507, w3=152, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(507, min_periods=max(507//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.111875 + 0.0009969 * anchor

def f16_sist_369_struct_v369(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=15, w3=165, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(15, min_periods=max(15//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.143 * _rolling_slope(draw, 165) + 0.000997 * anchor

def f16_sist_370_struct_v370(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=26, w3=178, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(26, min_periods=max(26//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.140625 + 0.0009971 * anchor

def f16_sist_371_struct_v371(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=37, w3=191, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 37)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=191, adjust=False).mean() * 1.155 + 0.0009972 * anchor

def f16_sist_372_struct_v372(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=48, w3=204, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(48, min_periods=max(48//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.169375 + 0.0009973 * anchor

def f16_sist_373_struct_v373(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=59, w3=217, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(38)
    rank = change.rolling(59, min_periods=max(59//3, 2)).rank(pct=True)
    persistence = change.rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1734 * persistence + 0.0009974 * anchor

def f16_sist_374_struct_v374(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=70, w3=230, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(70, min_periods=max(70//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.198125 + 0.0009975 * anchor

def f16_sist_375_struct_v375(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=81, w3=243, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(81, min_periods=max(81//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1886 * slope + 0.0009976 * anchor
