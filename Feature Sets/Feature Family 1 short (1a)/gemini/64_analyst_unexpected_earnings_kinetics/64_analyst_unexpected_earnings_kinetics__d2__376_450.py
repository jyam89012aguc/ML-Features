"""64 analyst unexpected earnings kinetics d2 second derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f64_asue_376_analyst_v376_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=123, w2=261, w3=535, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(123)
    drag = impulse.rolling(261, min_periods=max(261//3, 2)).mean()
    noise = impulse.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1225 + 0.0036377 * anchor
    return base_signal.diff().diff()

def f64_asue_377_analyst_v377_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=130, w2=272, w3=548, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 130)
    acceleration = _rolling_slope(velocity, 272)
    curvature = _rolling_slope(acceleration, 548)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2226 * acceleration + 0.0036378 * anchor
    return base_signal.diff().diff()

def f64_asue_378_analyst_v378_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=137, w2=283, w3=561, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(137, min_periods=max(137//3, 2)).mean(), upside.rolling(283, min_periods=max(283//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.15125 + 0.0036379 * anchor
    return base_signal.diff().diff()

def f64_asue_379_analyst_v379_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=144, w2=294, w3=574, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(294, min_periods=max(294//3, 2)).max()
    rebound = x - x.rolling(144, min_periods=max(144//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2378 * _rolling_slope(draw, 574) + 0.003638 * anchor
    return base_signal.diff().diff()

def f64_asue_380_analyst_v380_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=151, w2=305, w3=587, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.18 + 0.0036381 * anchor
    return base_signal.diff().diff()

def f64_asue_381_analyst_v381_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=158, w2=316, w3=600, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 316)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.194375 + 0.0036382 * anchor
    return base_signal.diff().diff()

def f64_asue_382_analyst_v382_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=165, w2=327, w3=613, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(327, min_periods=max(327//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.20875 + 0.0036383 * anchor
    return base_signal.diff().diff()

def f64_asue_383_analyst_v383_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=172, w2=338, w3=626, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(338, min_periods=max(338//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2682 * persistence + 0.0036384 * anchor
    return base_signal.diff().diff()

def f64_asue_384_analyst_v384_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=179, w2=349, w3=639, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(349, min_periods=max(349//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2375 + 0.0036385 * anchor
    return base_signal.diff().diff()

def f64_asue_385_analyst_v385_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=186, w2=360, w3=652, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(360, min_periods=max(360//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2834 * slope + 0.0036386 * anchor
    return base_signal.diff().diff()

def f64_asue_386_analyst_v386_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=193, w2=371, w3=665, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(371, min_periods=max(371//3, 2)).mean()
    noise = impulse.abs().rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.26625 + 0.0036387 * anchor
    return base_signal.diff().diff()

def f64_asue_387_analyst_v387_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=200, w2=382, w3=678, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 382)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2986 * acceleration + 0.0036388 * anchor
    return base_signal.diff().diff()

def f64_asue_388_analyst_v388_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=207, w2=393, w3=691, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(393, min_periods=max(393//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.295 + 0.0036389 * anchor
    return base_signal.diff().diff()

def f64_asue_389_analyst_v389_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=214, w2=404, w3=704, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(404, min_periods=max(404//3, 2)).max()
    rebound = x - x.rolling(214, min_periods=max(214//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3138 * _rolling_slope(draw, 704) + 0.003639 * anchor
    return base_signal.diff().diff()

def f64_asue_390_analyst_v390_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=221, w2=415, w3=717, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(415, min_periods=max(415//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.32375 + 0.0036391 * anchor
    return base_signal.diff().diff()

def f64_asue_391_analyst_v391_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=228, w2=426, w3=730, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 426)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.338125 + 0.0036392 * anchor
    return base_signal.diff().diff()

def f64_asue_392_analyst_v392_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=235, w2=437, w3=743, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(437, min_periods=max(437//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3525 + 0.0036393 * anchor
    return base_signal.diff().diff()

def f64_asue_393_analyst_v393_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=242, w2=448, w3=756, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(448, min_periods=max(448//3, 2)).rank(pct=True)
    persistence = change.rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3442 * persistence + 0.0036394 * anchor
    return base_signal.diff().diff()

def f64_asue_394_analyst_v394_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=249, w2=459, w3=769, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(459, min_periods=max(459//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38125 + 0.0036395 * anchor
    return base_signal.diff().diff()

def f64_asue_395_analyst_v395_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=5, w2=470, w3=25, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(470, min_periods=max(470//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3594 * slope + 0.0036396 * anchor
    return base_signal.diff().diff()

def f64_asue_396_analyst_v396_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=12, w2=481, w3=38, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(12)
    drag = impulse.rolling(481, min_periods=max(481//3, 2)).mean()
    noise = impulse.abs().rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41 + 0.0036397 * anchor
    return base_signal.diff().diff()

def f64_asue_397_analyst_v397_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=19, w2=492, w3=51, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 492)
    curvature = _rolling_slope(acceleration, 51)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3746 * acceleration + 0.0036398 * anchor
    return base_signal.diff().diff()

def f64_asue_398_analyst_v398_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=26, w2=503, w3=64, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(503, min_periods=max(503//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(64) * 1.43875 + 0.0036399 * anchor
    return base_signal.diff().diff()

def f64_asue_399_analyst_v399_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=33, w2=11, w3=77, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(11, min_periods=max(11//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3898 * _rolling_slope(draw, 77) + 0.00364 * anchor
    return base_signal.diff().diff()

def f64_asue_400_analyst_v400_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=40, w2=22, w3=90, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(22, min_periods=max(22//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4675 + 0.0036401 * anchor
    return base_signal.diff().diff()

def f64_asue_401_analyst_v401_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=47, w2=33, w3=103, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 33)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=103, adjust=False).mean() * 1.481875 + 0.0036402 * anchor
    return base_signal.diff().diff()

def f64_asue_402_analyst_v402_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=54, w2=44, w3=116, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(44, min_periods=max(44//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.49625 + 0.0036403 * anchor
    return base_signal.diff().diff()

def f64_asue_403_analyst_v403_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=61, w2=55, w3=129, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(61)
    rank = change.rolling(55, min_periods=max(55//3, 2)).rank(pct=True)
    persistence = change.rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0438 * persistence + 0.0036404 * anchor
    return base_signal.diff().diff()

def f64_asue_404_analyst_v404_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=68, w2=66, w3=142, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(66, min_periods=max(66//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.525 + 0.0036405 * anchor
    return base_signal.diff().diff()

def f64_asue_405_analyst_v405_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=75, w2=77, w3=155, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(77, min_periods=max(77//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.059 * slope + 0.0036406 * anchor
    return base_signal.diff().diff()

def f64_asue_406_analyst_v406_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=82, w2=88, w3=168, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(82)
    drag = impulse.rolling(88, min_periods=max(88//3, 2)).mean()
    noise = impulse.abs().rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.55375 + 0.0036407 * anchor
    return base_signal.diff().diff()

def f64_asue_407_analyst_v407_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=89, w2=99, w3=181, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 99)
    curvature = _rolling_slope(acceleration, 181)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0742 * acceleration + 0.0036408 * anchor
    return base_signal.diff().diff()

def f64_asue_408_analyst_v408_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=96, w2=110, w3=194, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5825 + 0.0036409 * anchor
    return base_signal.diff().diff()

def f64_asue_409_analyst_v409_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=103, w2=121, w3=207, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(121, min_periods=max(121//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0894 * _rolling_slope(draw, 207) + 0.003641 * anchor
    return base_signal.diff().diff()

def f64_asue_410_analyst_v410_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=110, w2=132, w3=220, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(132, min_periods=max(132//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.61125 + 0.0036411 * anchor
    return base_signal.diff().diff()

def f64_asue_411_analyst_v411_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=117, w2=143, w3=233, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 143)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=233, adjust=False).mean() * 0.8525 + 0.0036412 * anchor
    return base_signal.diff().diff()

def f64_asue_412_analyst_v412_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=124, w2=154, w3=246, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(154, min_periods=max(154//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.866875 + 0.0036413 * anchor
    return base_signal.diff().diff()

def f64_asue_413_analyst_v413_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=131, w2=165, w3=259, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1198 * persistence + 0.0036414 * anchor
    return base_signal.diff().diff()

def f64_asue_414_analyst_v414_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=138, w2=176, w3=272, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(176, min_periods=max(176//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.895625 + 0.0036415 * anchor
    return base_signal.diff().diff()

def f64_asue_415_analyst_v415_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=145, w2=187, w3=285, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.135 * slope + 0.0036416 * anchor
    return base_signal.diff().diff()

def f64_asue_416_analyst_v416_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=152, w2=198, w3=298, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(198, min_periods=max(198//3, 2)).mean()
    noise = impulse.abs().rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.924375 + 0.0036417 * anchor
    return base_signal.diff().diff()

def f64_asue_417_analyst_v417_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=159, w2=209, w3=311, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 209)
    curvature = _rolling_slope(acceleration, 311)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1502 * acceleration + 0.0036418 * anchor
    return base_signal.diff().diff()

def f64_asue_418_analyst_v418_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=166, w2=220, w3=324, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(220, min_periods=max(220//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.953125 + 0.0036419 * anchor
    return base_signal.diff().diff()

def f64_asue_419_analyst_v419_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=173, w2=231, w3=337, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(231, min_periods=max(231//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1654 * _rolling_slope(draw, 337) + 0.003642 * anchor
    return base_signal.diff().diff()

def f64_asue_420_analyst_v420_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=180, w2=242, w3=350, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(242, min_periods=max(242//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.981875 + 0.0036421 * anchor
    return base_signal.diff().diff()

def f64_asue_421_analyst_v421_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=187, w2=253, w3=363, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 253)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.99625 + 0.0036422 * anchor
    return base_signal.diff().diff()

def f64_asue_422_analyst_v422_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=194, w2=264, w3=376, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.010625 + 0.0036423 * anchor
    return base_signal.diff().diff()

def f64_asue_423_analyst_v423_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=201, w2=275, w3=389, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(275, min_periods=max(275//3, 2)).rank(pct=True)
    persistence = change.rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1958 * persistence + 0.0036424 * anchor
    return base_signal.diff().diff()

def f64_asue_424_analyst_v424_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=208, w2=286, w3=402, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(286, min_periods=max(286//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.039375 + 0.0036425 * anchor
    return base_signal.diff().diff()

def f64_asue_425_analyst_v425_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=215, w2=297, w3=415, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(297, min_periods=max(297//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.211 * slope + 0.0036426 * anchor
    return base_signal.diff().diff()

def f64_asue_426_analyst_v426_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=222, w2=308, w3=428, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(308, min_periods=max(308//3, 2)).mean()
    noise = impulse.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.068125 + 0.0036427 * anchor
    return base_signal.diff().diff()

def f64_asue_427_analyst_v427_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=229, w2=319, w3=441, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 319)
    curvature = _rolling_slope(acceleration, 441)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2262 * acceleration + 0.0036428 * anchor
    return base_signal.diff().diff()

def f64_asue_428_analyst_v428_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=236, w2=330, w3=454, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(330, min_periods=max(330//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.096875 + 0.0036429 * anchor
    return base_signal.diff().diff()

def f64_asue_429_analyst_v429_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=243, w2=341, w3=467, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(341, min_periods=max(341//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2414 * _rolling_slope(draw, 467) + 0.003643 * anchor
    return base_signal.diff().diff()

def f64_asue_430_analyst_v430_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=250, w2=352, w3=480, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(352, min_periods=max(352//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.125625 + 0.0036431 * anchor
    return base_signal.diff().diff()

def f64_asue_431_analyst_v431_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=6, w2=363, w3=493, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 363)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.14 + 0.0036432 * anchor
    return base_signal.diff().diff()

def f64_asue_432_analyst_v432_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=13, w2=374, w3=506, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(374, min_periods=max(374//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.154375 + 0.0036433 * anchor
    return base_signal.diff().diff()

def f64_asue_433_analyst_v433_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=20, w2=385, w3=519, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(20)
    rank = change.rolling(385, min_periods=max(385//3, 2)).rank(pct=True)
    persistence = change.rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2718 * persistence + 0.0036434 * anchor
    return base_signal.diff().diff()

def f64_asue_434_analyst_v434_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=27, w2=396, w3=532, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(396, min_periods=max(396//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.183125 + 0.0036435 * anchor
    return base_signal.diff().diff()

def f64_asue_435_analyst_v435_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=34, w2=407, w3=545, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(407, min_periods=max(407//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.287 * slope + 0.0036436 * anchor
    return base_signal.diff().diff()

def f64_asue_436_analyst_v436_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=41, w2=418, w3=558, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(41)
    drag = impulse.rolling(418, min_periods=max(418//3, 2)).mean()
    noise = impulse.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.211875 + 0.0036437 * anchor
    return base_signal.diff().diff()

def f64_asue_437_analyst_v437_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=48, w2=429, w3=571, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 571)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3022 * acceleration + 0.0036438 * anchor
    return base_signal.diff().diff()

def f64_asue_438_analyst_v438_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=55, w2=440, w3=584, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.240625 + 0.0036439 * anchor
    return base_signal.diff().diff()

def f64_asue_439_analyst_v439_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=62, w2=451, w3=597, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3174 * _rolling_slope(draw, 597) + 0.003644 * anchor
    return base_signal.diff().diff()

def f64_asue_440_analyst_v440_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=69, w2=462, w3=610, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.269375 + 0.0036441 * anchor
    return base_signal.diff().diff()

def f64_asue_441_analyst_v441_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=76, w2=473, w3=623, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 473)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.28375 + 0.0036442 * anchor
    return base_signal.diff().diff()

def f64_asue_442_analyst_v442_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=83, w2=484, w3=636, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(484, min_periods=max(484//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.298125 + 0.0036443 * anchor
    return base_signal.diff().diff()

def f64_asue_443_analyst_v443_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=90, w2=495, w3=649, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(90)
    rank = change.rolling(495, min_periods=max(495//3, 2)).rank(pct=True)
    persistence = change.rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3478 * persistence + 0.0036444 * anchor
    return base_signal.diff().diff()

def f64_asue_444_analyst_v444_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=97, w2=506, w3=662, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(506, min_periods=max(506//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.326875 + 0.0036445 * anchor
    return base_signal.diff().diff()

def f64_asue_445_analyst_v445_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=104, w2=14, w3=675, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(14, min_periods=max(14//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.363 * slope + 0.0036446 * anchor
    return base_signal.diff().diff()

def f64_asue_446_analyst_v446_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=111, w2=25, w3=688, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(111)
    drag = impulse.rolling(25, min_periods=max(25//3, 2)).mean()
    noise = impulse.abs().rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.355625 + 0.0036447 * anchor
    return base_signal.diff().diff()

def f64_asue_447_analyst_v447_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=118, w2=36, w3=701, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 36)
    curvature = _rolling_slope(acceleration, 701)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3782 * acceleration + 0.0036448 * anchor
    return base_signal.diff().diff()

def f64_asue_448_analyst_v448_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=125, w2=47, w3=714, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(47, min_periods=max(47//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.384375 + 0.0036449 * anchor
    return base_signal.diff().diff()

def f64_asue_449_analyst_v449_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=132, w2=58, w3=727, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(58, min_periods=max(58//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3934 * _rolling_slope(draw, 727) + 0.003645 * anchor
    return base_signal.diff().diff()

def f64_asue_450_analyst_v450_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=139, w2=69, w3=740, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(69, min_periods=max(69//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.413125 + 0.0036451 * anchor
    return base_signal.diff().diff()
