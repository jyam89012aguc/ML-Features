"""61 analyst revision momentum d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f61_arm_451_analyst_v451_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=96, w2=400, w3=63, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 400)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=63, adjust=False).mean() * 1.065625 + 0.0034652 * anchor
    return base_signal.diff().diff()

def f61_arm_452_analyst_v452_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=103, w2=411, w3=76, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(411, min_periods=max(411//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.08 + 0.0034653 * anchor
    return base_signal.diff().diff()

def f61_arm_453_analyst_v453_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=110, w2=422, w3=89, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(110)
    rank = change.rolling(422, min_periods=max(422//3, 2)).rank(pct=True)
    persistence = change.rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2942 * persistence + 0.0034654 * anchor
    return base_signal.diff().diff()

def f61_arm_454_analyst_v454_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=117, w2=433, w3=102, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(433, min_periods=max(433//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10875 + 0.0034655 * anchor
    return base_signal.diff().diff()

def f61_arm_455_analyst_v455_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=124, w2=444, w3=115, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(444, min_periods=max(444//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3094 * slope + 0.0034656 * anchor
    return base_signal.diff().diff()

def f61_arm_456_analyst_v456_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=131, w2=455, w3=128, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(455, min_periods=max(455//3, 2)).mean()
    noise = impulse.abs().rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1375 + 0.0034657 * anchor
    return base_signal.diff().diff()

def f61_arm_457_analyst_v457_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=138, w2=466, w3=141, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 466)
    curvature = _rolling_slope(acceleration, 141)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3246 * acceleration + 0.0034658 * anchor
    return base_signal.diff().diff()

def f61_arm_458_analyst_v458_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=145, w2=477, w3=154, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(477, min_periods=max(477//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.16625 + 0.0034659 * anchor
    return base_signal.diff().diff()

def f61_arm_459_analyst_v459_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=152, w2=488, w3=167, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(488, min_periods=max(488//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3398 * _rolling_slope(draw, 167) + 0.003466 * anchor
    return base_signal.diff().diff()

def f61_arm_460_analyst_v460_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=159, w2=499, w3=180, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(499, min_periods=max(499//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.195 + 0.0034661 * anchor
    return base_signal.diff().diff()

def f61_arm_461_analyst_v461_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=166, w2=510, w3=193, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 510)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=193, adjust=False).mean() * 1.209375 + 0.0034662 * anchor
    return base_signal.diff().diff()

def f61_arm_462_analyst_v462_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=173, w2=18, w3=206, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(18, min_periods=max(18//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.22375 + 0.0034663 * anchor
    return base_signal.diff().diff()

def f61_arm_463_analyst_v463_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=180, w2=29, w3=219, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(29, min_periods=max(29//3, 2)).rank(pct=True)
    persistence = change.rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3702 * persistence + 0.0034664 * anchor
    return base_signal.diff().diff()

def f61_arm_464_analyst_v464_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=187, w2=40, w3=232, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(40, min_periods=max(40//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2525 + 0.0034665 * anchor
    return base_signal.diff().diff()

def f61_arm_465_analyst_v465_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=194, w2=51, w3=245, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(51, min_periods=max(51//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3854 * slope + 0.0034666 * anchor
    return base_signal.diff().diff()

def f61_arm_466_analyst_v466_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=201, w2=62, w3=258, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.28125 + 0.0034667 * anchor
    return base_signal.diff().diff()

def f61_arm_467_analyst_v467_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=208, w2=73, w3=271, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 73)
    curvature = _rolling_slope(acceleration, 271)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4006 * acceleration + 0.0034668 * anchor
    return base_signal.diff().diff()

def f61_arm_468_analyst_v468_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=215, w2=84, w3=284, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(84, min_periods=max(84//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.31 + 0.0034669 * anchor
    return base_signal.diff().diff()

def f61_arm_469_analyst_v469_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=222, w2=95, w3=297, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(95, min_periods=max(95//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0394 * _rolling_slope(draw, 297) + 0.003467 * anchor
    return base_signal.diff().diff()

def f61_arm_470_analyst_v470_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=229, w2=106, w3=310, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(106, min_periods=max(106//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33875 + 0.0034671 * anchor
    return base_signal.diff().diff()

def f61_arm_471_analyst_v471_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=236, w2=117, w3=323, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.353125 + 0.0034672 * anchor
    return base_signal.diff().diff()

def f61_arm_472_analyst_v472_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=243, w2=128, w3=336, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3675 + 0.0034673 * anchor
    return base_signal.diff().diff()

def f61_arm_473_analyst_v473_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=250, w2=139, w3=349, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(139, min_periods=max(139//3, 2)).rank(pct=True)
    persistence = change.rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0698 * persistence + 0.0034674 * anchor
    return base_signal.diff().diff()

def f61_arm_474_analyst_v474_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=6, w2=150, w3=362, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(150, min_periods=max(150//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39625 + 0.0034675 * anchor
    return base_signal.diff().diff()

def f61_arm_475_analyst_v475_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=13, w2=161, w3=375, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.085 * slope + 0.0034676 * anchor
    return base_signal.diff().diff()

def f61_arm_476_analyst_v476_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=20, w2=172, w3=388, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(20)
    drag = impulse.rolling(172, min_periods=max(172//3, 2)).mean()
    noise = impulse.abs().rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.425 + 0.0034677 * anchor
    return base_signal.diff().diff()

def f61_arm_477_analyst_v477_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=27, w2=183, w3=401, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 183)
    curvature = _rolling_slope(acceleration, 401)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1002 * acceleration + 0.0034678 * anchor
    return base_signal.diff().diff()

def f61_arm_478_analyst_v478_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=34, w2=194, w3=414, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(194, min_periods=max(194//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.45375 + 0.0034679 * anchor
    return base_signal.diff().diff()

def f61_arm_479_analyst_v479_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=41, w2=205, w3=427, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(205, min_periods=max(205//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1154 * _rolling_slope(draw, 427) + 0.003468 * anchor
    return base_signal.diff().diff()

def f61_arm_480_analyst_v480_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=48, w2=216, w3=440, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(216, min_periods=max(216//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4825 + 0.0034681 * anchor
    return base_signal.diff().diff()

def f61_arm_481_analyst_v481_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=55, w2=227, w3=453, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 227)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.496875 + 0.0034682 * anchor
    return base_signal.diff().diff()

def f61_arm_482_analyst_v482_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=62, w2=238, w3=466, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(238, min_periods=max(238//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.51125 + 0.0034683 * anchor
    return base_signal.diff().diff()

def f61_arm_483_analyst_v483_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=69, w2=249, w3=479, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(69)
    rank = change.rolling(249, min_periods=max(249//3, 2)).rank(pct=True)
    persistence = change.rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1458 * persistence + 0.0034684 * anchor
    return base_signal.diff().diff()

def f61_arm_484_analyst_v484_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=76, w2=260, w3=492, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(260, min_periods=max(260//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54 + 0.0034685 * anchor
    return base_signal.diff().diff()

def f61_arm_485_analyst_v485_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=83, w2=271, w3=505, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(271, min_periods=max(271//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.161 * slope + 0.0034686 * anchor
    return base_signal.diff().diff()

def f61_arm_486_analyst_v486_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=90, w2=282, w3=518, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(90)
    drag = impulse.rolling(282, min_periods=max(282//3, 2)).mean()
    noise = impulse.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.56875 + 0.0034687 * anchor
    return base_signal.diff().diff()

def f61_arm_487_analyst_v487_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=97, w2=293, w3=531, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 293)
    curvature = _rolling_slope(acceleration, 531)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1762 * acceleration + 0.0034688 * anchor
    return base_signal.diff().diff()

def f61_arm_488_analyst_v488_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=104, w2=304, w3=544, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(104, min_periods=max(104//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5975 + 0.0034689 * anchor
    return base_signal.diff().diff()

def f61_arm_489_analyst_v489_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=111, w2=315, w3=557, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(315, min_periods=max(315//3, 2)).max()
    rebound = x - x.rolling(111, min_periods=max(111//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1914 * _rolling_slope(draw, 557) + 0.003469 * anchor
    return base_signal.diff().diff()

def f61_arm_490_analyst_v490_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=118, w2=326, w3=570, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(326, min_periods=max(326//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(570, min_periods=max(570//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.853125 + 0.0034691 * anchor
    return base_signal.diff().diff()

def f61_arm_491_analyst_v491_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=125, w2=337, w3=583, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 125)
    slow = _rolling_slope(x, 337)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8675 + 0.0034692 * anchor
    return base_signal.diff().diff()

def f61_arm_492_analyst_v492_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=132, w2=348, w3=596, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(348, min_periods=max(348//3, 2)).max()
    trough = x.rolling(132, min_periods=max(132//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.881875 + 0.0034693 * anchor
    return base_signal.diff().diff()

def f61_arm_493_analyst_v493_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=139, w2=359, w3=609, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(359, min_periods=max(359//3, 2)).rank(pct=True)
    persistence = change.rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2218 * persistence + 0.0034694 * anchor
    return base_signal.diff().diff()

def f61_arm_494_analyst_v494_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=146, w2=370, w3=622, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(146, min_periods=max(146//3, 2)).std()
    vol_slow = ret.rolling(370, min_periods=max(370//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.910625 + 0.0034695 * anchor
    return base_signal.diff().diff()

def f61_arm_495_analyst_v495_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=153, w2=381, w3=635, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(381, min_periods=max(381//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 153)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.237 * slope + 0.0034696 * anchor
    return base_signal.diff().diff()

def f61_arm_496_analyst_v496_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=160, w2=392, w3=648, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(392, min_periods=max(392//3, 2)).mean()
    noise = impulse.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.939375 + 0.0034697 * anchor
    return base_signal.diff().diff()

def f61_arm_497_analyst_v497_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=167, w2=403, w3=661, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 167)
    acceleration = _rolling_slope(velocity, 403)
    curvature = _rolling_slope(acceleration, 661)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2522 * acceleration + 0.0034698 * anchor
    return base_signal.diff().diff()

def f61_arm_498_analyst_v498_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=174, w2=414, w3=674, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(174, min_periods=max(174//3, 2)).mean(), upside.rolling(414, min_periods=max(414//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.968125 + 0.0034699 * anchor
    return base_signal.diff().diff()

def f61_arm_499_analyst_v499_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=181, w2=425, w3=687, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(425, min_periods=max(425//3, 2)).max()
    rebound = x - x.rolling(181, min_periods=max(181//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2674 * _rolling_slope(draw, 687) + 0.00347 * anchor
    return base_signal.diff().diff()

def f61_arm_500_analyst_v500_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=188, w2=436, w3=700, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 188)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.996875 + 0.0034701 * anchor
    return base_signal.diff().diff()

def f61_arm_501_analyst_v501_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=195, w2=447, w3=713, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 195)
    slow = _rolling_slope(x, 447)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.01125 + 0.0034702 * anchor
    return base_signal.diff().diff()

def f61_arm_502_analyst_v502_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=202, w2=458, w3=726, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(458, min_periods=max(458//3, 2)).max()
    trough = x.rolling(202, min_periods=max(202//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.025625 + 0.0034703 * anchor
    return base_signal.diff().diff()

def f61_arm_503_analyst_v503_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=209, w2=469, w3=739, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(469, min_periods=max(469//3, 2)).rank(pct=True)
    persistence = change.rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2978 * persistence + 0.0034704 * anchor
    return base_signal.diff().diff()

def f61_arm_504_analyst_v504_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=216, w2=480, w3=752, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(216, min_periods=max(216//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.054375 + 0.0034705 * anchor
    return base_signal.diff().diff()

def f61_arm_505_analyst_v505_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=223, w2=491, w3=765, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(491, min_periods=max(491//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 223)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.313 * slope + 0.0034706 * anchor
    return base_signal.diff().diff()

def f61_arm_506_analyst_v506_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=230, w2=502, w3=21, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(502, min_periods=max(502//3, 2)).mean()
    noise = impulse.abs().rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.083125 + 0.0034707 * anchor
    return base_signal.diff().diff()

def f61_arm_507_analyst_v507_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=237, w2=10, w3=34, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 237)
    acceleration = _rolling_slope(velocity, 10)
    curvature = _rolling_slope(acceleration, 34)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3282 * acceleration + 0.0034708 * anchor
    return base_signal.diff().diff()

def f61_arm_508_analyst_v508_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=244, w2=21, w3=47, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(21, min_periods=max(21//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(47) * 1.111875 + 0.0034709 * anchor
    return base_signal.diff().diff()

def f61_arm_509_analyst_v509_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=251, w2=32, w3=60, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3434 * _rolling_slope(draw, 60) + 0.003471 * anchor
    return base_signal.diff().diff()

def f61_arm_510_analyst_v510_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=7, w2=43, w3=73, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(43, min_periods=max(43//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.140625 + 0.0034711 * anchor
    return base_signal.diff().diff()

def f61_arm_511_analyst_v511_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=14, w2=54, w3=86, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 54)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=86, adjust=False).mean() * 1.155 + 0.0034712 * anchor
    return base_signal.diff().diff()

def f61_arm_512_analyst_v512_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=21, w2=65, w3=99, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(65, min_periods=max(65//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.169375 + 0.0034713 * anchor
    return base_signal.diff().diff()

def f61_arm_513_analyst_v513_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=28, w2=76, w3=112, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(28)
    rank = change.rolling(76, min_periods=max(76//3, 2)).rank(pct=True)
    persistence = change.rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3738 * persistence + 0.0034714 * anchor
    return base_signal.diff().diff()

def f61_arm_514_analyst_v514_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=35, w2=87, w3=125, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(87, min_periods=max(87//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.198125 + 0.0034715 * anchor
    return base_signal.diff().diff()

def f61_arm_515_analyst_v515_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=42, w2=98, w3=138, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(98, min_periods=max(98//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 42)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.389 * slope + 0.0034716 * anchor
    return base_signal.diff().diff()

def f61_arm_516_analyst_v516_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=49, w2=109, w3=151, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(49)
    drag = impulse.rolling(109, min_periods=max(109//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.226875 + 0.0034717 * anchor
    return base_signal.diff().diff()

def f61_arm_517_analyst_v517_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=56, w2=120, w3=164, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 56)
    acceleration = _rolling_slope(velocity, 120)
    curvature = _rolling_slope(acceleration, 164)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4042 * acceleration + 0.0034718 * anchor
    return base_signal.diff().diff()

def f61_arm_518_analyst_v518_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=63, w2=131, w3=177, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(131, min_periods=max(131//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.255625 + 0.0034719 * anchor
    return base_signal.diff().diff()

def f61_arm_519_analyst_v519_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=70, w2=142, w3=190, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(142, min_periods=max(142//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.043 * _rolling_slope(draw, 190) + 0.003472 * anchor
    return base_signal.diff().diff()

def f61_arm_520_analyst_v520_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=77, w2=153, w3=203, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(153, min_periods=max(153//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.284375 + 0.0034721 * anchor
    return base_signal.diff().diff()

def f61_arm_521_analyst_v521_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=84, w2=164, w3=216, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 164)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=216, adjust=False).mean() * 1.29875 + 0.0034722 * anchor
    return base_signal.diff().diff()

def f61_arm_522_analyst_v522_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=91, w2=175, w3=229, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(175, min_periods=max(175//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.313125 + 0.0034723 * anchor
    return base_signal.diff().diff()

def f61_arm_523_analyst_v523_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=98, w2=186, w3=242, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(98)
    rank = change.rolling(186, min_periods=max(186//3, 2)).rank(pct=True)
    persistence = change.rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0734 * persistence + 0.0034724 * anchor
    return base_signal.diff().diff()

def f61_arm_524_analyst_v524_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=105, w2=197, w3=255, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(197, min_periods=max(197//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.341875 + 0.0034725 * anchor
    return base_signal.diff().diff()

def f61_arm_525_analyst_v525_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=112, w2=208, w3=268, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(208, min_periods=max(208//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0886 * slope + 0.0034726 * anchor
    return base_signal.diff().diff()
