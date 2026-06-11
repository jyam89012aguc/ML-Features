"""62 analyst revision dispersion d2 second derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f62_ard_226_analyst_v226_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=211, w2=501, w3=396, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.044375 + 0.0035027 * anchor
    return base_signal.diff().diff()

def f62_ard_227_analyst_v227_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=218, w2=512, w3=409, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 512)
    curvature = _rolling_slope(acceleration, 409)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1254 * acceleration + 0.0035028 * anchor
    return base_signal.diff().diff()

def f62_ard_228_analyst_v228_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=225, w2=20, w3=422, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(20, min_periods=max(20//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.073125 + 0.0035029 * anchor
    return base_signal.diff().diff()

def f62_ard_229_analyst_v229_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=232, w2=31, w3=435, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(31, min_periods=max(31//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1406 * _rolling_slope(draw, 435) + 0.003503 * anchor
    return base_signal.diff().diff()

def f62_ard_230_analyst_v230_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=239, w2=42, w3=448, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(42, min_periods=max(42//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.101875 + 0.0035031 * anchor
    return base_signal.diff().diff()

def f62_ard_231_analyst_v231_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=246, w2=53, w3=461, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 53)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.11625 + 0.0035032 * anchor
    return base_signal.diff().diff()

def f62_ard_232_analyst_v232_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=253, w2=64, w3=474, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(64, min_periods=max(64//3, 2)).max()
    trough = x.rolling(253, min_periods=max(253//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.130625 + 0.0035033 * anchor
    return base_signal.diff().diff()

def f62_ard_233_analyst_v233_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=9, w2=75, w3=487, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(9)
    rank = change.rolling(75, min_periods=max(75//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.171 * persistence + 0.0035034 * anchor
    return base_signal.diff().diff()

def f62_ard_234_analyst_v234_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=16, w2=86, w3=500, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(86, min_periods=max(86//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.159375 + 0.0035035 * anchor
    return base_signal.diff().diff()

def f62_ard_235_analyst_v235_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=23, w2=97, w3=513, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(97, min_periods=max(97//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1862 * slope + 0.0035036 * anchor
    return base_signal.diff().diff()

def f62_ard_236_analyst_v236_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=30, w2=108, w3=526, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(30)
    drag = impulse.rolling(108, min_periods=max(108//3, 2)).mean()
    noise = impulse.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.188125 + 0.0035037 * anchor
    return base_signal.diff().diff()

def f62_ard_237_analyst_v237_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=37, w2=119, w3=539, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 119)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2014 * acceleration + 0.0035038 * anchor
    return base_signal.diff().diff()

def f62_ard_238_analyst_v238_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=44, w2=130, w3=552, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(130, min_periods=max(130//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.216875 + 0.0035039 * anchor
    return base_signal.diff().diff()

def f62_ard_239_analyst_v239_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=51, w2=141, w3=565, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2166 * _rolling_slope(draw, 565) + 0.003504 * anchor
    return base_signal.diff().diff()

def f62_ard_240_analyst_v240_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=58, w2=152, w3=578, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(152, min_periods=max(152//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.245625 + 0.0035041 * anchor
    return base_signal.diff().diff()

def f62_ard_241_analyst_v241_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=65, w2=163, w3=591, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 163)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.26 + 0.0035042 * anchor
    return base_signal.diff().diff()

def f62_ard_242_analyst_v242_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=72, w2=174, w3=604, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(174, min_periods=max(174//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.274375 + 0.0035043 * anchor
    return base_signal.diff().diff()

def f62_ard_243_analyst_v243_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=79, w2=185, w3=617, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(79)
    rank = change.rolling(185, min_periods=max(185//3, 2)).rank(pct=True)
    persistence = change.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.247 * persistence + 0.0035044 * anchor
    return base_signal.diff().diff()

def f62_ard_244_analyst_v244_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=86, w2=196, w3=630, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(196, min_periods=max(196//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.303125 + 0.0035045 * anchor
    return base_signal.diff().diff()

def f62_ard_245_analyst_v245_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=93, w2=207, w3=643, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(207, min_periods=max(207//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2622 * slope + 0.0035046 * anchor
    return base_signal.diff().diff()

def f62_ard_246_analyst_v246_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=100, w2=218, w3=656, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(100)
    drag = impulse.rolling(218, min_periods=max(218//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.331875 + 0.0035047 * anchor
    return base_signal.diff().diff()

def f62_ard_247_analyst_v247_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=107, w2=229, w3=669, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 229)
    curvature = _rolling_slope(acceleration, 669)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2774 * acceleration + 0.0035048 * anchor
    return base_signal.diff().diff()

def f62_ard_248_analyst_v248_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=114, w2=240, w3=682, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(240, min_periods=max(240//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.360625 + 0.0035049 * anchor
    return base_signal.diff().diff()

def f62_ard_249_analyst_v249_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=121, w2=251, w3=695, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(251, min_periods=max(251//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2926 * _rolling_slope(draw, 695) + 0.003505 * anchor
    return base_signal.diff().diff()

def f62_ard_250_analyst_v250_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=128, w2=262, w3=708, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(262, min_periods=max(262//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.389375 + 0.0035051 * anchor
    return base_signal.diff().diff()

def f62_ard_251_analyst_v251_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=135, w2=273, w3=721, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 273)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.40375 + 0.0035052 * anchor
    return base_signal.diff().diff()

def f62_ard_252_analyst_v252_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=142, w2=284, w3=734, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(284, min_periods=max(284//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.418125 + 0.0035053 * anchor
    return base_signal.diff().diff()

def f62_ard_253_analyst_v253_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=149, w2=295, w3=747, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.323 * persistence + 0.0035054 * anchor
    return base_signal.diff().diff()

def f62_ard_254_analyst_v254_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=156, w2=306, w3=760, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(306, min_periods=max(306//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.446875 + 0.0035055 * anchor
    return base_signal.diff().diff()

def f62_ard_255_analyst_v255_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=163, w2=317, w3=16, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(317, min_periods=max(317//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3382 * slope + 0.0035056 * anchor
    return base_signal.diff().diff()

def f62_ard_256_analyst_v256_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=170, w2=328, w3=29, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(328, min_periods=max(328//3, 2)).mean()
    noise = impulse.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.475625 + 0.0035057 * anchor
    return base_signal.diff().diff()

def f62_ard_257_analyst_v257_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=177, w2=339, w3=42, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 339)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3534 * acceleration + 0.0035058 * anchor
    return base_signal.diff().diff()

def f62_ard_258_analyst_v258_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=184, w2=350, w3=55, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(350, min_periods=max(350//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(55) * 1.504375 + 0.0035059 * anchor
    return base_signal.diff().diff()

def f62_ard_259_analyst_v259_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=191, w2=361, w3=68, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(361, min_periods=max(361//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3686 * _rolling_slope(draw, 68) + 0.003506 * anchor
    return base_signal.diff().diff()

def f62_ard_260_analyst_v260_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=198, w2=372, w3=81, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(372, min_periods=max(372//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.533125 + 0.0035061 * anchor
    return base_signal.diff().diff()

def f62_ard_261_analyst_v261_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=205, w2=383, w3=94, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 383)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=94, adjust=False).mean() * 1.5475 + 0.0035062 * anchor
    return base_signal.diff().diff()

def f62_ard_262_analyst_v262_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=212, w2=394, w3=107, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(394, min_periods=max(394//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.561875 + 0.0035063 * anchor
    return base_signal.diff().diff()

def f62_ard_263_analyst_v263_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=219, w2=405, w3=120, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(405, min_periods=max(405//3, 2)).rank(pct=True)
    persistence = change.rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.399 * persistence + 0.0035064 * anchor
    return base_signal.diff().diff()

def f62_ard_264_analyst_v264_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=226, w2=416, w3=133, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(416, min_periods=max(416//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.590625 + 0.0035065 * anchor
    return base_signal.diff().diff()

def f62_ard_265_analyst_v265_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=233, w2=427, w3=146, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(427, min_periods=max(427//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0378 * slope + 0.0035066 * anchor
    return base_signal.diff().diff()

def f62_ard_266_analyst_v266_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=240, w2=438, w3=159, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(438, min_periods=max(438//3, 2)).mean()
    noise = impulse.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.619375 + 0.0035067 * anchor
    return base_signal.diff().diff()

def f62_ard_267_analyst_v267_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=247, w2=449, w3=172, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 449)
    curvature = _rolling_slope(acceleration, 172)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.053 * acceleration + 0.0035068 * anchor
    return base_signal.diff().diff()

def f62_ard_268_analyst_v268_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=254, w2=460, w3=185, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(460, min_periods=max(460//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.875 + 0.0035069 * anchor
    return base_signal.diff().diff()

def f62_ard_269_analyst_v269_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=10, w2=471, w3=198, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(471, min_periods=max(471//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0682 * _rolling_slope(draw, 198) + 0.003507 * anchor
    return base_signal.diff().diff()

def f62_ard_270_analyst_v270_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=17, w2=482, w3=211, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.90375 + 0.0035071 * anchor
    return base_signal.diff().diff()

def f62_ard_271_analyst_v271_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=24, w2=493, w3=224, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 493)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=224, adjust=False).mean() * 0.918125 + 0.0035072 * anchor
    return base_signal.diff().diff()

def f62_ard_272_analyst_v272_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=31, w2=504, w3=237, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9325 + 0.0035073 * anchor
    return base_signal.diff().diff()

def f62_ard_273_analyst_v273_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=38, w2=12, w3=250, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(38)
    rank = change.rolling(12, min_periods=max(12//3, 2)).rank(pct=True)
    persistence = change.rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0986 * persistence + 0.0035074 * anchor
    return base_signal.diff().diff()

def f62_ard_274_analyst_v274_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=45, w2=23, w3=263, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96125 + 0.0035075 * anchor
    return base_signal.diff().diff()

def f62_ard_275_analyst_v275_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=52, w2=34, w3=276, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1138 * slope + 0.0035076 * anchor
    return base_signal.diff().diff()

def f62_ard_276_analyst_v276_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=59, w2=45, w3=289, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(59)
    drag = impulse.rolling(45, min_periods=max(45//3, 2)).mean()
    noise = impulse.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.99 + 0.0035077 * anchor
    return base_signal.diff().diff()

def f62_ard_277_analyst_v277_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=66, w2=56, w3=302, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 56)
    curvature = _rolling_slope(acceleration, 302)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.129 * acceleration + 0.0035078 * anchor
    return base_signal.diff().diff()

def f62_ard_278_analyst_v278_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=73, w2=67, w3=315, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(67, min_periods=max(67//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.01875 + 0.0035079 * anchor
    return base_signal.diff().diff()

def f62_ard_279_analyst_v279_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=80, w2=78, w3=328, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1442 * _rolling_slope(draw, 328) + 0.003508 * anchor
    return base_signal.diff().diff()

def f62_ard_280_analyst_v280_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=87, w2=89, w3=341, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(89, min_periods=max(89//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0475 + 0.0035081 * anchor
    return base_signal.diff().diff()

def f62_ard_281_analyst_v281_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=94, w2=100, w3=354, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 100)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.061875 + 0.0035082 * anchor
    return base_signal.diff().diff()

def f62_ard_282_analyst_v282_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=101, w2=111, w3=367, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(111, min_periods=max(111//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07625 + 0.0035083 * anchor
    return base_signal.diff().diff()

def f62_ard_283_analyst_v283_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=108, w2=122, w3=380, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(108)
    rank = change.rolling(122, min_periods=max(122//3, 2)).rank(pct=True)
    persistence = change.rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1746 * persistence + 0.0035084 * anchor
    return base_signal.diff().diff()

def f62_ard_284_analyst_v284_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=115, w2=133, w3=393, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(133, min_periods=max(133//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.105 + 0.0035085 * anchor
    return base_signal.diff().diff()

def f62_ard_285_analyst_v285_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=122, w2=144, w3=406, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(144, min_periods=max(144//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1898 * slope + 0.0035086 * anchor
    return base_signal.diff().diff()

def f62_ard_286_analyst_v286_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=129, w2=155, w3=419, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(155, min_periods=max(155//3, 2)).mean()
    noise = impulse.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13375 + 0.0035087 * anchor
    return base_signal.diff().diff()

def f62_ard_287_analyst_v287_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=136, w2=166, w3=432, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 166)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.205 * acceleration + 0.0035088 * anchor
    return base_signal.diff().diff()

def f62_ard_288_analyst_v288_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=143, w2=177, w3=445, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(177, min_periods=max(177//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1625 + 0.0035089 * anchor
    return base_signal.diff().diff()

def f62_ard_289_analyst_v289_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=150, w2=188, w3=458, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(188, min_periods=max(188//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2202 * _rolling_slope(draw, 458) + 0.003509 * anchor
    return base_signal.diff().diff()

def f62_ard_290_analyst_v290_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=157, w2=199, w3=471, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(199, min_periods=max(199//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.19125 + 0.0035091 * anchor
    return base_signal.diff().diff()

def f62_ard_291_analyst_v291_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=164, w2=210, w3=484, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 210)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.205625 + 0.0035092 * anchor
    return base_signal.diff().diff()

def f62_ard_292_analyst_v292_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=171, w2=221, w3=497, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(221, min_periods=max(221//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.22 + 0.0035093 * anchor
    return base_signal.diff().diff()

def f62_ard_293_analyst_v293_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=178, w2=232, w3=510, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(232, min_periods=max(232//3, 2)).rank(pct=True)
    persistence = change.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2506 * persistence + 0.0035094 * anchor
    return base_signal.diff().diff()

def f62_ard_294_analyst_v294_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=185, w2=243, w3=523, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(243, min_periods=max(243//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24875 + 0.0035095 * anchor
    return base_signal.diff().diff()

def f62_ard_295_analyst_v295_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=192, w2=254, w3=536, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(254, min_periods=max(254//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2658 * slope + 0.0035096 * anchor
    return base_signal.diff().diff()

def f62_ard_296_analyst_v296_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=199, w2=265, w3=549, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(265, min_periods=max(265//3, 2)).mean()
    noise = impulse.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2775 + 0.0035097 * anchor
    return base_signal.diff().diff()

def f62_ard_297_analyst_v297_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=206, w2=276, w3=562, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 276)
    curvature = _rolling_slope(acceleration, 562)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.281 * acceleration + 0.0035098 * anchor
    return base_signal.diff().diff()

def f62_ard_298_analyst_v298_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=213, w2=287, w3=575, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(287, min_periods=max(287//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.30625 + 0.0035099 * anchor
    return base_signal.diff().diff()

def f62_ard_299_analyst_v299_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=220, w2=298, w3=588, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(298, min_periods=max(298//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2962 * _rolling_slope(draw, 588) + 0.00351 * anchor
    return base_signal.diff().diff()

def f62_ard_300_analyst_v300_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=227, w2=309, w3=601, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(309, min_periods=max(309//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.335 + 0.0035101 * anchor
    return base_signal.diff().diff()
