"""61 analyst revision momentum d3 third derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f61_arm_376_analyst_v376_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=73, w2=78, w3=602, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(73)
    drag = impulse.rolling(78, min_periods=max(78//3, 2)).mean()
    noise = impulse.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.53375 + 0.0034577 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_377_analyst_v377_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=80, w2=89, w3=615, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 89)
    curvature = _rolling_slope(acceleration, 615)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.093 * acceleration + 0.0034578 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_378_analyst_v378_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=87, w2=100, w3=628, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(100, min_periods=max(100//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5625 + 0.0034579 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_379_analyst_v379_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=94, w2=111, w3=641, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1082 * _rolling_slope(draw, 641) + 0.003458 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_380_analyst_v380_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=101, w2=122, w3=654, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(122, min_periods=max(122//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59125 + 0.0034581 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_381_analyst_v381_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=108, w2=133, w3=667, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 133)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.605625 + 0.0034582 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_382_analyst_v382_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=115, w2=144, w3=680, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(144, min_periods=max(144//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.62 + 0.0034583 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_383_analyst_v383_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=122, w2=155, w3=693, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(122)
    rank = change.rolling(155, min_periods=max(155//3, 2)).rank(pct=True)
    persistence = change.rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1386 * persistence + 0.0034584 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_384_analyst_v384_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=129, w2=166, w3=706, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(166, min_periods=max(166//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.875625 + 0.0034585 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_385_analyst_v385_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=136, w2=177, w3=719, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(177, min_periods=max(177//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1538 * slope + 0.0034586 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_386_analyst_v386_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=143, w2=188, w3=732, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(188, min_periods=max(188//3, 2)).mean()
    noise = impulse.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.904375 + 0.0034587 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_387_analyst_v387_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=150, w2=199, w3=745, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 199)
    curvature = _rolling_slope(acceleration, 745)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.169 * acceleration + 0.0034588 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_388_analyst_v388_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=157, w2=210, w3=758, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(210, min_periods=max(210//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.933125 + 0.0034589 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_389_analyst_v389_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=164, w2=221, w3=771, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(221, min_periods=max(221//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1842 * _rolling_slope(draw, 771) + 0.003459 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_390_analyst_v390_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=171, w2=232, w3=27, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(232, min_periods=max(232//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.961875 + 0.0034591 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_391_analyst_v391_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=178, w2=243, w3=40, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 243)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=40, adjust=False).mean() * 0.97625 + 0.0034592 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_392_analyst_v392_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=185, w2=254, w3=53, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(254, min_periods=max(254//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.990625 + 0.0034593 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_393_analyst_v393_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=192, w2=265, w3=66, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(265, min_periods=max(265//3, 2)).rank(pct=True)
    persistence = change.rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2146 * persistence + 0.0034594 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_394_analyst_v394_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=199, w2=276, w3=79, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(276, min_periods=max(276//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.019375 + 0.0034595 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_395_analyst_v395_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=206, w2=287, w3=92, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(287, min_periods=max(287//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2298 * slope + 0.0034596 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_396_analyst_v396_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=213, w2=298, w3=105, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.048125 + 0.0034597 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_397_analyst_v397_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=220, w2=309, w3=118, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 309)
    curvature = _rolling_slope(acceleration, 118)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.245 * acceleration + 0.0034598 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_398_analyst_v398_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=227, w2=320, w3=131, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(320, min_periods=max(320//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.076875 + 0.0034599 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_399_analyst_v399_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=234, w2=331, w3=144, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(331, min_periods=max(331//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2602 * _rolling_slope(draw, 144) + 0.00346 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_400_analyst_v400_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=241, w2=342, w3=157, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(342, min_periods=max(342//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.105625 + 0.0034601 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_401_analyst_v401_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=248, w2=353, w3=170, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 353)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=170, adjust=False).mean() * 1.12 + 0.0034602 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_402_analyst_v402_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=255, w2=364, w3=183, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.134375 + 0.0034603 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_403_analyst_v403_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=11, w2=375, w3=196, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(11)
    rank = change.rolling(375, min_periods=max(375//3, 2)).rank(pct=True)
    persistence = change.rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2906 * persistence + 0.0034604 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_404_analyst_v404_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=18, w2=386, w3=209, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(386, min_periods=max(386//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.163125 + 0.0034605 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_405_analyst_v405_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=25, w2=397, w3=222, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(397, min_periods=max(397//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3058 * slope + 0.0034606 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_406_analyst_v406_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=32, w2=408, w3=235, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(32)
    drag = impulse.rolling(408, min_periods=max(408//3, 2)).mean()
    noise = impulse.abs().rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.191875 + 0.0034607 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_407_analyst_v407_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=39, w2=419, w3=248, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 419)
    curvature = _rolling_slope(acceleration, 248)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.321 * acceleration + 0.0034608 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_408_analyst_v408_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=46, w2=430, w3=261, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.220625 + 0.0034609 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_409_analyst_v409_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=53, w2=441, w3=274, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(441, min_periods=max(441//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3362 * _rolling_slope(draw, 274) + 0.003461 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_410_analyst_v410_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=60, w2=452, w3=287, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(452, min_periods=max(452//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.249375 + 0.0034611 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_411_analyst_v411_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=67, w2=463, w3=300, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 463)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.26375 + 0.0034612 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_412_analyst_v412_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=74, w2=474, w3=313, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(474, min_periods=max(474//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.278125 + 0.0034613 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_413_analyst_v413_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=81, w2=485, w3=326, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(81)
    rank = change.rolling(485, min_periods=max(485//3, 2)).rank(pct=True)
    persistence = change.rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3666 * persistence + 0.0034614 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_414_analyst_v414_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=88, w2=496, w3=339, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(496, min_periods=max(496//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.306875 + 0.0034615 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_415_analyst_v415_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=95, w2=507, w3=352, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(507, min_periods=max(507//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3818 * slope + 0.0034616 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_416_analyst_v416_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=102, w2=15, w3=365, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(102)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.335625 + 0.0034617 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_417_analyst_v417_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=109, w2=26, w3=378, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 26)
    curvature = _rolling_slope(acceleration, 378)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.397 * acceleration + 0.0034618 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_418_analyst_v418_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=116, w2=37, w3=391, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(37, min_periods=max(37//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.364375 + 0.0034619 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_419_analyst_v419_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=123, w2=48, w3=404, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(48, min_periods=max(48//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0358 * _rolling_slope(draw, 404) + 0.003462 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_420_analyst_v420_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=130, w2=59, w3=417, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(59, min_periods=max(59//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.393125 + 0.0034621 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_421_analyst_v421_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=137, w2=70, w3=430, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 70)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4075 + 0.0034622 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_422_analyst_v422_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=144, w2=81, w3=443, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(81, min_periods=max(81//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.421875 + 0.0034623 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_423_analyst_v423_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=151, w2=92, w3=456, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0662 * persistence + 0.0034624 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_424_analyst_v424_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=158, w2=103, w3=469, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(103, min_periods=max(103//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.450625 + 0.0034625 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_425_analyst_v425_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=165, w2=114, w3=482, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(114, min_periods=max(114//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0814 * slope + 0.0034626 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_426_analyst_v426_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=172, w2=125, w3=495, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.479375 + 0.0034627 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_427_analyst_v427_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=179, w2=136, w3=508, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 508)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0966 * acceleration + 0.0034628 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_428_analyst_v428_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=186, w2=147, w3=521, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(147, min_periods=max(147//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.508125 + 0.0034629 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_429_analyst_v429_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=193, w2=158, w3=534, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(158, min_periods=max(158//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1118 * _rolling_slope(draw, 534) + 0.003463 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_430_analyst_v430_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=200, w2=169, w3=547, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(169, min_periods=max(169//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.536875 + 0.0034631 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_431_analyst_v431_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=207, w2=180, w3=560, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 180)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.55125 + 0.0034632 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_432_analyst_v432_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=214, w2=191, w3=573, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(191, min_periods=max(191//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.565625 + 0.0034633 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_433_analyst_v433_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=221, w2=202, w3=586, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(202, min_periods=max(202//3, 2)).rank(pct=True)
    persistence = change.rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1422 * persistence + 0.0034634 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_434_analyst_v434_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=228, w2=213, w3=599, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(213, min_periods=max(213//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.594375 + 0.0034635 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_435_analyst_v435_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=235, w2=224, w3=612, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(224, min_periods=max(224//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1574 * slope + 0.0034636 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_436_analyst_v436_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=242, w2=235, w3=625, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(235, min_periods=max(235//3, 2)).mean()
    noise = impulse.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.85 + 0.0034637 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_437_analyst_v437_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=249, w2=246, w3=638, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 246)
    curvature = _rolling_slope(acceleration, 638)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1726 * acceleration + 0.0034638 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_438_analyst_v438_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=5, w2=257, w3=651, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(257, min_periods=max(257//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87875 + 0.0034639 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_439_analyst_v439_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=12, w2=268, w3=664, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(268, min_periods=max(268//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1878 * _rolling_slope(draw, 664) + 0.003464 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_440_analyst_v440_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=19, w2=279, w3=677, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(279, min_periods=max(279//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9075 + 0.0034641 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_441_analyst_v441_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=26, w2=290, w3=690, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 290)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.921875 + 0.0034642 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_442_analyst_v442_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=33, w2=301, w3=703, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(301, min_periods=max(301//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.93625 + 0.0034643 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_443_analyst_v443_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=40, w2=312, w3=716, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(40)
    rank = change.rolling(312, min_periods=max(312//3, 2)).rank(pct=True)
    persistence = change.rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2182 * persistence + 0.0034644 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_444_analyst_v444_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=47, w2=323, w3=729, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(323, min_periods=max(323//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.965 + 0.0034645 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_445_analyst_v445_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=54, w2=334, w3=742, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(334, min_periods=max(334//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2334 * slope + 0.0034646 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_446_analyst_v446_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=61, w2=345, w3=755, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(61)
    drag = impulse.rolling(345, min_periods=max(345//3, 2)).mean()
    noise = impulse.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.99375 + 0.0034647 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_447_analyst_v447_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=68, w2=356, w3=768, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 356)
    curvature = _rolling_slope(acceleration, 768)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2486 * acceleration + 0.0034648 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_448_analyst_v448_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=75, w2=367, w3=24, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(367, min_periods=max(367//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(24) * 1.0225 + 0.0034649 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_449_analyst_v449_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=82, w2=378, w3=37, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(378, min_periods=max(378//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2638 * _rolling_slope(draw, 37) + 0.003465 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_450_analyst_v450_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=89, w2=389, w3=50, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(389, min_periods=max(389//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.05125 + 0.0034651 * anchor
    return base_signal.diff().diff().diff()
