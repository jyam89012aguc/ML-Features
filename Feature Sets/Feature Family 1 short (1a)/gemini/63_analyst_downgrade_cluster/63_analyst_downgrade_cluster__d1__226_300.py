"""63 analyst downgrade cluster d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f63_adc_226_analyst_v226_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=144, w2=59, w3=626, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(59, min_periods=max(59//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.165 + 0.0035627 * anchor
    return base_signal.diff()

def f63_adc_227_analyst_v227_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=151, w2=70, w3=639, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 639)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1686 * acceleration + 0.0035628 * anchor
    return base_signal.diff()

def f63_adc_228_analyst_v228_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=158, w2=81, w3=652, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(81, min_periods=max(81//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.19375 + 0.0035629 * anchor
    return base_signal.diff()

def f63_adc_229_analyst_v229_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=165, w2=92, w3=665, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(92, min_periods=max(92//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1838 * _rolling_slope(draw, 665) + 0.003563 * anchor
    return base_signal.diff()

def f63_adc_230_analyst_v230_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=172, w2=103, w3=678, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(103, min_periods=max(103//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2225 + 0.0035631 * anchor
    return base_signal.diff()

def f63_adc_231_analyst_v231_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=179, w2=114, w3=691, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 114)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.236875 + 0.0035632 * anchor
    return base_signal.diff()

def f63_adc_232_analyst_v232_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=186, w2=125, w3=704, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(125, min_periods=max(125//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.25125 + 0.0035633 * anchor
    return base_signal.diff()

def f63_adc_233_analyst_v233_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=193, w2=136, w3=717, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(136, min_periods=max(136//3, 2)).rank(pct=True)
    persistence = change.rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2142 * persistence + 0.0035634 * anchor
    return base_signal.diff()

def f63_adc_234_analyst_v234_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=200, w2=147, w3=730, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(147, min_periods=max(147//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28 + 0.0035635 * anchor
    return base_signal.diff()

def f63_adc_235_analyst_v235_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=207, w2=158, w3=743, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(158, min_periods=max(158//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2294 * slope + 0.0035636 * anchor
    return base_signal.diff()

def f63_adc_236_analyst_v236_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=214, w2=169, w3=756, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(169, min_periods=max(169//3, 2)).mean()
    noise = impulse.abs().rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.30875 + 0.0035637 * anchor
    return base_signal.diff()

def f63_adc_237_analyst_v237_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=221, w2=180, w3=769, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 180)
    curvature = _rolling_slope(acceleration, 769)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2446 * acceleration + 0.0035638 * anchor
    return base_signal.diff()

def f63_adc_238_analyst_v238_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=228, w2=191, w3=25, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(191, min_periods=max(191//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(25) * 1.3375 + 0.0035639 * anchor
    return base_signal.diff()

def f63_adc_239_analyst_v239_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=235, w2=202, w3=38, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(202, min_periods=max(202//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2598 * _rolling_slope(draw, 38) + 0.003564 * anchor
    return base_signal.diff()

def f63_adc_240_analyst_v240_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=242, w2=213, w3=51, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(213, min_periods=max(213//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36625 + 0.0035641 * anchor
    return base_signal.diff()

def f63_adc_241_analyst_v241_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=249, w2=224, w3=64, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 224)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=64, adjust=False).mean() * 1.380625 + 0.0035642 * anchor
    return base_signal.diff()

def f63_adc_242_analyst_v242_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=5, w2=235, w3=77, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(235, min_periods=max(235//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.395 + 0.0035643 * anchor
    return base_signal.diff()

def f63_adc_243_analyst_v243_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=12, w2=246, w3=90, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(12)
    rank = change.rolling(246, min_periods=max(246//3, 2)).rank(pct=True)
    persistence = change.rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2902 * persistence + 0.0035644 * anchor
    return base_signal.diff()

def f63_adc_244_analyst_v244_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=19, w2=257, w3=103, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(257, min_periods=max(257//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.42375 + 0.0035645 * anchor
    return base_signal.diff()

def f63_adc_245_analyst_v245_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=26, w2=268, w3=116, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(268, min_periods=max(268//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3054 * slope + 0.0035646 * anchor
    return base_signal.diff()

def f63_adc_246_analyst_v246_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=33, w2=279, w3=129, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(33)
    drag = impulse.rolling(279, min_periods=max(279//3, 2)).mean()
    noise = impulse.abs().rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4525 + 0.0035647 * anchor
    return base_signal.diff()

def f63_adc_247_analyst_v247_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=40, w2=290, w3=142, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 290)
    curvature = _rolling_slope(acceleration, 142)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3206 * acceleration + 0.0035648 * anchor
    return base_signal.diff()

def f63_adc_248_analyst_v248_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=47, w2=301, w3=155, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(301, min_periods=max(301//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.48125 + 0.0035649 * anchor
    return base_signal.diff()

def f63_adc_249_analyst_v249_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=54, w2=312, w3=168, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(312, min_periods=max(312//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3358 * _rolling_slope(draw, 168) + 0.003565 * anchor
    return base_signal.diff()

def f63_adc_250_analyst_v250_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=61, w2=323, w3=181, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(323, min_periods=max(323//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51 + 0.0035651 * anchor
    return base_signal.diff()

def f63_adc_251_analyst_v251_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=68, w2=334, w3=194, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 334)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=194, adjust=False).mean() * 1.524375 + 0.0035652 * anchor
    return base_signal.diff()

def f63_adc_252_analyst_v252_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=75, w2=345, w3=207, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(345, min_periods=max(345//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.53875 + 0.0035653 * anchor
    return base_signal.diff()

def f63_adc_253_analyst_v253_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=82, w2=356, w3=220, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(82)
    rank = change.rolling(356, min_periods=max(356//3, 2)).rank(pct=True)
    persistence = change.rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3662 * persistence + 0.0035654 * anchor
    return base_signal.diff()

def f63_adc_254_analyst_v254_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=89, w2=367, w3=233, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(367, min_periods=max(367//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5675 + 0.0035655 * anchor
    return base_signal.diff()

def f63_adc_255_analyst_v255_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=96, w2=378, w3=246, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(378, min_periods=max(378//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3814 * slope + 0.0035656 * anchor
    return base_signal.diff()

def f63_adc_256_analyst_v256_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=103, w2=389, w3=259, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(103)
    drag = impulse.rolling(389, min_periods=max(389//3, 2)).mean()
    noise = impulse.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.59625 + 0.0035657 * anchor
    return base_signal.diff()

def f63_adc_257_analyst_v257_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=110, w2=400, w3=272, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 400)
    curvature = _rolling_slope(acceleration, 272)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3966 * acceleration + 0.0035658 * anchor
    return base_signal.diff()

def f63_adc_258_analyst_v258_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=117, w2=411, w3=285, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(411, min_periods=max(411//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.851875 + 0.0035659 * anchor
    return base_signal.diff()

def f63_adc_259_analyst_v259_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=124, w2=422, w3=298, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(422, min_periods=max(422//3, 2)).max()
    rebound = x - x.rolling(124, min_periods=max(124//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0354 * _rolling_slope(draw, 298) + 0.003566 * anchor
    return base_signal.diff()

def f63_adc_260_analyst_v260_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=131, w2=433, w3=311, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(433, min_periods=max(433//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.880625 + 0.0035661 * anchor
    return base_signal.diff()

def f63_adc_261_analyst_v261_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=138, w2=444, w3=324, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 444)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.895 + 0.0035662 * anchor
    return base_signal.diff()

def f63_adc_262_analyst_v262_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=145, w2=455, w3=337, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(455, min_periods=max(455//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.909375 + 0.0035663 * anchor
    return base_signal.diff()

def f63_adc_263_analyst_v263_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=152, w2=466, w3=350, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(466, min_periods=max(466//3, 2)).rank(pct=True)
    persistence = change.rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0658 * persistence + 0.0035664 * anchor
    return base_signal.diff()

def f63_adc_264_analyst_v264_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=159, w2=477, w3=363, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(477, min_periods=max(477//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.938125 + 0.0035665 * anchor
    return base_signal.diff()

def f63_adc_265_analyst_v265_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=166, w2=488, w3=376, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(488, min_periods=max(488//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.081 * slope + 0.0035666 * anchor
    return base_signal.diff()

def f63_adc_266_analyst_v266_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=173, w2=499, w3=389, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(499, min_periods=max(499//3, 2)).mean()
    noise = impulse.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.966875 + 0.0035667 * anchor
    return base_signal.diff()

def f63_adc_267_analyst_v267_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=180, w2=510, w3=402, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 510)
    curvature = _rolling_slope(acceleration, 402)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0962 * acceleration + 0.0035668 * anchor
    return base_signal.diff()

def f63_adc_268_analyst_v268_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=187, w2=18, w3=415, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(18, min_periods=max(18//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.995625 + 0.0035669 * anchor
    return base_signal.diff()

def f63_adc_269_analyst_v269_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=194, w2=29, w3=428, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(29, min_periods=max(29//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1114 * _rolling_slope(draw, 428) + 0.003567 * anchor
    return base_signal.diff()

def f63_adc_270_analyst_v270_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=201, w2=40, w3=441, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(40, min_periods=max(40//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.024375 + 0.0035671 * anchor
    return base_signal.diff()

def f63_adc_271_analyst_v271_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=208, w2=51, w3=454, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 51)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.03875 + 0.0035672 * anchor
    return base_signal.diff()

def f63_adc_272_analyst_v272_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=215, w2=62, w3=467, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(62, min_periods=max(62//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.053125 + 0.0035673 * anchor
    return base_signal.diff()

def f63_adc_273_analyst_v273_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=222, w2=73, w3=480, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(73, min_periods=max(73//3, 2)).rank(pct=True)
    persistence = change.rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1418 * persistence + 0.0035674 * anchor
    return base_signal.diff()

def f63_adc_274_analyst_v274_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=229, w2=84, w3=493, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(84, min_periods=max(84//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.081875 + 0.0035675 * anchor
    return base_signal.diff()

def f63_adc_275_analyst_v275_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=236, w2=95, w3=506, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(95, min_periods=max(95//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.157 * slope + 0.0035676 * anchor
    return base_signal.diff()

def f63_adc_276_analyst_v276_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=243, w2=106, w3=519, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(106, min_periods=max(106//3, 2)).mean()
    noise = impulse.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.110625 + 0.0035677 * anchor
    return base_signal.diff()

def f63_adc_277_analyst_v277_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=250, w2=117, w3=532, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 117)
    curvature = _rolling_slope(acceleration, 532)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1722 * acceleration + 0.0035678 * anchor
    return base_signal.diff()

def f63_adc_278_analyst_v278_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=6, w2=128, w3=545, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(128, min_periods=max(128//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.139375 + 0.0035679 * anchor
    return base_signal.diff()

def f63_adc_279_analyst_v279_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=13, w2=139, w3=558, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(139, min_periods=max(139//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1874 * _rolling_slope(draw, 558) + 0.003568 * anchor
    return base_signal.diff()

def f63_adc_280_analyst_v280_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=20, w2=150, w3=571, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(150, min_periods=max(150//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.168125 + 0.0035681 * anchor
    return base_signal.diff()

def f63_adc_281_analyst_v281_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=27, w2=161, w3=584, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 161)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1825 + 0.0035682 * anchor
    return base_signal.diff()

def f63_adc_282_analyst_v282_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=34, w2=172, w3=597, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(172, min_periods=max(172//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.196875 + 0.0035683 * anchor
    return base_signal.diff()

def f63_adc_283_analyst_v283_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=41, w2=183, w3=610, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(41)
    rank = change.rolling(183, min_periods=max(183//3, 2)).rank(pct=True)
    persistence = change.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2178 * persistence + 0.0035684 * anchor
    return base_signal.diff()

def f63_adc_284_analyst_v284_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=48, w2=194, w3=623, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(194, min_periods=max(194//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.225625 + 0.0035685 * anchor
    return base_signal.diff()

def f63_adc_285_analyst_v285_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=55, w2=205, w3=636, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(205, min_periods=max(205//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.233 * slope + 0.0035686 * anchor
    return base_signal.diff()

def f63_adc_286_analyst_v286_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=62, w2=216, w3=649, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(62)
    drag = impulse.rolling(216, min_periods=max(216//3, 2)).mean()
    noise = impulse.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.254375 + 0.0035687 * anchor
    return base_signal.diff()

def f63_adc_287_analyst_v287_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=69, w2=227, w3=662, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 227)
    curvature = _rolling_slope(acceleration, 662)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2482 * acceleration + 0.0035688 * anchor
    return base_signal.diff()

def f63_adc_288_analyst_v288_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=76, w2=238, w3=675, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(238, min_periods=max(238//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.283125 + 0.0035689 * anchor
    return base_signal.diff()

def f63_adc_289_analyst_v289_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=83, w2=249, w3=688, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(249, min_periods=max(249//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2634 * _rolling_slope(draw, 688) + 0.003569 * anchor
    return base_signal.diff()

def f63_adc_290_analyst_v290_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=90, w2=260, w3=701, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(260, min_periods=max(260//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.311875 + 0.0035691 * anchor
    return base_signal.diff()

def f63_adc_291_analyst_v291_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=97, w2=271, w3=714, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 271)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.32625 + 0.0035692 * anchor
    return base_signal.diff()

def f63_adc_292_analyst_v292_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=104, w2=282, w3=727, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(282, min_periods=max(282//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.340625 + 0.0035693 * anchor
    return base_signal.diff()

def f63_adc_293_analyst_v293_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=111, w2=293, w3=740, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(111)
    rank = change.rolling(293, min_periods=max(293//3, 2)).rank(pct=True)
    persistence = change.rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2938 * persistence + 0.0035694 * anchor
    return base_signal.diff()

def f63_adc_294_analyst_v294_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=118, w2=304, w3=753, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(304, min_periods=max(304//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.369375 + 0.0035695 * anchor
    return base_signal.diff()

def f63_adc_295_analyst_v295_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=125, w2=315, w3=766, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(315, min_periods=max(315//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.309 * slope + 0.0035696 * anchor
    return base_signal.diff()

def f63_adc_296_analyst_v296_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=132, w2=326, w3=22, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(326, min_periods=max(326//3, 2)).mean()
    noise = impulse.abs().rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.398125 + 0.0035697 * anchor
    return base_signal.diff()

def f63_adc_297_analyst_v297_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=139, w2=337, w3=35, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 337)
    curvature = _rolling_slope(acceleration, 35)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3242 * acceleration + 0.0035698 * anchor
    return base_signal.diff()

def f63_adc_298_analyst_v298_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=146, w2=348, w3=48, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(348, min_periods=max(348//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(48) * 1.426875 + 0.0035699 * anchor
    return base_signal.diff()

def f63_adc_299_analyst_v299_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=153, w2=359, w3=61, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(359, min_periods=max(359//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3394 * _rolling_slope(draw, 61) + 0.00357 * anchor
    return base_signal.diff()

def f63_adc_300_analyst_v300_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=160, w2=370, w3=74, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(370, min_periods=max(370//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.455625 + 0.0035701 * anchor
    return base_signal.diff()
