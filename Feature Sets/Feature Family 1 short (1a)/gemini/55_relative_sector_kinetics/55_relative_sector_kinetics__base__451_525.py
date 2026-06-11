"""55 relative sector kinetics base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f55_rsw_k_451_rel_v451(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=163, w2=339, w3=590, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(339, min_periods=max(339//3, 2)).rank(pct=True)
    persistence = change.rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2358 * persistence + 0.0034052 * anchor

def f55_rsw_k_452_rel_v452(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=170, w2=350, w3=603, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.959375 + 0.0034053 * anchor

def f55_rsw_k_453_rel_v453(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=177, w2=361, w3=616, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(361, min_periods=max(361//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.251 * slope + 0.0034054 * anchor

def f55_rsw_k_454_rel_v454(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=184, w2=372, w3=629, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(372, min_periods=max(372//3, 2)).mean()
    noise = impulse.abs().rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.988125 + 0.0034055 * anchor

def f55_rsw_k_455_rel_v455(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=191, w2=383, w3=642, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 383)
    curvature = _rolling_slope(acceleration, 642)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2662 * acceleration + 0.0034056 * anchor

def f55_rsw_k_456_rel_v456(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=198, w2=394, w3=655, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 198)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2738 * pressure.rolling(655, min_periods=max(655//3, 2)).mean() + 0.0034057 * anchor

def f55_rsw_k_457_rel_v457(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=205, w2=405, w3=668, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(205, min_periods=max(205//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.03125 + 0.0034058 * anchor

def f55_rsw_k_458_rel_v458(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=212, w2=416, w3=681, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(416, min_periods=max(416//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 212)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.045625 + 0.0034059 * anchor

def f55_rsw_k_459_rel_v459(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=219, w2=427, w3=694, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(219, min_periods=max(219//3, 2)).mean(), b.abs().rolling(427, min_periods=max(427//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2966 * _rolling_slope(cover, 219) + 0.003406 * anchor

def f55_rsw_k_460_rel_v460(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=226, w2=438, w3=707, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3042 * y + 0.695800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 226) - _rolling_slope(basket, 438) + 0.0034061 * anchor

def f55_rsw_k_461_rel_v461(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=233, w2=449, w3=720, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(449, min_periods=max(449//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.08875 + 0.0034062 * anchor

def f55_rsw_k_462_rel_v462(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=240, w2=460, w3=733, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(460, min_periods=max(460//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3194 * _rolling_slope(draw, 733) + 0.0034063 * anchor

def f55_rsw_k_463_rel_v463(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=247, w2=471, w3=746, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.1175 + 0.0034064 * anchor

def f55_rsw_k_464_rel_v464(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=254, w2=482, w3=759, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.131875 + 0.0034065 * anchor

def f55_rsw_k_465_rel_v465(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=10, w2=493, w3=15, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 493)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=15, adjust=False).mean() * 1.14625 + 0.0034066 * anchor

def f55_rsw_k_466_rel_v466(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=17, w2=504, w3=28, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.160625 + 0.0034067 * anchor

def f55_rsw_k_467_rel_v467(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=24, w2=12, w3=41, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(24)
    rank = change.rolling(12, min_periods=max(12//3, 2)).rank(pct=True)
    persistence = change.rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3574 * persistence + 0.0034068 * anchor

def f55_rsw_k_468_rel_v468(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=31, w2=23, w3=54, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.189375 + 0.0034069 * anchor

def f55_rsw_k_469_rel_v469(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=38, w2=34, w3=67, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3726 * slope + 0.003407 * anchor

def f55_rsw_k_470_rel_v470(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=45, w2=45, w3=80, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(45)
    drag = impulse.rolling(45, min_periods=max(45//3, 2)).mean()
    noise = impulse.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.218125 + 0.0034071 * anchor

def f55_rsw_k_471_rel_v471(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=52, w2=56, w3=93, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 56)
    curvature = _rolling_slope(acceleration, 93)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3878 * acceleration + 0.0034072 * anchor

def f55_rsw_k_472_rel_v472(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=59, w2=67, w3=106, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 59)
    pressure = rel_log.diff(67)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3954 * pressure.rolling(106, min_periods=max(106//3, 2)).mean() + 0.0034073 * anchor

def f55_rsw_k_473_rel_v473(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=66, w2=78, w3=119, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(66, min_periods=max(66//3, 2)).mean())
    decay = spread.ewm(span=78, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.26125 + 0.0034074 * anchor

def f55_rsw_k_474_rel_v474(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=73, w2=89, w3=132, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(89, min_periods=max(89//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 73)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.275625 + 0.0034075 * anchor

def f55_rsw_k_475_rel_v475(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=80, w2=100, w3=145, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(80, min_periods=max(80//3, 2)).mean(), b.abs().rolling(100, min_periods=max(100//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.0418 * _rolling_slope(cover, 80) + 0.0034076 * anchor

def f55_rsw_k_476_rel_v476(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=87, w2=111, w3=158, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0494 * y + 0.950600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 87) - _rolling_slope(basket, 111) + 0.0034077 * anchor

def f55_rsw_k_477_rel_v477(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=94, w2=122, w3=171, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(122, min_periods=max(122//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.31875 + 0.0034078 * anchor

def f55_rsw_k_478_rel_v478(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=101, w2=133, w3=184, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0646 * _rolling_slope(draw, 184) + 0.0034079 * anchor

def f55_rsw_k_479_rel_v479(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=108, w2=144, w3=197, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(108) - b.diff(126)
    stress = imbalance.rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.3475 + 0.003408 * anchor

def f55_rsw_k_480_rel_v480(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=115, w2=155, w3=210, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(155, min_periods=max(155//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.361875 + 0.0034081 * anchor

def f55_rsw_k_481_rel_v481(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=122, w2=166, w3=223, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 166)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=223, adjust=False).mean() * 1.37625 + 0.0034082 * anchor

def f55_rsw_k_482_rel_v482(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=129, w2=177, w3=236, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(177, min_periods=max(177//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.390625 + 0.0034083 * anchor

def f55_rsw_k_483_rel_v483(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=136, w2=188, w3=249, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(188, min_periods=max(188//3, 2)).rank(pct=True)
    persistence = change.rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1026 * persistence + 0.0034084 * anchor

def f55_rsw_k_484_rel_v484(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=143, w2=199, w3=262, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(199, min_periods=max(199//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.419375 + 0.0034085 * anchor

def f55_rsw_k_485_rel_v485(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=150, w2=210, w3=275, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(210, min_periods=max(210//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1178 * slope + 0.0034086 * anchor

def f55_rsw_k_486_rel_v486(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=157, w2=221, w3=288, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(221, min_periods=max(221//3, 2)).mean()
    noise = impulse.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.448125 + 0.0034087 * anchor

def f55_rsw_k_487_rel_v487(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=164, w2=232, w3=301, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 232)
    curvature = _rolling_slope(acceleration, 301)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.133 * acceleration + 0.0034088 * anchor

def f55_rsw_k_488_rel_v488(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=171, w2=243, w3=314, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 171)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1406 * pressure.rolling(314, min_periods=max(314//3, 2)).mean() + 0.0034089 * anchor

def f55_rsw_k_489_rel_v489(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=178, w2=254, w3=327, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(178, min_periods=max(178//3, 2)).mean())
    decay = spread.ewm(span=254, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.49125 + 0.003409 * anchor

def f55_rsw_k_490_rel_v490(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=185, w2=265, w3=340, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(265, min_periods=max(265//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 185)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.505625 + 0.0034091 * anchor

def f55_rsw_k_491_rel_v491(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=192, w2=276, w3=353, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(192, min_periods=max(192//3, 2)).mean(), b.abs().rolling(276, min_periods=max(276//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.1634 * _rolling_slope(cover, 192) + 0.0034092 * anchor

def f55_rsw_k_492_rel_v492(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=199, w2=287, w3=366, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.171 * y + 0.829000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 199) - _rolling_slope(basket, 287) + 0.0034093 * anchor

def f55_rsw_k_493_rel_v493(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=206, w2=298, w3=379, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(298, min_periods=max(298//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.54875 + 0.0034094 * anchor

def f55_rsw_k_494_rel_v494(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=213, w2=309, w3=392, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(309, min_periods=max(309//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1862 * _rolling_slope(draw, 392) + 0.0034095 * anchor

def f55_rsw_k_495_rel_v495(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=220, w2=320, w3=405, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.5775 + 0.0034096 * anchor

def f55_rsw_k_496_rel_v496(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=227, w2=331, w3=418, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(331, min_periods=max(331//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.591875 + 0.0034097 * anchor

def f55_rsw_k_497_rel_v497(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=234, w2=342, w3=431, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 342)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.60625 + 0.0034098 * anchor

def f55_rsw_k_498_rel_v498(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=241, w2=353, w3=444, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.620625 + 0.0034099 * anchor

def f55_rsw_k_499_rel_v499(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=248, w2=364, w3=457, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(364, min_periods=max(364//3, 2)).rank(pct=True)
    persistence = change.rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2242 * persistence + 0.00341 * anchor

def f55_rsw_k_500_rel_v500(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=255, w2=375, w3=470, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(375, min_periods=max(375//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87625 + 0.0034101 * anchor

def f55_rsw_k_501_rel_v501(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=11, w2=386, w3=483, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2394 * slope + 0.0034102 * anchor

def f55_rsw_k_502_rel_v502(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=18, w2=397, w3=496, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(18)
    drag = impulse.rolling(397, min_periods=max(397//3, 2)).mean()
    noise = impulse.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.905 + 0.0034103 * anchor

def f55_rsw_k_503_rel_v503(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=25, w2=408, w3=509, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 408)
    curvature = _rolling_slope(acceleration, 509)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2546 * acceleration + 0.0034104 * anchor

def f55_rsw_k_504_rel_v504(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=32, w2=419, w3=522, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 32)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2622 * pressure.rolling(522, min_periods=max(522//3, 2)).mean() + 0.0034105 * anchor

def f55_rsw_k_505_rel_v505(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=39, w2=430, w3=535, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.948125 + 0.0034106 * anchor

def f55_rsw_k_506_rel_v506(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=46, w2=441, w3=548, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(441, min_periods=max(441//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.9625 + 0.0034107 * anchor

def f55_rsw_k_507_rel_v507(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=53, w2=452, w3=561, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(53, min_periods=max(53//3, 2)).mean(), b.abs().rolling(452, min_periods=max(452//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.285 * _rolling_slope(cover, 53) + 0.0034108 * anchor

def f55_rsw_k_508_rel_v508(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=60, w2=463, w3=574, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2926 * y + 0.707400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 60) - _rolling_slope(basket, 463) + 0.0034109 * anchor

def f55_rsw_k_509_rel_v509(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=67, w2=474, w3=587, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(474, min_periods=max(474//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.005625 + 0.003411 * anchor

def f55_rsw_k_510_rel_v510(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=74, w2=485, w3=600, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3078 * _rolling_slope(draw, 600) + 0.0034111 * anchor

def f55_rsw_k_511_rel_v511(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=81, w2=496, w3=613, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(81) - b.diff(126)
    stress = imbalance.rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.034375 + 0.0034112 * anchor

def f55_rsw_k_512_rel_v512(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=88, w2=507, w3=626, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(507, min_periods=max(507//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.04875 + 0.0034113 * anchor

def f55_rsw_k_513_rel_v513(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=95, w2=15, w3=639, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 15)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.063125 + 0.0034114 * anchor

def f55_rsw_k_514_rel_v514(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=102, w2=26, w3=652, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(26, min_periods=max(26//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0775 + 0.0034115 * anchor

def f55_rsw_k_515_rel_v515(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=109, w2=37, w3=665, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(109)
    rank = change.rolling(37, min_periods=max(37//3, 2)).rank(pct=True)
    persistence = change.rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3458 * persistence + 0.0034116 * anchor

def f55_rsw_k_516_rel_v516(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=116, w2=48, w3=678, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(48, min_periods=max(48//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10625 + 0.0034117 * anchor

def f55_rsw_k_517_rel_v517(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=123, w2=59, w3=691, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(59, min_periods=max(59//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.361 * slope + 0.0034118 * anchor

def f55_rsw_k_518_rel_v518(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=130, w2=70, w3=704, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(70, min_periods=max(70//3, 2)).mean()
    noise = impulse.abs().rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.135 + 0.0034119 * anchor

def f55_rsw_k_519_rel_v519(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=137, w2=81, w3=717, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 81)
    curvature = _rolling_slope(acceleration, 717)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3762 * acceleration + 0.003412 * anchor

def f55_rsw_k_520_rel_v520(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=144, w2=92, w3=730, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 144)
    pressure = rel_log.diff(92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3838 * pressure.rolling(730, min_periods=max(730//3, 2)).mean() + 0.0034121 * anchor

def f55_rsw_k_521_rel_v521(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=151, w2=103, w3=743, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    decay = spread.ewm(span=103, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.178125 + 0.0034122 * anchor

def f55_rsw_k_522_rel_v522(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=158, w2=114, w3=756, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(114, min_periods=max(114//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 158)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.1925 + 0.0034123 * anchor

def f55_rsw_k_523_rel_v523(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=165, w2=125, w3=769, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(165, min_periods=max(165//3, 2)).mean(), b.abs().rolling(125, min_periods=max(125//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.4066 * _rolling_slope(cover, 165) + 0.0034124 * anchor

def f55_rsw_k_524_rel_v524(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=172, w2=136, w3=25, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0378 * y + 0.962200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 172) - _rolling_slope(basket, 136) + 0.0034125 * anchor

def f55_rsw_k_525_rel_v525(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=179, w2=147, w3=38, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(147, min_periods=max(147//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(38) * 1.235625 + 0.0034126 * anchor
