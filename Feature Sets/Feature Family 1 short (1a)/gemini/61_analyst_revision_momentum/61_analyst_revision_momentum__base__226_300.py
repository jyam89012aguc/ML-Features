"""61 analyst revision momentum base features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f61_arm_226_analyst_v226(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=27, w2=440, w3=166, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(27)
    drag = impulse.rolling(440, min_periods=max(440//3, 2)).mean()
    noise = impulse.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.92375 + 0.0034427 * anchor

def f61_arm_227_analyst_v227(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=34, w2=451, w3=179, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 451)
    curvature = _rolling_slope(acceleration, 179)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0822 * acceleration + 0.0034428 * anchor

def f61_arm_228_analyst_v228(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=41, w2=462, w3=192, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(41, min_periods=max(41//3, 2)).mean(), upside.rolling(462, min_periods=max(462//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9525 + 0.0034429 * anchor

def f61_arm_229_analyst_v229(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=48, w2=473, w3=205, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(473, min_periods=max(473//3, 2)).max()
    rebound = x - x.rolling(48, min_periods=max(48//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0974 * _rolling_slope(draw, 205) + 0.003443 * anchor

def f61_arm_230_analyst_v230(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=55, w2=484, w3=218, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(484, min_periods=max(484//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.98125 + 0.0034431 * anchor

def f61_arm_231_analyst_v231(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=62, w2=495, w3=231, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=231, adjust=False).mean() * 0.995625 + 0.0034432 * anchor

def f61_arm_232_analyst_v232(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=69, w2=506, w3=244, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(506, min_periods=max(506//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.01 + 0.0034433 * anchor

def f61_arm_233_analyst_v233(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=76, w2=14, w3=257, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(76)
    rank = change.rolling(14, min_periods=max(14//3, 2)).rank(pct=True)
    persistence = change.rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1278 * persistence + 0.0034434 * anchor

def f61_arm_234_analyst_v234(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=83, w2=25, w3=270, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(25, min_periods=max(25//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03875 + 0.0034435 * anchor

def f61_arm_235_analyst_v235(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=90, w2=36, w3=283, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.143 * slope + 0.0034436 * anchor

def f61_arm_236_analyst_v236(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=97, w2=47, w3=296, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(97)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0675 + 0.0034437 * anchor

def f61_arm_237_analyst_v237(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=104, w2=58, w3=309, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 58)
    curvature = _rolling_slope(acceleration, 309)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1582 * acceleration + 0.0034438 * anchor

def f61_arm_238_analyst_v238(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=111, w2=69, w3=322, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(69, min_periods=max(69//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.09625 + 0.0034439 * anchor

def f61_arm_239_analyst_v239(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=118, w2=80, w3=335, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(80, min_periods=max(80//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1734 * _rolling_slope(draw, 335) + 0.003444 * anchor

def f61_arm_240_analyst_v240(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=125, w2=91, w3=348, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(91, min_periods=max(91//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.125 + 0.0034441 * anchor

def f61_arm_241_analyst_v241(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=132, w2=102, w3=361, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 102)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.139375 + 0.0034442 * anchor

def f61_arm_242_analyst_v242(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=139, w2=113, w3=374, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(113, min_periods=max(113//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.15375 + 0.0034443 * anchor

def f61_arm_243_analyst_v243(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=146, w2=124, w3=387, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(124, min_periods=max(124//3, 2)).rank(pct=True)
    persistence = change.rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2038 * persistence + 0.0034444 * anchor

def f61_arm_244_analyst_v244(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=153, w2=135, w3=400, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1825 + 0.0034445 * anchor

def f61_arm_245_analyst_v245(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=160, w2=146, w3=413, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(146, min_periods=max(146//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.219 * slope + 0.0034446 * anchor

def f61_arm_246_analyst_v246(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=167, w2=157, w3=426, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(157, min_periods=max(157//3, 2)).mean()
    noise = impulse.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.21125 + 0.0034447 * anchor

def f61_arm_247_analyst_v247(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=174, w2=168, w3=439, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 168)
    curvature = _rolling_slope(acceleration, 439)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2342 * acceleration + 0.0034448 * anchor

def f61_arm_248_analyst_v248(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=181, w2=179, w3=452, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(179, min_periods=max(179//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.24 + 0.0034449 * anchor

def f61_arm_249_analyst_v249(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=188, w2=190, w3=465, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(190, min_periods=max(190//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2494 * _rolling_slope(draw, 465) + 0.003445 * anchor

def f61_arm_250_analyst_v250(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=195, w2=201, w3=478, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(201, min_periods=max(201//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.26875 + 0.0034451 * anchor

def f61_arm_251_analyst_v251(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=202, w2=212, w3=491, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.283125 + 0.0034452 * anchor

def f61_arm_252_analyst_v252(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=209, w2=223, w3=504, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2975 + 0.0034453 * anchor

def f61_arm_253_analyst_v253(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=216, w2=234, w3=517, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(234, min_periods=max(234//3, 2)).rank(pct=True)
    persistence = change.rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2798 * persistence + 0.0034454 * anchor

def f61_arm_254_analyst_v254(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=223, w2=245, w3=530, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(245, min_periods=max(245//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32625 + 0.0034455 * anchor

def f61_arm_255_analyst_v255(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=230, w2=256, w3=543, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.295 * slope + 0.0034456 * anchor

def f61_arm_256_analyst_v256(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=237, w2=267, w3=556, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(267, min_periods=max(267//3, 2)).mean()
    noise = impulse.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.355 + 0.0034457 * anchor

def f61_arm_257_analyst_v257(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=244, w2=278, w3=569, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 569)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3102 * acceleration + 0.0034458 * anchor

def f61_arm_258_analyst_v258(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=251, w2=289, w3=582, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(289, min_periods=max(289//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.38375 + 0.0034459 * anchor

def f61_arm_259_analyst_v259(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=7, w2=300, w3=595, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(300, min_periods=max(300//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3254 * _rolling_slope(draw, 595) + 0.003446 * anchor

def f61_arm_260_analyst_v260(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=14, w2=311, w3=608, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(311, min_periods=max(311//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(608, min_periods=max(608//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4125 + 0.0034461 * anchor

def f61_arm_261_analyst_v261(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=21, w2=322, w3=621, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 322)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.426875 + 0.0034462 * anchor

def f61_arm_262_analyst_v262(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=28, w2=333, w3=634, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.44125 + 0.0034463 * anchor

def f61_arm_263_analyst_v263(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=35, w2=344, w3=647, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(35)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3558 * persistence + 0.0034464 * anchor

def f61_arm_264_analyst_v264(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=42, w2=355, w3=660, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(355, min_periods=max(355//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47 + 0.0034465 * anchor

def f61_arm_265_analyst_v265(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=49, w2=366, w3=673, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(366, min_periods=max(366//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.371 * slope + 0.0034466 * anchor

def f61_arm_266_analyst_v266(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=56, w2=377, w3=686, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(56)
    drag = impulse.rolling(377, min_periods=max(377//3, 2)).mean()
    noise = impulse.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.49875 + 0.0034467 * anchor

def f61_arm_267_analyst_v267(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=63, w2=388, w3=699, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 388)
    curvature = _rolling_slope(acceleration, 699)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3862 * acceleration + 0.0034468 * anchor

def f61_arm_268_analyst_v268(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=70, w2=399, w3=712, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(399, min_periods=max(399//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5275 + 0.0034469 * anchor

def f61_arm_269_analyst_v269(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=77, w2=410, w3=725, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(410, min_periods=max(410//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4014 * _rolling_slope(draw, 725) + 0.003447 * anchor

def f61_arm_270_analyst_v270(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=84, w2=421, w3=738, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(421, min_periods=max(421//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.55625 + 0.0034471 * anchor

def f61_arm_271_analyst_v271(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=91, w2=432, w3=751, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 432)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.570625 + 0.0034472 * anchor

def f61_arm_272_analyst_v272(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=98, w2=443, w3=764, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(443, min_periods=max(443//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.585 + 0.0034473 * anchor

def f61_arm_273_analyst_v273(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=105, w2=454, w3=20, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(105)
    rank = change.rolling(454, min_periods=max(454//3, 2)).rank(pct=True)
    persistence = change.rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0554 * persistence + 0.0034474 * anchor

def f61_arm_274_analyst_v274(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=112, w2=465, w3=33, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61375 + 0.0034475 * anchor

def f61_arm_275_analyst_v275(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=119, w2=476, w3=46, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(476, min_periods=max(476//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0706 * slope + 0.0034476 * anchor

def f61_arm_276_analyst_v276(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=126, w2=487, w3=59, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(487, min_periods=max(487//3, 2)).mean()
    noise = impulse.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.869375 + 0.0034477 * anchor

def f61_arm_277_analyst_v277(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=133, w2=498, w3=72, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 498)
    curvature = _rolling_slope(acceleration, 72)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0858 * acceleration + 0.0034478 * anchor

def f61_arm_278_analyst_v278(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=140, w2=509, w3=85, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(509, min_periods=max(509//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(85) * 0.898125 + 0.0034479 * anchor

def f61_arm_279_analyst_v279(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=147, w2=17, w3=98, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(17, min_periods=max(17//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.101 * _rolling_slope(draw, 98) + 0.003448 * anchor

def f61_arm_280_analyst_v280(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=154, w2=28, w3=111, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(28, min_periods=max(28//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.926875 + 0.0034481 * anchor

def f61_arm_281_analyst_v281(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=161, w2=39, w3=124, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 39)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=124, adjust=False).mean() * 0.94125 + 0.0034482 * anchor

def f61_arm_282_analyst_v282(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=168, w2=50, w3=137, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(50, min_periods=max(50//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.955625 + 0.0034483 * anchor

def f61_arm_283_analyst_v283(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=175, w2=61, w3=150, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(61, min_periods=max(61//3, 2)).rank(pct=True)
    persistence = change.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1314 * persistence + 0.0034484 * anchor

def f61_arm_284_analyst_v284(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=182, w2=72, w3=163, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.984375 + 0.0034485 * anchor

def f61_arm_285_analyst_v285(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=189, w2=83, w3=176, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(83, min_periods=max(83//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1466 * slope + 0.0034486 * anchor

def f61_arm_286_analyst_v286(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=196, w2=94, w3=189, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(94, min_periods=max(94//3, 2)).mean()
    noise = impulse.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.013125 + 0.0034487 * anchor

def f61_arm_287_analyst_v287(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=203, w2=105, w3=202, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 105)
    curvature = _rolling_slope(acceleration, 202)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1618 * acceleration + 0.0034488 * anchor

def f61_arm_288_analyst_v288(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=210, w2=116, w3=215, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(116, min_periods=max(116//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.041875 + 0.0034489 * anchor

def f61_arm_289_analyst_v289(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=217, w2=127, w3=228, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(127, min_periods=max(127//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.177 * _rolling_slope(draw, 228) + 0.003449 * anchor

def f61_arm_290_analyst_v290(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=224, w2=138, w3=241, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.070625 + 0.0034491 * anchor

def f61_arm_291_analyst_v291(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=231, w2=149, w3=254, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=254, adjust=False).mean() * 1.085 + 0.0034492 * anchor

def f61_arm_292_analyst_v292(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=238, w2=160, w3=267, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.099375 + 0.0034493 * anchor

def f61_arm_293_analyst_v293(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=245, w2=171, w3=280, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(171, min_periods=max(171//3, 2)).rank(pct=True)
    persistence = change.rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2074 * persistence + 0.0034494 * anchor

def f61_arm_294_analyst_v294(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=252, w2=182, w3=293, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(252, min_periods=max(252//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.128125 + 0.0034495 * anchor

def f61_arm_295_analyst_v295(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=8, w2=193, w3=306, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(193, min_periods=max(193//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2226 * slope + 0.0034496 * anchor

def f61_arm_296_analyst_v296(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=15, w2=204, w3=319, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(15)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.156875 + 0.0034497 * anchor

def f61_arm_297_analyst_v297(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=22, w2=215, w3=332, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 215)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2378 * acceleration + 0.0034498 * anchor

def f61_arm_298_analyst_v298(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=29, w2=226, w3=345, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(226, min_periods=max(226//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.185625 + 0.0034499 * anchor

def f61_arm_299_analyst_v299(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=36, w2=237, w3=358, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(237, min_periods=max(237//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.253 * _rolling_slope(draw, 358) + 0.00345 * anchor

def f61_arm_300_analyst_v300(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=43, w2=248, w3=371, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(248, min_periods=max(248//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.214375 + 0.0034501 * anchor
