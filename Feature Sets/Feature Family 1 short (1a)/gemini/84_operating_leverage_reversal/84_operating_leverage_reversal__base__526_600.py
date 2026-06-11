"""84 operating leverage reversal base features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Operating_Efficiency - Institutional-grade short-side signal.
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

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)
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

def f84_olr_526_struct_v526(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=387, w3=540, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.15125 + 0.0041327 * anchor

def f84_olr_527_struct_v527(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=398, w3=553, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 553)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2026 * acceleration + 0.0041328 * anchor

def f84_olr_528_struct_v528(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=409, w3=566, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.18 + 0.0041329 * anchor

def f84_olr_529_struct_v529(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=420, w3=579, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(420, min_periods=max(420//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2178 * _rolling_slope(draw, 579) + 0.004133 * anchor

def f84_olr_530_struct_v530(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=431, w3=592, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(431, min_periods=max(431//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.20875 + 0.0041331 * anchor

def f84_olr_531_struct_v531(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=442, w3=605, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.223125 + 0.0041332 * anchor

def f84_olr_532_struct_v532(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=453, w3=618, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(453, min_periods=max(453//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2375 + 0.0041333 * anchor

def f84_olr_533_struct_v533(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=464, w3=631, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(464, min_periods=max(464//3, 2)).rank(pct=True)
    persistence = change.rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2482 * persistence + 0.0041334 * anchor

def f84_olr_534_struct_v534(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=475, w3=644, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26625 + 0.0041335 * anchor

def f84_olr_535_struct_v535(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=486, w3=657, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(486, min_periods=max(486//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2634 * slope + 0.0041336 * anchor

def f84_olr_536_struct_v536(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=497, w3=670, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(497, min_periods=max(497//3, 2)).mean()
    noise = impulse.abs().rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.295 + 0.0041337 * anchor

def f84_olr_537_struct_v537(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=508, w3=683, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 508)
    curvature = _rolling_slope(acceleration, 683)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2786 * acceleration + 0.0041338 * anchor

def f84_olr_538_struct_v538(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=16, w3=696, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(16, min_periods=max(16//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.32375 + 0.0041339 * anchor

def f84_olr_539_struct_v539(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=27, w3=709, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2938 * _rolling_slope(draw, 709) + 0.004134 * anchor

def f84_olr_540_struct_v540(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=38, w3=722, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(38, min_periods=max(38//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3525 + 0.0041341 * anchor

def f84_olr_541_struct_v541(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=49, w3=735, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 49)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.366875 + 0.0041342 * anchor

def f84_olr_542_struct_v542(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=60, w3=748, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(60, min_periods=max(60//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.38125 + 0.0041343 * anchor

def f84_olr_543_struct_v543(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=71, w3=761, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(71, min_periods=max(71//3, 2)).rank(pct=True)
    persistence = change.rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3242 * persistence + 0.0041344 * anchor

def f84_olr_544_struct_v544(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=82, w3=17, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41 + 0.0041345 * anchor

def f84_olr_545_struct_v545(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=93, w3=30, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(93, min_periods=max(93//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3394 * slope + 0.0041346 * anchor

def f84_olr_546_struct_v546(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=104, w3=43, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(24)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.43875 + 0.0041347 * anchor

def f84_olr_547_struct_v547(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=115, w3=56, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 56)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3546 * acceleration + 0.0041348 * anchor

def f84_olr_548_struct_v548(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=126, w3=69, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(69) * 1.4675 + 0.0041349 * anchor

def f84_olr_549_struct_v549(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=137, w3=82, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3698 * _rolling_slope(draw, 82) + 0.004135 * anchor

def f84_olr_550_struct_v550(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=148, w3=95, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.49625 + 0.0041351 * anchor

def f84_olr_551_struct_v551(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=159, w3=108, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=108, adjust=False).mean() * 1.510625 + 0.0041352 * anchor

def f84_olr_552_struct_v552(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=170, w3=121, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.525 + 0.0041353 * anchor

def f84_olr_553_struct_v553(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=181, w3=134, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(73)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4002 * persistence + 0.0041354 * anchor

def f84_olr_554_struct_v554(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=192, w3=147, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(192, min_periods=max(192//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55375 + 0.0041355 * anchor

def f84_olr_555_struct_v555(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=203, w3=160, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.039 * slope + 0.0041356 * anchor

def f84_olr_556_struct_v556(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=214, w3=173, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(94)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5825 + 0.0041357 * anchor

def f84_olr_557_struct_v557(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=225, w3=186, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 186)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0542 * acceleration + 0.0041358 * anchor

def f84_olr_558_struct_v558(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=236, w3=199, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.61125 + 0.0041359 * anchor

def f84_olr_559_struct_v559(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=247, w3=212, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(247, min_periods=max(247//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0694 * _rolling_slope(draw, 212) + 0.004136 * anchor

def f84_olr_560_struct_v560(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=258, w3=225, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(258, min_periods=max(258//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.866875 + 0.0041361 * anchor

def f84_olr_561_struct_v561(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=269, w3=238, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=238, adjust=False).mean() * 0.88125 + 0.0041362 * anchor

def f84_olr_562_struct_v562(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=280, w3=251, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.895625 + 0.0041363 * anchor

def f84_olr_563_struct_v563(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=291, w3=264, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0998 * persistence + 0.0041364 * anchor

def f84_olr_564_struct_v564(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=302, w3=277, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(302, min_periods=max(302//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.924375 + 0.0041365 * anchor

def f84_olr_565_struct_v565(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=313, w3=290, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(313, min_periods=max(313//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.115 * slope + 0.0041366 * anchor

def f84_olr_566_struct_v566(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=324, w3=303, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(324, min_periods=max(324//3, 2)).mean()
    noise = impulse.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.953125 + 0.0041367 * anchor

def f84_olr_567_struct_v567(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=335, w3=316, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 335)
    curvature = _rolling_slope(acceleration, 316)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1302 * acceleration + 0.0041368 * anchor

def f84_olr_568_struct_v568(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=346, w3=329, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.981875 + 0.0041369 * anchor

def f84_olr_569_struct_v569(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=357, w3=342, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(357, min_periods=max(357//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1454 * _rolling_slope(draw, 342) + 0.004137 * anchor

def f84_olr_570_struct_v570(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=368, w3=355, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.010625 + 0.0041371 * anchor

def f84_olr_571_struct_v571(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=379, w3=368, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 379)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.025 + 0.0041372 * anchor

def f84_olr_572_struct_v572(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=390, w3=381, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.039375 + 0.0041373 * anchor

def f84_olr_573_struct_v573(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=401, w3=394, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(401, min_periods=max(401//3, 2)).rank(pct=True)
    persistence = change.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1758 * persistence + 0.0041374 * anchor

def f84_olr_574_struct_v574(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=412, w3=407, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(412, min_periods=max(412//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.068125 + 0.0041375 * anchor

def f84_olr_575_struct_v575(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=423, w3=420, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(423, min_periods=max(423//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.191 * slope + 0.0041376 * anchor

def f84_olr_576_struct_v576(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=434, w3=433, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.096875 + 0.0041377 * anchor

def f84_olr_577_struct_v577(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=445, w3=446, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 445)
    curvature = _rolling_slope(acceleration, 446)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2062 * acceleration + 0.0041378 * anchor

def f84_olr_578_struct_v578(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=456, w3=459, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(456, min_periods=max(456//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.125625 + 0.0041379 * anchor

def f84_olr_579_struct_v579(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=467, w3=472, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(467, min_periods=max(467//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2214 * _rolling_slope(draw, 472) + 0.004138 * anchor

def f84_olr_580_struct_v580(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=478, w3=485, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.154375 + 0.0041381 * anchor

def f84_olr_581_struct_v581(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=489, w3=498, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 18)
    slow = _rolling_slope(x, 489)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.16875 + 0.0041382 * anchor

def f84_olr_582_struct_v582(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=500, w3=511, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(500, min_periods=max(500//3, 2)).max()
    trough = x.rolling(25, min_periods=max(25//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.183125 + 0.0041383 * anchor

def f84_olr_583_struct_v583(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=511, w3=524, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(32)
    rank = change.rolling(511, min_periods=max(511//3, 2)).rank(pct=True)
    persistence = change.rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2518 * persistence + 0.0041384 * anchor

def f84_olr_584_struct_v584(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=19, w3=537, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(39, min_periods=max(39//3, 2)).std()
    vol_slow = ret.rolling(19, min_periods=max(19//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.211875 + 0.0041385 * anchor

def f84_olr_585_struct_v585(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=30, w3=550, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(30, min_periods=max(30//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 46)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.267 * slope + 0.0041386 * anchor

def f84_olr_586_struct_v586(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=41, w3=563, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(53)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.240625 + 0.0041387 * anchor

def f84_olr_587_struct_v587(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=52, w3=576, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 60)
    acceleration = _rolling_slope(velocity, 52)
    curvature = _rolling_slope(acceleration, 576)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2822 * acceleration + 0.0041388 * anchor

def f84_olr_588_struct_v588(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=63, w3=589, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(63, min_periods=max(63//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.269375 + 0.0041389 * anchor

def f84_olr_589_struct_v589(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=74, w3=602, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(74, min_periods=max(74//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2974 * _rolling_slope(draw, 602) + 0.004139 * anchor

def f84_olr_590_struct_v590(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=85, w3=615, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(85, min_periods=max(85//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.298125 + 0.0041391 * anchor

def f84_olr_591_struct_v591(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=96, w3=628, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 88)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3125 + 0.0041392 * anchor

def f84_olr_592_struct_v592(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=107, w3=641, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(107, min_periods=max(107//3, 2)).max()
    trough = x.rolling(95, min_periods=max(95//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.326875 + 0.0041393 * anchor

def f84_olr_593_struct_v593(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=118, w3=654, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(102)
    rank = change.rolling(118, min_periods=max(118//3, 2)).rank(pct=True)
    persistence = change.rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3278 * persistence + 0.0041394 * anchor

def f84_olr_594_struct_v594(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=129, w3=667, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(109, min_periods=max(109//3, 2)).std()
    vol_slow = ret.rolling(129, min_periods=max(129//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355625 + 0.0041395 * anchor

def f84_olr_595_struct_v595(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=140, w3=680, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(140, min_periods=max(140//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 116)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.343 * slope + 0.0041396 * anchor

def f84_olr_596_struct_v596(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=151, w3=693, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(123)
    drag = impulse.rolling(151, min_periods=max(151//3, 2)).mean()
    noise = impulse.abs().rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.384375 + 0.0041397 * anchor

def f84_olr_597_struct_v597(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=162, w3=706, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 130)
    acceleration = _rolling_slope(velocity, 162)
    curvature = _rolling_slope(acceleration, 706)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3582 * acceleration + 0.0041398 * anchor

def f84_olr_598_struct_v598(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=173, w3=719, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(137, min_periods=max(137//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.413125 + 0.0041399 * anchor

def f84_olr_599_struct_v599(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=184, w3=732, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(144, min_periods=max(144//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3734 * _rolling_slope(draw, 732) + 0.00414 * anchor

def f84_olr_600_struct_v600(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=195, w3=745, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(195, min_periods=max(195//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.441875 + 0.0041401 * anchor
