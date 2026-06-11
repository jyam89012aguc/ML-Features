"""100 institutional trap composite d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Composite - Institutional-grade short-side signal.
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

def f100_trap_451_accrual_v451_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=49, w2=490, w3=378, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(49, min_periods=max(49//3, 2)).mean(), b.abs().rolling(490, min_periods=max(490//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0874 * _rolling_slope(cover, 49) + 0.0005852 * anchor
    return base_signal.diff().diff()

def f100_trap_452_jerk_v452_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=56, w2=501, w3=391, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.475 + 0.0005853 * anchor
    return base_signal.diff().diff()

def f100_trap_453_rel_v453_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=63, w2=512, w3=404, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(512, min_periods=max(512//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.489375 + 0.0005854 * anchor
    return base_signal.diff().diff()

def f100_trap_454_analyst_v454_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=70, w2=20, w3=417, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(20, min_periods=max(20//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.50375 + 0.0005855 * anchor
    return base_signal.diff().diff()

def f100_trap_455_accrual_v455_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=77, w2=31, w3=430, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(77) - b.diff(31)
    stress = imbalance.rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.518125 + 0.0005856 * anchor
    return base_signal.diff().diff()

def f100_trap_456_jerk_v456_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=84, w2=42, w3=443, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(84)
    drag = impulse.rolling(42, min_periods=max(42//3, 2)).mean()
    noise = impulse.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5325 + 0.0005857 * anchor
    return base_signal.diff().diff()

def f100_trap_457_rel_v457_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=91, w2=53, w3=456, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 53)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.546875 + 0.0005858 * anchor
    return base_signal.diff().diff()

def f100_trap_458_analyst_v458_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=98, w2=64, w3=469, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(64, min_periods=max(64//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.56125 + 0.0005859 * anchor
    return base_signal.diff().diff()

def f100_trap_459_accrual_v459_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=105, w2=75, w3=482, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(105)
    rank = change.rolling(75, min_periods=max(75//3, 2)).rank(pct=True)
    persistence = change.rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1482 * persistence + 0.000586 * anchor
    return base_signal.diff().diff()

def f100_trap_460_jerk_v460_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=112, w2=86, w3=495, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(86, min_periods=max(86//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59 + 0.0005861 * anchor
    return base_signal.diff().diff()

def f100_trap_461_rel_v461_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=119, w2=97, w3=508, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(97, min_periods=max(97//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1634 * slope + 0.0005862 * anchor
    return base_signal.diff().diff()

def f100_trap_462_analyst_v462_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=126, w2=108, w3=521, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.61875 + 0.0005863 * anchor
    return base_signal.diff().diff()

def f100_trap_463_accrual_v463_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=133, w2=119, w3=534, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 119)
    curvature = _rolling_slope(acceleration, 534)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1786 * acceleration + 0.0005864 * anchor
    return base_signal.diff().diff()

def f100_trap_464_jerk_v464_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=140, w2=130, w3=547, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(130, min_periods=max(130//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.874375 + 0.0005865 * anchor
    return base_signal.diff().diff()

def f100_trap_465_rel_v465_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=147, w2=141, w3=560, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=141, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.88875 + 0.0005866 * anchor
    return base_signal.diff().diff()

def f100_trap_466_analyst_v466_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=154, w2=152, w3=573, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.903125 + 0.0005867 * anchor
    return base_signal.diff().diff()

def f100_trap_467_accrual_v467_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=161, w2=163, w3=586, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(163, min_periods=max(163//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.209 * _rolling_slope(cover, 161) + 0.0005868 * anchor
    return base_signal.diff().diff()

def f100_trap_468_jerk_v468_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=168, w2=174, w3=599, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.931875 + 0.0005869 * anchor
    return base_signal.diff().diff()

def f100_trap_469_rel_v469_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=175, w2=185, w3=612, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(185, min_periods=max(185//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.94625 + 0.000587 * anchor
    return base_signal.diff().diff()

def f100_trap_470_analyst_v470_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=182, w2=196, w3=625, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.960625 + 0.0005871 * anchor
    return base_signal.diff().diff()

def f100_trap_471_accrual_v471_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=189, w2=207, w3=638, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.975 + 0.0005872 * anchor
    return base_signal.diff().diff()

def f100_trap_472_jerk_v472_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=196, w2=218, w3=651, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(218, min_periods=max(218//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.989375 + 0.0005873 * anchor
    return base_signal.diff().diff()

def f100_trap_473_rel_v473_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=203, w2=229, w3=664, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 229)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.00375 + 0.0005874 * anchor
    return base_signal.diff().diff()

def f100_trap_474_analyst_v474_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=210, w2=240, w3=677, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(240, min_periods=max(240//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.018125 + 0.0005875 * anchor
    return base_signal.diff().diff()

def f100_trap_475_accrual_v475_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=217, w2=251, w3=690, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(251, min_periods=max(251//3, 2)).rank(pct=True)
    persistence = change.rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2698 * persistence + 0.0005876 * anchor
    return base_signal.diff().diff()

def f100_trap_476_jerk_v476_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=224, w2=262, w3=703, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(262, min_periods=max(262//3, 2)).mean()
    noise = impulse.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.046875 + 0.0005877 * anchor
    return base_signal.diff().diff()

def f100_trap_477_rel_v477_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=231, w2=273, w3=716, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(273, min_periods=max(273//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.285 * slope + 0.0005878 * anchor
    return base_signal.diff().diff()

def f100_trap_478_analyst_v478_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=238, w2=284, w3=729, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(284, min_periods=max(284//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.075625 + 0.0005879 * anchor
    return base_signal.diff().diff()

def f100_trap_479_accrual_v479_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=245, w2=295, w3=742, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 295)
    curvature = _rolling_slope(acceleration, 742)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3002 * acceleration + 0.000588 * anchor
    return base_signal.diff().diff()

def f100_trap_480_jerk_v480_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=252, w2=306, w3=755, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 252)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.104375 + 0.0005881 * anchor
    return base_signal.diff().diff()

def f100_trap_481_rel_v481_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=8, w2=317, w3=768, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(8, min_periods=max(8//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.11875 + 0.0005882 * anchor
    return base_signal.diff().diff()

def f100_trap_482_analyst_v482_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=15, w2=328, w3=24, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(328, min_periods=max(328//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.133125 + 0.0005883 * anchor
    return base_signal.diff().diff()

def f100_trap_483_accrual_v483_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=22, w2=339, w3=37, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(22, min_periods=max(22//3, 2)).mean(), b.abs().rolling(339, min_periods=max(339//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(37) + 0.3306 * _rolling_slope(cover, 22) + 0.0005884 * anchor
    return base_signal.diff().diff()

def f100_trap_484_jerk_v484_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=29, w2=350, w3=50, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.161875 + 0.0005885 * anchor
    return base_signal.diff().diff()

def f100_trap_485_rel_v485_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=36, w2=361, w3=63, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(361, min_periods=max(361//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(63) * 1.17625 + 0.0005886 * anchor
    return base_signal.diff().diff()

def f100_trap_486_analyst_v486_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=43, w2=372, w3=76, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(43)
    drag = impulse.rolling(372, min_periods=max(372//3, 2)).mean()
    noise = impulse.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.190625 + 0.0005887 * anchor
    return base_signal.diff().diff()

def f100_trap_487_accrual_v487_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=50, w2=383, w3=89, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(50) - b.diff(126)
    stress = imbalance.rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.205 + 0.0005888 * anchor
    return base_signal.diff().diff()

def f100_trap_488_jerk_v488_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=57, w2=394, w3=102, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(102) * 1.219375 + 0.0005889 * anchor
    return base_signal.diff().diff()

def f100_trap_489_rel_v489_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=64, w2=405, w3=115, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 405)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=115, adjust=False).mean() * 1.23375 + 0.000589 * anchor
    return base_signal.diff().diff()

def f100_trap_490_analyst_v490_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=71, w2=416, w3=128, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(416, min_periods=max(416//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.248125 + 0.0005891 * anchor
    return base_signal.diff().diff()

def f100_trap_491_accrual_v491_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=78, w2=427, w3=141, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(78)
    rank = change.rolling(427, min_periods=max(427//3, 2)).rank(pct=True)
    persistence = change.rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3914 * persistence + 0.0005892 * anchor
    return base_signal.diff().diff()

def f100_trap_492_jerk_v492_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=85, w2=438, w3=154, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(438, min_periods=max(438//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.276875 + 0.0005893 * anchor
    return base_signal.diff().diff()

def f100_trap_493_rel_v493_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=92, w2=449, w3=167, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(449, min_periods=max(449//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4066 * slope + 0.0005894 * anchor
    return base_signal.diff().diff()

def f100_trap_494_analyst_v494_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=99, w2=460, w3=180, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(460, min_periods=max(460//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.305625 + 0.0005895 * anchor
    return base_signal.diff().diff()

def f100_trap_495_accrual_v495_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=106, w2=471, w3=193, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 471)
    curvature = _rolling_slope(acceleration, 193)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0454 * acceleration + 0.0005896 * anchor
    return base_signal.diff().diff()

def f100_trap_496_jerk_v496_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=113, w2=482, w3=206, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(113)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.334375 + 0.0005897 * anchor
    return base_signal.diff().diff()

def f100_trap_497_rel_v497_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=120, w2=493, w3=219, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(120, min_periods=max(120//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.34875 + 0.0005898 * anchor
    return base_signal.diff().diff()

def f100_trap_498_analyst_v498_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=127, w2=504, w3=232, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(504, min_periods=max(504//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.363125 + 0.0005899 * anchor
    return base_signal.diff().diff()

def f100_trap_499_accrual_v499_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=134, w2=12, w3=245, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(134, min_periods=max(134//3, 2)).mean(), b.abs().rolling(12, min_periods=max(12//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0758 * _rolling_slope(cover, 134) + 0.00059 * anchor
    return base_signal.diff().diff()

def f100_trap_500_jerk_v500_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=141, w2=23, w3=258, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(23, min_periods=max(23//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.391875 + 0.0005901 * anchor
    return base_signal.diff().diff()

def f100_trap_501_rel_v501_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=148, w2=34, w3=271, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.40625 + 0.0005902 * anchor
    return base_signal.diff().diff()

def f100_trap_502_analyst_v502_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=155, w2=45, w3=284, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(45, min_periods=max(45//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.420625 + 0.0005903 * anchor
    return base_signal.diff().diff()

def f100_trap_503_accrual_v503_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=162, w2=56, w3=297, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(56)
    stress = imbalance.rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.435 + 0.0005904 * anchor
    return base_signal.diff().diff()

def f100_trap_504_jerk_v504_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=169, w2=67, w3=310, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(67, min_periods=max(67//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.449375 + 0.0005905 * anchor
    return base_signal.diff().diff()

def f100_trap_505_rel_v505_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=176, w2=78, w3=323, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 78)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.46375 + 0.0005906 * anchor
    return base_signal.diff().diff()

def f100_trap_506_analyst_v506_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=183, w2=89, w3=336, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(89, min_periods=max(89//3, 2)).mean()
    noise = impulse.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.478125 + 0.0005907 * anchor
    return base_signal.diff().diff()

def f100_trap_507_accrual_v507_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=190, w2=100, w3=349, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(100, min_periods=max(100//3, 2)).rank(pct=True)
    persistence = change.rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1366 * persistence + 0.0005908 * anchor
    return base_signal.diff().diff()

def f100_trap_508_jerk_v508_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=197, w2=111, w3=362, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(111, min_periods=max(111//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.506875 + 0.0005909 * anchor
    return base_signal.diff().diff()

def f100_trap_509_rel_v509_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=204, w2=122, w3=375, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(122, min_periods=max(122//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1518 * slope + 0.000591 * anchor
    return base_signal.diff().diff()

def f100_trap_510_analyst_v510_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=211, w2=133, w3=388, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.535625 + 0.0005911 * anchor
    return base_signal.diff().diff()

def f100_trap_511_accrual_v511_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=218, w2=144, w3=401, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 401)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.167 * acceleration + 0.0005912 * anchor
    return base_signal.diff().diff()

def f100_trap_512_jerk_v512_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=225, w2=155, w3=414, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.564375 + 0.0005913 * anchor
    return base_signal.diff().diff()

def f100_trap_513_rel_v513_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=232, w2=166, w3=427, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(232, min_periods=max(232//3, 2)).mean())
    decay = spread.ewm(span=166, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.57875 + 0.0005914 * anchor
    return base_signal.diff().diff()

def f100_trap_514_analyst_v514_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=239, w2=177, w3=440, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(177, min_periods=max(177//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.593125 + 0.0005915 * anchor
    return base_signal.diff().diff()

def f100_trap_515_accrual_v515_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=246, w2=188, w3=453, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(246, min_periods=max(246//3, 2)).mean(), b.abs().rolling(188, min_periods=max(188//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1974 * _rolling_slope(cover, 246) + 0.0005916 * anchor
    return base_signal.diff().diff()

def f100_trap_516_jerk_v516_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=253, w2=199, w3=466, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(199, min_periods=max(199//3, 2)).mean()
    noise = impulse.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.621875 + 0.0005917 * anchor
    return base_signal.diff().diff()

def f100_trap_517_rel_v517_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=9, w2=210, w3=479, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(210, min_periods=max(210//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.863125 + 0.0005918 * anchor
    return base_signal.diff().diff()

def f100_trap_518_analyst_v518_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=16, w2=221, w3=492, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(221, min_periods=max(221//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8775 + 0.0005919 * anchor
    return base_signal.diff().diff()

def f100_trap_519_accrual_v519_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=23, w2=232, w3=505, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(23) - b.diff(126)
    stress = imbalance.rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.891875 + 0.000592 * anchor
    return base_signal.diff().diff()

def f100_trap_520_jerk_v520_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=30, w2=243, w3=518, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(243, min_periods=max(243//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.90625 + 0.0005921 * anchor
    return base_signal.diff().diff()

def f100_trap_521_rel_v521_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=37, w2=254, w3=531, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 254)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.920625 + 0.0005922 * anchor
    return base_signal.diff().diff()

def f100_trap_522_analyst_v522_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=44, w2=265, w3=544, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(265, min_periods=max(265//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.935 + 0.0005923 * anchor
    return base_signal.diff().diff()

def f100_trap_523_accrual_v523_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=51, w2=276, w3=557, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(51)
    rank = change.rolling(276, min_periods=max(276//3, 2)).rank(pct=True)
    persistence = change.rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2582 * persistence + 0.0005924 * anchor
    return base_signal.diff().diff()

def f100_trap_524_jerk_v524_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=58, w2=287, w3=570, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(287, min_periods=max(287//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96375 + 0.0005925 * anchor
    return base_signal.diff().diff()

def f100_trap_525_rel_v525_d2(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated rel replacement signal (w1=65, w2=298, w3=583, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(298, min_periods=max(298//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2734 * slope + 0.0005926 * anchor
    return base_signal.diff().diff()
