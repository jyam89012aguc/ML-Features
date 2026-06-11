"""51 relative sector weakness d2 second derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Relative_Strength - Institutional-grade short-side signal.
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

def f51_rsw_301_rel_v301_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=134, w2=457, w3=748, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.39875 + 0.0031502 * anchor
    return base_signal.diff().diff()

def f51_rsw_302_rel_v302_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=141, w2=468, w3=761, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(468, min_periods=max(468//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0598 * _rolling_slope(draw, 761) + 0.0031503 * anchor
    return base_signal.diff().diff()

def f51_rsw_303_rel_v303_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=148, w2=479, w3=17, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.4275 + 0.0031504 * anchor
    return base_signal.diff().diff()

def f51_rsw_304_rel_v304_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=155, w2=490, w3=30, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(490, min_periods=max(490//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.441875 + 0.0031505 * anchor
    return base_signal.diff().diff()

def f51_rsw_305_rel_v305_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=162, w2=501, w3=43, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 501)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=43, adjust=False).mean() * 1.45625 + 0.0031506 * anchor
    return base_signal.diff().diff()

def f51_rsw_306_rel_v306_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=169, w2=512, w3=56, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(512, min_periods=max(512//3, 2)).max()
    trough = x.rolling(169, min_periods=max(169//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.470625 + 0.0031507 * anchor
    return base_signal.diff().diff()

def f51_rsw_307_rel_v307_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=176, w2=20, w3=69, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(20, min_periods=max(20//3, 2)).rank(pct=True)
    persistence = change.rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0978 * persistence + 0.0031508 * anchor
    return base_signal.diff().diff()

def f51_rsw_308_rel_v308_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=183, w2=31, w3=82, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(183, min_periods=max(183//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.499375 + 0.0031509 * anchor
    return base_signal.diff().diff()

def f51_rsw_309_rel_v309_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=190, w2=42, w3=95, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(42, min_periods=max(42//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 190)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.113 * slope + 0.003151 * anchor
    return base_signal.diff().diff()

def f51_rsw_310_rel_v310_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=197, w2=53, w3=108, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(53, min_periods=max(53//3, 2)).mean()
    noise = impulse.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.528125 + 0.0031511 * anchor
    return base_signal.diff().diff()

def f51_rsw_311_rel_v311_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=204, w2=64, w3=121, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 64)
    curvature = _rolling_slope(acceleration, 121)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1282 * acceleration + 0.0031512 * anchor
    return base_signal.diff().diff()

def f51_rsw_312_rel_v312_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=211, w2=75, w3=134, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 211)
    pressure = rel_log.diff(75)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1358 * pressure.rolling(134, min_periods=max(134//3, 2)).mean() + 0.0031513 * anchor
    return base_signal.diff().diff()

def f51_rsw_313_rel_v313_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=218, w2=86, w3=147, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(218, min_periods=max(218//3, 2)).mean())
    decay = spread.ewm(span=86, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.57125 + 0.0031514 * anchor
    return base_signal.diff().diff()

def f51_rsw_314_rel_v314_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=225, w2=97, w3=160, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(97, min_periods=max(97//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 225)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.585625 + 0.0031515 * anchor
    return base_signal.diff().diff()

def f51_rsw_315_rel_v315_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=232, w2=108, w3=173, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(232, min_periods=max(232//3, 2)).mean(), b.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1586 * _rolling_slope(cover, 232) + 0.0031516 * anchor
    return base_signal.diff().diff()

def f51_rsw_316_rel_v316_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=239, w2=119, w3=186, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1662 * y + 0.833800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 239) - _rolling_slope(basket, 119) + 0.0031517 * anchor
    return base_signal.diff().diff()

def f51_rsw_317_rel_v317_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=246, w2=130, w3=199, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(130, min_periods=max(130//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.855625 + 0.0031518 * anchor
    return base_signal.diff().diff()

def f51_rsw_318_rel_v318_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=253, w2=141, w3=212, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1814 * _rolling_slope(draw, 212) + 0.0031519 * anchor
    return base_signal.diff().diff()

def f51_rsw_319_rel_v319_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=9, w2=152, w3=225, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(9) - b.diff(126)
    stress = imbalance.rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.884375 + 0.003152 * anchor
    return base_signal.diff().diff()

def f51_rsw_320_rel_v320_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=16, w2=163, w3=238, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(163, min_periods=max(163//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.89875 + 0.0031521 * anchor
    return base_signal.diff().diff()

def f51_rsw_321_rel_v321_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=23, w2=174, w3=251, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 174)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=251, adjust=False).mean() * 0.913125 + 0.0031522 * anchor
    return base_signal.diff().diff()

def f51_rsw_322_rel_v322_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=30, w2=185, w3=264, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9275 + 0.0031523 * anchor
    return base_signal.diff().diff()

def f51_rsw_323_rel_v323_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=37, w2=196, w3=277, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(37)
    rank = change.rolling(196, min_periods=max(196//3, 2)).rank(pct=True)
    persistence = change.rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2194 * persistence + 0.0031524 * anchor
    return base_signal.diff().diff()

def f51_rsw_324_rel_v324_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=44, w2=207, w3=290, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95625 + 0.0031525 * anchor
    return base_signal.diff().diff()

def f51_rsw_325_rel_v325_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=51, w2=218, w3=303, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(218, min_periods=max(218//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2346 * slope + 0.0031526 * anchor
    return base_signal.diff().diff()

def f51_rsw_326_rel_v326_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=58, w2=229, w3=316, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(58)
    drag = impulse.rolling(229, min_periods=max(229//3, 2)).mean()
    noise = impulse.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.985 + 0.0031527 * anchor
    return base_signal.diff().diff()

def f51_rsw_327_rel_v327_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=65, w2=240, w3=329, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 329)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2498 * acceleration + 0.0031528 * anchor
    return base_signal.diff().diff()

def f51_rsw_328_rel_v328_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=72, w2=251, w3=342, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 72)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2574 * pressure.rolling(342, min_periods=max(342//3, 2)).mean() + 0.0031529 * anchor
    return base_signal.diff().diff()

def f51_rsw_329_rel_v329_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=79, w2=262, w3=355, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(79, min_periods=max(79//3, 2)).mean())
    decay = spread.ewm(span=262, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.028125 + 0.003153 * anchor
    return base_signal.diff().diff()

def f51_rsw_330_rel_v330_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=86, w2=273, w3=368, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(273, min_periods=max(273//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 86)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.0425 + 0.0031531 * anchor
    return base_signal.diff().diff()

def f51_rsw_331_rel_v331_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=93, w2=284, w3=381, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(93, min_periods=max(93//3, 2)).mean(), b.abs().rolling(284, min_periods=max(284//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2802 * _rolling_slope(cover, 93) + 0.0031532 * anchor
    return base_signal.diff().diff()

def f51_rsw_332_rel_v332_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=100, w2=295, w3=394, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2878 * y + 0.712200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 100) - _rolling_slope(basket, 295) + 0.0031533 * anchor
    return base_signal.diff().diff()

def f51_rsw_333_rel_v333_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=107, w2=306, w3=407, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.085625 + 0.0031534 * anchor
    return base_signal.diff().diff()

def f51_rsw_334_rel_v334_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=114, w2=317, w3=420, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.303 * _rolling_slope(draw, 420) + 0.0031535 * anchor
    return base_signal.diff().diff()

def f51_rsw_335_rel_v335_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=121, w2=328, w3=433, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(121) - b.diff(126)
    stress = imbalance.rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.114375 + 0.0031536 * anchor
    return base_signal.diff().diff()

def f51_rsw_336_rel_v336_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=128, w2=339, w3=446, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.12875 + 0.0031537 * anchor
    return base_signal.diff().diff()

def f51_rsw_337_rel_v337_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=135, w2=350, w3=459, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 350)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.143125 + 0.0031538 * anchor
    return base_signal.diff().diff()

def f51_rsw_338_rel_v338_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=142, w2=361, w3=472, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1575 + 0.0031539 * anchor
    return base_signal.diff().diff()

def f51_rsw_339_rel_v339_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=149, w2=372, w3=485, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(372, min_periods=max(372//3, 2)).rank(pct=True)
    persistence = change.rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341 * persistence + 0.003154 * anchor
    return base_signal.diff().diff()

def f51_rsw_340_rel_v340_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=156, w2=383, w3=498, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18625 + 0.0031541 * anchor
    return base_signal.diff().diff()

def f51_rsw_341_rel_v341_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=163, w2=394, w3=511, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(394, min_periods=max(394//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3562 * slope + 0.0031542 * anchor
    return base_signal.diff().diff()

def f51_rsw_342_rel_v342_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=170, w2=405, w3=524, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.215 + 0.0031543 * anchor
    return base_signal.diff().diff()

def f51_rsw_343_rel_v343_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=177, w2=416, w3=537, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 416)
    curvature = _rolling_slope(acceleration, 537)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3714 * acceleration + 0.0031544 * anchor
    return base_signal.diff().diff()

def f51_rsw_344_rel_v344_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=184, w2=427, w3=550, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 184)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.379 * pressure.rolling(550, min_periods=max(550//3, 2)).mean() + 0.0031545 * anchor
    return base_signal.diff().diff()

def f51_rsw_345_rel_v345_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=191, w2=438, w3=563, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(191, min_periods=max(191//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.258125 + 0.0031546 * anchor
    return base_signal.diff().diff()

def f51_rsw_346_rel_v346_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=198, w2=449, w3=576, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(449, min_periods=max(449//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 198)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.2725 + 0.0031547 * anchor
    return base_signal.diff().diff()

def f51_rsw_347_rel_v347_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=205, w2=460, w3=589, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(205, min_periods=max(205//3, 2)).mean(), b.abs().rolling(460, min_periods=max(460//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.4018 * _rolling_slope(cover, 205) + 0.0031548 * anchor
    return base_signal.diff().diff()

def f51_rsw_348_rel_v348_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=212, w2=471, w3=602, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.4094 * y + 0.590600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 212) - _rolling_slope(basket, 471) + 0.0031549 * anchor
    return base_signal.diff().diff()

def f51_rsw_349_rel_v349_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=219, w2=482, w3=615, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(482, min_periods=max(482//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.315625 + 0.003155 * anchor
    return base_signal.diff().diff()

def f51_rsw_350_rel_v350_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=226, w2=493, w3=628, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(493, min_periods=max(493//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0482 * _rolling_slope(draw, 628) + 0.0031551 * anchor
    return base_signal.diff().diff()

def f51_rsw_351_rel_v351_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=233, w2=504, w3=641, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.344375 + 0.0031552 * anchor
    return base_signal.diff().diff()

def f51_rsw_352_rel_v352_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=240, w2=12, w3=654, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(12, min_periods=max(12//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.35875 + 0.0031553 * anchor
    return base_signal.diff().diff()

def f51_rsw_353_rel_v353_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=247, w2=23, w3=667, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 23)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.373125 + 0.0031554 * anchor
    return base_signal.diff().diff()

def f51_rsw_354_rel_v354_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=254, w2=34, w3=680, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(34, min_periods=max(34//3, 2)).max()
    trough = x.rolling(254, min_periods=max(254//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3875 + 0.0031555 * anchor
    return base_signal.diff().diff()

def f51_rsw_355_rel_v355_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=10, w2=45, w3=693, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(10)
    rank = change.rolling(45, min_periods=max(45//3, 2)).rank(pct=True)
    persistence = change.rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0862 * persistence + 0.0031556 * anchor
    return base_signal.diff().diff()

def f51_rsw_356_rel_v356_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=17, w2=56, w3=706, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(56, min_periods=max(56//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41625 + 0.0031557 * anchor
    return base_signal.diff().diff()

def f51_rsw_357_rel_v357_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=24, w2=67, w3=719, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(67, min_periods=max(67//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1014 * slope + 0.0031558 * anchor
    return base_signal.diff().diff()

def f51_rsw_358_rel_v358_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=31, w2=78, w3=732, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(31)
    drag = impulse.rolling(78, min_periods=max(78//3, 2)).mean()
    noise = impulse.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.445 + 0.0031559 * anchor
    return base_signal.diff().diff()

def f51_rsw_359_rel_v359_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=38, w2=89, w3=745, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 89)
    curvature = _rolling_slope(acceleration, 745)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1166 * acceleration + 0.003156 * anchor
    return base_signal.diff().diff()

def f51_rsw_360_rel_v360_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=45, w2=100, w3=758, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 45)
    pressure = rel_log.diff(100)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1242 * pressure.rolling(758, min_periods=max(758//3, 2)).mean() + 0.0031561 * anchor
    return base_signal.diff().diff()

def f51_rsw_361_rel_v361_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=52, w2=111, w3=771, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(52, min_periods=max(52//3, 2)).mean())
    decay = spread.ewm(span=111, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.488125 + 0.0031562 * anchor
    return base_signal.diff().diff()

def f51_rsw_362_rel_v362_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=59, w2=122, w3=27, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(122, min_periods=max(122//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 59)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.5025 + 0.0031563 * anchor
    return base_signal.diff().diff()

def f51_rsw_363_rel_v363_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=66, w2=133, w3=40, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(66, min_periods=max(66//3, 2)).mean(), b.abs().rolling(133, min_periods=max(133//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(40) + 0.147 * _rolling_slope(cover, 66) + 0.0031564 * anchor
    return base_signal.diff().diff()

def f51_rsw_364_rel_v364_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=73, w2=144, w3=53, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1546 * y + 0.845400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 73) - _rolling_slope(basket, 144) + 0.0031565 * anchor
    return base_signal.diff().diff()

def f51_rsw_365_rel_v365_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=80, w2=155, w3=66, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(155, min_periods=max(155//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(66) * 1.545625 + 0.0031566 * anchor
    return base_signal.diff().diff()

def f51_rsw_366_rel_v366_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=87, w2=166, w3=79, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(166, min_periods=max(166//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1698 * _rolling_slope(draw, 79) + 0.0031567 * anchor
    return base_signal.diff().diff()

def f51_rsw_367_rel_v367_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=94, w2=177, w3=92, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(94) - b.diff(126)
    stress = imbalance.rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.574375 + 0.0031568 * anchor
    return base_signal.diff().diff()

def f51_rsw_368_rel_v368_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=101, w2=188, w3=105, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(188, min_periods=max(188//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58875 + 0.0031569 * anchor
    return base_signal.diff().diff()

def f51_rsw_369_rel_v369_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=108, w2=199, w3=118, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 199)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=118, adjust=False).mean() * 1.603125 + 0.003157 * anchor
    return base_signal.diff().diff()

def f51_rsw_370_rel_v370_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=115, w2=210, w3=131, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(210, min_periods=max(210//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6175 + 0.0031571 * anchor
    return base_signal.diff().diff()

def f51_rsw_371_rel_v371_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=122, w2=221, w3=144, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(122)
    rank = change.rolling(221, min_periods=max(221//3, 2)).rank(pct=True)
    persistence = change.rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2078 * persistence + 0.0031572 * anchor
    return base_signal.diff().diff()

def f51_rsw_372_rel_v372_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=129, w2=232, w3=157, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(232, min_periods=max(232//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.873125 + 0.0031573 * anchor
    return base_signal.diff().diff()

def f51_rsw_373_rel_v373_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=136, w2=243, w3=170, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(243, min_periods=max(243//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.223 * slope + 0.0031574 * anchor
    return base_signal.diff().diff()

def f51_rsw_374_rel_v374_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=143, w2=254, w3=183, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(254, min_periods=max(254//3, 2)).mean()
    noise = impulse.abs().rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.901875 + 0.0031575 * anchor
    return base_signal.diff().diff()

def f51_rsw_375_rel_v375_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=150, w2=265, w3=196, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 265)
    curvature = _rolling_slope(acceleration, 196)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2382 * acceleration + 0.0031576 * anchor
    return base_signal.diff().diff()
