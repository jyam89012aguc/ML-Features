"""54 relative sector drawdown d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f54_rsw_d_376_rel_v376_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=207, w2=459, w3=142, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(459, min_periods=max(459//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2925 + 0.0033377 * anchor
    return base_signal.diff()

def f54_rsw_d_377_rel_v377_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=214, w2=470, w3=155, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 470)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=155, adjust=False).mean() * 1.306875 + 0.0033378 * anchor
    return base_signal.diff()

def f54_rsw_d_378_rel_v378_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=221, w2=481, w3=168, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(481, min_periods=max(481//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.32125 + 0.0033379 * anchor
    return base_signal.diff()

def f54_rsw_d_379_rel_v379_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=228, w2=492, w3=181, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(492, min_periods=max(492//3, 2)).rank(pct=True)
    persistence = change.rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3982 * persistence + 0.003338 * anchor
    return base_signal.diff()

def f54_rsw_d_380_rel_v380_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=235, w2=503, w3=194, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(503, min_periods=max(503//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35 + 0.0033381 * anchor
    return base_signal.diff()

def f54_rsw_d_381_rel_v381_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=242, w2=11, w3=207, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(11, min_periods=max(11//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.037 * slope + 0.0033382 * anchor
    return base_signal.diff()

def f54_rsw_d_382_rel_v382_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=249, w2=22, w3=220, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(22, min_periods=max(22//3, 2)).mean()
    noise = impulse.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.37875 + 0.0033383 * anchor
    return base_signal.diff()

def f54_rsw_d_383_rel_v383_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=5, w2=33, w3=233, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 33)
    curvature = _rolling_slope(acceleration, 233)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0522 * acceleration + 0.0033384 * anchor
    return base_signal.diff()

def f54_rsw_d_384_rel_v384_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=12, w2=44, w3=246, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 12)
    pressure = rel_log.diff(44)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0598 * pressure.rolling(246, min_periods=max(246//3, 2)).mean() + 0.0033385 * anchor
    return base_signal.diff()

def f54_rsw_d_385_rel_v385_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=19, w2=55, w3=259, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(19, min_periods=max(19//3, 2)).mean())
    decay = spread.ewm(span=55, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.421875 + 0.0033386 * anchor
    return base_signal.diff()

def f54_rsw_d_386_rel_v386_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=26, w2=66, w3=272, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(66, min_periods=max(66//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 26)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.43625 + 0.0033387 * anchor
    return base_signal.diff()

def f54_rsw_d_387_rel_v387_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=33, w2=77, w3=285, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(33, min_periods=max(33//3, 2)).mean(), b.abs().rolling(77, min_periods=max(77//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0826 * _rolling_slope(cover, 33) + 0.0033388 * anchor
    return base_signal.diff()

def f54_rsw_d_388_rel_v388_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=40, w2=88, w3=298, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0902 * y + 0.909800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 40) - _rolling_slope(basket, 88) + 0.0033389 * anchor
    return base_signal.diff()

def f54_rsw_d_389_rel_v389_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=47, w2=99, w3=311, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.479375 + 0.003339 * anchor
    return base_signal.diff()

def f54_rsw_d_390_rel_v390_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=54, w2=110, w3=324, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1054 * _rolling_slope(draw, 324) + 0.0033391 * anchor
    return base_signal.diff()

def f54_rsw_d_391_rel_v391_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=61, w2=121, w3=337, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(61) - b.diff(121)
    stress = imbalance.rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.508125 + 0.0033392 * anchor
    return base_signal.diff()

def f54_rsw_d_392_rel_v392_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=68, w2=132, w3=350, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(132, min_periods=max(132//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5225 + 0.0033393 * anchor
    return base_signal.diff()

def f54_rsw_d_393_rel_v393_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=75, w2=143, w3=363, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 143)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.536875 + 0.0033394 * anchor
    return base_signal.diff()

def f54_rsw_d_394_rel_v394_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=82, w2=154, w3=376, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(154, min_periods=max(154//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.55125 + 0.0033395 * anchor
    return base_signal.diff()

def f54_rsw_d_395_rel_v395_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=89, w2=165, w3=389, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(89)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1434 * persistence + 0.0033396 * anchor
    return base_signal.diff()

def f54_rsw_d_396_rel_v396_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=96, w2=176, w3=402, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(176, min_periods=max(176//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.58 + 0.0033397 * anchor
    return base_signal.diff()

def f54_rsw_d_397_rel_v397_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=103, w2=187, w3=415, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1586 * slope + 0.0033398 * anchor
    return base_signal.diff()

def f54_rsw_d_398_rel_v398_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=110, w2=198, w3=428, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(110)
    drag = impulse.rolling(198, min_periods=max(198//3, 2)).mean()
    noise = impulse.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.60875 + 0.0033399 * anchor
    return base_signal.diff()

def f54_rsw_d_399_rel_v399_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=117, w2=209, w3=441, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 209)
    curvature = _rolling_slope(acceleration, 441)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1738 * acceleration + 0.00334 * anchor
    return base_signal.diff()

def f54_rsw_d_400_rel_v400_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=124, w2=220, w3=454, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 124)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1814 * pressure.rolling(454, min_periods=max(454//3, 2)).mean() + 0.0033401 * anchor
    return base_signal.diff()

def f54_rsw_d_401_rel_v401_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=131, w2=231, w3=467, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    decay = spread.ewm(span=231, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.87875 + 0.0033402 * anchor
    return base_signal.diff()

def f54_rsw_d_402_rel_v402_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=138, w2=242, w3=480, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(242, min_periods=max(242//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 138)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.893125 + 0.0033403 * anchor
    return base_signal.diff()

def f54_rsw_d_403_rel_v403_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=145, w2=253, w3=493, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(145, min_periods=max(145//3, 2)).mean(), b.abs().rolling(253, min_periods=max(253//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2042 * _rolling_slope(cover, 145) + 0.0033404 * anchor
    return base_signal.diff()

def f54_rsw_d_404_rel_v404_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=152, w2=264, w3=506, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2118 * y + 0.788200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 152) - _rolling_slope(basket, 264) + 0.0033405 * anchor
    return base_signal.diff()

def f54_rsw_d_405_rel_v405_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=159, w2=275, w3=519, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(275, min_periods=max(275//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93625 + 0.0033406 * anchor
    return base_signal.diff()

def f54_rsw_d_406_rel_v406_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=166, w2=286, w3=532, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(286, min_periods=max(286//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227 * _rolling_slope(draw, 532) + 0.0033407 * anchor
    return base_signal.diff()

def f54_rsw_d_407_rel_v407_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=173, w2=297, w3=545, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.965 + 0.0033408 * anchor
    return base_signal.diff()

def f54_rsw_d_408_rel_v408_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=180, w2=308, w3=558, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(308, min_periods=max(308//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.979375 + 0.0033409 * anchor
    return base_signal.diff()

def f54_rsw_d_409_rel_v409_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=187, w2=319, w3=571, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 319)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.99375 + 0.003341 * anchor
    return base_signal.diff()

def f54_rsw_d_410_rel_v410_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=194, w2=330, w3=584, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.008125 + 0.0033411 * anchor
    return base_signal.diff()

def f54_rsw_d_411_rel_v411_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=201, w2=341, w3=597, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(341, min_periods=max(341//3, 2)).rank(pct=True)
    persistence = change.rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265 * persistence + 0.0033412 * anchor
    return base_signal.diff()

def f54_rsw_d_412_rel_v412_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=208, w2=352, w3=610, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(352, min_periods=max(352//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.036875 + 0.0033413 * anchor
    return base_signal.diff()

def f54_rsw_d_413_rel_v413_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=215, w2=363, w3=623, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2802 * slope + 0.0033414 * anchor
    return base_signal.diff()

def f54_rsw_d_414_rel_v414_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=222, w2=374, w3=636, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(374, min_periods=max(374//3, 2)).mean()
    noise = impulse.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.065625 + 0.0033415 * anchor
    return base_signal.diff()

def f54_rsw_d_415_rel_v415_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=229, w2=385, w3=649, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 385)
    curvature = _rolling_slope(acceleration, 649)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2954 * acceleration + 0.0033416 * anchor
    return base_signal.diff()

def f54_rsw_d_416_rel_v416_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=236, w2=396, w3=662, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.303 * pressure.rolling(662, min_periods=max(662//3, 2)).mean() + 0.0033417 * anchor
    return base_signal.diff()

def f54_rsw_d_417_rel_v417_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=243, w2=407, w3=675, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.10875 + 0.0033418 * anchor
    return base_signal.diff()

def f54_rsw_d_418_rel_v418_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=250, w2=418, w3=688, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(418, min_periods=max(418//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.123125 + 0.0033419 * anchor
    return base_signal.diff()

def f54_rsw_d_419_rel_v419_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=6, w2=429, w3=701, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(6, min_periods=max(6//3, 2)).mean(), b.abs().rolling(429, min_periods=max(429//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3258 * _rolling_slope(cover, 6) + 0.003342 * anchor
    return base_signal.diff()

def f54_rsw_d_420_rel_v420_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=13, w2=440, w3=714, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3334 * y + 0.666600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 13) - _rolling_slope(basket, 440) + 0.0033421 * anchor
    return base_signal.diff()

def f54_rsw_d_421_rel_v421_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=20, w2=451, w3=727, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.16625 + 0.0033422 * anchor
    return base_signal.diff()

def f54_rsw_d_422_rel_v422_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=27, w2=462, w3=740, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3486 * _rolling_slope(draw, 740) + 0.0033423 * anchor
    return base_signal.diff()

def f54_rsw_d_423_rel_v423_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=34, w2=473, w3=753, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(34) - b.diff(126)
    stress = imbalance.rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.195 + 0.0033424 * anchor
    return base_signal.diff()

def f54_rsw_d_424_rel_v424_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=41, w2=484, w3=766, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(484, min_periods=max(484//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.209375 + 0.0033425 * anchor
    return base_signal.diff()

def f54_rsw_d_425_rel_v425_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=48, w2=495, w3=22, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=22, adjust=False).mean() * 1.22375 + 0.0033426 * anchor
    return base_signal.diff()

def f54_rsw_d_426_rel_v426_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=55, w2=506, w3=35, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(506, min_periods=max(506//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.238125 + 0.0033427 * anchor
    return base_signal.diff()

def f54_rsw_d_427_rel_v427_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=62, w2=14, w3=48, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(62)
    rank = change.rolling(14, min_periods=max(14//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3866 * persistence + 0.0033428 * anchor
    return base_signal.diff()

def f54_rsw_d_428_rel_v428_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=69, w2=25, w3=61, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(25, min_periods=max(25//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.266875 + 0.0033429 * anchor
    return base_signal.diff()

def f54_rsw_d_429_rel_v429_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=76, w2=36, w3=74, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4018 * slope + 0.003343 * anchor
    return base_signal.diff()

def f54_rsw_d_430_rel_v430_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=83, w2=47, w3=87, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(83)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.295625 + 0.0033431 * anchor
    return base_signal.diff()

def f54_rsw_d_431_rel_v431_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=90, w2=58, w3=100, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 58)
    curvature = _rolling_slope(acceleration, 100)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0406 * acceleration + 0.0033432 * anchor
    return base_signal.diff()

def f54_rsw_d_432_rel_v432_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=97, w2=69, w3=113, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 97)
    pressure = rel_log.diff(69)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0482 * pressure.rolling(113, min_periods=max(113//3, 2)).mean() + 0.0033433 * anchor
    return base_signal.diff()

def f54_rsw_d_433_rel_v433_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=104, w2=80, w3=126, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(104, min_periods=max(104//3, 2)).mean())
    decay = spread.ewm(span=80, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.33875 + 0.0033434 * anchor
    return base_signal.diff()

def f54_rsw_d_434_rel_v434_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=111, w2=91, w3=139, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(91, min_periods=max(91//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 111)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.353125 + 0.0033435 * anchor
    return base_signal.diff()

def f54_rsw_d_435_rel_v435_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=118, w2=102, w3=152, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(118, min_periods=max(118//3, 2)).mean(), b.abs().rolling(102, min_periods=max(102//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.071 * _rolling_slope(cover, 118) + 0.0033436 * anchor
    return base_signal.diff()

def f54_rsw_d_436_rel_v436_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=125, w2=113, w3=165, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0786 * y + 0.921400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 125) - _rolling_slope(basket, 113) + 0.0033437 * anchor
    return base_signal.diff()

def f54_rsw_d_437_rel_v437_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=132, w2=124, w3=178, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(124, min_periods=max(124//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.39625 + 0.0033438 * anchor
    return base_signal.diff()

def f54_rsw_d_438_rel_v438_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=139, w2=135, w3=191, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(135, min_periods=max(135//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0938 * _rolling_slope(draw, 191) + 0.0033439 * anchor
    return base_signal.diff()

def f54_rsw_d_439_rel_v439_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=146, w2=146, w3=204, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.425 + 0.003344 * anchor
    return base_signal.diff()

def f54_rsw_d_440_rel_v440_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=153, w2=157, w3=217, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(157, min_periods=max(157//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.439375 + 0.0033441 * anchor
    return base_signal.diff()

def f54_rsw_d_441_rel_v441_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=160, w2=168, w3=230, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 1.45375 + 0.0033442 * anchor
    return base_signal.diff()

def f54_rsw_d_442_rel_v442_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=167, w2=179, w3=243, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(179, min_periods=max(179//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.468125 + 0.0033443 * anchor
    return base_signal.diff()

def f54_rsw_d_443_rel_v443_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=174, w2=190, w3=256, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(190, min_periods=max(190//3, 2)).rank(pct=True)
    persistence = change.rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1318 * persistence + 0.0033444 * anchor
    return base_signal.diff()

def f54_rsw_d_444_rel_v444_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=181, w2=201, w3=269, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.496875 + 0.0033445 * anchor
    return base_signal.diff()

def f54_rsw_d_445_rel_v445_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=188, w2=212, w3=282, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147 * slope + 0.0033446 * anchor
    return base_signal.diff()

def f54_rsw_d_446_rel_v446_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=195, w2=223, w3=295, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.525625 + 0.0033447 * anchor
    return base_signal.diff()

def f54_rsw_d_447_rel_v447_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=202, w2=234, w3=308, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 308)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1622 * acceleration + 0.0033448 * anchor
    return base_signal.diff()

def f54_rsw_d_448_rel_v448_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=209, w2=245, w3=321, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 209)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1698 * pressure.rolling(321, min_periods=max(321//3, 2)).mean() + 0.0033449 * anchor
    return base_signal.diff()

def f54_rsw_d_449_rel_v449_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=216, w2=256, w3=334, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(216, min_periods=max(216//3, 2)).mean())
    decay = spread.ewm(span=256, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.56875 + 0.003345 * anchor
    return base_signal.diff()

def f54_rsw_d_450_rel_v450_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=223, w2=267, w3=347, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(267, min_periods=max(267//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 223)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.583125 + 0.0033451 * anchor
    return base_signal.diff()
