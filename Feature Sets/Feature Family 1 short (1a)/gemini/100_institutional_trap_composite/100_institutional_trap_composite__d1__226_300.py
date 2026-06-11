"""100 institutional trap composite d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f100_trap_226_analyst_v226_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=231, w2=27, w3=481, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(27, min_periods=max(27//3, 2)).mean()
    noise = impulse.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31875 + 0.0005627 * anchor
    return base_signal.diff()

def f100_trap_227_accrual_v227_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=238, w2=38, w3=494, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(238, min_periods=max(238//3, 2)).mean(), b.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.267 * _rolling_slope(cover, 238) + 0.0005628 * anchor
    return base_signal.diff()

def f100_trap_228_jerk_v228_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=245, w2=49, w3=507, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(49, min_periods=max(49//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3475 + 0.0005629 * anchor
    return base_signal.diff()

def f100_trap_229_rel_v229_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=252, w2=60, w3=520, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(60, min_periods=max(60//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.361875 + 0.000563 * anchor
    return base_signal.diff()

def f100_trap_230_analyst_v230_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=8, w2=71, w3=533, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(71, min_periods=max(71//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.37625 + 0.0005631 * anchor
    return base_signal.diff()

def f100_trap_231_accrual_v231_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=15, w2=82, w3=546, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(15) - b.diff(82)
    stress = imbalance.rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.390625 + 0.0005632 * anchor
    return base_signal.diff()

def f100_trap_232_jerk_v232_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=22, w2=93, w3=559, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.405 + 0.0005633 * anchor
    return base_signal.diff()

def f100_trap_233_rel_v233_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=29, w2=104, w3=572, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 104)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.419375 + 0.0005634 * anchor
    return base_signal.diff()

def f100_trap_234_analyst_v234_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=36, w2=115, w3=585, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43375 + 0.0005635 * anchor
    return base_signal.diff()

def f100_trap_235_accrual_v235_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=43, w2=126, w3=598, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(43)
    rank = change.rolling(126, min_periods=max(126//3, 2)).rank(pct=True)
    persistence = change.rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3278 * persistence + 0.0005636 * anchor
    return base_signal.diff()

def f100_trap_236_jerk_v236_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=50, w2=137, w3=611, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(50)
    drag = impulse.rolling(137, min_periods=max(137//3, 2)).mean()
    noise = impulse.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4625 + 0.0005637 * anchor
    return base_signal.diff()

def f100_trap_237_rel_v237_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=57, w2=148, w3=624, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(148, min_periods=max(148//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.343 * slope + 0.0005638 * anchor
    return base_signal.diff()

def f100_trap_238_analyst_v238_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=64, w2=159, w3=637, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(159, min_periods=max(159//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49125 + 0.0005639 * anchor
    return base_signal.diff()

def f100_trap_239_accrual_v239_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=71, w2=170, w3=650, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 170)
    curvature = _rolling_slope(acceleration, 650)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3582 * acceleration + 0.000564 * anchor
    return base_signal.diff()

def f100_trap_240_jerk_v240_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=78, w2=181, w3=663, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(181, min_periods=max(181//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.52 + 0.0005641 * anchor
    return base_signal.diff()

def f100_trap_241_rel_v241_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=85, w2=192, w3=676, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(85, min_periods=max(85//3, 2)).mean())
    decay = spread.ewm(span=192, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.534375 + 0.0005642 * anchor
    return base_signal.diff()

def f100_trap_242_analyst_v242_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=92, w2=203, w3=689, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(203, min_periods=max(203//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.54875 + 0.0005643 * anchor
    return base_signal.diff()

def f100_trap_243_accrual_v243_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=99, w2=214, w3=702, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(99, min_periods=max(99//3, 2)).mean(), b.abs().rolling(214, min_periods=max(214//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3886 * _rolling_slope(cover, 99) + 0.0005644 * anchor
    return base_signal.diff()

def f100_trap_244_jerk_v244_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=106, w2=225, w3=715, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(225, min_periods=max(225//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5775 + 0.0005645 * anchor
    return base_signal.diff()

def f100_trap_245_rel_v245_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=113, w2=236, w3=728, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.591875 + 0.0005646 * anchor
    return base_signal.diff()

def f100_trap_246_analyst_v246_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=120, w2=247, w3=741, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(120)
    drag = impulse.rolling(247, min_periods=max(247//3, 2)).mean()
    noise = impulse.abs().rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.60625 + 0.0005647 * anchor
    return base_signal.diff()

def f100_trap_247_accrual_v247_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=127, w2=258, w3=754, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.620625 + 0.0005648 * anchor
    return base_signal.diff()

def f100_trap_248_jerk_v248_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=134, w2=269, w3=767, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(269, min_periods=max(269//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.861875 + 0.0005649 * anchor
    return base_signal.diff()

def f100_trap_249_rel_v249_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=141, w2=280, w3=23, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 280)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=23, adjust=False).mean() * 0.87625 + 0.000565 * anchor
    return base_signal.diff()

def f100_trap_250_analyst_v250_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=148, w2=291, w3=36, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(291, min_periods=max(291//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.890625 + 0.0005651 * anchor
    return base_signal.diff()

def f100_trap_251_accrual_v251_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=155, w2=302, w3=49, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(302, min_periods=max(302//3, 2)).rank(pct=True)
    persistence = change.rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.073 * persistence + 0.0005652 * anchor
    return base_signal.diff()

def f100_trap_252_jerk_v252_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=162, w2=313, w3=62, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(313, min_periods=max(313//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.919375 + 0.0005653 * anchor
    return base_signal.diff()

def f100_trap_253_rel_v253_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=169, w2=324, w3=75, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(324, min_periods=max(324//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0882 * slope + 0.0005654 * anchor
    return base_signal.diff()

def f100_trap_254_analyst_v254_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=176, w2=335, w3=88, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(335, min_periods=max(335//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.948125 + 0.0005655 * anchor
    return base_signal.diff()

def f100_trap_255_accrual_v255_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=183, w2=346, w3=101, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 346)
    curvature = _rolling_slope(acceleration, 101)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1034 * acceleration + 0.0005656 * anchor
    return base_signal.diff()

def f100_trap_256_jerk_v256_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=190, w2=357, w3=114, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(357, min_periods=max(357//3, 2)).mean()
    noise = impulse.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.976875 + 0.0005657 * anchor
    return base_signal.diff()

def f100_trap_257_rel_v257_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=197, w2=368, w3=127, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.99125 + 0.0005658 * anchor
    return base_signal.diff()

def f100_trap_258_analyst_v258_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=204, w2=379, w3=140, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(379, min_periods=max(379//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.005625 + 0.0005659 * anchor
    return base_signal.diff()

def f100_trap_259_accrual_v259_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=211, w2=390, w3=153, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(211, min_periods=max(211//3, 2)).mean(), b.abs().rolling(390, min_periods=max(390//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1338 * _rolling_slope(cover, 211) + 0.000566 * anchor
    return base_signal.diff()

def f100_trap_260_jerk_v260_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=218, w2=401, w3=166, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(401, min_periods=max(401//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.034375 + 0.0005661 * anchor
    return base_signal.diff()

def f100_trap_261_rel_v261_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=225, w2=412, w3=179, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04875 + 0.0005662 * anchor
    return base_signal.diff()

def f100_trap_262_analyst_v262_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=232, w2=423, w3=192, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(423, min_periods=max(423//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.063125 + 0.0005663 * anchor
    return base_signal.diff()

def f100_trap_263_accrual_v263_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=239, w2=434, w3=205, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0775 + 0.0005664 * anchor
    return base_signal.diff()

def f100_trap_264_jerk_v264_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=246, w2=445, w3=218, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(445, min_periods=max(445//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.091875 + 0.0005665 * anchor
    return base_signal.diff()

def f100_trap_265_rel_v265_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=253, w2=456, w3=231, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 253)
    slow = _rolling_slope(x, 456)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=231, adjust=False).mean() * 1.10625 + 0.0005666 * anchor
    return base_signal.diff()

def f100_trap_266_analyst_v266_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=9, w2=467, w3=244, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(9)
    drag = impulse.rolling(467, min_periods=max(467//3, 2)).mean()
    noise = impulse.abs().rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.120625 + 0.0005667 * anchor
    return base_signal.diff()

def f100_trap_267_accrual_v267_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=16, w2=478, w3=257, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(16)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1946 * persistence + 0.0005668 * anchor
    return base_signal.diff()

def f100_trap_268_jerk_v268_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=23, w2=489, w3=270, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(489, min_periods=max(489//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.149375 + 0.0005669 * anchor
    return base_signal.diff()

def f100_trap_269_rel_v269_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=30, w2=500, w3=283, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2098 * slope + 0.000567 * anchor
    return base_signal.diff()

def f100_trap_270_analyst_v270_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=37, w2=511, w3=296, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(511, min_periods=max(511//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.178125 + 0.0005671 * anchor
    return base_signal.diff()

def f100_trap_271_accrual_v271_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=44, w2=19, w3=309, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 19)
    curvature = _rolling_slope(acceleration, 309)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.225 * acceleration + 0.0005672 * anchor
    return base_signal.diff()

def f100_trap_272_jerk_v272_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=51, w2=30, w3=322, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.206875 + 0.0005673 * anchor
    return base_signal.diff()

def f100_trap_273_rel_v273_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=58, w2=41, w3=335, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(58, min_periods=max(58//3, 2)).mean())
    decay = spread.ewm(span=41, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.22125 + 0.0005674 * anchor
    return base_signal.diff()

def f100_trap_274_analyst_v274_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=65, w2=52, w3=348, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.235625 + 0.0005675 * anchor
    return base_signal.diff()

def f100_trap_275_accrual_v275_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=72, w2=63, w3=361, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(72, min_periods=max(72//3, 2)).mean(), b.abs().rolling(63, min_periods=max(63//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2554 * _rolling_slope(cover, 72) + 0.0005676 * anchor
    return base_signal.diff()

def f100_trap_276_jerk_v276_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=79, w2=74, w3=374, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(79)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.264375 + 0.0005677 * anchor
    return base_signal.diff()

def f100_trap_277_rel_v277_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=86, w2=85, w3=387, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(85, min_periods=max(85//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.27875 + 0.0005678 * anchor
    return base_signal.diff()

def f100_trap_278_analyst_v278_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=93, w2=96, w3=400, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(96, min_periods=max(96//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.293125 + 0.0005679 * anchor
    return base_signal.diff()

def f100_trap_279_accrual_v279_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=100, w2=107, w3=413, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(100) - b.diff(107)
    stress = imbalance.rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.3075 + 0.000568 * anchor
    return base_signal.diff()

def f100_trap_280_jerk_v280_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=107, w2=118, w3=426, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(118, min_periods=max(118//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.321875 + 0.0005681 * anchor
    return base_signal.diff()

def f100_trap_281_rel_v281_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=114, w2=129, w3=439, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 129)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.33625 + 0.0005682 * anchor
    return base_signal.diff()

def f100_trap_282_analyst_v282_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=121, w2=140, w3=452, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(140, min_periods=max(140//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.350625 + 0.0005683 * anchor
    return base_signal.diff()

def f100_trap_283_accrual_v283_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=128, w2=151, w3=465, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(151, min_periods=max(151//3, 2)).rank(pct=True)
    persistence = change.rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3162 * persistence + 0.0005684 * anchor
    return base_signal.diff()

def f100_trap_284_jerk_v284_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=135, w2=162, w3=478, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(162, min_periods=max(162//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.379375 + 0.0005685 * anchor
    return base_signal.diff()

def f100_trap_285_rel_v285_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=142, w2=173, w3=491, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(173, min_periods=max(173//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3314 * slope + 0.0005686 * anchor
    return base_signal.diff()

def f100_trap_286_analyst_v286_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=149, w2=184, w3=504, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(184, min_periods=max(184//3, 2)).mean()
    noise = impulse.abs().rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.408125 + 0.0005687 * anchor
    return base_signal.diff()

def f100_trap_287_accrual_v287_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=156, w2=195, w3=517, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 517)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3466 * acceleration + 0.0005688 * anchor
    return base_signal.diff()

def f100_trap_288_jerk_v288_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=163, w2=206, w3=530, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.436875 + 0.0005689 * anchor
    return base_signal.diff()

def f100_trap_289_rel_v289_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=170, w2=217, w3=543, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(170, min_periods=max(170//3, 2)).mean())
    decay = spread.ewm(span=217, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.45125 + 0.000569 * anchor
    return base_signal.diff()

def f100_trap_290_analyst_v290_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=177, w2=228, w3=556, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(228, min_periods=max(228//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.465625 + 0.0005691 * anchor
    return base_signal.diff()

def f100_trap_291_accrual_v291_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=184, w2=239, w3=569, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(184, min_periods=max(184//3, 2)).mean(), b.abs().rolling(239, min_periods=max(239//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.377 * _rolling_slope(cover, 184) + 0.0005692 * anchor
    return base_signal.diff()

def f100_trap_292_jerk_v292_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=191, w2=250, w3=582, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(250, min_periods=max(250//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.494375 + 0.0005693 * anchor
    return base_signal.diff()

def f100_trap_293_rel_v293_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=198, w2=261, w3=595, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(261, min_periods=max(261//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.50875 + 0.0005694 * anchor
    return base_signal.diff()

def f100_trap_294_analyst_v294_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=205, w2=272, w3=608, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(272, min_periods=max(272//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.523125 + 0.0005695 * anchor
    return base_signal.diff()

def f100_trap_295_accrual_v295_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=212, w2=283, w3=621, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.5375 + 0.0005696 * anchor
    return base_signal.diff()

def f100_trap_296_jerk_v296_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=219, w2=294, w3=634, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(294, min_periods=max(294//3, 2)).mean()
    noise = impulse.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.551875 + 0.0005697 * anchor
    return base_signal.diff()

def f100_trap_297_rel_v297_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=226, w2=305, w3=647, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 305)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.56625 + 0.0005698 * anchor
    return base_signal.diff()

def f100_trap_298_analyst_v298_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=233, w2=316, w3=660, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(316, min_periods=max(316//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.580625 + 0.0005699 * anchor
    return base_signal.diff()

def f100_trap_299_accrual_v299_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=240, w2=327, w3=673, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(327, min_periods=max(327//3, 2)).rank(pct=True)
    persistence = change.rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0614 * persistence + 0.00057 * anchor
    return base_signal.diff()

def f100_trap_300_jerk_v300_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=247, w2=338, w3=686, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.609375 + 0.0005701 * anchor
    return base_signal.diff()
