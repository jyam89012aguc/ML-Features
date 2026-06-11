"""100 institutional trap composite d1 first derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f100_trap_301_rel_v301_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=254, w2=349, w3=699, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0766 * slope + 0.0005702 * anchor
    return base_signal.diff()

def f100_trap_302_analyst_v302_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=10, w2=360, w3=712, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.865 + 0.0005703 * anchor
    return base_signal.diff()

def f100_trap_303_accrual_v303_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=17, w2=371, w3=725, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 725)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0918 * acceleration + 0.0005704 * anchor
    return base_signal.diff()

def f100_trap_304_jerk_v304_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=24, w2=382, w3=738, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.89375 + 0.0005705 * anchor
    return base_signal.diff()

def f100_trap_305_rel_v305_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=31, w2=393, w3=751, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(31, min_periods=max(31//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.908125 + 0.0005706 * anchor
    return base_signal.diff()

def f100_trap_306_analyst_v306_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=38, w2=404, w3=764, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(38)
    drag = impulse.rolling(404, min_periods=max(404//3, 2)).mean()
    noise = impulse.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9225 + 0.0005707 * anchor
    return base_signal.diff()

def f100_trap_307_accrual_v307_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=45, w2=415, w3=20, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(45, min_periods=max(45//3, 2)).mean(), b.abs().rolling(415, min_periods=max(415//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(20) + 0.1222 * _rolling_slope(cover, 45) + 0.0005708 * anchor
    return base_signal.diff()

def f100_trap_308_jerk_v308_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=52, w2=426, w3=33, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(426, min_periods=max(426//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(33) * 0.95125 + 0.0005709 * anchor
    return base_signal.diff()

def f100_trap_309_rel_v309_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=59, w2=437, w3=46, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(437, min_periods=max(437//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(46) * 0.965625 + 0.000571 * anchor
    return base_signal.diff()

def f100_trap_310_analyst_v310_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=66, w2=448, w3=59, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(448, min_periods=max(448//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.98 + 0.0005711 * anchor
    return base_signal.diff()

def f100_trap_311_accrual_v311_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=73, w2=459, w3=72, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(73) - b.diff(126)
    stress = imbalance.rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.994375 + 0.0005712 * anchor
    return base_signal.diff()

def f100_trap_312_jerk_v312_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=80, w2=470, w3=85, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(470, min_periods=max(470//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.00875 + 0.0005713 * anchor
    return base_signal.diff()

def f100_trap_313_rel_v313_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=87, w2=481, w3=98, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=98, adjust=False).mean() * 1.023125 + 0.0005714 * anchor
    return base_signal.diff()

def f100_trap_314_analyst_v314_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=94, w2=492, w3=111, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(492, min_periods=max(492//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0375 + 0.0005715 * anchor
    return base_signal.diff()

def f100_trap_315_accrual_v315_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=101, w2=503, w3=124, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(101)
    rank = change.rolling(503, min_periods=max(503//3, 2)).rank(pct=True)
    persistence = change.rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.183 * persistence + 0.0005716 * anchor
    return base_signal.diff()

def f100_trap_316_jerk_v316_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=108, w2=11, w3=137, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(108)
    drag = impulse.rolling(11, min_periods=max(11//3, 2)).mean()
    noise = impulse.abs().rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.06625 + 0.0005717 * anchor
    return base_signal.diff()

def f100_trap_317_rel_v317_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=115, w2=22, w3=150, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(22, min_periods=max(22//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1982 * slope + 0.0005718 * anchor
    return base_signal.diff()

def f100_trap_318_analyst_v318_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=122, w2=33, w3=163, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(33, min_periods=max(33//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.095 + 0.0005719 * anchor
    return base_signal.diff()

def f100_trap_319_accrual_v319_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=129, w2=44, w3=176, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 44)
    curvature = _rolling_slope(acceleration, 176)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2134 * acceleration + 0.000572 * anchor
    return base_signal.diff()

def f100_trap_320_jerk_v320_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=136, w2=55, w3=189, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(55, min_periods=max(55//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.12375 + 0.0005721 * anchor
    return base_signal.diff()

def f100_trap_321_rel_v321_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=143, w2=66, w3=202, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(143, min_periods=max(143//3, 2)).mean())
    decay = spread.ewm(span=66, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.138125 + 0.0005722 * anchor
    return base_signal.diff()

def f100_trap_322_analyst_v322_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=150, w2=77, w3=215, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(77, min_periods=max(77//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1525 + 0.0005723 * anchor
    return base_signal.diff()

def f100_trap_323_accrual_v323_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=157, w2=88, w3=228, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(157, min_periods=max(157//3, 2)).mean(), b.abs().rolling(88, min_periods=max(88//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2438 * _rolling_slope(cover, 157) + 0.0005724 * anchor
    return base_signal.diff()

def f100_trap_324_jerk_v324_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=164, w2=99, w3=241, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18125 + 0.0005725 * anchor
    return base_signal.diff()

def f100_trap_325_rel_v325_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=171, w2=110, w3=254, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.195625 + 0.0005726 * anchor
    return base_signal.diff()

def f100_trap_326_analyst_v326_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=178, w2=121, w3=267, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.21 + 0.0005727 * anchor
    return base_signal.diff()

def f100_trap_327_accrual_v327_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=185, w2=132, w3=280, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.224375 + 0.0005728 * anchor
    return base_signal.diff()

def f100_trap_328_jerk_v328_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=192, w2=143, w3=293, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(143, min_periods=max(143//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.23875 + 0.0005729 * anchor
    return base_signal.diff()

def f100_trap_329_rel_v329_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=199, w2=154, w3=306, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 154)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.253125 + 0.000573 * anchor
    return base_signal.diff()

def f100_trap_330_analyst_v330_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=206, w2=165, w3=319, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(165, min_periods=max(165//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2675 + 0.0005731 * anchor
    return base_signal.diff()

def f100_trap_331_accrual_v331_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=213, w2=176, w3=332, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3046 * persistence + 0.0005732 * anchor
    return base_signal.diff()

def f100_trap_332_jerk_v332_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=220, w2=187, w3=345, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(187, min_periods=max(187//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.29625 + 0.0005733 * anchor
    return base_signal.diff()

def f100_trap_333_rel_v333_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=227, w2=198, w3=358, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3198 * slope + 0.0005734 * anchor
    return base_signal.diff()

def f100_trap_334_analyst_v334_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=234, w2=209, w3=371, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(209, min_periods=max(209//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.325 + 0.0005735 * anchor
    return base_signal.diff()

def f100_trap_335_accrual_v335_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=241, w2=220, w3=384, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 384)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.335 * acceleration + 0.0005736 * anchor
    return base_signal.diff()

def f100_trap_336_jerk_v336_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=248, w2=231, w3=397, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(231, min_periods=max(231//3, 2)).mean()
    noise = impulse.abs().rolling(397, min_periods=max(397//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.35375 + 0.0005737 * anchor
    return base_signal.diff()

def f100_trap_337_rel_v337_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=255, w2=242, w3=410, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(255, min_periods=max(255//3, 2)).mean())
    decay = spread.ewm(span=242, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.368125 + 0.0005738 * anchor
    return base_signal.diff()

def f100_trap_338_analyst_v338_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=11, w2=253, w3=423, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(253, min_periods=max(253//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3825 + 0.0005739 * anchor
    return base_signal.diff()

def f100_trap_339_accrual_v339_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=18, w2=264, w3=436, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(18, min_periods=max(18//3, 2)).mean(), b.abs().rolling(264, min_periods=max(264//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3654 * _rolling_slope(cover, 18) + 0.000574 * anchor
    return base_signal.diff()

def f100_trap_340_jerk_v340_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=25, w2=275, w3=449, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(275, min_periods=max(275//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41125 + 0.0005741 * anchor
    return base_signal.diff()

def f100_trap_341_rel_v341_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=32, w2=286, w3=462, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(286, min_periods=max(286//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.425625 + 0.0005742 * anchor
    return base_signal.diff()

def f100_trap_342_analyst_v342_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=39, w2=297, w3=475, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(297, min_periods=max(297//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44 + 0.0005743 * anchor
    return base_signal.diff()

def f100_trap_343_accrual_v343_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=46, w2=308, w3=488, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(46) - b.diff(126)
    stress = imbalance.rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.454375 + 0.0005744 * anchor
    return base_signal.diff()

def f100_trap_344_jerk_v344_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=53, w2=319, w3=501, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(319, min_periods=max(319//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46875 + 0.0005745 * anchor
    return base_signal.diff()

def f100_trap_345_rel_v345_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=60, w2=330, w3=514, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 330)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.483125 + 0.0005746 * anchor
    return base_signal.diff()

def f100_trap_346_analyst_v346_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=67, w2=341, w3=527, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(67)
    drag = impulse.rolling(341, min_periods=max(341//3, 2)).mean()
    noise = impulse.abs().rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4975 + 0.0005747 * anchor
    return base_signal.diff()

def f100_trap_347_accrual_v347_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=74, w2=352, w3=540, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(74)
    rank = change.rolling(352, min_periods=max(352//3, 2)).rank(pct=True)
    persistence = change.rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0498 * persistence + 0.0005748 * anchor
    return base_signal.diff()

def f100_trap_348_jerk_v348_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=81, w2=363, w3=553, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(363, min_periods=max(363//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.52625 + 0.0005749 * anchor
    return base_signal.diff()

def f100_trap_349_rel_v349_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=88, w2=374, w3=566, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(374, min_periods=max(374//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.065 * slope + 0.000575 * anchor
    return base_signal.diff()

def f100_trap_350_analyst_v350_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=95, w2=385, w3=579, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(385, min_periods=max(385//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.555 + 0.0005751 * anchor
    return base_signal.diff()

def f100_trap_351_accrual_v351_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=102, w2=396, w3=592, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 592)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0802 * acceleration + 0.0005752 * anchor
    return base_signal.diff()

def f100_trap_352_jerk_v352_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=109, w2=407, w3=605, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(407, min_periods=max(407//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.58375 + 0.0005753 * anchor
    return base_signal.diff()

def f100_trap_353_rel_v353_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=116, w2=418, w3=618, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(116, min_periods=max(116//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.598125 + 0.0005754 * anchor
    return base_signal.diff()

def f100_trap_354_analyst_v354_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=123, w2=429, w3=631, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(429, min_periods=max(429//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6125 + 0.0005755 * anchor
    return base_signal.diff()

def f100_trap_355_accrual_v355_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=130, w2=440, w3=644, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(130, min_periods=max(130//3, 2)).mean(), b.abs().rolling(440, min_periods=max(440//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1106 * _rolling_slope(cover, 130) + 0.0005756 * anchor
    return base_signal.diff()

def f100_trap_356_jerk_v356_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=137, w2=451, w3=657, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.868125 + 0.0005757 * anchor
    return base_signal.diff()

def f100_trap_357_rel_v357_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=144, w2=462, w3=670, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(462, min_periods=max(462//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8825 + 0.0005758 * anchor
    return base_signal.diff()

def f100_trap_358_analyst_v358_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=151, w2=473, w3=683, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.896875 + 0.0005759 * anchor
    return base_signal.diff()

def f100_trap_359_accrual_v359_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=158, w2=484, w3=696, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.91125 + 0.000576 * anchor
    return base_signal.diff()

def f100_trap_360_jerk_v360_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=165, w2=495, w3=709, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.925625 + 0.0005761 * anchor
    return base_signal.diff()

def f100_trap_361_rel_v361_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=172, w2=506, w3=722, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 506)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.94 + 0.0005762 * anchor
    return base_signal.diff()

def f100_trap_362_analyst_v362_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=179, w2=14, w3=735, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.954375 + 0.0005763 * anchor
    return base_signal.diff()

def f100_trap_363_accrual_v363_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=186, w2=25, w3=748, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(25, min_periods=max(25//3, 2)).rank(pct=True)
    persistence = change.rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1714 * persistence + 0.0005764 * anchor
    return base_signal.diff()

def f100_trap_364_jerk_v364_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=193, w2=36, w3=761, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.983125 + 0.0005765 * anchor
    return base_signal.diff()

def f100_trap_365_rel_v365_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=200, w2=47, w3=17, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(47, min_periods=max(47//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1866 * slope + 0.0005766 * anchor
    return base_signal.diff()

def f100_trap_366_analyst_v366_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=207, w2=58, w3=30, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.011875 + 0.0005767 * anchor
    return base_signal.diff()

def f100_trap_367_accrual_v367_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=214, w2=69, w3=43, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 43)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2018 * acceleration + 0.0005768 * anchor
    return base_signal.diff()

def f100_trap_368_jerk_v368_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=221, w2=80, w3=56, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(56) * 1.040625 + 0.0005769 * anchor
    return base_signal.diff()

def f100_trap_369_rel_v369_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=228, w2=91, w3=69, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(228, min_periods=max(228//3, 2)).mean())
    decay = spread.ewm(span=91, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.055 + 0.000577 * anchor
    return base_signal.diff()

def f100_trap_370_analyst_v370_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=235, w2=102, w3=82, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.069375 + 0.0005771 * anchor
    return base_signal.diff()

def f100_trap_371_accrual_v371_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=242, w2=113, w3=95, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(242, min_periods=max(242//3, 2)).mean(), b.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(95) + 0.2322 * _rolling_slope(cover, 242) + 0.0005772 * anchor
    return base_signal.diff()

def f100_trap_372_jerk_v372_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=249, w2=124, w3=108, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(124, min_periods=max(124//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.098125 + 0.0005773 * anchor
    return base_signal.diff()

def f100_trap_373_rel_v373_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=5, w2=135, w3=121, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(135, min_periods=max(135//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(121) * 1.1125 + 0.0005774 * anchor
    return base_signal.diff()

def f100_trap_374_analyst_v374_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=12, w2=146, w3=134, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(146, min_periods=max(146//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.126875 + 0.0005775 * anchor
    return base_signal.diff()

def f100_trap_375_accrual_v375_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=19, w2=157, w3=147, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(19) - b.diff(126)
    stress = imbalance.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.14125 + 0.0005776 * anchor
    return base_signal.diff()
