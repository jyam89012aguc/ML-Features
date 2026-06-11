"""53 relative sector volatility d2 second derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f53_rsw_v_301_rel_v301_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=251, w2=76, w3=451, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(76, min_periods=max(76//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.866875 + 0.0032702 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_302_rel_v302_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=7, w2=87, w3=464, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(87, min_periods=max(87//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1462 * _rolling_slope(draw, 464) + 0.0032703 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_303_rel_v303_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=14, w2=98, w3=477, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(14) - b.diff(98)
    stress = imbalance.rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.895625 + 0.0032704 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_304_rel_v304_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=21, w2=109, w3=490, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.91 + 0.0032705 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_305_rel_v305_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=28, w2=120, w3=503, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.924375 + 0.0032706 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_306_rel_v306_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=35, w2=131, w3=516, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.93875 + 0.0032707 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_307_rel_v307_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=42, w2=142, w3=529, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(42)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1842 * persistence + 0.0032708 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_308_rel_v308_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=49, w2=153, w3=542, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9675 + 0.0032709 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_309_rel_v309_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=56, w2=164, w3=555, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1994 * slope + 0.003271 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_310_rel_v310_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=63, w2=175, w3=568, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(63)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.99625 + 0.0032711 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_311_rel_v311_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=70, w2=186, w3=581, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2146 * acceleration + 0.0032712 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_312_rel_v312_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=77, w2=197, w3=594, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 77)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2222 * pressure.rolling(594, min_periods=max(594//3, 2)).mean() + 0.0032713 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_313_rel_v313_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=84, w2=208, w3=607, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    decay = spread.ewm(span=208, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.039375 + 0.0032714 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_314_rel_v314_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=91, w2=219, w3=620, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(219, min_periods=max(219//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 91)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.05375 + 0.0032715 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_315_rel_v315_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=98, w2=230, w3=633, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(98, min_periods=max(98//3, 2)).mean(), b.abs().rolling(230, min_periods=max(230//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.245 * _rolling_slope(cover, 98) + 0.0032716 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_316_rel_v316_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=105, w2=241, w3=646, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2526 * y + 0.747400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 105) - _rolling_slope(basket, 241) + 0.0032717 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_317_rel_v317_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=112, w2=252, w3=659, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.096875 + 0.0032718 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_318_rel_v318_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=119, w2=263, w3=672, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2678 * _rolling_slope(draw, 672) + 0.0032719 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_319_rel_v319_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=126, w2=274, w3=685, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.125625 + 0.003272 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_320_rel_v320_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=133, w2=285, w3=698, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(285, min_periods=max(285//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.14 + 0.0032721 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_321_rel_v321_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=140, w2=296, w3=711, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 296)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.154375 + 0.0032722 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_322_rel_v322_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=147, w2=307, w3=724, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(307, min_periods=max(307//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.16875 + 0.0032723 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_323_rel_v323_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=154, w2=318, w3=737, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(318, min_periods=max(318//3, 2)).rank(pct=True)
    persistence = change.rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3058 * persistence + 0.0032724 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_324_rel_v324_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=161, w2=329, w3=750, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(329, min_periods=max(329//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1975 + 0.0032725 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_325_rel_v325_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=168, w2=340, w3=763, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(340, min_periods=max(340//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.321 * slope + 0.0032726 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_326_rel_v326_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=175, w2=351, w3=19, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(351, min_periods=max(351//3, 2)).mean()
    noise = impulse.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.22625 + 0.0032727 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_327_rel_v327_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=182, w2=362, w3=32, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 362)
    curvature = _rolling_slope(acceleration, 32)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3362 * acceleration + 0.0032728 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_328_rel_v328_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=189, w2=373, w3=45, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 189)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3438 * pressure.rolling(45, min_periods=max(45//3, 2)).mean() + 0.0032729 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_329_rel_v329_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=196, w2=384, w3=58, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.269375 + 0.003273 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_330_rel_v330_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=203, w2=395, w3=71, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(395, min_periods=max(395//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 203)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.28375 + 0.0032731 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_331_rel_v331_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=210, w2=406, w3=84, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(210, min_periods=max(210//3, 2)).mean(), b.abs().rolling(406, min_periods=max(406//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(84) + 0.3666 * _rolling_slope(cover, 210) + 0.0032732 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_332_rel_v332_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=217, w2=417, w3=97, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3742 * y + 0.625800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 217) - _rolling_slope(basket, 417) + 0.0032733 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_333_rel_v333_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=224, w2=428, w3=110, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(428, min_periods=max(428//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(110) * 1.326875 + 0.0032734 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_334_rel_v334_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=231, w2=439, w3=123, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(439, min_periods=max(439//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3894 * _rolling_slope(draw, 123) + 0.0032735 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_335_rel_v335_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=238, w2=450, w3=136, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.355625 + 0.0032736 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_336_rel_v336_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=245, w2=461, w3=149, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.37 + 0.0032737 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_337_rel_v337_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=252, w2=472, w3=162, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=162, adjust=False).mean() * 1.384375 + 0.0032738 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_338_rel_v338_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=8, w2=483, w3=175, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.39875 + 0.0032739 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_339_rel_v339_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=15, w2=494, w3=188, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(15)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.051 * persistence + 0.003274 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_340_rel_v340_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=22, w2=505, w3=201, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4275 + 0.0032741 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_341_rel_v341_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=29, w2=13, w3=214, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0662 * slope + 0.0032742 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_342_rel_v342_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=36, w2=24, w3=227, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(36)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45625 + 0.0032743 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_343_rel_v343_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=43, w2=35, w3=240, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0814 * acceleration + 0.0032744 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_344_rel_v344_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=50, w2=46, w3=253, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 50)
    pressure = rel_log.diff(46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.089 * pressure.rolling(253, min_periods=max(253//3, 2)).mean() + 0.0032745 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_345_rel_v345_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=57, w2=57, w3=266, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(57, min_periods=max(57//3, 2)).mean())
    decay = spread.ewm(span=57, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.499375 + 0.0032746 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_346_rel_v346_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=64, w2=68, w3=279, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(68, min_periods=max(68//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 64)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.51375 + 0.0032747 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_347_rel_v347_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=71, w2=79, w3=292, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(71, min_periods=max(71//3, 2)).mean(), b.abs().rolling(79, min_periods=max(79//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1118 * _rolling_slope(cover, 71) + 0.0032748 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_348_rel_v348_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=78, w2=90, w3=305, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1194 * y + 0.880600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 78) - _rolling_slope(basket, 90) + 0.0032749 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_349_rel_v349_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=85, w2=101, w3=318, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(101, min_periods=max(101//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.556875 + 0.003275 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_350_rel_v350_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=92, w2=112, w3=331, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1346 * _rolling_slope(draw, 331) + 0.0032751 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_351_rel_v351_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=99, w2=123, w3=344, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(99) - b.diff(123)
    stress = imbalance.rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.585625 + 0.0032752 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_352_rel_v352_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=106, w2=134, w3=357, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.6 + 0.0032753 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_353_rel_v353_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=113, w2=145, w3=370, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.614375 + 0.0032754 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_354_rel_v354_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=120, w2=156, w3=383, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.855625 + 0.0032755 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_355_rel_v355_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=127, w2=167, w3=396, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(167, min_periods=max(167//3, 2)).rank(pct=True)
    persistence = change.rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1726 * persistence + 0.0032756 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_356_rel_v356_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=134, w2=178, w3=409, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.884375 + 0.0032757 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_357_rel_v357_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=141, w2=189, w3=422, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(189, min_periods=max(189//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1878 * slope + 0.0032758 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_358_rel_v358_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=148, w2=200, w3=435, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.913125 + 0.0032759 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_359_rel_v359_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=155, w2=211, w3=448, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 211)
    curvature = _rolling_slope(acceleration, 448)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.203 * acceleration + 0.003276 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_360_rel_v360_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=162, w2=222, w3=461, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 162)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2106 * pressure.rolling(461, min_periods=max(461//3, 2)).mean() + 0.0032761 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_361_rel_v361_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=169, w2=233, w3=474, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(169, min_periods=max(169//3, 2)).mean())
    decay = spread.ewm(span=233, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.95625 + 0.0032762 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_362_rel_v362_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=176, w2=244, w3=487, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(244, min_periods=max(244//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 176)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.970625 + 0.0032763 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_363_rel_v363_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=183, w2=255, w3=500, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(183, min_periods=max(183//3, 2)).mean(), b.abs().rolling(255, min_periods=max(255//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2334 * _rolling_slope(cover, 183) + 0.0032764 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_364_rel_v364_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=190, w2=266, w3=513, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.241 * y + 0.759000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 190) - _rolling_slope(basket, 266) + 0.0032765 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_365_rel_v365_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=197, w2=277, w3=526, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.01375 + 0.0032766 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_366_rel_v366_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=204, w2=288, w3=539, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2562 * _rolling_slope(draw, 539) + 0.0032767 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_367_rel_v367_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=211, w2=299, w3=552, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0425 + 0.0032768 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_368_rel_v368_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=218, w2=310, w3=565, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(310, min_periods=max(310//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.056875 + 0.0032769 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_369_rel_v369_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=225, w2=321, w3=578, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.07125 + 0.003277 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_370_rel_v370_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=232, w2=332, w3=591, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.085625 + 0.0032771 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_371_rel_v371_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=239, w2=343, w3=604, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2942 * persistence + 0.0032772 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_372_rel_v372_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=246, w2=354, w3=617, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(354, min_periods=max(354//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.114375 + 0.0032773 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_373_rel_v373_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=253, w2=365, w3=630, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(365, min_periods=max(365//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3094 * slope + 0.0032774 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_374_rel_v374_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=9, w2=376, w3=643, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(9)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.143125 + 0.0032775 * anchor
    return base_signal.diff().diff()

def f53_rsw_v_375_rel_v375_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=16, w2=387, w3=656, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 387)
    curvature = _rolling_slope(acceleration, 656)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3246 * acceleration + 0.0032776 * anchor
    return base_signal.diff().diff()
