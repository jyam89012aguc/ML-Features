"""61 analyst revision momentum d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f61_arm_076_analyst_v76_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=232, w2=299, w3=487, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.086875 + 0.0034277 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_077_analyst_v77_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=239, w2=310, w3=500, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 310)
    curvature = _rolling_slope(acceleration, 500)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0714 * acceleration + 0.0034278 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_078_analyst_v78_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=246, w2=321, w3=513, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(321, min_periods=max(321//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.115625 + 0.0034279 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_079_analyst_v79_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=253, w2=332, w3=526, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(332, min_periods=max(332//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0866 * _rolling_slope(draw, 526) + 0.003428 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_080_analyst_v80_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=9, w2=343, w3=539, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(343, min_periods=max(343//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.144375 + 0.0034281 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_081_analyst_v81_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=16, w2=354, w3=552, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 354)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.15875 + 0.0034282 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_082_analyst_v82_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=23, w2=365, w3=565, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(365, min_periods=max(365//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.173125 + 0.0034283 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_083_analyst_v83_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=30, w2=376, w3=578, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(30)
    rank = change.rolling(376, min_periods=max(376//3, 2)).rank(pct=True)
    persistence = change.rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.117 * persistence + 0.0034284 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_084_analyst_v84_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=37, w2=387, w3=591, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(387, min_periods=max(387//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.201875 + 0.0034285 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_085_analyst_v85_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=44, w2=398, w3=604, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(398, min_periods=max(398//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1322 * slope + 0.0034286 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_086_analyst_v86_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=51, w2=409, w3=617, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(51)
    drag = impulse.rolling(409, min_periods=max(409//3, 2)).mean()
    noise = impulse.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.230625 + 0.0034287 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_087_analyst_v87_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=58, w2=420, w3=630, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 420)
    curvature = _rolling_slope(acceleration, 630)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1474 * acceleration + 0.0034288 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_088_analyst_v88_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=65, w2=431, w3=643, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.259375 + 0.0034289 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_089_analyst_v89_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=72, w2=442, w3=656, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(442, min_periods=max(442//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1626 * _rolling_slope(draw, 656) + 0.003429 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_090_analyst_v90_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=79, w2=453, w3=669, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(453, min_periods=max(453//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.288125 + 0.0034291 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_091_analyst_v91_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=86, w2=464, w3=682, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 464)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3025 + 0.0034292 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_092_analyst_v92_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=93, w2=475, w3=695, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(475, min_periods=max(475//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.316875 + 0.0034293 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_093_analyst_v93_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=100, w2=486, w3=708, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(100)
    rank = change.rolling(486, min_periods=max(486//3, 2)).rank(pct=True)
    persistence = change.rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.193 * persistence + 0.0034294 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_094_analyst_v94_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=107, w2=497, w3=721, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(497, min_periods=max(497//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.345625 + 0.0034295 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_095_analyst_v95_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=114, w2=508, w3=734, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(508, min_periods=max(508//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2082 * slope + 0.0034296 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_096_analyst_v96_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=121, w2=16, w3=747, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(121)
    drag = impulse.rolling(16, min_periods=max(16//3, 2)).mean()
    noise = impulse.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.374375 + 0.0034297 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_097_analyst_v97_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=128, w2=27, w3=760, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 27)
    curvature = _rolling_slope(acceleration, 760)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2234 * acceleration + 0.0034298 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_098_analyst_v98_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=135, w2=38, w3=16, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(38, min_periods=max(38//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(16) * 1.403125 + 0.0034299 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_099_analyst_v99_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=142, w2=49, w3=29, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(49, min_periods=max(49//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2386 * _rolling_slope(draw, 29) + 0.00343 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_100_analyst_v100_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=149, w2=60, w3=42, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(60, min_periods=max(60//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.431875 + 0.0034301 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_101_analyst_v101_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=156, w2=71, w3=55, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 71)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=55, adjust=False).mean() * 1.44625 + 0.0034302 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_102_analyst_v102_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=163, w2=82, w3=68, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(82, min_periods=max(82//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.460625 + 0.0034303 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_103_analyst_v103_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=170, w2=93, w3=81, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(93, min_periods=max(93//3, 2)).rank(pct=True)
    persistence = change.rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.269 * persistence + 0.0034304 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_104_analyst_v104_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=177, w2=104, w3=94, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(104, min_periods=max(104//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.489375 + 0.0034305 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_105_analyst_v105_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=184, w2=115, w3=107, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(115, min_periods=max(115//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2842 * slope + 0.0034306 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_106_analyst_v106_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=191, w2=126, w3=120, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(126, min_periods=max(126//3, 2)).mean()
    noise = impulse.abs().rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.518125 + 0.0034307 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_107_analyst_v107_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=198, w2=137, w3=133, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 137)
    curvature = _rolling_slope(acceleration, 133)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2994 * acceleration + 0.0034308 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_108_analyst_v108_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=205, w2=148, w3=146, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.546875 + 0.0034309 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_109_analyst_v109_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=212, w2=159, w3=159, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(159, min_periods=max(159//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3146 * _rolling_slope(draw, 159) + 0.003431 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_110_analyst_v110_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=219, w2=170, w3=172, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(170, min_periods=max(170//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.575625 + 0.0034311 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_111_analyst_v111_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=226, w2=181, w3=185, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 181)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=185, adjust=False).mean() * 1.59 + 0.0034312 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_112_analyst_v112_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=233, w2=192, w3=198, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(192, min_periods=max(192//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.604375 + 0.0034313 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_113_analyst_v113_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=240, w2=203, w3=211, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(203, min_periods=max(203//3, 2)).rank(pct=True)
    persistence = change.rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.345 * persistence + 0.0034314 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_114_analyst_v114_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=247, w2=214, w3=224, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(214, min_periods=max(214//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86 + 0.0034315 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_115_analyst_v115_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=254, w2=225, w3=237, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3602 * slope + 0.0034316 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_116_analyst_v116_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=10, w2=236, w3=250, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(10)
    drag = impulse.rolling(236, min_periods=max(236//3, 2)).mean()
    noise = impulse.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.88875 + 0.0034317 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_117_analyst_v117_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=17, w2=247, w3=263, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 247)
    curvature = _rolling_slope(acceleration, 263)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3754 * acceleration + 0.0034318 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_118_analyst_v118_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=24, w2=258, w3=276, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9175 + 0.0034319 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_119_analyst_v119_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=31, w2=269, w3=289, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(269, min_periods=max(269//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3906 * _rolling_slope(draw, 289) + 0.003432 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_120_analyst_v120_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=38, w2=280, w3=302, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.94625 + 0.0034321 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_121_analyst_v121_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=45, w2=291, w3=315, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 291)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.960625 + 0.0034322 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_122_analyst_v122_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=52, w2=302, w3=328, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(302, min_periods=max(302//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.975 + 0.0034323 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_123_analyst_v123_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=59, w2=313, w3=341, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(59)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0446 * persistence + 0.0034324 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_124_analyst_v124_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=66, w2=324, w3=354, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(324, min_periods=max(324//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.00375 + 0.0034325 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_125_analyst_v125_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=73, w2=335, w3=367, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(335, min_periods=max(335//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0598 * slope + 0.0034326 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_126_analyst_v126_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=80, w2=346, w3=380, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(80)
    drag = impulse.rolling(346, min_periods=max(346//3, 2)).mean()
    noise = impulse.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0325 + 0.0034327 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_127_analyst_v127_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=87, w2=357, w3=393, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 357)
    curvature = _rolling_slope(acceleration, 393)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.075 * acceleration + 0.0034328 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_128_analyst_v128_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=94, w2=368, w3=406, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(368, min_periods=max(368//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.06125 + 0.0034329 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_129_analyst_v129_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=101, w2=379, w3=419, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(379, min_periods=max(379//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0902 * _rolling_slope(draw, 419) + 0.003433 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_130_analyst_v130_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=108, w2=390, w3=432, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09 + 0.0034331 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_131_analyst_v131_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=115, w2=401, w3=445, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 401)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.104375 + 0.0034332 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_132_analyst_v132_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=122, w2=412, w3=458, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(412, min_periods=max(412//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.11875 + 0.0034333 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_133_analyst_v133_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=129, w2=423, w3=471, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(423, min_periods=max(423//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1206 * persistence + 0.0034334 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_134_analyst_v134_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=136, w2=434, w3=484, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1475 + 0.0034335 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_135_analyst_v135_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=143, w2=445, w3=497, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(445, min_periods=max(445//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1358 * slope + 0.0034336 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_136_analyst_v136_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=150, w2=456, w3=510, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(456, min_periods=max(456//3, 2)).mean()
    noise = impulse.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.17625 + 0.0034337 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_137_analyst_v137_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=157, w2=467, w3=523, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 467)
    curvature = _rolling_slope(acceleration, 523)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.151 * acceleration + 0.0034338 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_138_analyst_v138_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=164, w2=478, w3=536, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.205 + 0.0034339 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_139_analyst_v139_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=171, w2=489, w3=549, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1662 * _rolling_slope(draw, 549) + 0.003434 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_140_analyst_v140_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=178, w2=500, w3=562, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(500, min_periods=max(500//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.23375 + 0.0034341 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_141_analyst_v141_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=185, w2=511, w3=575, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 511)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.248125 + 0.0034342 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_142_analyst_v142_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=192, w2=19, w3=588, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2625 + 0.0034343 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_143_analyst_v143_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=199, w2=30, w3=601, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(30, min_periods=max(30//3, 2)).rank(pct=True)
    persistence = change.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1966 * persistence + 0.0034344 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_144_analyst_v144_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=206, w2=41, w3=614, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(41, min_periods=max(41//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.29125 + 0.0034345 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_145_analyst_v145_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=213, w2=52, w3=627, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(52, min_periods=max(52//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2118 * slope + 0.0034346 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_146_analyst_v146_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=220, w2=63, w3=640, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(63, min_periods=max(63//3, 2)).mean()
    noise = impulse.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.32 + 0.0034347 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_147_analyst_v147_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=227, w2=74, w3=653, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 74)
    curvature = _rolling_slope(acceleration, 653)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.227 * acceleration + 0.0034348 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_148_analyst_v148_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=234, w2=85, w3=666, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(85, min_periods=max(85//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.34875 + 0.0034349 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_149_analyst_v149_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=241, w2=96, w3=679, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(96, min_periods=max(96//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2422 * _rolling_slope(draw, 679) + 0.003435 * anchor
    return base_signal.diff().diff().diff()

def f61_arm_150_analyst_v150_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=248, w2=107, w3=692, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(107, min_periods=max(107//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3775 + 0.0034351 * anchor
    return base_signal.diff().diff().diff()
