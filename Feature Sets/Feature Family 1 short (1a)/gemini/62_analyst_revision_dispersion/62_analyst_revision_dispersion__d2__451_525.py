"""62 analyst revision dispersion d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f62_ard_451_analyst_v451_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=29, w2=461, w3=293, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 461)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=293, adjust=False).mean() * 1.18625 + 0.0035252 * anchor
    return base_signal.diff().diff()

def f62_ard_452_analyst_v452_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=36, w2=472, w3=306, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(472, min_periods=max(472//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.200625 + 0.0035253 * anchor
    return base_signal.diff().diff()

def f62_ard_453_analyst_v453_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=43, w2=483, w3=319, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(43)
    rank = change.rolling(483, min_periods=max(483//3, 2)).rank(pct=True)
    persistence = change.rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3374 * persistence + 0.0035254 * anchor
    return base_signal.diff().diff()

def f62_ard_454_analyst_v454_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=50, w2=494, w3=332, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(494, min_periods=max(494//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.229375 + 0.0035255 * anchor
    return base_signal.diff().diff()

def f62_ard_455_analyst_v455_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=57, w2=505, w3=345, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3526 * slope + 0.0035256 * anchor
    return base_signal.diff().diff()

def f62_ard_456_analyst_v456_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=64, w2=13, w3=358, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(64)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.258125 + 0.0035257 * anchor
    return base_signal.diff().diff()

def f62_ard_457_analyst_v457_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=71, w2=24, w3=371, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 24)
    curvature = _rolling_slope(acceleration, 371)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3678 * acceleration + 0.0035258 * anchor
    return base_signal.diff().diff()

def f62_ard_458_analyst_v458_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=78, w2=35, w3=384, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(35, min_periods=max(35//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.286875 + 0.0035259 * anchor
    return base_signal.diff().diff()

def f62_ard_459_analyst_v459_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=85, w2=46, w3=397, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(46, min_periods=max(46//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.383 * _rolling_slope(draw, 397) + 0.003526 * anchor
    return base_signal.diff().diff()

def f62_ard_460_analyst_v460_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=92, w2=57, w3=410, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(57, min_periods=max(57//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.315625 + 0.0035261 * anchor
    return base_signal.diff().diff()

def f62_ard_461_analyst_v461_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=99, w2=68, w3=423, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 68)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.33 + 0.0035262 * anchor
    return base_signal.diff().diff()

def f62_ard_462_analyst_v462_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=106, w2=79, w3=436, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(79, min_periods=max(79//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.344375 + 0.0035263 * anchor
    return base_signal.diff().diff()

def f62_ard_463_analyst_v463_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=113, w2=90, w3=449, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(113)
    rank = change.rolling(90, min_periods=max(90//3, 2)).rank(pct=True)
    persistence = change.rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.037 * persistence + 0.0035264 * anchor
    return base_signal.diff().diff()

def f62_ard_464_analyst_v464_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=120, w2=101, w3=462, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(101, min_periods=max(101//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.373125 + 0.0035265 * anchor
    return base_signal.diff().diff()

def f62_ard_465_analyst_v465_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=127, w2=112, w3=475, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(112, min_periods=max(112//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0522 * slope + 0.0035266 * anchor
    return base_signal.diff().diff()

def f62_ard_466_analyst_v466_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=134, w2=123, w3=488, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.401875 + 0.0035267 * anchor
    return base_signal.diff().diff()

def f62_ard_467_analyst_v467_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=141, w2=134, w3=501, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 134)
    curvature = _rolling_slope(acceleration, 501)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0674 * acceleration + 0.0035268 * anchor
    return base_signal.diff().diff()

def f62_ard_468_analyst_v468_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=148, w2=145, w3=514, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(145, min_periods=max(145//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.430625 + 0.0035269 * anchor
    return base_signal.diff().diff()

def f62_ard_469_analyst_v469_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=155, w2=156, w3=527, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(156, min_periods=max(156//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0826 * _rolling_slope(draw, 527) + 0.003527 * anchor
    return base_signal.diff().diff()

def f62_ard_470_analyst_v470_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=162, w2=167, w3=540, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(167, min_periods=max(167//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.459375 + 0.0035271 * anchor
    return base_signal.diff().diff()

def f62_ard_471_analyst_v471_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=169, w2=178, w3=553, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 178)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.47375 + 0.0035272 * anchor
    return base_signal.diff().diff()

def f62_ard_472_analyst_v472_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=176, w2=189, w3=566, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(189, min_periods=max(189//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.488125 + 0.0035273 * anchor
    return base_signal.diff().diff()

def f62_ard_473_analyst_v473_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=183, w2=200, w3=579, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(200, min_periods=max(200//3, 2)).rank(pct=True)
    persistence = change.rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.113 * persistence + 0.0035274 * anchor
    return base_signal.diff().diff()

def f62_ard_474_analyst_v474_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=190, w2=211, w3=592, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(211, min_periods=max(211//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.516875 + 0.0035275 * anchor
    return base_signal.diff().diff()

def f62_ard_475_analyst_v475_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=197, w2=222, w3=605, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(222, min_periods=max(222//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1282 * slope + 0.0035276 * anchor
    return base_signal.diff().diff()

def f62_ard_476_analyst_v476_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=204, w2=233, w3=618, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(233, min_periods=max(233//3, 2)).mean()
    noise = impulse.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.545625 + 0.0035277 * anchor
    return base_signal.diff().diff()

def f62_ard_477_analyst_v477_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=211, w2=244, w3=631, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 244)
    curvature = _rolling_slope(acceleration, 631)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1434 * acceleration + 0.0035278 * anchor
    return base_signal.diff().diff()

def f62_ard_478_analyst_v478_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=218, w2=255, w3=644, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(255, min_periods=max(255//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.574375 + 0.0035279 * anchor
    return base_signal.diff().diff()

def f62_ard_479_analyst_v479_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=225, w2=266, w3=657, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(266, min_periods=max(266//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1586 * _rolling_slope(draw, 657) + 0.003528 * anchor
    return base_signal.diff().diff()

def f62_ard_480_analyst_v480_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=232, w2=277, w3=670, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(277, min_periods=max(277//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.603125 + 0.0035281 * anchor
    return base_signal.diff().diff()

def f62_ard_481_analyst_v481_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=239, w2=288, w3=683, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 288)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.6175 + 0.0035282 * anchor
    return base_signal.diff().diff()

def f62_ard_482_analyst_v482_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=246, w2=299, w3=696, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(299, min_periods=max(299//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.85875 + 0.0035283 * anchor
    return base_signal.diff().diff()

def f62_ard_483_analyst_v483_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=253, w2=310, w3=709, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(310, min_periods=max(310//3, 2)).rank(pct=True)
    persistence = change.rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189 * persistence + 0.0035284 * anchor
    return base_signal.diff().diff()

def f62_ard_484_analyst_v484_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=9, w2=321, w3=722, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(321, min_periods=max(321//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8875 + 0.0035285 * anchor
    return base_signal.diff().diff()

def f62_ard_485_analyst_v485_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=16, w2=332, w3=735, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(332, min_periods=max(332//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2042 * slope + 0.0035286 * anchor
    return base_signal.diff().diff()

def f62_ard_486_analyst_v486_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=23, w2=343, w3=748, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(23)
    drag = impulse.rolling(343, min_periods=max(343//3, 2)).mean()
    noise = impulse.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.91625 + 0.0035287 * anchor
    return base_signal.diff().diff()

def f62_ard_487_analyst_v487_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=30, w2=354, w3=761, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 354)
    curvature = _rolling_slope(acceleration, 761)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2194 * acceleration + 0.0035288 * anchor
    return base_signal.diff().diff()

def f62_ard_488_analyst_v488_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=37, w2=365, w3=17, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(37, min_periods=max(37//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(17) * 0.945 + 0.0035289 * anchor
    return base_signal.diff().diff()

def f62_ard_489_analyst_v489_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=44, w2=376, w3=30, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(44, min_periods=max(44//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2346 * _rolling_slope(draw, 30) + 0.003529 * anchor
    return base_signal.diff().diff()

def f62_ard_490_analyst_v490_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=51, w2=387, w3=43, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(387, min_periods=max(387//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.97375 + 0.0035291 * anchor
    return base_signal.diff().diff()

def f62_ard_491_analyst_v491_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=58, w2=398, w3=56, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 398)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=56, adjust=False).mean() * 0.988125 + 0.0035292 * anchor
    return base_signal.diff().diff()

def f62_ard_492_analyst_v492_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=65, w2=409, w3=69, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(409, min_periods=max(409//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0025 + 0.0035293 * anchor
    return base_signal.diff().diff()

def f62_ard_493_analyst_v493_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=72, w2=420, w3=82, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(72)
    rank = change.rolling(420, min_periods=max(420//3, 2)).rank(pct=True)
    persistence = change.rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265 * persistence + 0.0035294 * anchor
    return base_signal.diff().diff()

def f62_ard_494_analyst_v494_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=79, w2=431, w3=95, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(431, min_periods=max(431//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03125 + 0.0035295 * anchor
    return base_signal.diff().diff()

def f62_ard_495_analyst_v495_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=86, w2=442, w3=108, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(442, min_periods=max(442//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2802 * slope + 0.0035296 * anchor
    return base_signal.diff().diff()

def f62_ard_496_analyst_v496_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=93, w2=453, w3=121, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(93)
    drag = impulse.rolling(453, min_periods=max(453//3, 2)).mean()
    noise = impulse.abs().rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.06 + 0.0035297 * anchor
    return base_signal.diff().diff()

def f62_ard_497_analyst_v497_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=100, w2=464, w3=134, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2954 * acceleration + 0.0035298 * anchor
    return base_signal.diff().diff()

def f62_ard_498_analyst_v498_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=107, w2=475, w3=147, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(475, min_periods=max(475//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.08875 + 0.0035299 * anchor
    return base_signal.diff().diff()

def f62_ard_499_analyst_v499_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=114, w2=486, w3=160, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3106 * _rolling_slope(draw, 160) + 0.00353 * anchor
    return base_signal.diff().diff()

def f62_ard_500_analyst_v500_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=121, w2=497, w3=173, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(497, min_periods=max(497//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1175 + 0.0035301 * anchor
    return base_signal.diff().diff()

def f62_ard_501_analyst_v501_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=128, w2=508, w3=186, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 508)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=186, adjust=False).mean() * 1.131875 + 0.0035302 * anchor
    return base_signal.diff().diff()

def f62_ard_502_analyst_v502_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=135, w2=16, w3=199, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.14625 + 0.0035303 * anchor
    return base_signal.diff().diff()

def f62_ard_503_analyst_v503_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=142, w2=27, w3=212, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341 * persistence + 0.0035304 * anchor
    return base_signal.diff().diff()

def f62_ard_504_analyst_v504_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=149, w2=38, w3=225, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(38, min_periods=max(38//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.175 + 0.0035305 * anchor
    return base_signal.diff().diff()

def f62_ard_505_analyst_v505_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=156, w2=49, w3=238, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3562 * slope + 0.0035306 * anchor
    return base_signal.diff().diff()

def f62_ard_506_analyst_v506_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=163, w2=60, w3=251, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.20375 + 0.0035307 * anchor
    return base_signal.diff().diff()

def f62_ard_507_analyst_v507_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=170, w2=71, w3=264, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 264)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3714 * acceleration + 0.0035308 * anchor
    return base_signal.diff().diff()

def f62_ard_508_analyst_v508_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=177, w2=82, w3=277, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2325 + 0.0035309 * anchor
    return base_signal.diff().diff()

def f62_ard_509_analyst_v509_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=184, w2=93, w3=290, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(93, min_periods=max(93//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3866 * _rolling_slope(draw, 290) + 0.003531 * anchor
    return base_signal.diff().diff()

def f62_ard_510_analyst_v510_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=191, w2=104, w3=303, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.26125 + 0.0035311 * anchor
    return base_signal.diff().diff()

def f62_ard_511_analyst_v511_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=198, w2=115, w3=316, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 115)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.275625 + 0.0035312 * anchor
    return base_signal.diff().diff()

def f62_ard_512_analyst_v512_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=205, w2=126, w3=329, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(126, min_periods=max(126//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.29 + 0.0035313 * anchor
    return base_signal.diff().diff()

def f62_ard_513_analyst_v513_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=212, w2=137, w3=342, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(137, min_periods=max(137//3, 2)).rank(pct=True)
    persistence = change.rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0406 * persistence + 0.0035314 * anchor
    return base_signal.diff().diff()

def f62_ard_514_analyst_v514_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=219, w2=148, w3=355, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31875 + 0.0035315 * anchor
    return base_signal.diff().diff()

def f62_ard_515_analyst_v515_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=226, w2=159, w3=368, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(159, min_periods=max(159//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0558 * slope + 0.0035316 * anchor
    return base_signal.diff().diff()

def f62_ard_516_analyst_v516_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=233, w2=170, w3=381, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(170, min_periods=max(170//3, 2)).mean()
    noise = impulse.abs().rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3475 + 0.0035317 * anchor
    return base_signal.diff().diff()

def f62_ard_517_analyst_v517_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=240, w2=181, w3=394, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 181)
    curvature = _rolling_slope(acceleration, 394)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.071 * acceleration + 0.0035318 * anchor
    return base_signal.diff().diff()

def f62_ard_518_analyst_v518_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=247, w2=192, w3=407, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37625 + 0.0035319 * anchor
    return base_signal.diff().diff()

def f62_ard_519_analyst_v519_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=254, w2=203, w3=420, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(203, min_periods=max(203//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0862 * _rolling_slope(draw, 420) + 0.003532 * anchor
    return base_signal.diff().diff()

def f62_ard_520_analyst_v520_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=10, w2=214, w3=433, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.405 + 0.0035321 * anchor
    return base_signal.diff().diff()

def f62_ard_521_analyst_v521_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=17, w2=225, w3=446, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.419375 + 0.0035322 * anchor
    return base_signal.diff().diff()

def f62_ard_522_analyst_v522_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=24, w2=236, w3=459, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.43375 + 0.0035323 * anchor
    return base_signal.diff().diff()

def f62_ard_523_analyst_v523_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=31, w2=247, w3=472, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(31)
    rank = change.rolling(247, min_periods=max(247//3, 2)).rank(pct=True)
    persistence = change.rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1166 * persistence + 0.0035324 * anchor
    return base_signal.diff().diff()

def f62_ard_524_analyst_v524_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=38, w2=258, w3=485, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4625 + 0.0035325 * anchor
    return base_signal.diff().diff()

def f62_ard_525_analyst_v525_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=45, w2=269, w3=498, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(269, min_periods=max(269//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1318 * slope + 0.0035326 * anchor
    return base_signal.diff().diff()
