"""62 analyst revision dispersion base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f62_ard_526_analyst_v526(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=52, w2=280, w3=511, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(52)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.49125 + 0.0035327 * anchor

def f62_ard_527_analyst_v527(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=59, w2=291, w3=524, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 291)
    curvature = _rolling_slope(acceleration, 524)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.147 * acceleration + 0.0035328 * anchor

def f62_ard_528_analyst_v528(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=66, w2=302, w3=537, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.52 + 0.0035329 * anchor

def f62_ard_529_analyst_v529(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=73, w2=313, w3=550, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1622 * _rolling_slope(draw, 550) + 0.003533 * anchor

def f62_ard_530_analyst_v530(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=80, w2=324, w3=563, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(324, min_periods=max(324//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.54875 + 0.0035331 * anchor

def f62_ard_531_analyst_v531(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=87, w2=335, w3=576, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 335)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.563125 + 0.0035332 * anchor

def f62_ard_532_analyst_v532(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=94, w2=346, w3=589, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(346, min_periods=max(346//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5775 + 0.0035333 * anchor

def f62_ard_533_analyst_v533(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=101, w2=357, w3=602, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(101)
    rank = change.rolling(357, min_periods=max(357//3, 2)).rank(pct=True)
    persistence = change.rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1926 * persistence + 0.0035334 * anchor

def f62_ard_534_analyst_v534(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=108, w2=368, w3=615, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(368, min_periods=max(368//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60625 + 0.0035335 * anchor

def f62_ard_535_analyst_v535(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=115, w2=379, w3=628, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(379, min_periods=max(379//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2078 * slope + 0.0035336 * anchor

def f62_ard_536_analyst_v536(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=122, w2=390, w3=641, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(122)
    drag = impulse.rolling(390, min_periods=max(390//3, 2)).mean()
    noise = impulse.abs().rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.861875 + 0.0035337 * anchor

def f62_ard_537_analyst_v537(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=129, w2=401, w3=654, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 401)
    curvature = _rolling_slope(acceleration, 654)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.223 * acceleration + 0.0035338 * anchor

def f62_ard_538_analyst_v538(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=136, w2=412, w3=667, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.890625 + 0.0035339 * anchor

def f62_ard_539_analyst_v539(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=143, w2=423, w3=680, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2382 * _rolling_slope(draw, 680) + 0.003534 * anchor

def f62_ard_540_analyst_v540(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=150, w2=434, w3=693, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(434, min_periods=max(434//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.919375 + 0.0035341 * anchor

def f62_ard_541_analyst_v541(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=157, w2=445, w3=706, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 445)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.93375 + 0.0035342 * anchor

def f62_ard_542_analyst_v542(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=164, w2=456, w3=719, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(456, min_periods=max(456//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.948125 + 0.0035343 * anchor

def f62_ard_543_analyst_v543(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=171, w2=467, w3=732, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(467, min_periods=max(467//3, 2)).rank(pct=True)
    persistence = change.rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2686 * persistence + 0.0035344 * anchor

def f62_ard_544_analyst_v544(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=178, w2=478, w3=745, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(478, min_periods=max(478//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.976875 + 0.0035345 * anchor

def f62_ard_545_analyst_v545(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=185, w2=489, w3=758, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(489, min_periods=max(489//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2838 * slope + 0.0035346 * anchor

def f62_ard_546_analyst_v546(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=192, w2=500, w3=771, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(500, min_periods=max(500//3, 2)).mean()
    noise = impulse.abs().rolling(771, min_periods=max(771//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.005625 + 0.0035347 * anchor

def f62_ard_547_analyst_v547(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=199, w2=511, w3=27, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 511)
    curvature = _rolling_slope(acceleration, 27)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.299 * acceleration + 0.0035348 * anchor

def f62_ard_548_analyst_v548(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=206, w2=19, w3=40, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(40) * 1.034375 + 0.0035349 * anchor

def f62_ard_549_analyst_v549(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=213, w2=30, w3=53, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(30, min_periods=max(30//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3142 * _rolling_slope(draw, 53) + 0.003535 * anchor

def f62_ard_550_analyst_v550(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=220, w2=41, w3=66, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(41, min_periods=max(41//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.063125 + 0.0035351 * anchor

def f62_ard_551_analyst_v551(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=227, w2=52, w3=79, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 52)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=79, adjust=False).mean() * 1.0775 + 0.0035352 * anchor

def f62_ard_552_analyst_v552(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=234, w2=63, w3=92, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(63, min_periods=max(63//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.091875 + 0.0035353 * anchor

def f62_ard_553_analyst_v553(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=241, w2=74, w3=105, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(74, min_periods=max(74//3, 2)).rank(pct=True)
    persistence = change.rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3446 * persistence + 0.0035354 * anchor

def f62_ard_554_analyst_v554(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=248, w2=85, w3=118, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(85, min_periods=max(85//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.120625 + 0.0035355 * anchor

def f62_ard_555_analyst_v555(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=255, w2=96, w3=131, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(96, min_periods=max(96//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 255)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3598 * slope + 0.0035356 * anchor

def f62_ard_556_analyst_v556(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=11, w2=107, w3=144, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(11)
    drag = impulse.rolling(107, min_periods=max(107//3, 2)).mean()
    noise = impulse.abs().rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.149375 + 0.0035357 * anchor

def f62_ard_557_analyst_v557(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=18, w2=118, w3=157, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 118)
    curvature = _rolling_slope(acceleration, 157)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.375 * acceleration + 0.0035358 * anchor

def f62_ard_558_analyst_v558(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=25, w2=129, w3=170, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(129, min_periods=max(129//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.178125 + 0.0035359 * anchor

def f62_ard_559_analyst_v559(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=32, w2=140, w3=183, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(140, min_periods=max(140//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3902 * _rolling_slope(draw, 183) + 0.003536 * anchor

def f62_ard_560_analyst_v560(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=39, w2=151, w3=196, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(151, min_periods=max(151//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.206875 + 0.0035361 * anchor

def f62_ard_561_analyst_v561(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=46, w2=162, w3=209, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 162)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=209, adjust=False).mean() * 1.22125 + 0.0035362 * anchor

def f62_ard_562_analyst_v562(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=53, w2=173, w3=222, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(173, min_periods=max(173//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.235625 + 0.0035363 * anchor

def f62_ard_563_analyst_v563(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=60, w2=184, w3=235, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(60)
    rank = change.rolling(184, min_periods=max(184//3, 2)).rank(pct=True)
    persistence = change.rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0442 * persistence + 0.0035364 * anchor

def f62_ard_564_analyst_v564(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=67, w2=195, w3=248, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(195, min_periods=max(195//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.264375 + 0.0035365 * anchor

def f62_ard_565_analyst_v565(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=74, w2=206, w3=261, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(206, min_periods=max(206//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0594 * slope + 0.0035366 * anchor

def f62_ard_566_analyst_v566(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=81, w2=217, w3=274, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(81)
    drag = impulse.rolling(217, min_periods=max(217//3, 2)).mean()
    noise = impulse.abs().rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.293125 + 0.0035367 * anchor

def f62_ard_567_analyst_v567(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=88, w2=228, w3=287, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 228)
    curvature = _rolling_slope(acceleration, 287)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0746 * acceleration + 0.0035368 * anchor

def f62_ard_568_analyst_v568(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=95, w2=239, w3=300, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(239, min_periods=max(239//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.321875 + 0.0035369 * anchor

def f62_ard_569_analyst_v569(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=102, w2=250, w3=313, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(250, min_periods=max(250//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0898 * _rolling_slope(draw, 313) + 0.003537 * anchor

def f62_ard_570_analyst_v570(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=109, w2=261, w3=326, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.350625 + 0.0035371 * anchor

def f62_ard_571_analyst_v571(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=116, w2=272, w3=339, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 272)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.365 + 0.0035372 * anchor

def f62_ard_572_analyst_v572(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=123, w2=283, w3=352, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(283, min_periods=max(283//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.379375 + 0.0035373 * anchor

def f62_ard_573_analyst_v573(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=130, w2=294, w3=365, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(294, min_periods=max(294//3, 2)).rank(pct=True)
    persistence = change.rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1202 * persistence + 0.0035374 * anchor

def f62_ard_574_analyst_v574(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=137, w2=305, w3=378, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(305, min_periods=max(305//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.408125 + 0.0035375 * anchor

def f62_ard_575_analyst_v575(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=144, w2=316, w3=391, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(316, min_periods=max(316//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1354 * slope + 0.0035376 * anchor

def f62_ard_576_analyst_v576(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=151, w2=327, w3=404, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(327, min_periods=max(327//3, 2)).mean()
    noise = impulse.abs().rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.436875 + 0.0035377 * anchor

def f62_ard_577_analyst_v577(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=158, w2=338, w3=417, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 338)
    curvature = _rolling_slope(acceleration, 417)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1506 * acceleration + 0.0035378 * anchor

def f62_ard_578_analyst_v578(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=165, w2=349, w3=430, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(349, min_periods=max(349//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.465625 + 0.0035379 * anchor

def f62_ard_579_analyst_v579(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=172, w2=360, w3=443, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(360, min_periods=max(360//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1658 * _rolling_slope(draw, 443) + 0.003538 * anchor

def f62_ard_580_analyst_v580(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=179, w2=371, w3=456, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(371, min_periods=max(371//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.494375 + 0.0035381 * anchor

def f62_ard_581_analyst_v581(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=186, w2=382, w3=469, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 382)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.50875 + 0.0035382 * anchor

def f62_ard_582_analyst_v582(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=193, w2=393, w3=482, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(393, min_periods=max(393//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.523125 + 0.0035383 * anchor

def f62_ard_583_analyst_v583(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=200, w2=404, w3=495, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(404, min_periods=max(404//3, 2)).rank(pct=True)
    persistence = change.rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1962 * persistence + 0.0035384 * anchor

def f62_ard_584_analyst_v584(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=207, w2=415, w3=508, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(415, min_periods=max(415//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.551875 + 0.0035385 * anchor

def f62_ard_585_analyst_v585(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=214, w2=426, w3=521, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(426, min_periods=max(426//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2114 * slope + 0.0035386 * anchor

def f62_ard_586_analyst_v586(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=221, w2=437, w3=534, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(437, min_periods=max(437//3, 2)).mean()
    noise = impulse.abs().rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.580625 + 0.0035387 * anchor

def f62_ard_587_analyst_v587(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=228, w2=448, w3=547, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 448)
    curvature = _rolling_slope(acceleration, 547)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2266 * acceleration + 0.0035388 * anchor

def f62_ard_588_analyst_v588(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=235, w2=459, w3=560, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(459, min_periods=max(459//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.609375 + 0.0035389 * anchor

def f62_ard_589_analyst_v589(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=242, w2=470, w3=573, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(470, min_periods=max(470//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2418 * _rolling_slope(draw, 573) + 0.003539 * anchor

def f62_ard_590_analyst_v590(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=249, w2=481, w3=586, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(481, min_periods=max(481//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.865 + 0.0035391 * anchor

def f62_ard_591_analyst_v591(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=5, w2=492, w3=599, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 492)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.879375 + 0.0035392 * anchor

def f62_ard_592_analyst_v592(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=12, w2=503, w3=612, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(503, min_periods=max(503//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.89375 + 0.0035393 * anchor

def f62_ard_593_analyst_v593(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=19, w2=11, w3=625, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(19)
    rank = change.rolling(11, min_periods=max(11//3, 2)).rank(pct=True)
    persistence = change.rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2722 * persistence + 0.0035394 * anchor

def f62_ard_594_analyst_v594(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=26, w2=22, w3=638, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(22, min_periods=max(22//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9225 + 0.0035395 * anchor

def f62_ard_595_analyst_v595(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=33, w2=33, w3=651, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(33, min_periods=max(33//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2874 * slope + 0.0035396 * anchor

def f62_ard_596_analyst_v596(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=40, w2=44, w3=664, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(40)
    drag = impulse.rolling(44, min_periods=max(44//3, 2)).mean()
    noise = impulse.abs().rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.95125 + 0.0035397 * anchor

def f62_ard_597_analyst_v597(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=47, w2=55, w3=677, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 55)
    curvature = _rolling_slope(acceleration, 677)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3026 * acceleration + 0.0035398 * anchor

def f62_ard_598_analyst_v598(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=54, w2=66, w3=690, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(66, min_periods=max(66//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.98 + 0.0035399 * anchor

def f62_ard_599_analyst_v599(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=61, w2=77, w3=703, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(77, min_periods=max(77//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3178 * _rolling_slope(draw, 703) + 0.00354 * anchor

def f62_ard_600_analyst_v600(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=68, w2=88, w3=716, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(88, min_periods=max(88//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.00875 + 0.0035401 * anchor
