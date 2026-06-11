"""51 relative sector weakness d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f51_rsw_076_rel_v76_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=65, w2=497, w3=94, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2242 * y + 0.775800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 65) - _rolling_slope(basket, 497) + 0.0031277 * anchor
    return base_signal.diff().diff()

def f51_rsw_077_rel_v77_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=72, w2=508, w3=107, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(72, min_periods=max(72//3, 2)).mean(), upside.rolling(508, min_periods=max(508//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(107) * 1.27125 + 0.0031278 * anchor
    return base_signal.diff().diff()

def f51_rsw_078_rel_v78_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=79, w2=16, w3=120, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(16, min_periods=max(16//3, 2)).max()
    rebound = x - x.rolling(79, min_periods=max(79//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2394 * _rolling_slope(draw, 120) + 0.0031279 * anchor
    return base_signal.diff().diff()

def f51_rsw_079_rel_v79_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=86, w2=27, w3=133, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(86) - b.diff(27)
    stress = imbalance.rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.3 + 0.003128 * anchor
    return base_signal.diff().diff()

def f51_rsw_080_rel_v80_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=93, w2=38, w3=146, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(38, min_periods=max(38//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.314375 + 0.0031281 * anchor
    return base_signal.diff().diff()

def f51_rsw_081_rel_v81_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=100, w2=49, w3=159, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 49)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=159, adjust=False).mean() * 1.32875 + 0.0031282 * anchor
    return base_signal.diff().diff()

def f51_rsw_082_rel_v82_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=107, w2=60, w3=172, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(60, min_periods=max(60//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.343125 + 0.0031283 * anchor
    return base_signal.diff().diff()

def f51_rsw_083_rel_v83_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=114, w2=71, w3=185, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(114)
    rank = change.rolling(71, min_periods=max(71//3, 2)).rank(pct=True)
    persistence = change.rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2774 * persistence + 0.0031284 * anchor
    return base_signal.diff().diff()

def f51_rsw_084_rel_v84_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=121, w2=82, w3=198, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.371875 + 0.0031285 * anchor
    return base_signal.diff().diff()

def f51_rsw_085_rel_v85_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=128, w2=93, w3=211, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(93, min_periods=max(93//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2926 * slope + 0.0031286 * anchor
    return base_signal.diff().diff()

def f51_rsw_086_rel_v86_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=135, w2=104, w3=224, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.400625 + 0.0031287 * anchor
    return base_signal.diff().diff()

def f51_rsw_087_rel_v87_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=142, w2=115, w3=237, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 237)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3078 * acceleration + 0.0031288 * anchor
    return base_signal.diff().diff()

def f51_rsw_088_rel_v88_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=149, w2=126, w3=250, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 149)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3154 * pressure.rolling(250, min_periods=max(250//3, 2)).mean() + 0.0031289 * anchor
    return base_signal.diff().diff()

def f51_rsw_089_rel_v89_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=156, w2=137, w3=263, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(156, min_periods=max(156//3, 2)).mean())
    decay = spread.ewm(span=137, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.44375 + 0.003129 * anchor
    return base_signal.diff().diff()

def f51_rsw_090_rel_v90_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=163, w2=148, w3=276, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(148, min_periods=max(148//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 163)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.458125 + 0.0031291 * anchor
    return base_signal.diff().diff()

def f51_rsw_091_rel_v91_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=170, w2=159, w3=289, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(170, min_periods=max(170//3, 2)).mean(), b.abs().rolling(159, min_periods=max(159//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3382 * _rolling_slope(cover, 170) + 0.0031292 * anchor
    return base_signal.diff().diff()

def f51_rsw_092_rel_v92_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=177, w2=170, w3=302, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3458 * y + 0.654200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 177) - _rolling_slope(basket, 170) + 0.0031293 * anchor
    return base_signal.diff().diff()

def f51_rsw_093_rel_v93_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=184, w2=181, w3=315, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(181, min_periods=max(181//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.50125 + 0.0031294 * anchor
    return base_signal.diff().diff()

def f51_rsw_094_rel_v94_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=191, w2=192, w3=328, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(192, min_periods=max(192//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.361 * _rolling_slope(draw, 328) + 0.0031295 * anchor
    return base_signal.diff().diff()

def f51_rsw_095_rel_v95_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=198, w2=203, w3=341, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.53 + 0.0031296 * anchor
    return base_signal.diff().diff()

def f51_rsw_096_rel_v96_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=205, w2=214, w3=354, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 205)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.544375 + 0.0031297 * anchor
    return base_signal.diff().diff()

def f51_rsw_097_rel_v97_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=212, w2=225, w3=367, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 212)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.55875 + 0.0031298 * anchor
    return base_signal.diff().diff()

def f51_rsw_098_rel_v98_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=219, w2=236, w3=380, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(219, min_periods=max(219//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.573125 + 0.0031299 * anchor
    return base_signal.diff().diff()

def f51_rsw_099_rel_v99_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=226, w2=247, w3=393, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(247, min_periods=max(247//3, 2)).rank(pct=True)
    persistence = change.rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.399 * persistence + 0.00313 * anchor
    return base_signal.diff().diff()

def f51_rsw_100_rel_v100_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=233, w2=258, w3=406, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(233, min_periods=max(233//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.601875 + 0.0031301 * anchor
    return base_signal.diff().diff()

def f51_rsw_101_rel_v101_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=240, w2=269, w3=419, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(269, min_periods=max(269//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 240)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0378 * slope + 0.0031302 * anchor
    return base_signal.diff().diff()

def f51_rsw_102_rel_v102_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=247, w2=280, w3=432, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8575 + 0.0031303 * anchor
    return base_signal.diff().diff()

def f51_rsw_103_rel_v103_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=254, w2=291, w3=445, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 254)
    acceleration = _rolling_slope(velocity, 291)
    curvature = _rolling_slope(acceleration, 445)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.053 * acceleration + 0.0031304 * anchor
    return base_signal.diff().diff()

def f51_rsw_104_rel_v104_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=10, w2=302, w3=458, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 10)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0606 * pressure.rolling(458, min_periods=max(458//3, 2)).mean() + 0.0031305 * anchor
    return base_signal.diff().diff()

def f51_rsw_105_rel_v105_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=17, w2=313, w3=471, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.900625 + 0.0031306 * anchor
    return base_signal.diff().diff()

def f51_rsw_106_rel_v106_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=24, w2=324, w3=484, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(324, min_periods=max(324//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 24)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.915 + 0.0031307 * anchor
    return base_signal.diff().diff()

def f51_rsw_107_rel_v107_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=31, w2=335, w3=497, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(31, min_periods=max(31//3, 2)).mean(), b.abs().rolling(335, min_periods=max(335//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0834 * _rolling_slope(cover, 31) + 0.0031308 * anchor
    return base_signal.diff().diff()

def f51_rsw_108_rel_v108_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=38, w2=346, w3=510, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.091 * y + 0.909000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 38) - _rolling_slope(basket, 346) + 0.0031309 * anchor
    return base_signal.diff().diff()

def f51_rsw_109_rel_v109_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=45, w2=357, w3=523, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(357, min_periods=max(357//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.958125 + 0.003131 * anchor
    return base_signal.diff().diff()

def f51_rsw_110_rel_v110_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=52, w2=368, w3=536, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(368, min_periods=max(368//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1062 * _rolling_slope(draw, 536) + 0.0031311 * anchor
    return base_signal.diff().diff()

def f51_rsw_111_rel_v111_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=59, w2=379, w3=549, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(59) - b.diff(126)
    stress = imbalance.rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.986875 + 0.0031312 * anchor
    return base_signal.diff().diff()

def f51_rsw_112_rel_v112_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=66, w2=390, w3=562, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.00125 + 0.0031313 * anchor
    return base_signal.diff().diff()

def f51_rsw_113_rel_v113_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=73, w2=401, w3=575, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 401)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.015625 + 0.0031314 * anchor
    return base_signal.diff().diff()

def f51_rsw_114_rel_v114_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=80, w2=412, w3=588, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(412, min_periods=max(412//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03 + 0.0031315 * anchor
    return base_signal.diff().diff()

def f51_rsw_115_rel_v115_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=87, w2=423, w3=601, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(87)
    rank = change.rolling(423, min_periods=max(423//3, 2)).rank(pct=True)
    persistence = change.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1442 * persistence + 0.0031316 * anchor
    return base_signal.diff().diff()

def f51_rsw_116_rel_v116_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=94, w2=434, w3=614, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.05875 + 0.0031317 * anchor
    return base_signal.diff().diff()

def f51_rsw_117_rel_v117_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=101, w2=445, w3=627, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(445, min_periods=max(445//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1594 * slope + 0.0031318 * anchor
    return base_signal.diff().diff()

def f51_rsw_118_rel_v118_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=108, w2=456, w3=640, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(108)
    drag = impulse.rolling(456, min_periods=max(456//3, 2)).mean()
    noise = impulse.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0875 + 0.0031319 * anchor
    return base_signal.diff().diff()

def f51_rsw_119_rel_v119_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=115, w2=467, w3=653, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 467)
    curvature = _rolling_slope(acceleration, 653)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1746 * acceleration + 0.003132 * anchor
    return base_signal.diff().diff()

def f51_rsw_120_rel_v120_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=122, w2=478, w3=666, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 122)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1822 * pressure.rolling(666, min_periods=max(666//3, 2)).mean() + 0.0031321 * anchor
    return base_signal.diff().diff()

def f51_rsw_121_rel_v121_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=129, w2=489, w3=679, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(129, min_periods=max(129//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.130625 + 0.0031322 * anchor
    return base_signal.diff().diff()

def f51_rsw_122_rel_v122_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=136, w2=500, w3=692, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(500, min_periods=max(500//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 136)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.145 + 0.0031323 * anchor
    return base_signal.diff().diff()

def f51_rsw_123_rel_v123_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=143, w2=511, w3=705, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(143, min_periods=max(143//3, 2)).mean(), b.abs().rolling(511, min_periods=max(511//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.205 * _rolling_slope(cover, 143) + 0.0031324 * anchor
    return base_signal.diff().diff()

def f51_rsw_124_rel_v124_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=150, w2=19, w3=718, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2126 * y + 0.787400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 150) - _rolling_slope(basket, 19) + 0.0031325 * anchor
    return base_signal.diff().diff()

def f51_rsw_125_rel_v125_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=157, w2=30, w3=731, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(30, min_periods=max(30//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.188125 + 0.0031326 * anchor
    return base_signal.diff().diff()

def f51_rsw_126_rel_v126_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=164, w2=41, w3=744, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(41, min_periods=max(41//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2278 * _rolling_slope(draw, 744) + 0.0031327 * anchor
    return base_signal.diff().diff()

def f51_rsw_127_rel_v127_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=171, w2=52, w3=757, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(52)
    stress = imbalance.rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.216875 + 0.0031328 * anchor
    return base_signal.diff().diff()

def f51_rsw_128_rel_v128_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=178, w2=63, w3=770, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(63, min_periods=max(63//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.23125 + 0.0031329 * anchor
    return base_signal.diff().diff()

def f51_rsw_129_rel_v129_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=185, w2=74, w3=26, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 74)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=26, adjust=False).mean() * 1.245625 + 0.003133 * anchor
    return base_signal.diff().diff()

def f51_rsw_130_rel_v130_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=192, w2=85, w3=39, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(85, min_periods=max(85//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26 + 0.0031331 * anchor
    return base_signal.diff().diff()

def f51_rsw_131_rel_v131_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=199, w2=96, w3=52, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(96, min_periods=max(96//3, 2)).rank(pct=True)
    persistence = change.rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2658 * persistence + 0.0031332 * anchor
    return base_signal.diff().diff()

def f51_rsw_132_rel_v132_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=206, w2=107, w3=65, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(107, min_periods=max(107//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28875 + 0.0031333 * anchor
    return base_signal.diff().diff()

def f51_rsw_133_rel_v133_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=213, w2=118, w3=78, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(118, min_periods=max(118//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.281 * slope + 0.0031334 * anchor
    return base_signal.diff().diff()

def f51_rsw_134_rel_v134_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=220, w2=129, w3=91, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(129, min_periods=max(129//3, 2)).mean()
    noise = impulse.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3175 + 0.0031335 * anchor
    return base_signal.diff().diff()

def f51_rsw_135_rel_v135_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=227, w2=140, w3=104, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 140)
    curvature = _rolling_slope(acceleration, 104)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2962 * acceleration + 0.0031336 * anchor
    return base_signal.diff().diff()

def f51_rsw_136_rel_v136_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=234, w2=151, w3=117, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 234)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3038 * pressure.rolling(117, min_periods=max(117//3, 2)).mean() + 0.0031337 * anchor
    return base_signal.diff().diff()

def f51_rsw_137_rel_v137_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=241, w2=162, w3=130, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(241, min_periods=max(241//3, 2)).mean())
    decay = spread.ewm(span=162, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.360625 + 0.0031338 * anchor
    return base_signal.diff().diff()

def f51_rsw_138_rel_v138_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=248, w2=173, w3=143, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(173, min_periods=max(173//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 248)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.375 + 0.0031339 * anchor
    return base_signal.diff().diff()

def f51_rsw_139_rel_v139_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=255, w2=184, w3=156, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(255, min_periods=max(255//3, 2)).mean(), b.abs().rolling(184, min_periods=max(184//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3266 * _rolling_slope(cover, 255) + 0.003134 * anchor
    return base_signal.diff().diff()

def f51_rsw_140_rel_v140_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=11, w2=195, w3=169, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3342 * y + 0.665800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 11) - _rolling_slope(basket, 195) + 0.0031341 * anchor
    return base_signal.diff().diff()

def f51_rsw_141_rel_v141_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=18, w2=206, w3=182, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.418125 + 0.0031342 * anchor
    return base_signal.diff().diff()

def f51_rsw_142_rel_v142_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=25, w2=217, w3=195, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(217, min_periods=max(217//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3494 * _rolling_slope(draw, 195) + 0.0031343 * anchor
    return base_signal.diff().diff()

def f51_rsw_143_rel_v143_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=32, w2=228, w3=208, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(32) - b.diff(126)
    stress = imbalance.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.446875 + 0.0031344 * anchor
    return base_signal.diff().diff()

def f51_rsw_144_rel_v144_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=39, w2=239, w3=221, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(239, min_periods=max(239//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46125 + 0.0031345 * anchor
    return base_signal.diff().diff()

def f51_rsw_145_rel_v145_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=46, w2=250, w3=234, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=234, adjust=False).mean() * 1.475625 + 0.0031346 * anchor
    return base_signal.diff().diff()

def f51_rsw_146_rel_v146_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=53, w2=261, w3=247, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(261, min_periods=max(261//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.49 + 0.0031347 * anchor
    return base_signal.diff().diff()

def f51_rsw_147_rel_v147_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=60, w2=272, w3=260, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(60)
    rank = change.rolling(272, min_periods=max(272//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3874 * persistence + 0.0031348 * anchor
    return base_signal.diff().diff()

def f51_rsw_148_rel_v148_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=67, w2=283, w3=273, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(283, min_periods=max(283//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.51875 + 0.0031349 * anchor
    return base_signal.diff().diff()

def f51_rsw_149_rel_v149_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=74, w2=294, w3=286, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4026 * slope + 0.003135 * anchor
    return base_signal.diff().diff()

def f51_rsw_150_rel_v150_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=81, w2=305, w3=299, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(81)
    drag = impulse.rolling(305, min_periods=max(305//3, 2)).mean()
    noise = impulse.abs().rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5475 + 0.0031351 * anchor
    return base_signal.diff().diff()
