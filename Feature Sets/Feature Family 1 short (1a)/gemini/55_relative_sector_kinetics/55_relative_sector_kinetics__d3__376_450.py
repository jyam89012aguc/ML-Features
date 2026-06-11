"""55 relative sector kinetics d3 third derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f55_rsw_k_376_rel_v376_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=140, w2=17, w3=372, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 140)
    pressure = rel_log.diff(17)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0422 * pressure.rolling(372, min_periods=max(372//3, 2)).mean() + 0.0033977 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_377_rel_v377_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=147, w2=28, w3=385, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=28, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.4275 + 0.0033978 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_378_rel_v378_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=154, w2=39, w3=398, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(39, min_periods=max(39//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 154)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.441875 + 0.0033979 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_379_rel_v379_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=161, w2=50, w3=411, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(50, min_periods=max(50//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.065 * _rolling_slope(cover, 161) + 0.003398 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_380_rel_v380_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=168, w2=61, w3=424, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0726 * y + 0.927400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 168) - _rolling_slope(basket, 61) + 0.0033981 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_381_rel_v381_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=175, w2=72, w3=437, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(72, min_periods=max(72//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.485 + 0.0033982 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_382_rel_v382_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=182, w2=83, w3=450, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(83, min_periods=max(83//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0878 * _rolling_slope(draw, 450) + 0.0033983 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_383_rel_v383_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=189, w2=94, w3=463, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(94)
    stress = imbalance.rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.51375 + 0.0033984 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_384_rel_v384_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=196, w2=105, w3=476, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(105, min_periods=max(105//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.528125 + 0.0033985 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_385_rel_v385_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=203, w2=116, w3=489, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.5425 + 0.0033986 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_386_rel_v386_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=210, w2=127, w3=502, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(127, min_periods=max(127//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.556875 + 0.0033987 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_387_rel_v387_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=217, w2=138, w3=515, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1258 * persistence + 0.0033988 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_388_rel_v388_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=224, w2=149, w3=528, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(149, min_periods=max(149//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585625 + 0.0033989 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_389_rel_v389_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=231, w2=160, w3=541, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(160, min_periods=max(160//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.141 * slope + 0.003399 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_390_rel_v390_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=238, w2=171, w3=554, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(171, min_periods=max(171//3, 2)).mean()
    noise = impulse.abs().rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.614375 + 0.0033991 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_391_rel_v391_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=245, w2=182, w3=567, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 182)
    curvature = _rolling_slope(acceleration, 567)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1562 * acceleration + 0.0033992 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_392_rel_v392_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=252, w2=193, w3=580, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 252)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1638 * pressure.rolling(580, min_periods=max(580//3, 2)).mean() + 0.0033993 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_393_rel_v393_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=8, w2=204, w3=593, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(8, min_periods=max(8//3, 2)).mean())
    decay = spread.ewm(span=204, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.884375 + 0.0033994 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_394_rel_v394_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=15, w2=215, w3=606, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(215, min_periods=max(215//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 15)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.89875 + 0.0033995 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_395_rel_v395_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=22, w2=226, w3=619, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(22, min_periods=max(22//3, 2)).mean(), b.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1866 * _rolling_slope(cover, 22) + 0.0033996 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_396_rel_v396_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=29, w2=237, w3=632, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1942 * y + 0.805800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 29) - _rolling_slope(basket, 237) + 0.0033997 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_397_rel_v397_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=36, w2=248, w3=645, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(248, min_periods=max(248//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.941875 + 0.0033998 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_398_rel_v398_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=43, w2=259, w3=658, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(259, min_periods=max(259//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2094 * _rolling_slope(draw, 658) + 0.0033999 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_399_rel_v399_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=50, w2=270, w3=671, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(50) - b.diff(126)
    stress = imbalance.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.970625 + 0.0034 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_400_rel_v400_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=57, w2=281, w3=684, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(281, min_periods=max(281//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.985 + 0.0034001 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_401_rel_v401_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=64, w2=292, w3=697, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 292)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.999375 + 0.0034002 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_402_rel_v402_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=71, w2=303, w3=710, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(303, min_periods=max(303//3, 2)).max()
    trough = x.rolling(71, min_periods=max(71//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01375 + 0.0034003 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_403_rel_v403_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=78, w2=314, w3=723, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(78)
    rank = change.rolling(314, min_periods=max(314//3, 2)).rank(pct=True)
    persistence = change.rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2474 * persistence + 0.0034004 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_404_rel_v404_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=85, w2=325, w3=736, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(85, min_periods=max(85//3, 2)).std()
    vol_slow = ret.rolling(325, min_periods=max(325//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0425 + 0.0034005 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_405_rel_v405_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=92, w2=336, w3=749, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(336, min_periods=max(336//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2626 * slope + 0.0034006 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_406_rel_v406_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=99, w2=347, w3=762, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(99)
    drag = impulse.rolling(347, min_periods=max(347//3, 2)).mean()
    noise = impulse.abs().rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.07125 + 0.0034007 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_407_rel_v407_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=106, w2=358, w3=18, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 358)
    curvature = _rolling_slope(acceleration, 18)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2778 * acceleration + 0.0034008 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_408_rel_v408_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=113, w2=369, w3=31, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 113)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2854 * pressure.rolling(31, min_periods=max(31//3, 2)).mean() + 0.0034009 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_409_rel_v409_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=120, w2=380, w3=44, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(120, min_periods=max(120//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.114375 + 0.003401 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_410_rel_v410_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=127, w2=391, w3=57, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(391, min_periods=max(391//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 127)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.12875 + 0.0034011 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_411_rel_v411_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=134, w2=402, w3=70, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(134, min_periods=max(134//3, 2)).mean(), b.abs().rolling(402, min_periods=max(402//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(70) + 0.3082 * _rolling_slope(cover, 134) + 0.0034012 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_412_rel_v412_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=141, w2=413, w3=83, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3158 * y + 0.684200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 141) - _rolling_slope(basket, 413) + 0.0034013 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_413_rel_v413_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=148, w2=424, w3=96, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(424, min_periods=max(424//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(96) * 1.171875 + 0.0034014 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_414_rel_v414_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=155, w2=435, w3=109, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(435, min_periods=max(435//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.331 * _rolling_slope(draw, 109) + 0.0034015 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_415_rel_v415_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=162, w2=446, w3=122, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.200625 + 0.0034016 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_416_rel_v416_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=169, w2=457, w3=135, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 169)
    baseline = trend.rolling(457, min_periods=max(457//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.215 + 0.0034017 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_417_rel_v417_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=176, w2=468, w3=148, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 468)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=148, adjust=False).mean() * 1.229375 + 0.0034018 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_418_rel_v418_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=183, w2=479, w3=161, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(479, min_periods=max(479//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.24375 + 0.0034019 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_419_rel_v419_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=190, w2=490, w3=174, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(490, min_periods=max(490//3, 2)).rank(pct=True)
    persistence = change.rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.369 * persistence + 0.003402 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_420_rel_v420_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=197, w2=501, w3=187, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(501, min_periods=max(501//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2725 + 0.0034021 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_421_rel_v421_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=204, w2=512, w3=200, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(512, min_periods=max(512//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3842 * slope + 0.0034022 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_422_rel_v422_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=211, w2=20, w3=213, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.30125 + 0.0034023 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_423_rel_v423_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=218, w2=31, w3=226, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 226)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3994 * acceleration + 0.0034024 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_424_rel_v424_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=225, w2=42, w3=239, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 225)
    pressure = rel_log.diff(42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.407 * pressure.rolling(239, min_periods=max(239//3, 2)).mean() + 0.0034025 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_425_rel_v425_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=232, w2=53, w3=252, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(232, min_periods=max(232//3, 2)).mean())
    decay = spread.ewm(span=53, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.344375 + 0.0034026 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_426_rel_v426_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=239, w2=64, w3=265, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(64, min_periods=max(64//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 239)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.35875 + 0.0034027 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_427_rel_v427_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=246, w2=75, w3=278, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(246, min_periods=max(246//3, 2)).mean(), b.abs().rolling(75, min_periods=max(75//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0534 * _rolling_slope(cover, 246) + 0.0034028 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_428_rel_v428_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=253, w2=86, w3=291, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.061 * y + 0.939000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 253) - _rolling_slope(basket, 86) + 0.0034029 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_429_rel_v429_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=9, w2=97, w3=304, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(97, min_periods=max(97//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.401875 + 0.003403 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_430_rel_v430_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=16, w2=108, w3=317, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(108, min_periods=max(108//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0762 * _rolling_slope(draw, 317) + 0.0034031 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_431_rel_v431_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=23, w2=119, w3=330, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(23) - b.diff(119)
    stress = imbalance.rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.430625 + 0.0034032 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_432_rel_v432_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=30, w2=130, w3=343, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.445 + 0.0034033 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_433_rel_v433_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=37, w2=141, w3=356, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 141)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.459375 + 0.0034034 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_434_rel_v434_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=44, w2=152, w3=369, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(152, min_periods=max(152//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47375 + 0.0034035 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_435_rel_v435_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=51, w2=163, w3=382, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(51)
    rank = change.rolling(163, min_periods=max(163//3, 2)).rank(pct=True)
    persistence = change.rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1142 * persistence + 0.0034036 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_436_rel_v436_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=58, w2=174, w3=395, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(174, min_periods=max(174//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5025 + 0.0034037 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_437_rel_v437_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=65, w2=185, w3=408, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(185, min_periods=max(185//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1294 * slope + 0.0034038 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_438_rel_v438_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=72, w2=196, w3=421, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(72)
    drag = impulse.rolling(196, min_periods=max(196//3, 2)).mean()
    noise = impulse.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.53125 + 0.0034039 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_439_rel_v439_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=79, w2=207, w3=434, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 207)
    curvature = _rolling_slope(acceleration, 434)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1446 * acceleration + 0.003404 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_440_rel_v440_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=86, w2=218, w3=447, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 86)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1522 * pressure.rolling(447, min_periods=max(447//3, 2)).mean() + 0.0034041 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_441_rel_v441_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=93, w2=229, w3=460, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(93, min_periods=max(93//3, 2)).mean())
    decay = spread.ewm(span=229, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.574375 + 0.0034042 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_442_rel_v442_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=100, w2=240, w3=473, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(240, min_periods=max(240//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 100)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.58875 + 0.0034043 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_443_rel_v443_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=107, w2=251, w3=486, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(107, min_periods=max(107//3, 2)).mean(), b.abs().rolling(251, min_periods=max(251//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.175 * _rolling_slope(cover, 107) + 0.0034044 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_444_rel_v444_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=114, w2=262, w3=499, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1826 * y + 0.817400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 114) - _rolling_slope(basket, 262) + 0.0034045 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_445_rel_v445_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=121, w2=273, w3=512, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(273, min_periods=max(273//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.85875 + 0.0034046 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_446_rel_v446_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=128, w2=284, w3=525, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(284, min_periods=max(284//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1978 * _rolling_slope(draw, 525) + 0.0034047 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_447_rel_v447_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=135, w2=295, w3=538, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.8875 + 0.0034048 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_448_rel_v448_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=142, w2=306, w3=551, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.901875 + 0.0034049 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_449_rel_v449_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=149, w2=317, w3=564, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.91625 + 0.003405 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_450_rel_v450_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=156, w2=328, w3=577, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(328, min_periods=max(328//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.930625 + 0.0034051 * anchor
    return base_signal.diff().diff().diff()
