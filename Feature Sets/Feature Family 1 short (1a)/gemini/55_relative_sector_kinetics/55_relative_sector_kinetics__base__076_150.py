"""55 relative sector kinetics base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f55_rsw_k_076_rel_v76(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=48, w2=238, w3=257, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.397 * y + 0.603000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 48) - _rolling_slope(basket, 238) + 0.0033677 * anchor

def f55_rsw_k_077_rel_v77(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=55, w2=249, w3=270, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(249, min_periods=max(249//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.980625 + 0.0033678 * anchor

def f55_rsw_k_078_rel_v78(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=62, w2=260, w3=283, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(260, min_periods=max(260//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0358 * _rolling_slope(draw, 283) + 0.0033679 * anchor

def f55_rsw_k_079_rel_v79(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=69, w2=271, w3=296, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(69) - b.diff(126)
    stress = imbalance.rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.009375 + 0.003368 * anchor

def f55_rsw_k_080_rel_v80(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=76, w2=282, w3=309, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(282, min_periods=max(282//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.02375 + 0.0033681 * anchor

def f55_rsw_k_081_rel_v81(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=83, w2=293, w3=322, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.038125 + 0.0033682 * anchor

def f55_rsw_k_082_rel_v82(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=90, w2=304, w3=335, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(304, min_periods=max(304//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0525 + 0.0033683 * anchor

def f55_rsw_k_083_rel_v83(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=97, w2=315, w3=348, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(97)
    rank = change.rolling(315, min_periods=max(315//3, 2)).rank(pct=True)
    persistence = change.rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0738 * persistence + 0.0033684 * anchor

def f55_rsw_k_084_rel_v84(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=104, w2=326, w3=361, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.08125 + 0.0033685 * anchor

def f55_rsw_k_085_rel_v85(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=111, w2=337, w3=374, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(337, min_periods=max(337//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.089 * slope + 0.0033686 * anchor

def f55_rsw_k_086_rel_v86(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=118, w2=348, w3=387, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(118)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.11 + 0.0033687 * anchor

def f55_rsw_k_087_rel_v87(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=125, w2=359, w3=400, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 400)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1042 * acceleration + 0.0033688 * anchor

def f55_rsw_k_088_rel_v88(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=132, w2=370, w3=413, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 132)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1118 * pressure.rolling(413, min_periods=max(413//3, 2)).mean() + 0.0033689 * anchor

def f55_rsw_k_089_rel_v89(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=139, w2=381, w3=426, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(139, min_periods=max(139//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.153125 + 0.003369 * anchor

def f55_rsw_k_090_rel_v90(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=146, w2=392, w3=439, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(392, min_periods=max(392//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 146)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.1675 + 0.0033691 * anchor

def f55_rsw_k_091_rel_v91(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=153, w2=403, w3=452, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(153, min_periods=max(153//3, 2)).mean(), b.abs().rolling(403, min_periods=max(403//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.1346 * _rolling_slope(cover, 153) + 0.0033692 * anchor

def f55_rsw_k_092_rel_v92(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=160, w2=414, w3=465, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1422 * y + 0.857800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 160) - _rolling_slope(basket, 414) + 0.0033693 * anchor

def f55_rsw_k_093_rel_v93(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=167, w2=425, w3=478, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.210625 + 0.0033694 * anchor

def f55_rsw_k_094_rel_v94(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=174, w2=436, w3=491, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1574 * _rolling_slope(draw, 491) + 0.0033695 * anchor

def f55_rsw_k_095_rel_v95(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=181, w2=447, w3=504, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.239375 + 0.0033696 * anchor

def f55_rsw_k_096_rel_v96(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=188, w2=458, w3=517, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 188)
    baseline = trend.rolling(458, min_periods=max(458//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.25375 + 0.0033697 * anchor

def f55_rsw_k_097_rel_v97(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=195, w2=469, w3=530, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 195)
    slow = _rolling_slope(x, 469)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.268125 + 0.0033698 * anchor

def f55_rsw_k_098_rel_v98(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=202, w2=480, w3=543, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(480, min_periods=max(480//3, 2)).max()
    trough = x.rolling(202, min_periods=max(202//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2825 + 0.0033699 * anchor

def f55_rsw_k_099_rel_v99(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=209, w2=491, w3=556, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(491, min_periods=max(491//3, 2)).rank(pct=True)
    persistence = change.rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1954 * persistence + 0.00337 * anchor

def f55_rsw_k_100_rel_v100(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=216, w2=502, w3=569, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(216, min_periods=max(216//3, 2)).std()
    vol_slow = ret.rolling(502, min_periods=max(502//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31125 + 0.0033701 * anchor

def f55_rsw_k_101_rel_v101(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=223, w2=10, w3=582, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(10, min_periods=max(10//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 223)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2106 * slope + 0.0033702 * anchor

def f55_rsw_k_102_rel_v102(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=230, w2=21, w3=595, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(21, min_periods=max(21//3, 2)).mean()
    noise = impulse.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.34 + 0.0033703 * anchor

def f55_rsw_k_103_rel_v103(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=237, w2=32, w3=608, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 237)
    acceleration = _rolling_slope(velocity, 32)
    curvature = _rolling_slope(acceleration, 608)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2258 * acceleration + 0.0033704 * anchor

def f55_rsw_k_104_rel_v104(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=244, w2=43, w3=621, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 244)
    pressure = rel_log.diff(43)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2334 * pressure.rolling(621, min_periods=max(621//3, 2)).mean() + 0.0033705 * anchor

def f55_rsw_k_105_rel_v105(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=251, w2=54, w3=634, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(251, min_periods=max(251//3, 2)).mean())
    decay = spread.ewm(span=54, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.383125 + 0.0033706 * anchor

def f55_rsw_k_106_rel_v106(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=7, w2=65, w3=647, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(65, min_periods=max(65//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 7)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.3975 + 0.0033707 * anchor

def f55_rsw_k_107_rel_v107(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=14, w2=76, w3=660, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(14, min_periods=max(14//3, 2)).mean(), b.abs().rolling(76, min_periods=max(76//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2562 * _rolling_slope(cover, 14) + 0.0033708 * anchor

def f55_rsw_k_108_rel_v108(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=21, w2=87, w3=673, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2638 * y + 0.736200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 21) - _rolling_slope(basket, 87) + 0.0033709 * anchor

def f55_rsw_k_109_rel_v109(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=28, w2=98, w3=686, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.440625 + 0.003371 * anchor

def f55_rsw_k_110_rel_v110(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=35, w2=109, w3=699, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(109, min_periods=max(109//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.279 * _rolling_slope(draw, 699) + 0.0033711 * anchor

def f55_rsw_k_111_rel_v111(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=42, w2=120, w3=712, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(42) - b.diff(120)
    stress = imbalance.rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.469375 + 0.0033712 * anchor

def f55_rsw_k_112_rel_v112(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=49, w2=131, w3=725, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(131, min_periods=max(131//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.48375 + 0.0033713 * anchor

def f55_rsw_k_113_rel_v113(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=56, w2=142, w3=738, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.498125 + 0.0033714 * anchor

def f55_rsw_k_114_rel_v114(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=63, w2=153, w3=751, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(153, min_periods=max(153//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5125 + 0.0033715 * anchor

def f55_rsw_k_115_rel_v115(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=70, w2=164, w3=764, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(70)
    rank = change.rolling(164, min_periods=max(164//3, 2)).rank(pct=True)
    persistence = change.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.317 * persistence + 0.0033716 * anchor

def f55_rsw_k_116_rel_v116(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=77, w2=175, w3=20, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54125 + 0.0033717 * anchor

def f55_rsw_k_117_rel_v117(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=84, w2=186, w3=33, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(186, min_periods=max(186//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3322 * slope + 0.0033718 * anchor

def f55_rsw_k_118_rel_v118(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=91, w2=197, w3=46, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(91)
    drag = impulse.rolling(197, min_periods=max(197//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.57 + 0.0033719 * anchor

def f55_rsw_k_119_rel_v119(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=98, w2=208, w3=59, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 208)
    curvature = _rolling_slope(acceleration, 59)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3474 * acceleration + 0.003372 * anchor

def f55_rsw_k_120_rel_v120(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=105, w2=219, w3=72, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 105)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.355 * pressure.rolling(72, min_periods=max(72//3, 2)).mean() + 0.0033721 * anchor

def f55_rsw_k_121_rel_v121(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=112, w2=230, w3=85, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(112, min_periods=max(112//3, 2)).mean())
    decay = spread.ewm(span=230, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.613125 + 0.0033722 * anchor

def f55_rsw_k_122_rel_v122(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=119, w2=241, w3=98, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(241, min_periods=max(241//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 119)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.854375 + 0.0033723 * anchor

def f55_rsw_k_123_rel_v123(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=126, w2=252, w3=111, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(126, min_periods=max(126//3, 2)).mean(), b.abs().rolling(252, min_periods=max(252//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(111) + 0.3778 * _rolling_slope(cover, 126) + 0.0033724 * anchor

def f55_rsw_k_124_rel_v124(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=133, w2=263, w3=124, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3854 * y + 0.614600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 133) - _rolling_slope(basket, 263) + 0.0033725 * anchor

def f55_rsw_k_125_rel_v125(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=140, w2=274, w3=137, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(274, min_periods=max(274//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8975 + 0.0033726 * anchor

def f55_rsw_k_126_rel_v126(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=147, w2=285, w3=150, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(285, min_periods=max(285//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4006 * _rolling_slope(draw, 150) + 0.0033727 * anchor

def f55_rsw_k_127_rel_v127(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=154, w2=296, w3=163, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.92625 + 0.0033728 * anchor

def f55_rsw_k_128_rel_v128(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=161, w2=307, w3=176, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.940625 + 0.0033729 * anchor

def f55_rsw_k_129_rel_v129(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=168, w2=318, w3=189, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=189, adjust=False).mean() * 0.955 + 0.003373 * anchor

def f55_rsw_k_130_rel_v130(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=175, w2=329, w3=202, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(329, min_periods=max(329//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.969375 + 0.0033731 * anchor

def f55_rsw_k_131_rel_v131(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=182, w2=340, w3=215, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(340, min_periods=max(340//3, 2)).rank(pct=True)
    persistence = change.rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0622 * persistence + 0.0033732 * anchor

def f55_rsw_k_132_rel_v132(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=189, w2=351, w3=228, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(351, min_periods=max(351//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.998125 + 0.0033733 * anchor

def f55_rsw_k_133_rel_v133(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=196, w2=362, w3=241, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(362, min_periods=max(362//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0774 * slope + 0.0033734 * anchor

def f55_rsw_k_134_rel_v134(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=203, w2=373, w3=254, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(373, min_periods=max(373//3, 2)).mean()
    noise = impulse.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.026875 + 0.0033735 * anchor

def f55_rsw_k_135_rel_v135(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=210, w2=384, w3=267, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 384)
    curvature = _rolling_slope(acceleration, 267)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0926 * acceleration + 0.0033736 * anchor

def f55_rsw_k_136_rel_v136(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=217, w2=395, w3=280, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 217)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1002 * pressure.rolling(280, min_periods=max(280//3, 2)).mean() + 0.0033737 * anchor

def f55_rsw_k_137_rel_v137(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=224, w2=406, w3=293, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(224, min_periods=max(224//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.07 + 0.0033738 * anchor

def f55_rsw_k_138_rel_v138(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=231, w2=417, w3=306, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(417, min_periods=max(417//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 231)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.084375 + 0.0033739 * anchor

def f55_rsw_k_139_rel_v139(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=238, w2=428, w3=319, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(238, min_periods=max(238//3, 2)).mean(), b.abs().rolling(428, min_periods=max(428//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.123 * _rolling_slope(cover, 238) + 0.003374 * anchor

def f55_rsw_k_140_rel_v140(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=245, w2=439, w3=332, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1306 * y + 0.869400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 245) - _rolling_slope(basket, 439) + 0.0033741 * anchor

def f55_rsw_k_141_rel_v141(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=252, w2=450, w3=345, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1275 + 0.0033742 * anchor

def f55_rsw_k_142_rel_v142(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=8, w2=461, w3=358, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1458 * _rolling_slope(draw, 358) + 0.0033743 * anchor

def f55_rsw_k_143_rel_v143(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=15, w2=472, w3=371, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(15) - b.diff(126)
    stress = imbalance.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.15625 + 0.0033744 * anchor

def f55_rsw_k_144_rel_v144(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=22, w2=483, w3=384, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.170625 + 0.0033745 * anchor

def f55_rsw_k_145_rel_v145(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=29, w2=494, w3=397, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 494)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.185 + 0.0033746 * anchor

def f55_rsw_k_146_rel_v146(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=36, w2=505, w3=410, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.199375 + 0.0033747 * anchor

def f55_rsw_k_147_rel_v147(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=43, w2=13, w3=423, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(43)
    rank = change.rolling(13, min_periods=max(13//3, 2)).rank(pct=True)
    persistence = change.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1838 * persistence + 0.0033748 * anchor

def f55_rsw_k_148_rel_v148(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=50, w2=24, w3=436, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(24, min_periods=max(24//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.228125 + 0.0033749 * anchor

def f55_rsw_k_149_rel_v149(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=57, w2=35, w3=449, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.199 * slope + 0.003375 * anchor

def f55_rsw_k_150_rel_v150(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=64, w2=46, w3=462, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(64)
    drag = impulse.rolling(46, min_periods=max(46//3, 2)).mean()
    noise = impulse.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.256875 + 0.0033751 * anchor
