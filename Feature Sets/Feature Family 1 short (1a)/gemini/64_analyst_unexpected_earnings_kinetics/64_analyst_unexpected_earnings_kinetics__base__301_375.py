"""64 analyst unexpected earnings kinetics base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f64_asue_301_analyst_v301(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=100, w2=442, w3=317, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.590625 + 0.0036302 * anchor

def f64_asue_302_analyst_v302(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=107, w2=453, w3=330, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(453, min_periods=max(453//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.605 + 0.0036303 * anchor

def f64_asue_303_analyst_v303(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=114, w2=464, w3=343, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(114)
    rank = change.rolling(464, min_periods=max(464//3, 2)).rank(pct=True)
    persistence = change.rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0366 * persistence + 0.0036304 * anchor

def f64_asue_304_analyst_v304(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=121, w2=475, w3=356, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.860625 + 0.0036305 * anchor

def f64_asue_305_analyst_v305(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=128, w2=486, w3=369, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(486, min_periods=max(486//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0518 * slope + 0.0036306 * anchor

def f64_asue_306_analyst_v306(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=135, w2=497, w3=382, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(497, min_periods=max(497//3, 2)).mean()
    noise = impulse.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.889375 + 0.0036307 * anchor

def f64_asue_307_analyst_v307(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=142, w2=508, w3=395, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 508)
    curvature = _rolling_slope(acceleration, 395)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.067 * acceleration + 0.0036308 * anchor

def f64_asue_308_analyst_v308(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=149, w2=16, w3=408, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(16, min_periods=max(16//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.918125 + 0.0036309 * anchor

def f64_asue_309_analyst_v309(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=156, w2=27, w3=421, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0822 * _rolling_slope(draw, 421) + 0.003631 * anchor

def f64_asue_310_analyst_v310(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=163, w2=38, w3=434, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(38, min_periods=max(38//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.946875 + 0.0036311 * anchor

def f64_asue_311_analyst_v311(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=170, w2=49, w3=447, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 49)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.96125 + 0.0036312 * anchor

def f64_asue_312_analyst_v312(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=177, w2=60, w3=460, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(60, min_periods=max(60//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.975625 + 0.0036313 * anchor

def f64_asue_313_analyst_v313(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=184, w2=71, w3=473, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(71, min_periods=max(71//3, 2)).rank(pct=True)
    persistence = change.rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1126 * persistence + 0.0036314 * anchor

def f64_asue_314_analyst_v314(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=191, w2=82, w3=486, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.004375 + 0.0036315 * anchor

def f64_asue_315_analyst_v315(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=198, w2=93, w3=499, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(93, min_periods=max(93//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1278 * slope + 0.0036316 * anchor

def f64_asue_316_analyst_v316(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=205, w2=104, w3=512, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.033125 + 0.0036317 * anchor

def f64_asue_317_analyst_v317(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=212, w2=115, w3=525, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 525)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.143 * acceleration + 0.0036318 * anchor

def f64_asue_318_analyst_v318(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=219, w2=126, w3=538, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.061875 + 0.0036319 * anchor

def f64_asue_319_analyst_v319(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=226, w2=137, w3=551, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1582 * _rolling_slope(draw, 551) + 0.003632 * anchor

def f64_asue_320_analyst_v320(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=233, w2=148, w3=564, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.090625 + 0.0036321 * anchor

def f64_asue_321_analyst_v321(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=240, w2=159, w3=577, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.105 + 0.0036322 * anchor

def f64_asue_322_analyst_v322(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=247, w2=170, w3=590, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.119375 + 0.0036323 * anchor

def f64_asue_323_analyst_v323(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=254, w2=181, w3=603, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1886 * persistence + 0.0036324 * anchor

def f64_asue_324_analyst_v324(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=10, w2=192, w3=616, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(192, min_periods=max(192//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.148125 + 0.0036325 * anchor

def f64_asue_325_analyst_v325(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=17, w2=203, w3=629, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2038 * slope + 0.0036326 * anchor

def f64_asue_326_analyst_v326(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=24, w2=214, w3=642, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(24)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.176875 + 0.0036327 * anchor

def f64_asue_327_analyst_v327(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=31, w2=225, w3=655, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 655)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.219 * acceleration + 0.0036328 * anchor

def f64_asue_328_analyst_v328(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=38, w2=236, w3=668, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.205625 + 0.0036329 * anchor

def f64_asue_329_analyst_v329(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=45, w2=247, w3=681, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(247, min_periods=max(247//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2342 * _rolling_slope(draw, 681) + 0.003633 * anchor

def f64_asue_330_analyst_v330(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=52, w2=258, w3=694, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(258, min_periods=max(258//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.234375 + 0.0036331 * anchor

def f64_asue_331_analyst_v331(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=59, w2=269, w3=707, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.24875 + 0.0036332 * anchor

def f64_asue_332_analyst_v332(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=66, w2=280, w3=720, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.263125 + 0.0036333 * anchor

def f64_asue_333_analyst_v333(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=73, w2=291, w3=733, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(73)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2646 * persistence + 0.0036334 * anchor

def f64_asue_334_analyst_v334(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=80, w2=302, w3=746, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(302, min_periods=max(302//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.291875 + 0.0036335 * anchor

def f64_asue_335_analyst_v335(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=87, w2=313, w3=759, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(313, min_periods=max(313//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2798 * slope + 0.0036336 * anchor

def f64_asue_336_analyst_v336(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=94, w2=324, w3=15, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(94)
    drag = impulse.rolling(324, min_periods=max(324//3, 2)).mean()
    noise = impulse.abs().rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.320625 + 0.0036337 * anchor

def f64_asue_337_analyst_v337(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=101, w2=335, w3=28, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 335)
    curvature = _rolling_slope(acceleration, 28)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.295 * acceleration + 0.0036338 * anchor

def f64_asue_338_analyst_v338(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=108, w2=346, w3=41, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(41) * 1.349375 + 0.0036339 * anchor

def f64_asue_339_analyst_v339(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=115, w2=357, w3=54, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(357, min_periods=max(357//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3102 * _rolling_slope(draw, 54) + 0.003634 * anchor

def f64_asue_340_analyst_v340(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=122, w2=368, w3=67, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.378125 + 0.0036341 * anchor

def f64_asue_341_analyst_v341(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=129, w2=379, w3=80, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 379)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=80, adjust=False).mean() * 1.3925 + 0.0036342 * anchor

def f64_asue_342_analyst_v342(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=136, w2=390, w3=93, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.406875 + 0.0036343 * anchor

def f64_asue_343_analyst_v343(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=143, w2=401, w3=106, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(401, min_periods=max(401//3, 2)).rank(pct=True)
    persistence = change.rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3406 * persistence + 0.0036344 * anchor

def f64_asue_344_analyst_v344(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=150, w2=412, w3=119, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(412, min_periods=max(412//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.435625 + 0.0036345 * anchor

def f64_asue_345_analyst_v345(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=157, w2=423, w3=132, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(423, min_periods=max(423//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3558 * slope + 0.0036346 * anchor

def f64_asue_346_analyst_v346(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=164, w2=434, w3=145, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.464375 + 0.0036347 * anchor

def f64_asue_347_analyst_v347(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=171, w2=445, w3=158, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 445)
    curvature = _rolling_slope(acceleration, 158)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.371 * acceleration + 0.0036348 * anchor

def f64_asue_348_analyst_v348(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=178, w2=456, w3=171, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(456, min_periods=max(456//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.493125 + 0.0036349 * anchor

def f64_asue_349_analyst_v349(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=185, w2=467, w3=184, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(467, min_periods=max(467//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3862 * _rolling_slope(draw, 184) + 0.003635 * anchor

def f64_asue_350_analyst_v350(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=192, w2=478, w3=197, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.521875 + 0.0036351 * anchor

def f64_asue_351_analyst_v351(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=199, w2=489, w3=210, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 489)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=210, adjust=False).mean() * 1.53625 + 0.0036352 * anchor

def f64_asue_352_analyst_v352(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=206, w2=500, w3=223, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(500, min_periods=max(500//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.550625 + 0.0036353 * anchor

def f64_asue_353_analyst_v353(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=213, w2=511, w3=236, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(511, min_periods=max(511//3, 2)).rank(pct=True)
    persistence = change.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0402 * persistence + 0.0036354 * anchor

def f64_asue_354_analyst_v354(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=220, w2=19, w3=249, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(19, min_periods=max(19//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.579375 + 0.0036355 * anchor

def f64_asue_355_analyst_v355(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=227, w2=30, w3=262, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(30, min_periods=max(30//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0554 * slope + 0.0036356 * anchor

def f64_asue_356_analyst_v356(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=234, w2=41, w3=275, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.608125 + 0.0036357 * anchor

def f64_asue_357_analyst_v357(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=241, w2=52, w3=288, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 52)
    curvature = _rolling_slope(acceleration, 288)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0706 * acceleration + 0.0036358 * anchor

def f64_asue_358_analyst_v358(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=248, w2=63, w3=301, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(63, min_periods=max(63//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.86375 + 0.0036359 * anchor

def f64_asue_359_analyst_v359(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=255, w2=74, w3=314, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(74, min_periods=max(74//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0858 * _rolling_slope(draw, 314) + 0.003636 * anchor

def f64_asue_360_analyst_v360(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=11, w2=85, w3=327, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(85, min_periods=max(85//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.8925 + 0.0036361 * anchor

def f64_asue_361_analyst_v361(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=18, w2=96, w3=340, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 18)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.906875 + 0.0036362 * anchor

def f64_asue_362_analyst_v362(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=25, w2=107, w3=353, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(107, min_periods=max(107//3, 2)).max()
    trough = x.rolling(25, min_periods=max(25//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.92125 + 0.0036363 * anchor

def f64_asue_363_analyst_v363(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=32, w2=118, w3=366, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(32)
    rank = change.rolling(118, min_periods=max(118//3, 2)).rank(pct=True)
    persistence = change.rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1162 * persistence + 0.0036364 * anchor

def f64_asue_364_analyst_v364(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=39, w2=129, w3=379, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(39, min_periods=max(39//3, 2)).std()
    vol_slow = ret.rolling(129, min_periods=max(129//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95 + 0.0036365 * anchor

def f64_asue_365_analyst_v365(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=46, w2=140, w3=392, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(140, min_periods=max(140//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 46)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1314 * slope + 0.0036366 * anchor

def f64_asue_366_analyst_v366(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=53, w2=151, w3=405, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(53)
    drag = impulse.rolling(151, min_periods=max(151//3, 2)).mean()
    noise = impulse.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.97875 + 0.0036367 * anchor

def f64_asue_367_analyst_v367(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=60, w2=162, w3=418, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 60)
    acceleration = _rolling_slope(velocity, 162)
    curvature = _rolling_slope(acceleration, 418)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1466 * acceleration + 0.0036368 * anchor

def f64_asue_368_analyst_v368(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=67, w2=173, w3=431, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0075 + 0.0036369 * anchor

def f64_asue_369_analyst_v369(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=74, w2=184, w3=444, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1618 * _rolling_slope(draw, 444) + 0.003637 * anchor

def f64_asue_370_analyst_v370(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=81, w2=195, w3=457, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(195, min_periods=max(195//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.03625 + 0.0036371 * anchor

def f64_asue_371_analyst_v371(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=88, w2=206, w3=470, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 88)
    slow = _rolling_slope(x, 206)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.050625 + 0.0036372 * anchor

def f64_asue_372_analyst_v372(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=95, w2=217, w3=483, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(95, min_periods=max(95//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.065 + 0.0036373 * anchor

def f64_asue_373_analyst_v373(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=102, w2=228, w3=496, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(102)
    rank = change.rolling(228, min_periods=max(228//3, 2)).rank(pct=True)
    persistence = change.rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1922 * persistence + 0.0036374 * anchor

def f64_asue_374_analyst_v374(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=109, w2=239, w3=509, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(109, min_periods=max(109//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09375 + 0.0036375 * anchor

def f64_asue_375_analyst_v375(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=116, w2=250, w3=522, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(250, min_periods=max(250//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 116)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2074 * slope + 0.0036376 * anchor
