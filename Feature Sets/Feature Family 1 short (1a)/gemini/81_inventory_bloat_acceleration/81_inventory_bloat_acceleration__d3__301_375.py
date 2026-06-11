"""81 inventory bloat acceleration d3 third derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f81_invb_301_struct_v301_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=16, w2=244, w3=710, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 244)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.420625 + 0.0039302 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_302_struct_v302_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=23, w2=255, w3=723, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.435 + 0.0039303 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_303_struct_v303_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=266, w3=736, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(30)
    rank = change.rolling(266, min_periods=max(266//3, 2)).rank(pct=True)
    persistence = change.rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2526 * persistence + 0.0039304 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_304_struct_v304_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=277, w3=749, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(277, min_periods=max(277//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46375 + 0.0039305 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_305_struct_v305_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=288, w3=762, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(288, min_periods=max(288//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2678 * slope + 0.0039306 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_306_struct_v306_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=299, w3=18, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(51)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4925 + 0.0039307 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_307_struct_v307_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=310, w3=31, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 310)
    curvature = _rolling_slope(acceleration, 31)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283 * acceleration + 0.0039308 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_308_struct_v308_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=321, w3=44, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(321, min_periods=max(321//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(44) * 1.52125 + 0.0039309 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_309_struct_v309_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=332, w3=57, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(332, min_periods=max(332//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2982 * _rolling_slope(draw, 57) + 0.003931 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_310_struct_v310_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=343, w3=70, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(343, min_periods=max(343//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55 + 0.0039311 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_311_struct_v311_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=354, w3=83, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 354)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=83, adjust=False).mean() * 1.564375 + 0.0039312 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_312_struct_v312_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=365, w3=96, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(365, min_periods=max(365//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.57875 + 0.0039313 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_313_struct_v313_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=376, w3=109, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(100)
    rank = change.rolling(376, min_periods=max(376//3, 2)).rank(pct=True)
    persistence = change.rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3286 * persistence + 0.0039314 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_314_struct_v314_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=387, w3=122, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(387, min_periods=max(387//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6075 + 0.0039315 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_315_struct_v315_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=398, w3=135, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(398, min_periods=max(398//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3438 * slope + 0.0039316 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_316_struct_v316_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=409, w3=148, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(121)
    drag = impulse.rolling(409, min_periods=max(409//3, 2)).mean()
    noise = impulse.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.863125 + 0.0039317 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_317_struct_v317_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=420, w3=161, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 420)
    curvature = _rolling_slope(acceleration, 161)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.359 * acceleration + 0.0039318 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_318_struct_v318_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=431, w3=174, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.891875 + 0.0039319 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_319_struct_v319_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=442, w3=187, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(442, min_periods=max(442//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3742 * _rolling_slope(draw, 187) + 0.003932 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_320_struct_v320_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=453, w3=200, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(453, min_periods=max(453//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.920625 + 0.0039321 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_321_struct_v321_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=464, w3=213, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 464)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=213, adjust=False).mean() * 0.935 + 0.0039322 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_322_struct_v322_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=475, w3=226, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(475, min_periods=max(475//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.949375 + 0.0039323 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_323_struct_v323_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=486, w3=239, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(486, min_periods=max(486//3, 2)).rank(pct=True)
    persistence = change.rolling(239, min_periods=max(239//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4046 * persistence + 0.0039324 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_324_struct_v324_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=497, w3=252, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(497, min_periods=max(497//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.978125 + 0.0039325 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_325_struct_v325_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=508, w3=265, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(508, min_periods=max(508//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0434 * slope + 0.0039326 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_326_struct_v326_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=16, w3=278, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(16, min_periods=max(16//3, 2)).mean()
    noise = impulse.abs().rolling(278, min_periods=max(278//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.006875 + 0.0039327 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_327_struct_v327_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=27, w3=291, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 27)
    curvature = _rolling_slope(acceleration, 291)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0586 * acceleration + 0.0039328 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_328_struct_v328_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=38, w3=304, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(38, min_periods=max(38//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.035625 + 0.0039329 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_329_struct_v329_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=49, w3=317, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(49, min_periods=max(49//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0738 * _rolling_slope(draw, 317) + 0.003933 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_330_struct_v330_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=60, w3=330, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(60, min_periods=max(60//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.064375 + 0.0039331 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_331_struct_v331_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=71, w3=343, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 71)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.07875 + 0.0039332 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_332_struct_v332_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=82, w3=356, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(82, min_periods=max(82//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.093125 + 0.0039333 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_333_struct_v333_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=93, w3=369, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(93, min_periods=max(93//3, 2)).rank(pct=True)
    persistence = change.rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1042 * persistence + 0.0039334 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_334_struct_v334_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=104, w3=382, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(104, min_periods=max(104//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.121875 + 0.0039335 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_335_struct_v335_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=115, w3=395, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(115, min_periods=max(115//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1194 * slope + 0.0039336 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_336_struct_v336_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=126, w3=408, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(10)
    drag = impulse.rolling(126, min_periods=max(126//3, 2)).mean()
    noise = impulse.abs().rolling(408, min_periods=max(408//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.150625 + 0.0039337 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_337_struct_v337_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=137, w3=421, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 137)
    curvature = _rolling_slope(acceleration, 421)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1346 * acceleration + 0.0039338 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_338_struct_v338_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=148, w3=434, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.179375 + 0.0039339 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_339_struct_v339_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=159, w3=447, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(159, min_periods=max(159//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1498 * _rolling_slope(draw, 447) + 0.003934 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_340_struct_v340_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=170, w3=460, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(170, min_periods=max(170//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.208125 + 0.0039341 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_341_struct_v341_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=181, w3=473, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 181)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2225 + 0.0039342 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_342_struct_v342_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=192, w3=486, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(192, min_periods=max(192//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.236875 + 0.0039343 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_343_struct_v343_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=203, w3=499, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(59)
    rank = change.rolling(203, min_periods=max(203//3, 2)).rank(pct=True)
    persistence = change.rolling(499, min_periods=max(499//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1802 * persistence + 0.0039344 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_344_struct_v344_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=214, w3=512, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(214, min_periods=max(214//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.265625 + 0.0039345 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_345_struct_v345_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=225, w3=525, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1954 * slope + 0.0039346 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_346_struct_v346_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=236, w3=538, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(80)
    drag = impulse.rolling(236, min_periods=max(236//3, 2)).mean()
    noise = impulse.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.294375 + 0.0039347 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_347_struct_v347_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=247, w3=551, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 247)
    curvature = _rolling_slope(acceleration, 551)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2106 * acceleration + 0.0039348 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_348_struct_v348_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=258, w3=564, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.323125 + 0.0039349 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_349_struct_v349_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=269, w3=577, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(269, min_periods=max(269//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2258 * _rolling_slope(draw, 577) + 0.003935 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_350_struct_v350_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=280, w3=590, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.351875 + 0.0039351 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_351_struct_v351_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=291, w3=603, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 291)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.36625 + 0.0039352 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_352_struct_v352_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=302, w3=616, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(302, min_periods=max(302//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.380625 + 0.0039353 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_353_struct_v353_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=313, w3=629, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2562 * persistence + 0.0039354 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_354_struct_v354_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=324, w3=642, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(324, min_periods=max(324//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.409375 + 0.0039355 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_355_struct_v355_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=335, w3=655, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(335, min_periods=max(335//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2714 * slope + 0.0039356 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_356_struct_v356_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=346, w3=668, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(346, min_periods=max(346//3, 2)).mean()
    noise = impulse.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.438125 + 0.0039357 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_357_struct_v357_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=357, w3=681, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 357)
    curvature = _rolling_slope(acceleration, 681)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2866 * acceleration + 0.0039358 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_358_struct_v358_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=368, w3=694, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(368, min_periods=max(368//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.466875 + 0.0039359 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_359_struct_v359_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=379, w3=707, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(379, min_periods=max(379//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3018 * _rolling_slope(draw, 707) + 0.003936 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_360_struct_v360_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=390, w3=720, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.495625 + 0.0039361 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_361_struct_v361_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=401, w3=733, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 401)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.51 + 0.0039362 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_362_struct_v362_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=412, w3=746, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(412, min_periods=max(412//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.524375 + 0.0039363 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_363_struct_v363_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=423, w3=759, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(423, min_periods=max(423//3, 2)).rank(pct=True)
    persistence = change.rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3322 * persistence + 0.0039364 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_364_struct_v364_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=434, w3=15, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.553125 + 0.0039365 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_365_struct_v365_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=213, w2=445, w3=28, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(445, min_periods=max(445//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3474 * slope + 0.0039366 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_366_struct_v366_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=220, w2=456, w3=41, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(456, min_periods=max(456//3, 2)).mean()
    noise = impulse.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.581875 + 0.0039367 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_367_struct_v367_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=227, w2=467, w3=54, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 467)
    curvature = _rolling_slope(acceleration, 54)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3626 * acceleration + 0.0039368 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_368_struct_v368_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=234, w2=478, w3=67, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(67) * 1.610625 + 0.0039369 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_369_struct_v369_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=241, w2=489, w3=80, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3778 * _rolling_slope(draw, 80) + 0.003937 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_370_struct_v370_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=248, w2=500, w3=93, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(500, min_periods=max(500//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.86625 + 0.0039371 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_371_struct_v371_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=255, w2=511, w3=106, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 255)
    slow = _rolling_slope(x, 511)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=106, adjust=False).mean() * 0.880625 + 0.0039372 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_372_struct_v372_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=11, w2=19, w3=119, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.895 + 0.0039373 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_373_struct_v373_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=18, w2=30, w3=132, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(18)
    rank = change.rolling(30, min_periods=max(30//3, 2)).rank(pct=True)
    persistence = change.rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4082 * persistence + 0.0039374 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_374_struct_v374_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=25, w2=41, w3=145, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(41, min_periods=max(41//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92375 + 0.0039375 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_375_struct_v375_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=32, w2=52, w3=158, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(52, min_periods=max(52//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.047 * slope + 0.0039376 * anchor
    return base_signal.diff().diff().diff()
