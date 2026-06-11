"""64 analyst unexpected earnings kinetics d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Analyst_Sentiment - Institutional-grade short-side signal.
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

def f64_asue_526_analyst_v526_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=169, w2=402, w3=214, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.959375 + 0.0036527 * anchor
    return base_signal.diff()

def f64_asue_527_analyst_v527_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=176, w2=413, w3=227, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 227)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2334 * acceleration + 0.0036528 * anchor
    return base_signal.diff()

def f64_asue_528_analyst_v528_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=183, w2=424, w3=240, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(424, min_periods=max(424//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.988125 + 0.0036529 * anchor
    return base_signal.diff()

def f64_asue_529_analyst_v529_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=190, w2=435, w3=253, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(435, min_periods=max(435//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2486 * _rolling_slope(draw, 253) + 0.003653 * anchor
    return base_signal.diff()

def f64_asue_530_analyst_v530_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=197, w2=446, w3=266, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 197)
    baseline = trend.rolling(446, min_periods=max(446//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.016875 + 0.0036531 * anchor
    return base_signal.diff()

def f64_asue_531_analyst_v531_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=204, w2=457, w3=279, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 204)
    slow = _rolling_slope(x, 457)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=279, adjust=False).mean() * 1.03125 + 0.0036532 * anchor
    return base_signal.diff()

def f64_asue_532_analyst_v532_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=211, w2=468, w3=292, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(468, min_periods=max(468//3, 2)).max()
    trough = x.rolling(211, min_periods=max(211//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.045625 + 0.0036533 * anchor
    return base_signal.diff()

def f64_asue_533_analyst_v533_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=218, w2=479, w3=305, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.279 * persistence + 0.0036534 * anchor
    return base_signal.diff()

def f64_asue_534_analyst_v534_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=225, w2=490, w3=318, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(225, min_periods=max(225//3, 2)).std()
    vol_slow = ret.rolling(490, min_periods=max(490//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.074375 + 0.0036535 * anchor
    return base_signal.diff()

def f64_asue_535_analyst_v535_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=232, w2=501, w3=331, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 232)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2942 * slope + 0.0036536 * anchor
    return base_signal.diff()

def f64_asue_536_analyst_v536_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=239, w2=512, w3=344, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(512, min_periods=max(512//3, 2)).mean()
    noise = impulse.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.103125 + 0.0036537 * anchor
    return base_signal.diff()

def f64_asue_537_analyst_v537_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=246, w2=20, w3=357, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 246)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3094 * acceleration + 0.0036538 * anchor
    return base_signal.diff()

def f64_asue_538_analyst_v538_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=253, w2=31, w3=370, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(31, min_periods=max(31//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.131875 + 0.0036539 * anchor
    return base_signal.diff()

def f64_asue_539_analyst_v539_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=9, w2=42, w3=383, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(42, min_periods=max(42//3, 2)).max()
    rebound = x - x.rolling(9, min_periods=max(9//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3246 * _rolling_slope(draw, 383) + 0.003654 * anchor
    return base_signal.diff()

def f64_asue_540_analyst_v540_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=16, w2=53, w3=396, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.160625 + 0.0036541 * anchor
    return base_signal.diff()

def f64_asue_541_analyst_v541_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=23, w2=64, w3=409, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 64)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.175 + 0.0036542 * anchor
    return base_signal.diff()

def f64_asue_542_analyst_v542_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=30, w2=75, w3=422, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(75, min_periods=max(75//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.189375 + 0.0036543 * anchor
    return base_signal.diff()

def f64_asue_543_analyst_v543_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=37, w2=86, w3=435, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(37)
    rank = change.rolling(86, min_periods=max(86//3, 2)).rank(pct=True)
    persistence = change.rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355 * persistence + 0.0036544 * anchor
    return base_signal.diff()

def f64_asue_544_analyst_v544_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=44, w2=97, w3=448, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.218125 + 0.0036545 * anchor
    return base_signal.diff()

def f64_asue_545_analyst_v545_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=51, w2=108, w3=461, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(108, min_periods=max(108//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3702 * slope + 0.0036546 * anchor
    return base_signal.diff()

def f64_asue_546_analyst_v546_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=58, w2=119, w3=474, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(58)
    drag = impulse.rolling(119, min_periods=max(119//3, 2)).mean()
    noise = impulse.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.246875 + 0.0036547 * anchor
    return base_signal.diff()

def f64_asue_547_analyst_v547_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=65, w2=130, w3=487, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 130)
    curvature = _rolling_slope(acceleration, 487)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3854 * acceleration + 0.0036548 * anchor
    return base_signal.diff()

def f64_asue_548_analyst_v548_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=72, w2=141, w3=500, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(72, min_periods=max(72//3, 2)).mean(), upside.rolling(141, min_periods=max(141//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.275625 + 0.0036549 * anchor
    return base_signal.diff()

def f64_asue_549_analyst_v549_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=79, w2=152, w3=513, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(152, min_periods=max(152//3, 2)).max()
    rebound = x - x.rolling(79, min_periods=max(79//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4006 * _rolling_slope(draw, 513) + 0.003655 * anchor
    return base_signal.diff()

def f64_asue_550_analyst_v550_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=86, w2=163, w3=526, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(163, min_periods=max(163//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.304375 + 0.0036551 * anchor
    return base_signal.diff()

def f64_asue_551_analyst_v551_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=93, w2=174, w3=539, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 174)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.31875 + 0.0036552 * anchor
    return base_signal.diff()

def f64_asue_552_analyst_v552_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=100, w2=185, w3=552, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.333125 + 0.0036553 * anchor
    return base_signal.diff()

def f64_asue_553_analyst_v553_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=107, w2=196, w3=565, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(107)
    rank = change.rolling(196, min_periods=max(196//3, 2)).rank(pct=True)
    persistence = change.rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0546 * persistence + 0.0036554 * anchor
    return base_signal.diff()

def f64_asue_554_analyst_v554_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=114, w2=207, w3=578, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.361875 + 0.0036555 * anchor
    return base_signal.diff()

def f64_asue_555_analyst_v555_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=121, w2=218, w3=591, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(218, min_periods=max(218//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0698 * slope + 0.0036556 * anchor
    return base_signal.diff()

def f64_asue_556_analyst_v556_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=128, w2=229, w3=604, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(229, min_periods=max(229//3, 2)).mean()
    noise = impulse.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.390625 + 0.0036557 * anchor
    return base_signal.diff()

def f64_asue_557_analyst_v557_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=135, w2=240, w3=617, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 617)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.085 * acceleration + 0.0036558 * anchor
    return base_signal.diff()

def f64_asue_558_analyst_v558_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=142, w2=251, w3=630, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.419375 + 0.0036559 * anchor
    return base_signal.diff()

def f64_asue_559_analyst_v559_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=149, w2=262, w3=643, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1002 * _rolling_slope(draw, 643) + 0.003656 * anchor
    return base_signal.diff()

def f64_asue_560_analyst_v560_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=156, w2=273, w3=656, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(273, min_periods=max(273//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.448125 + 0.0036561 * anchor
    return base_signal.diff()

def f64_asue_561_analyst_v561_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=163, w2=284, w3=669, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 284)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4625 + 0.0036562 * anchor
    return base_signal.diff()

def f64_asue_562_analyst_v562_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=170, w2=295, w3=682, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.476875 + 0.0036563 * anchor
    return base_signal.diff()

def f64_asue_563_analyst_v563_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=177, w2=306, w3=695, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(306, min_periods=max(306//3, 2)).rank(pct=True)
    persistence = change.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1306 * persistence + 0.0036564 * anchor
    return base_signal.diff()

def f64_asue_564_analyst_v564_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=184, w2=317, w3=708, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(317, min_periods=max(317//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.505625 + 0.0036565 * anchor
    return base_signal.diff()

def f64_asue_565_analyst_v565_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=191, w2=328, w3=721, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(328, min_periods=max(328//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1458 * slope + 0.0036566 * anchor
    return base_signal.diff()

def f64_asue_566_analyst_v566_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=198, w2=339, w3=734, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.534375 + 0.0036567 * anchor
    return base_signal.diff()

def f64_asue_567_analyst_v567_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=205, w2=350, w3=747, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 747)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.161 * acceleration + 0.0036568 * anchor
    return base_signal.diff()

def f64_asue_568_analyst_v568_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=212, w2=361, w3=760, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(361, min_periods=max(361//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.563125 + 0.0036569 * anchor
    return base_signal.diff()

def f64_asue_569_analyst_v569_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=219, w2=372, w3=16, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(372, min_periods=max(372//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1762 * _rolling_slope(draw, 16) + 0.003657 * anchor
    return base_signal.diff()

def f64_asue_570_analyst_v570_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=226, w2=383, w3=29, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(383, min_periods=max(383//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.591875 + 0.0036571 * anchor
    return base_signal.diff()

def f64_asue_571_analyst_v571_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=233, w2=394, w3=42, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 394)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=42, adjust=False).mean() * 1.60625 + 0.0036572 * anchor
    return base_signal.diff()

def f64_asue_572_analyst_v572_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=240, w2=405, w3=55, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(405, min_periods=max(405//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.620625 + 0.0036573 * anchor
    return base_signal.diff()

def f64_asue_573_analyst_v573_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=247, w2=416, w3=68, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(416, min_periods=max(416//3, 2)).rank(pct=True)
    persistence = change.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2066 * persistence + 0.0036574 * anchor
    return base_signal.diff()

def f64_asue_574_analyst_v574_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=254, w2=427, w3=81, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(427, min_periods=max(427//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87625 + 0.0036575 * anchor
    return base_signal.diff()

def f64_asue_575_analyst_v575_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=10, w2=438, w3=94, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2218 * slope + 0.0036576 * anchor
    return base_signal.diff()

def f64_asue_576_analyst_v576_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=17, w2=449, w3=107, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(17)
    drag = impulse.rolling(449, min_periods=max(449//3, 2)).mean()
    noise = impulse.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.905 + 0.0036577 * anchor
    return base_signal.diff()

def f64_asue_577_analyst_v577_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=24, w2=460, w3=120, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 460)
    curvature = _rolling_slope(acceleration, 120)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.237 * acceleration + 0.0036578 * anchor
    return base_signal.diff()

def f64_asue_578_analyst_v578_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=31, w2=471, w3=133, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(471, min_periods=max(471//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93375 + 0.0036579 * anchor
    return base_signal.diff()

def f64_asue_579_analyst_v579_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=38, w2=482, w3=146, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(482, min_periods=max(482//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2522 * _rolling_slope(draw, 146) + 0.003658 * anchor
    return base_signal.diff()

def f64_asue_580_analyst_v580_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=45, w2=493, w3=159, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(493, min_periods=max(493//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9625 + 0.0036581 * anchor
    return base_signal.diff()

def f64_asue_581_analyst_v581_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=52, w2=504, w3=172, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 504)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=172, adjust=False).mean() * 0.976875 + 0.0036582 * anchor
    return base_signal.diff()

def f64_asue_582_analyst_v582_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=59, w2=12, w3=185, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(12, min_periods=max(12//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.99125 + 0.0036583 * anchor
    return base_signal.diff()

def f64_asue_583_analyst_v583_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=66, w2=23, w3=198, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(66)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2826 * persistence + 0.0036584 * anchor
    return base_signal.diff()

def f64_asue_584_analyst_v584_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=73, w2=34, w3=211, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(34, min_periods=max(34//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.02 + 0.0036585 * anchor
    return base_signal.diff()

def f64_asue_585_analyst_v585_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=80, w2=45, w3=224, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(45, min_periods=max(45//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2978 * slope + 0.0036586 * anchor
    return base_signal.diff()

def f64_asue_586_analyst_v586_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=87, w2=56, w3=237, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(87)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.04875 + 0.0036587 * anchor
    return base_signal.diff()

def f64_asue_587_analyst_v587_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=94, w2=67, w3=250, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 67)
    curvature = _rolling_slope(acceleration, 250)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.313 * acceleration + 0.0036588 * anchor
    return base_signal.diff()

def f64_asue_588_analyst_v588_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=101, w2=78, w3=263, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(78, min_periods=max(78//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0775 + 0.0036589 * anchor
    return base_signal.diff()

def f64_asue_589_analyst_v589_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=108, w2=89, w3=276, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3282 * _rolling_slope(draw, 276) + 0.003659 * anchor
    return base_signal.diff()

def f64_asue_590_analyst_v590_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=115, w2=100, w3=289, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(100, min_periods=max(100//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.10625 + 0.0036591 * anchor
    return base_signal.diff()

def f64_asue_591_analyst_v591_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=122, w2=111, w3=302, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 111)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.120625 + 0.0036592 * anchor
    return base_signal.diff()

def f64_asue_592_analyst_v592_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=129, w2=122, w3=315, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.135 + 0.0036593 * anchor
    return base_signal.diff()

def f64_asue_593_analyst_v593_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=136, w2=133, w3=328, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(133, min_periods=max(133//3, 2)).rank(pct=True)
    persistence = change.rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3586 * persistence + 0.0036594 * anchor
    return base_signal.diff()

def f64_asue_594_analyst_v594_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=143, w2=144, w3=341, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(144, min_periods=max(144//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16375 + 0.0036595 * anchor
    return base_signal.diff()

def f64_asue_595_analyst_v595_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=150, w2=155, w3=354, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(155, min_periods=max(155//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3738 * slope + 0.0036596 * anchor
    return base_signal.diff()

def f64_asue_596_analyst_v596_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=157, w2=166, w3=367, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(166, min_periods=max(166//3, 2)).mean()
    noise = impulse.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1925 + 0.0036597 * anchor
    return base_signal.diff()

def f64_asue_597_analyst_v597_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=164, w2=177, w3=380, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 177)
    curvature = _rolling_slope(acceleration, 380)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.389 * acceleration + 0.0036598 * anchor
    return base_signal.diff()

def f64_asue_598_analyst_v598_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=171, w2=188, w3=393, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(188, min_periods=max(188//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.22125 + 0.0036599 * anchor
    return base_signal.diff()

def f64_asue_599_analyst_v599_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=178, w2=199, w3=406, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(199, min_periods=max(199//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4042 * _rolling_slope(draw, 406) + 0.00366 * anchor
    return base_signal.diff()

def f64_asue_600_analyst_v600_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=185, w2=210, w3=419, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(210, min_periods=max(210//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.25 + 0.0036601 * anchor
    return base_signal.diff()
