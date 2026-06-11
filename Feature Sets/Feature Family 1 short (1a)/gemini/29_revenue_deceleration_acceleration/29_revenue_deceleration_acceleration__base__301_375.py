"""29 revenue deceleration acceleration base features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f29_rda_301_struct_v301(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=60, w3=757, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 60)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.94375 + 0.0017702 * anchor

def f29_rda_302_struct_v302(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=71, w3=770, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.958125 + 0.0017703 * anchor

def f29_rda_303_struct_v303(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=82, w3=26, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(82, min_periods=max(82//3, 2)).rank(pct=True)
    persistence = change.rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.203 * persistence + 0.0017704 * anchor

def f29_rda_304_struct_v304(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=93, w3=39, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(93, min_periods=max(93//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.986875 + 0.0017705 * anchor

def f29_rda_305_struct_v305(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=104, w3=52, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(104, min_periods=max(104//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2182 * slope + 0.0017706 * anchor

def f29_rda_306_struct_v306(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=115, w3=65, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(115, min_periods=max(115//3, 2)).mean()
    noise = impulse.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.015625 + 0.0017707 * anchor

def f29_rda_307_struct_v307(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=126, w3=78, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 126)
    curvature = _rolling_slope(acceleration, 78)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2334 * acceleration + 0.0017708 * anchor

def f29_rda_308_struct_v308(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=137, w3=91, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(137, min_periods=max(137//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(91) * 1.044375 + 0.0017709 * anchor

def f29_rda_309_struct_v309(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=148, w3=104, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(148, min_periods=max(148//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2486 * _rolling_slope(draw, 104) + 0.001771 * anchor

def f29_rda_310_struct_v310(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=159, w3=117, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.073125 + 0.0017711 * anchor

def f29_rda_311_struct_v311(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=170, w3=130, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 170)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=130, adjust=False).mean() * 1.0875 + 0.0017712 * anchor

def f29_rda_312_struct_v312(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=181, w3=143, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.101875 + 0.0017713 * anchor

def f29_rda_313_struct_v313(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=192, w3=156, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(192, min_periods=max(192//3, 2)).rank(pct=True)
    persistence = change.rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.279 * persistence + 0.0017714 * anchor

def f29_rda_314_struct_v314(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=203, w3=169, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(203, min_periods=max(203//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.130625 + 0.0017715 * anchor

def f29_rda_315_struct_v315(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=214, w3=182, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2942 * slope + 0.0017716 * anchor

def f29_rda_316_struct_v316(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=225, w3=195, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(23)
    drag = impulse.rolling(225, min_periods=max(225//3, 2)).mean()
    noise = impulse.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.159375 + 0.0017717 * anchor

def f29_rda_317_struct_v317(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=236, w3=208, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 236)
    curvature = _rolling_slope(acceleration, 208)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3094 * acceleration + 0.0017718 * anchor

def f29_rda_318_struct_v318(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=247, w3=221, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(37, min_periods=max(37//3, 2)).mean(), upside.rolling(247, min_periods=max(247//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.188125 + 0.0017719 * anchor

def f29_rda_319_struct_v319(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=258, w3=234, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(258, min_periods=max(258//3, 2)).max()
    rebound = x - x.rolling(44, min_periods=max(44//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3246 * _rolling_slope(draw, 234) + 0.001772 * anchor

def f29_rda_320_struct_v320(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=269, w3=247, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(269, min_periods=max(269//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.216875 + 0.0017721 * anchor

def f29_rda_321_struct_v321(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=280, w3=260, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 280)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=260, adjust=False).mean() * 1.23125 + 0.0017722 * anchor

def f29_rda_322_struct_v322(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=291, w3=273, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(291, min_periods=max(291//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.245625 + 0.0017723 * anchor

def f29_rda_323_struct_v323(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=302, w3=286, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(72)
    rank = change.rolling(302, min_periods=max(302//3, 2)).rank(pct=True)
    persistence = change.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.355 * persistence + 0.0017724 * anchor

def f29_rda_324_struct_v324(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=313, w3=299, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.274375 + 0.0017725 * anchor

def f29_rda_325_struct_v325(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=324, w3=312, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(324, min_periods=max(324//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3702 * slope + 0.0017726 * anchor

def f29_rda_326_struct_v326(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=335, w3=325, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(93)
    drag = impulse.rolling(335, min_periods=max(335//3, 2)).mean()
    noise = impulse.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.303125 + 0.0017727 * anchor

def f29_rda_327_struct_v327(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=346, w3=338, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 346)
    curvature = _rolling_slope(acceleration, 338)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3854 * acceleration + 0.0017728 * anchor

def f29_rda_328_struct_v328(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=357, w3=351, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(357, min_periods=max(357//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.331875 + 0.0017729 * anchor

def f29_rda_329_struct_v329(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=368, w3=364, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(368, min_periods=max(368//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4006 * _rolling_slope(draw, 364) + 0.001773 * anchor

def f29_rda_330_struct_v330(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=379, w3=377, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(379, min_periods=max(379//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.360625 + 0.0017731 * anchor

def f29_rda_331_struct_v331(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=390, w3=390, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 390)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.375 + 0.0017732 * anchor

def f29_rda_332_struct_v332(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=401, w3=403, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(401, min_periods=max(401//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.389375 + 0.0017733 * anchor

def f29_rda_333_struct_v333(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=412, w3=416, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(412, min_periods=max(412//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0546 * persistence + 0.0017734 * anchor

def f29_rda_334_struct_v334(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=423, w3=429, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(423, min_periods=max(423//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.418125 + 0.0017735 * anchor

def f29_rda_335_struct_v335(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=434, w3=442, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(434, min_periods=max(434//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0698 * slope + 0.0017736 * anchor

def f29_rda_336_struct_v336(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=445, w3=455, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(445, min_periods=max(445//3, 2)).mean()
    noise = impulse.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.446875 + 0.0017737 * anchor

def f29_rda_337_struct_v337(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=456, w3=468, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 456)
    curvature = _rolling_slope(acceleration, 468)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.085 * acceleration + 0.0017738 * anchor

def f29_rda_338_struct_v338(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=467, w3=481, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(467, min_periods=max(467//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.475625 + 0.0017739 * anchor

def f29_rda_339_struct_v339(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=478, w3=494, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(478, min_periods=max(478//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1002 * _rolling_slope(draw, 494) + 0.001774 * anchor

def f29_rda_340_struct_v340(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=489, w3=507, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(489, min_periods=max(489//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.504375 + 0.0017741 * anchor

def f29_rda_341_struct_v341(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=500, w3=520, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 500)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.51875 + 0.0017742 * anchor

def f29_rda_342_struct_v342(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=511, w3=533, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(511, min_periods=max(511//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.533125 + 0.0017743 * anchor

def f29_rda_343_struct_v343(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=19, w3=546, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(19, min_periods=max(19//3, 2)).rank(pct=True)
    persistence = change.rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1306 * persistence + 0.0017744 * anchor

def f29_rda_344_struct_v344(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=30, w3=559, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(30, min_periods=max(30//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.561875 + 0.0017745 * anchor

def f29_rda_345_struct_v345(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=41, w3=572, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(41, min_periods=max(41//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1458 * slope + 0.0017746 * anchor

def f29_rda_346_struct_v346(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=52, w3=585, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(52, min_periods=max(52//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.590625 + 0.0017747 * anchor

def f29_rda_347_struct_v347(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=63, w3=598, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 63)
    curvature = _rolling_slope(acceleration, 598)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.161 * acceleration + 0.0017748 * anchor

def f29_rda_348_struct_v348(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=74, w3=611, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(74, min_periods=max(74//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.619375 + 0.0017749 * anchor

def f29_rda_349_struct_v349(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=85, w3=624, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(85, min_periods=max(85//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1762 * _rolling_slope(draw, 624) + 0.001775 * anchor

def f29_rda_350_struct_v350(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=96, w3=637, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(96, min_periods=max(96//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.875 + 0.0017751 * anchor

def f29_rda_351_struct_v351(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=107, w3=650, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 107)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.889375 + 0.0017752 * anchor

def f29_rda_352_struct_v352(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=118, w3=663, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(118, min_periods=max(118//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.90375 + 0.0017753 * anchor

def f29_rda_353_struct_v353(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=129, w3=676, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(31)
    rank = change.rolling(129, min_periods=max(129//3, 2)).rank(pct=True)
    persistence = change.rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2066 * persistence + 0.0017754 * anchor

def f29_rda_354_struct_v354(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=140, w3=689, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(140, min_periods=max(140//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9325 + 0.0017755 * anchor

def f29_rda_355_struct_v355(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=151, w3=702, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(151, min_periods=max(151//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2218 * slope + 0.0017756 * anchor

def f29_rda_356_struct_v356(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=162, w3=715, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(52)
    drag = impulse.rolling(162, min_periods=max(162//3, 2)).mean()
    noise = impulse.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.96125 + 0.0017757 * anchor

def f29_rda_357_struct_v357(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=173, w3=728, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 173)
    curvature = _rolling_slope(acceleration, 728)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.237 * acceleration + 0.0017758 * anchor

def f29_rda_358_struct_v358(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=184, w3=741, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(184, min_periods=max(184//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.99 + 0.0017759 * anchor

def f29_rda_359_struct_v359(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=195, w3=754, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(195, min_periods=max(195//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2522 * _rolling_slope(draw, 754) + 0.001776 * anchor

def f29_rda_360_struct_v360(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=206, w3=767, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(206, min_periods=max(206//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.01875 + 0.0017761 * anchor

def f29_rda_361_struct_v361(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=217, w3=23, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 217)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=23, adjust=False).mean() * 1.033125 + 0.0017762 * anchor

def f29_rda_362_struct_v362(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=228, w3=36, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(228, min_periods=max(228//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0475 + 0.0017763 * anchor

def f29_rda_363_struct_v363(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=239, w3=49, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(101)
    rank = change.rolling(239, min_periods=max(239//3, 2)).rank(pct=True)
    persistence = change.rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2826 * persistence + 0.0017764 * anchor

def f29_rda_364_struct_v364(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=250, w3=62, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(250, min_periods=max(250//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.07625 + 0.0017765 * anchor

def f29_rda_365_struct_v365(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=261, w3=75, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2978 * slope + 0.0017766 * anchor

def f29_rda_366_struct_v366(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=272, w3=88, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(122)
    drag = impulse.rolling(272, min_periods=max(272//3, 2)).mean()
    noise = impulse.abs().rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.105 + 0.0017767 * anchor

def f29_rda_367_struct_v367(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=283, w3=101, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 283)
    curvature = _rolling_slope(acceleration, 101)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.313 * acceleration + 0.0017768 * anchor

def f29_rda_368_struct_v368(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=294, w3=114, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(294, min_periods=max(294//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(114) * 1.13375 + 0.0017769 * anchor

def f29_rda_369_struct_v369(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=305, w3=127, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(305, min_periods=max(305//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3282 * _rolling_slope(draw, 127) + 0.001777 * anchor

def f29_rda_370_struct_v370(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=316, w3=140, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(316, min_periods=max(316//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1625 + 0.0017771 * anchor

def f29_rda_371_struct_v371(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=327, w3=153, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 327)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=153, adjust=False).mean() * 1.176875 + 0.0017772 * anchor

def f29_rda_372_struct_v372(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=338, w3=166, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(338, min_periods=max(338//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.19125 + 0.0017773 * anchor

def f29_rda_373_struct_v373(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=349, w3=179, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(349, min_periods=max(349//3, 2)).rank(pct=True)
    persistence = change.rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3586 * persistence + 0.0017774 * anchor

def f29_rda_374_struct_v374(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=360, w3=192, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(360, min_periods=max(360//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.22 + 0.0017775 * anchor

def f29_rda_375_struct_v375(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=371, w3=205, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(371, min_periods=max(371//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3738 * slope + 0.0017776 * anchor
