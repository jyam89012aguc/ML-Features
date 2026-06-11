"""54 relative sector drawdown d2 second derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f54_rsw_d_526_rel_v526_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=253, w2=97, w3=578, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(97, min_periods=max(97//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.129375 + 0.0033527 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_527_rel_v527_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=9, w2=108, w3=591, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 108)
    curvature = _rolling_slope(acceleration, 591)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3938 * acceleration + 0.0033528 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_528_rel_v528_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=16, w2=119, w3=604, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 16)
    pressure = rel_log.diff(119)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.4014 * pressure.rolling(604, min_periods=max(604//3, 2)).mean() + 0.0033529 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_529_rel_v529_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=23, w2=130, w3=617, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(23, min_periods=max(23//3, 2)).mean())
    decay = spread.ewm(span=130, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.1725 + 0.003353 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_530_rel_v530_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=30, w2=141, w3=630, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(141, min_periods=max(141//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 30)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.186875 + 0.0033531 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_531_rel_v531_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=37, w2=152, w3=643, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(37, min_periods=max(37//3, 2)).mean(), b.abs().rolling(152, min_periods=max(152//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0478 * _rolling_slope(cover, 37) + 0.0033532 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_532_rel_v532_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=44, w2=163, w3=656, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0554 * y + 0.944600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 44) - _rolling_slope(basket, 163) + 0.0033533 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_533_rel_v533_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=51, w2=174, w3=669, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.23 + 0.0033534 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_534_rel_v534_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=58, w2=185, w3=682, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(185, min_periods=max(185//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0706 * _rolling_slope(draw, 682) + 0.0033535 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_535_rel_v535_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=65, w2=196, w3=695, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(65) - b.diff(126)
    stress = imbalance.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.25875 + 0.0033536 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_536_rel_v536_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=72, w2=207, w3=708, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(207, min_periods=max(207//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.273125 + 0.0033537 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_537_rel_v537_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=79, w2=218, w3=721, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2875 + 0.0033538 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_538_rel_v538_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=86, w2=229, w3=734, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(229, min_periods=max(229//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.301875 + 0.0033539 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_539_rel_v539_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=93, w2=240, w3=747, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(93)
    rank = change.rolling(240, min_periods=max(240//3, 2)).rank(pct=True)
    persistence = change.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1086 * persistence + 0.003354 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_540_rel_v540_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=100, w2=251, w3=760, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.330625 + 0.0033541 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_541_rel_v541_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=107, w2=262, w3=16, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1238 * slope + 0.0033542 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_542_rel_v542_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=114, w2=273, w3=29, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(114)
    drag = impulse.rolling(273, min_periods=max(273//3, 2)).mean()
    noise = impulse.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.359375 + 0.0033543 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_543_rel_v543_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=121, w2=284, w3=42, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 284)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.139 * acceleration + 0.0033544 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_544_rel_v544_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=128, w2=295, w3=55, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 128)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1466 * pressure.rolling(55, min_periods=max(55//3, 2)).mean() + 0.0033545 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_545_rel_v545_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=135, w2=306, w3=68, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(135, min_periods=max(135//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.4025 + 0.0033546 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_546_rel_v546_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=142, w2=317, w3=81, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(317, min_periods=max(317//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.416875 + 0.0033547 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_547_rel_v547_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=149, w2=328, w3=94, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(149, min_periods=max(149//3, 2)).mean(), b.abs().rolling(328, min_periods=max(328//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(94) + 0.1694 * _rolling_slope(cover, 149) + 0.0033548 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_548_rel_v548_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=156, w2=339, w3=107, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.177 * y + 0.823000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 156) - _rolling_slope(basket, 339) + 0.0033549 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_549_rel_v549_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=163, w2=350, w3=120, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(350, min_periods=max(350//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(120) * 1.46 + 0.003355 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_550_rel_v550_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=170, w2=361, w3=133, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(361, min_periods=max(361//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1922 * _rolling_slope(draw, 133) + 0.0033551 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_551_rel_v551_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=177, w2=372, w3=146, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.48875 + 0.0033552 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_552_rel_v552_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=184, w2=383, w3=159, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(383, min_periods=max(383//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.503125 + 0.0033553 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_553_rel_v553_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=191, w2=394, w3=172, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 394)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=172, adjust=False).mean() * 1.5175 + 0.0033554 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_554_rel_v554_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=198, w2=405, w3=185, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(405, min_periods=max(405//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.531875 + 0.0033555 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_555_rel_v555_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=205, w2=416, w3=198, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(416, min_periods=max(416//3, 2)).rank(pct=True)
    persistence = change.rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2302 * persistence + 0.0033556 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_556_rel_v556_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=212, w2=427, w3=211, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(427, min_periods=max(427//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.560625 + 0.0033557 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_557_rel_v557_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=219, w2=438, w3=224, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2454 * slope + 0.0033558 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_558_rel_v558_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=226, w2=449, w3=237, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(449, min_periods=max(449//3, 2)).mean()
    noise = impulse.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.589375 + 0.0033559 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_559_rel_v559_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=233, w2=460, w3=250, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 460)
    curvature = _rolling_slope(acceleration, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2606 * acceleration + 0.003356 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_560_rel_v560_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=240, w2=471, w3=263, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 240)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2682 * pressure.rolling(263, min_periods=max(263//3, 2)).mean() + 0.0033561 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_561_rel_v561_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=247, w2=482, w3=276, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(247, min_periods=max(247//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.859375 + 0.0033562 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_562_rel_v562_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=254, w2=493, w3=289, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(493, min_periods=max(493//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 254)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.87375 + 0.0033563 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_563_rel_v563_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=10, w2=504, w3=302, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(504, min_periods=max(504//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.291 * _rolling_slope(cover, 10) + 0.0033564 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_564_rel_v564_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=17, w2=12, w3=315, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2986 * y + 0.701400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 12) + 0.0033565 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_565_rel_v565_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=24, w2=23, w3=328, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(23, min_periods=max(23//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.916875 + 0.0033566 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_566_rel_v566_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=31, w2=34, w3=341, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(34, min_periods=max(34//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3138 * _rolling_slope(draw, 341) + 0.0033567 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_567_rel_v567_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=38, w2=45, w3=354, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(38) - b.diff(45)
    stress = imbalance.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.945625 + 0.0033568 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_568_rel_v568_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=45, w2=56, w3=367, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(56, min_periods=max(56//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.96 + 0.0033569 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_569_rel_v569_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=52, w2=67, w3=380, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.974375 + 0.003357 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_570_rel_v570_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=59, w2=78, w3=393, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.98875 + 0.0033571 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_571_rel_v571_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=66, w2=89, w3=406, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(66)
    rank = change.rolling(89, min_periods=max(89//3, 2)).rank(pct=True)
    persistence = change.rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3518 * persistence + 0.0033572 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_572_rel_v572_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=73, w2=100, w3=419, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0175 + 0.0033573 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_573_rel_v573_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=80, w2=111, w3=432, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.367 * slope + 0.0033574 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_574_rel_v574_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=87, w2=122, w3=445, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(87)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.04625 + 0.0033575 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_575_rel_v575_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=94, w2=133, w3=458, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 133)
    curvature = _rolling_slope(acceleration, 458)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3822 * acceleration + 0.0033576 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_576_rel_v576_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=101, w2=144, w3=471, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 101)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3898 * pressure.rolling(471, min_periods=max(471//3, 2)).mean() + 0.0033577 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_577_rel_v577_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=108, w2=155, w3=484, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=155, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.089375 + 0.0033578 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_578_rel_v578_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=115, w2=166, w3=497, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(166, min_periods=max(166//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 115)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.10375 + 0.0033579 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_579_rel_v579_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=122, w2=177, w3=510, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(122, min_periods=max(122//3, 2)).mean(), b.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0362 * _rolling_slope(cover, 122) + 0.003358 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_580_rel_v580_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=129, w2=188, w3=523, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0438 * y + 0.956200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 129) - _rolling_slope(basket, 188) + 0.0033581 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_581_rel_v581_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=136, w2=199, w3=536, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(199, min_periods=max(199//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.146875 + 0.0033582 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_582_rel_v582_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=143, w2=210, w3=549, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.059 * _rolling_slope(draw, 549) + 0.0033583 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_583_rel_v583_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=150, w2=221, w3=562, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.175625 + 0.0033584 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_584_rel_v584_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=157, w2=232, w3=575, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(232, min_periods=max(232//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.19 + 0.0033585 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_585_rel_v585_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=164, w2=243, w3=588, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 243)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.204375 + 0.0033586 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_586_rel_v586_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=171, w2=254, w3=601, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(254, min_periods=max(254//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21875 + 0.0033587 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_587_rel_v587_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=178, w2=265, w3=614, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(265, min_periods=max(265//3, 2)).rank(pct=True)
    persistence = change.rolling(614, min_periods=max(614//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.097 * persistence + 0.0033588 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_588_rel_v588_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=185, w2=276, w3=627, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(276, min_periods=max(276//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2475 + 0.0033589 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_589_rel_v589_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=192, w2=287, w3=640, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(287, min_periods=max(287//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1122 * slope + 0.003359 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_590_rel_v590_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=199, w2=298, w3=653, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27625 + 0.0033591 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_591_rel_v591_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=206, w2=309, w3=666, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 309)
    curvature = _rolling_slope(acceleration, 666)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1274 * acceleration + 0.0033592 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_592_rel_v592_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=213, w2=320, w3=679, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 213)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.135 * pressure.rolling(679, min_periods=max(679//3, 2)).mean() + 0.0033593 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_593_rel_v593_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=220, w2=331, w3=692, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(220, min_periods=max(220//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.319375 + 0.0033594 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_594_rel_v594_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=227, w2=342, w3=705, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(342, min_periods=max(342//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 227)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.33375 + 0.0033595 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_595_rel_v595_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=234, w2=353, w3=718, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(234, min_periods=max(234//3, 2)).mean(), b.abs().rolling(353, min_periods=max(353//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1578 * _rolling_slope(cover, 234) + 0.0033596 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_596_rel_v596_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=241, w2=364, w3=731, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1654 * y + 0.834600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 241) - _rolling_slope(basket, 364) + 0.0033597 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_597_rel_v597_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=248, w2=375, w3=744, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(375, min_periods=max(375//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.376875 + 0.0033598 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_598_rel_v598_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=255, w2=386, w3=757, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(386, min_periods=max(386//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1806 * _rolling_slope(draw, 757) + 0.0033599 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_599_rel_v599_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=11, w2=397, w3=770, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(11) - b.diff(126)
    stress = imbalance.rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.405625 + 0.00336 * anchor
    return base_signal.diff().diff()

def f54_rsw_d_600_rel_v600_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=18, w2=408, w3=26, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(408, min_periods=max(408//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.42 + 0.0033601 * anchor
    return base_signal.diff().diff()
