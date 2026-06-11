"""84 operating leverage reversal d1 first derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f84_olr_301_struct_v301_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=427, w3=643, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.009375 + 0.0041102 * anchor
    return base_signal.diff()

def f84_olr_302_struct_v302_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=438, w3=656, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(438, min_periods=max(438//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.02375 + 0.0041103 * anchor
    return base_signal.diff()

def f84_olr_303_struct_v303_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=449, w3=669, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(80)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3822 * persistence + 0.0041104 * anchor
    return base_signal.diff()

def f84_olr_304_struct_v304_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=460, w3=682, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(460, min_periods=max(460//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0525 + 0.0041105 * anchor
    return base_signal.diff()

def f84_olr_305_struct_v305_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=471, w3=695, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(471, min_periods=max(471//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3974 * slope + 0.0041106 * anchor
    return base_signal.diff()

def f84_olr_306_struct_v306_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=482, w3=708, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(101)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.08125 + 0.0041107 * anchor
    return base_signal.diff()

def f84_olr_307_struct_v307_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=493, w3=721, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 493)
    curvature = _rolling_slope(acceleration, 721)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0362 * acceleration + 0.0041108 * anchor
    return base_signal.diff()

def f84_olr_308_struct_v308_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=504, w3=734, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(504, min_periods=max(504//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.11 + 0.0041109 * anchor
    return base_signal.diff()

def f84_olr_309_struct_v309_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=12, w3=747, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(12, min_periods=max(12//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0514 * _rolling_slope(draw, 747) + 0.004111 * anchor
    return base_signal.diff()

def f84_olr_310_struct_v310_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=23, w3=760, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(23, min_periods=max(23//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.13875 + 0.0041111 * anchor
    return base_signal.diff()

def f84_olr_311_struct_v311_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=34, w3=16, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 34)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=16, adjust=False).mean() * 1.153125 + 0.0041112 * anchor
    return base_signal.diff()

def f84_olr_312_struct_v312_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=45, w3=29, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(45, min_periods=max(45//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1675 + 0.0041113 * anchor
    return base_signal.diff()

def f84_olr_313_struct_v313_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=56, w3=42, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(56, min_periods=max(56//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0818 * persistence + 0.0041114 * anchor
    return base_signal.diff()

def f84_olr_314_struct_v314_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=67, w3=55, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(67, min_periods=max(67//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.19625 + 0.0041115 * anchor
    return base_signal.diff()

def f84_olr_315_struct_v315_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=78, w3=68, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(78, min_periods=max(78//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.097 * slope + 0.0041116 * anchor
    return base_signal.diff()

def f84_olr_316_struct_v316_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=89, w3=81, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(89, min_periods=max(89//3, 2)).mean()
    noise = impulse.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.225 + 0.0041117 * anchor
    return base_signal.diff()

def f84_olr_317_struct_v317_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=100, w3=94, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 100)
    curvature = _rolling_slope(acceleration, 94)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1122 * acceleration + 0.0041118 * anchor
    return base_signal.diff()

def f84_olr_318_struct_v318_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=111, w3=107, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(111, min_periods=max(111//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(107) * 1.25375 + 0.0041119 * anchor
    return base_signal.diff()

def f84_olr_319_struct_v319_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=122, w3=120, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(122, min_periods=max(122//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1274 * _rolling_slope(draw, 120) + 0.004112 * anchor
    return base_signal.diff()

def f84_olr_320_struct_v320_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=133, w3=133, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2825 + 0.0041121 * anchor
    return base_signal.diff()

def f84_olr_321_struct_v321_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=144, w3=146, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=146, adjust=False).mean() * 1.296875 + 0.0041122 * anchor
    return base_signal.diff()

def f84_olr_322_struct_v322_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=155, w3=159, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.31125 + 0.0041123 * anchor
    return base_signal.diff()

def f84_olr_323_struct_v323_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=166, w3=172, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(166, min_periods=max(166//3, 2)).rank(pct=True)
    persistence = change.rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1578 * persistence + 0.0041124 * anchor
    return base_signal.diff()

def f84_olr_324_struct_v324_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=177, w3=185, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(177, min_periods=max(177//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34 + 0.0041125 * anchor
    return base_signal.diff()

def f84_olr_325_struct_v325_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=188, w3=198, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(188, min_periods=max(188//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.173 * slope + 0.0041126 * anchor
    return base_signal.diff()

def f84_olr_326_struct_v326_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=199, w3=211, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(199, min_periods=max(199//3, 2)).mean()
    noise = impulse.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.36875 + 0.0041127 * anchor
    return base_signal.diff()

def f84_olr_327_struct_v327_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=210, w3=224, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 210)
    curvature = _rolling_slope(acceleration, 224)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1882 * acceleration + 0.0041128 * anchor
    return base_signal.diff()

def f84_olr_328_struct_v328_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=221, w3=237, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(255, min_periods=max(255//3, 2)).mean(), upside.rolling(221, min_periods=max(221//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3975 + 0.0041129 * anchor
    return base_signal.diff()

def f84_olr_329_struct_v329_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=232, w3=250, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(232, min_periods=max(232//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2034 * _rolling_slope(draw, 250) + 0.004113 * anchor
    return base_signal.diff()

def f84_olr_330_struct_v330_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=243, w3=263, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(243, min_periods=max(243//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.42625 + 0.0041131 * anchor
    return base_signal.diff()

def f84_olr_331_struct_v331_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=254, w3=276, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 254)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=276, adjust=False).mean() * 1.440625 + 0.0041132 * anchor
    return base_signal.diff()

def f84_olr_332_struct_v332_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=265, w3=289, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(265, min_periods=max(265//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.455 + 0.0041133 * anchor
    return base_signal.diff()

def f84_olr_333_struct_v333_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=276, w3=302, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(39)
    rank = change.rolling(276, min_periods=max(276//3, 2)).rank(pct=True)
    persistence = change.rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2338 * persistence + 0.0041134 * anchor
    return base_signal.diff()

def f84_olr_334_struct_v334_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=287, w3=315, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(287, min_periods=max(287//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.48375 + 0.0041135 * anchor
    return base_signal.diff()

def f84_olr_335_struct_v335_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=298, w3=328, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(298, min_periods=max(298//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.249 * slope + 0.0041136 * anchor
    return base_signal.diff()

def f84_olr_336_struct_v336_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=309, w3=341, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(60)
    drag = impulse.rolling(309, min_periods=max(309//3, 2)).mean()
    noise = impulse.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5125 + 0.0041137 * anchor
    return base_signal.diff()

def f84_olr_337_struct_v337_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=320, w3=354, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 320)
    curvature = _rolling_slope(acceleration, 354)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2642 * acceleration + 0.0041138 * anchor
    return base_signal.diff()

def f84_olr_338_struct_v338_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=331, w3=367, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(74, min_periods=max(74//3, 2)).mean(), upside.rolling(331, min_periods=max(331//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.54125 + 0.0041139 * anchor
    return base_signal.diff()

def f84_olr_339_struct_v339_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=342, w3=380, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(342, min_periods=max(342//3, 2)).max()
    rebound = x - x.rolling(81, min_periods=max(81//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2794 * _rolling_slope(draw, 380) + 0.004114 * anchor
    return base_signal.diff()

def f84_olr_340_struct_v340_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=353, w3=393, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(353, min_periods=max(353//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.57 + 0.0041141 * anchor
    return base_signal.diff()

def f84_olr_341_struct_v341_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=364, w3=406, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 364)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.584375 + 0.0041142 * anchor
    return base_signal.diff()

def f84_olr_342_struct_v342_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=375, w3=419, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(375, min_periods=max(375//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.59875 + 0.0041143 * anchor
    return base_signal.diff()

def f84_olr_343_struct_v343_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=386, w3=432, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(109)
    rank = change.rolling(386, min_periods=max(386//3, 2)).rank(pct=True)
    persistence = change.rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3098 * persistence + 0.0041144 * anchor
    return base_signal.diff()

def f84_olr_344_struct_v344_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=397, w3=445, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.854375 + 0.0041145 * anchor
    return base_signal.diff()

def f84_olr_345_struct_v345_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=408, w3=458, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(408, min_periods=max(408//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.325 * slope + 0.0041146 * anchor
    return base_signal.diff()

def f84_olr_346_struct_v346_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=419, w3=471, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(419, min_periods=max(419//3, 2)).mean()
    noise = impulse.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.883125 + 0.0041147 * anchor
    return base_signal.diff()

def f84_olr_347_struct_v347_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=430, w3=484, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 430)
    curvature = _rolling_slope(acceleration, 484)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3402 * acceleration + 0.0041148 * anchor
    return base_signal.diff()

def f84_olr_348_struct_v348_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=441, w3=497, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(441, min_periods=max(441//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.911875 + 0.0041149 * anchor
    return base_signal.diff()

def f84_olr_349_struct_v349_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=452, w3=510, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3554 * _rolling_slope(draw, 510) + 0.004115 * anchor
    return base_signal.diff()

def f84_olr_350_struct_v350_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=463, w3=523, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(463, min_periods=max(463//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.940625 + 0.0041151 * anchor
    return base_signal.diff()

def f84_olr_351_struct_v351_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=474, w3=536, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.955 + 0.0041152 * anchor
    return base_signal.diff()

def f84_olr_352_struct_v352_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=485, w3=549, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(485, min_periods=max(485//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.969375 + 0.0041153 * anchor
    return base_signal.diff()

def f84_olr_353_struct_v353_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=496, w3=562, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3858 * persistence + 0.0041154 * anchor
    return base_signal.diff()

def f84_olr_354_struct_v354_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=507, w3=575, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(507, min_periods=max(507//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.998125 + 0.0041155 * anchor
    return base_signal.diff()

def f84_olr_355_struct_v355_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=15, w3=588, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(15, min_periods=max(15//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.401 * slope + 0.0041156 * anchor
    return base_signal.diff()

def f84_olr_356_struct_v356_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=26, w3=601, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(26, min_periods=max(26//3, 2)).mean()
    noise = impulse.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.026875 + 0.0041157 * anchor
    return base_signal.diff()

def f84_olr_357_struct_v357_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=37, w3=614, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 37)
    curvature = _rolling_slope(acceleration, 614)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0398 * acceleration + 0.0041158 * anchor
    return base_signal.diff()

def f84_olr_358_struct_v358_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=48, w3=627, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.055625 + 0.0041159 * anchor
    return base_signal.diff()

def f84_olr_359_struct_v359_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=59, w3=640, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.055 * _rolling_slope(draw, 640) + 0.004116 * anchor
    return base_signal.diff()

def f84_olr_360_struct_v360_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=70, w3=653, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(70, min_periods=max(70//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.084375 + 0.0041161 * anchor
    return base_signal.diff()

def f84_olr_361_struct_v361_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=81, w3=666, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 81)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.09875 + 0.0041162 * anchor
    return base_signal.diff()

def f84_olr_362_struct_v362_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=92, w3=679, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.113125 + 0.0041163 * anchor
    return base_signal.diff()

def f84_olr_363_struct_v363_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=103, w3=692, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(103, min_periods=max(103//3, 2)).rank(pct=True)
    persistence = change.rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0854 * persistence + 0.0041164 * anchor
    return base_signal.diff()

def f84_olr_364_struct_v364_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=114, w3=705, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(114, min_periods=max(114//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.141875 + 0.0041165 * anchor
    return base_signal.diff()

def f84_olr_365_struct_v365_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=125, w3=718, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(125, min_periods=max(125//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1006 * slope + 0.0041166 * anchor
    return base_signal.diff()

def f84_olr_366_struct_v366_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=136, w3=731, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(19)
    drag = impulse.rolling(136, min_periods=max(136//3, 2)).mean()
    noise = impulse.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.170625 + 0.0041167 * anchor
    return base_signal.diff()

def f84_olr_367_struct_v367_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=147, w3=744, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 147)
    curvature = _rolling_slope(acceleration, 744)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1158 * acceleration + 0.0041168 * anchor
    return base_signal.diff()

def f84_olr_368_struct_v368_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=158, w3=757, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(158, min_periods=max(158//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.199375 + 0.0041169 * anchor
    return base_signal.diff()

def f84_olr_369_struct_v369_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=169, w3=770, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(169, min_periods=max(169//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.131 * _rolling_slope(draw, 770) + 0.004117 * anchor
    return base_signal.diff()

def f84_olr_370_struct_v370_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=180, w3=26, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(180, min_periods=max(180//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.228125 + 0.0041171 * anchor
    return base_signal.diff()

def f84_olr_371_struct_v371_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=191, w3=39, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 191)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=39, adjust=False).mean() * 1.2425 + 0.0041172 * anchor
    return base_signal.diff()

def f84_olr_372_struct_v372_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=202, w3=52, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(202, min_periods=max(202//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.256875 + 0.0041173 * anchor
    return base_signal.diff()

def f84_olr_373_struct_v373_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=213, w3=65, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(68)
    rank = change.rolling(213, min_periods=max(213//3, 2)).rank(pct=True)
    persistence = change.rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1614 * persistence + 0.0041174 * anchor
    return base_signal.diff()

def f84_olr_374_struct_v374_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=224, w3=78, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(224, min_periods=max(224//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.285625 + 0.0041175 * anchor
    return base_signal.diff()

def f84_olr_375_struct_v375_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=235, w3=91, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(235, min_periods=max(235//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1766 * slope + 0.0041176 * anchor
    return base_signal.diff()
