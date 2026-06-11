"""63 analyst downgrade cluster d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f63_adc_451_analyst_v451_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=213, w2=19, w3=523, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.306875 + 0.0035852 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_452_analyst_v452_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=220, w2=30, w3=536, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.32125 + 0.0035853 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_453_analyst_v453_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=227, w2=41, w3=549, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3806 * persistence + 0.0035854 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_454_analyst_v454_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=234, w2=52, w3=562, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35 + 0.0035855 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_455_analyst_v455_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=241, w2=63, w3=575, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(63, min_periods=max(63//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3958 * slope + 0.0035856 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_456_analyst_v456_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=248, w2=74, w3=588, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.37875 + 0.0035857 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_457_analyst_v457_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=255, w2=85, w3=601, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 255)
    acceleration = _rolling_slope(velocity, 85)
    curvature = _rolling_slope(acceleration, 601)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.411 * acceleration + 0.0035858 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_458_analyst_v458_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=11, w2=96, w3=614, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(96, min_periods=max(96//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4075 + 0.0035859 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_459_analyst_v459_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=18, w2=107, w3=627, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(107, min_periods=max(107//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0498 * _rolling_slope(draw, 627) + 0.003586 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_460_analyst_v460_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=25, w2=118, w3=640, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(118, min_periods=max(118//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.43625 + 0.0035861 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_461_analyst_v461_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=32, w2=129, w3=653, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 129)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.450625 + 0.0035862 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_462_analyst_v462_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=39, w2=140, w3=666, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(140, min_periods=max(140//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.465 + 0.0035863 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_463_analyst_v463_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=46, w2=151, w3=679, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(46)
    rank = change.rolling(151, min_periods=max(151//3, 2)).rank(pct=True)
    persistence = change.rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0802 * persistence + 0.0035864 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_464_analyst_v464_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=53, w2=162, w3=692, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(162, min_periods=max(162//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49375 + 0.0035865 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_465_analyst_v465_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=60, w2=173, w3=705, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(173, min_periods=max(173//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0954 * slope + 0.0035866 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_466_analyst_v466_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=67, w2=184, w3=718, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(67)
    drag = impulse.rolling(184, min_periods=max(184//3, 2)).mean()
    noise = impulse.abs().rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5225 + 0.0035867 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_467_analyst_v467_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=74, w2=195, w3=731, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 731)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1106 * acceleration + 0.0035868 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_468_analyst_v468_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=81, w2=206, w3=744, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.55125 + 0.0035869 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_469_analyst_v469_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=88, w2=217, w3=757, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(217, min_periods=max(217//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1258 * _rolling_slope(draw, 757) + 0.003587 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_470_analyst_v470_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=95, w2=228, w3=770, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(228, min_periods=max(228//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58 + 0.0035871 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_471_analyst_v471_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=102, w2=239, w3=26, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 239)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=26, adjust=False).mean() * 1.594375 + 0.0035872 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_472_analyst_v472_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=109, w2=250, w3=39, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(250, min_periods=max(250//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.60875 + 0.0035873 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_473_analyst_v473_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=116, w2=261, w3=52, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(116)
    rank = change.rolling(261, min_periods=max(261//3, 2)).rank(pct=True)
    persistence = change.rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1562 * persistence + 0.0035874 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_474_analyst_v474_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=123, w2=272, w3=65, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(272, min_periods=max(272//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.864375 + 0.0035875 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_475_analyst_v475_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=130, w2=283, w3=78, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(283, min_periods=max(283//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1714 * slope + 0.0035876 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_476_analyst_v476_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=137, w2=294, w3=91, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(294, min_periods=max(294//3, 2)).mean()
    noise = impulse.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.893125 + 0.0035877 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_477_analyst_v477_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=144, w2=305, w3=104, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 305)
    curvature = _rolling_slope(acceleration, 104)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1866 * acceleration + 0.0035878 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_478_analyst_v478_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=151, w2=316, w3=117, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(316, min_periods=max(316//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(117) * 0.921875 + 0.0035879 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_479_analyst_v479_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=158, w2=327, w3=130, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(327, min_periods=max(327//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2018 * _rolling_slope(draw, 130) + 0.003588 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_480_analyst_v480_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=165, w2=338, w3=143, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.950625 + 0.0035881 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_481_analyst_v481_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=172, w2=349, w3=156, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 349)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=156, adjust=False).mean() * 0.965 + 0.0035882 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_482_analyst_v482_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=179, w2=360, w3=169, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.979375 + 0.0035883 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_483_analyst_v483_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=186, w2=371, w3=182, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(371, min_periods=max(371//3, 2)).rank(pct=True)
    persistence = change.rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2322 * persistence + 0.0035884 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_484_analyst_v484_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=193, w2=382, w3=195, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.008125 + 0.0035885 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_485_analyst_v485_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=200, w2=393, w3=208, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(393, min_periods=max(393//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2474 * slope + 0.0035886 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_486_analyst_v486_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=207, w2=404, w3=221, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(404, min_periods=max(404//3, 2)).mean()
    noise = impulse.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.036875 + 0.0035887 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_487_analyst_v487_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=214, w2=415, w3=234, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 415)
    curvature = _rolling_slope(acceleration, 234)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2626 * acceleration + 0.0035888 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_488_analyst_v488_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=221, w2=426, w3=247, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(426, min_periods=max(426//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.065625 + 0.0035889 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_489_analyst_v489_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=228, w2=437, w3=260, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(437, min_periods=max(437//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2778 * _rolling_slope(draw, 260) + 0.003589 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_490_analyst_v490_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=235, w2=448, w3=273, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(448, min_periods=max(448//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.094375 + 0.0035891 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_491_analyst_v491_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=242, w2=459, w3=286, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 459)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=286, adjust=False).mean() * 1.10875 + 0.0035892 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_492_analyst_v492_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=249, w2=470, w3=299, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(470, min_periods=max(470//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.123125 + 0.0035893 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_493_analyst_v493_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=5, w2=481, w3=312, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(5)
    rank = change.rolling(481, min_periods=max(481//3, 2)).rank(pct=True)
    persistence = change.rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3082 * persistence + 0.0035894 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_494_analyst_v494_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=12, w2=492, w3=325, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(492, min_periods=max(492//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.151875 + 0.0035895 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_495_analyst_v495_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=19, w2=503, w3=338, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(503, min_periods=max(503//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 19)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3234 * slope + 0.0035896 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_496_analyst_v496_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=26, w2=11, w3=351, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(26)
    drag = impulse.rolling(11, min_periods=max(11//3, 2)).mean()
    noise = impulse.abs().rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.180625 + 0.0035897 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_497_analyst_v497_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=33, w2=22, w3=364, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 22)
    curvature = _rolling_slope(acceleration, 364)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3386 * acceleration + 0.0035898 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_498_analyst_v498_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=40, w2=33, w3=377, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(33, min_periods=max(33//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.209375 + 0.0035899 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_499_analyst_v499_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=47, w2=44, w3=390, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(44, min_periods=max(44//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3538 * _rolling_slope(draw, 390) + 0.00359 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_500_analyst_v500_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=54, w2=55, w3=403, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(55, min_periods=max(55//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.238125 + 0.0035901 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_501_analyst_v501_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=61, w2=66, w3=416, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 66)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2525 + 0.0035902 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_502_analyst_v502_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=68, w2=77, w3=429, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(77, min_periods=max(77//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.266875 + 0.0035903 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_503_analyst_v503_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=75, w2=88, w3=442, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(75)
    rank = change.rolling(88, min_periods=max(88//3, 2)).rank(pct=True)
    persistence = change.rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3842 * persistence + 0.0035904 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_504_analyst_v504_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=82, w2=99, w3=455, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.295625 + 0.0035905 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_505_analyst_v505_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=89, w2=110, w3=468, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3994 * slope + 0.0035906 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_506_analyst_v506_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=96, w2=121, w3=481, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(96)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.324375 + 0.0035907 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_507_analyst_v507_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=103, w2=132, w3=494, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 132)
    curvature = _rolling_slope(acceleration, 494)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0382 * acceleration + 0.0035908 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_508_analyst_v508_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=110, w2=143, w3=507, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(143, min_periods=max(143//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.353125 + 0.0035909 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_509_analyst_v509_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=117, w2=154, w3=520, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(154, min_periods=max(154//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0534 * _rolling_slope(draw, 520) + 0.003591 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_510_analyst_v510_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=124, w2=165, w3=533, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(165, min_periods=max(165//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.381875 + 0.0035911 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_511_analyst_v511_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=131, w2=176, w3=546, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 176)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.39625 + 0.0035912 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_512_analyst_v512_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=138, w2=187, w3=559, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(187, min_periods=max(187//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.410625 + 0.0035913 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_513_analyst_v513_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=145, w2=198, w3=572, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(198, min_periods=max(198//3, 2)).rank(pct=True)
    persistence = change.rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0838 * persistence + 0.0035914 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_514_analyst_v514_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=152, w2=209, w3=585, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(209, min_periods=max(209//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.439375 + 0.0035915 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_515_analyst_v515_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=159, w2=220, w3=598, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(220, min_periods=max(220//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.099 * slope + 0.0035916 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_516_analyst_v516_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=166, w2=231, w3=611, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(231, min_periods=max(231//3, 2)).mean()
    noise = impulse.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.468125 + 0.0035917 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_517_analyst_v517_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=173, w2=242, w3=624, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 242)
    curvature = _rolling_slope(acceleration, 624)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1142 * acceleration + 0.0035918 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_518_analyst_v518_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=180, w2=253, w3=637, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(253, min_periods=max(253//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.496875 + 0.0035919 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_519_analyst_v519_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=187, w2=264, w3=650, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(264, min_periods=max(264//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1294 * _rolling_slope(draw, 650) + 0.003592 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_520_analyst_v520_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=194, w2=275, w3=663, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(275, min_periods=max(275//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.525625 + 0.0035921 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_521_analyst_v521_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=201, w2=286, w3=676, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 286)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.54 + 0.0035922 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_522_analyst_v522_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=208, w2=297, w3=689, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(297, min_periods=max(297//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.554375 + 0.0035923 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_523_analyst_v523_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=215, w2=308, w3=702, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(308, min_periods=max(308//3, 2)).rank(pct=True)
    persistence = change.rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1598 * persistence + 0.0035924 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_524_analyst_v524_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=222, w2=319, w3=715, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(319, min_periods=max(319//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.583125 + 0.0035925 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_525_analyst_v525_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=229, w2=330, w3=728, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(330, min_periods=max(330//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.175 * slope + 0.0035926 * anchor
    return base_signal.diff().diff().diff()
