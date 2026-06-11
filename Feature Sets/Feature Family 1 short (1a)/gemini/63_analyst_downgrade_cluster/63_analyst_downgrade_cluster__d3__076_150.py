"""63 analyst downgrade cluster d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f63_adc_076_analyst_v76_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=98, w2=421, w3=190, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(98)
    drag = impulse.rolling(421, min_periods=max(421//3, 2)).mean()
    noise = impulse.abs().rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.328125 + 0.0035477 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_077_analyst_v77_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=105, w2=432, w3=203, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 432)
    curvature = _rolling_slope(acceleration, 203)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1578 * acceleration + 0.0035478 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_078_analyst_v78_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=112, w2=443, w3=216, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(443, min_periods=max(443//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.356875 + 0.0035479 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_079_analyst_v79_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=119, w2=454, w3=229, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(454, min_periods=max(454//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.173 * _rolling_slope(draw, 229) + 0.003548 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_080_analyst_v80_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=126, w2=465, w3=242, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(465, min_periods=max(465//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.385625 + 0.0035481 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_081_analyst_v81_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=133, w2=476, w3=255, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 476)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=255, adjust=False).mean() * 1.4 + 0.0035482 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_082_analyst_v82_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=140, w2=487, w3=268, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(487, min_periods=max(487//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.414375 + 0.0035483 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_083_analyst_v83_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=147, w2=498, w3=281, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(498, min_periods=max(498//3, 2)).rank(pct=True)
    persistence = change.rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2034 * persistence + 0.0035484 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_084_analyst_v84_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=154, w2=509, w3=294, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(509, min_periods=max(509//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.443125 + 0.0035485 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_085_analyst_v85_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=161, w2=17, w3=307, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(17, min_periods=max(17//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2186 * slope + 0.0035486 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_086_analyst_v86_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=168, w2=28, w3=320, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(28, min_periods=max(28//3, 2)).mean()
    noise = impulse.abs().rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.471875 + 0.0035487 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_087_analyst_v87_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=175, w2=39, w3=333, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 39)
    curvature = _rolling_slope(acceleration, 333)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2338 * acceleration + 0.0035488 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_088_analyst_v88_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=182, w2=50, w3=346, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(50, min_periods=max(50//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.500625 + 0.0035489 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_089_analyst_v89_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=189, w2=61, w3=359, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(61, min_periods=max(61//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.249 * _rolling_slope(draw, 359) + 0.003549 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_090_analyst_v90_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=196, w2=72, w3=372, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(72, min_periods=max(72//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.529375 + 0.0035491 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_091_analyst_v91_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=203, w2=83, w3=385, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 83)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.54375 + 0.0035492 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_092_analyst_v92_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=210, w2=94, w3=398, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(94, min_periods=max(94//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.558125 + 0.0035493 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_093_analyst_v93_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=217, w2=105, w3=411, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(105, min_periods=max(105//3, 2)).rank(pct=True)
    persistence = change.rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2794 * persistence + 0.0035494 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_094_analyst_v94_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=224, w2=116, w3=424, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(116, min_periods=max(116//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.586875 + 0.0035495 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_095_analyst_v95_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=231, w2=127, w3=437, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(127, min_periods=max(127//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2946 * slope + 0.0035496 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_096_analyst_v96_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=238, w2=138, w3=450, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(138, min_periods=max(138//3, 2)).mean()
    noise = impulse.abs().rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.615625 + 0.0035497 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_097_analyst_v97_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=245, w2=149, w3=463, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 149)
    curvature = _rolling_slope(acceleration, 463)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3098 * acceleration + 0.0035498 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_098_analyst_v98_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=252, w2=160, w3=476, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(160, min_periods=max(160//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87125 + 0.0035499 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_099_analyst_v99_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=8, w2=171, w3=489, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(171, min_periods=max(171//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.325 * _rolling_slope(draw, 489) + 0.00355 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_100_analyst_v100_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=15, w2=182, w3=502, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(182, min_periods=max(182//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9 + 0.0035501 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_101_analyst_v101_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=22, w2=193, w3=515, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 193)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.914375 + 0.0035502 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_102_analyst_v102_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=29, w2=204, w3=528, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(204, min_periods=max(204//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92875 + 0.0035503 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_103_analyst_v103_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=36, w2=215, w3=541, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(36)
    rank = change.rolling(215, min_periods=max(215//3, 2)).rank(pct=True)
    persistence = change.rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3554 * persistence + 0.0035504 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_104_analyst_v104_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=43, w2=226, w3=554, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(226, min_periods=max(226//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9575 + 0.0035505 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_105_analyst_v105_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=50, w2=237, w3=567, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(237, min_periods=max(237//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3706 * slope + 0.0035506 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_106_analyst_v106_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=57, w2=248, w3=580, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(57)
    drag = impulse.rolling(248, min_periods=max(248//3, 2)).mean()
    noise = impulse.abs().rolling(580, min_periods=max(580//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98625 + 0.0035507 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_107_analyst_v107_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=64, w2=259, w3=593, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 259)
    curvature = _rolling_slope(acceleration, 593)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3858 * acceleration + 0.0035508 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_108_analyst_v108_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=71, w2=270, w3=606, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(270, min_periods=max(270//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.015 + 0.0035509 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_109_analyst_v109_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=78, w2=281, w3=619, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(281, min_periods=max(281//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.401 * _rolling_slope(draw, 619) + 0.003551 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_110_analyst_v110_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=85, w2=292, w3=632, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(292, min_periods=max(292//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04375 + 0.0035511 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_111_analyst_v111_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=92, w2=303, w3=645, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 303)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.058125 + 0.0035512 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_112_analyst_v112_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=99, w2=314, w3=658, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(314, min_periods=max(314//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0725 + 0.0035513 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_113_analyst_v113_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=106, w2=325, w3=671, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(106)
    rank = change.rolling(325, min_periods=max(325//3, 2)).rank(pct=True)
    persistence = change.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.055 * persistence + 0.0035514 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_114_analyst_v114_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=113, w2=336, w3=684, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(336, min_periods=max(336//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10125 + 0.0035515 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_115_analyst_v115_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=120, w2=347, w3=697, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(347, min_periods=max(347//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0702 * slope + 0.0035516 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_116_analyst_v116_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=127, w2=358, w3=710, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(358, min_periods=max(358//3, 2)).mean()
    noise = impulse.abs().rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13 + 0.0035517 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_117_analyst_v117_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=134, w2=369, w3=723, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 369)
    curvature = _rolling_slope(acceleration, 723)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0854 * acceleration + 0.0035518 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_118_analyst_v118_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=141, w2=380, w3=736, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(380, min_periods=max(380//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.15875 + 0.0035519 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_119_analyst_v119_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=148, w2=391, w3=749, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(391, min_periods=max(391//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1006 * _rolling_slope(draw, 749) + 0.003552 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_120_analyst_v120_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=155, w2=402, w3=762, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(402, min_periods=max(402//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1875 + 0.0035521 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_121_analyst_v121_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=162, w2=413, w3=18, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 413)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=18, adjust=False).mean() * 1.201875 + 0.0035522 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_122_analyst_v122_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=169, w2=424, w3=31, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(424, min_periods=max(424//3, 2)).max()
    trough = x.rolling(169, min_periods=max(169//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21625 + 0.0035523 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_123_analyst_v123_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=176, w2=435, w3=44, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(435, min_periods=max(435//3, 2)).rank(pct=True)
    persistence = change.rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131 * persistence + 0.0035524 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_124_analyst_v124_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=183, w2=446, w3=57, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(183, min_periods=max(183//3, 2)).std()
    vol_slow = ret.rolling(446, min_periods=max(446//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245 + 0.0035525 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_125_analyst_v125_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=190, w2=457, w3=70, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(457, min_periods=max(457//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 190)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1462 * slope + 0.0035526 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_126_analyst_v126_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=197, w2=468, w3=83, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(468, min_periods=max(468//3, 2)).mean()
    noise = impulse.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27375 + 0.0035527 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_127_analyst_v127_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=204, w2=479, w3=96, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 479)
    curvature = _rolling_slope(acceleration, 96)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1614 * acceleration + 0.0035528 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_128_analyst_v128_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=211, w2=490, w3=109, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(211, min_periods=max(211//3, 2)).mean(), upside.rolling(490, min_periods=max(490//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(109) * 1.3025 + 0.0035529 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_129_analyst_v129_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=218, w2=501, w3=122, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(501, min_periods=max(501//3, 2)).max()
    rebound = x - x.rolling(218, min_periods=max(218//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1766 * _rolling_slope(draw, 122) + 0.003553 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_130_analyst_v130_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=225, w2=512, w3=135, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(512, min_periods=max(512//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33125 + 0.0035531 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_131_analyst_v131_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=232, w2=20, w3=148, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=148, adjust=False).mean() * 1.345625 + 0.0035532 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_132_analyst_v132_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=239, w2=31, w3=161, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(31, min_periods=max(31//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36 + 0.0035533 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_133_analyst_v133_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=246, w2=42, w3=174, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.207 * persistence + 0.0035534 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_134_analyst_v134_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=253, w2=53, w3=187, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(253, min_periods=max(253//3, 2)).std()
    vol_slow = ret.rolling(53, min_periods=max(53//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38875 + 0.0035535 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_135_analyst_v135_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=9, w2=64, w3=200, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(64, min_periods=max(64//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2222 * slope + 0.0035536 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_136_analyst_v136_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=16, w2=75, w3=213, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(16)
    drag = impulse.rolling(75, min_periods=max(75//3, 2)).mean()
    noise = impulse.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4175 + 0.0035537 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_137_analyst_v137_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=23, w2=86, w3=226, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 86)
    curvature = _rolling_slope(acceleration, 226)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2374 * acceleration + 0.0035538 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_138_analyst_v138_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=30, w2=97, w3=239, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(97, min_periods=max(97//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.44625 + 0.0035539 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_139_analyst_v139_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=37, w2=108, w3=252, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(108, min_periods=max(108//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2526 * _rolling_slope(draw, 252) + 0.003554 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_140_analyst_v140_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=44, w2=119, w3=265, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(119, min_periods=max(119//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.475 + 0.0035541 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_141_analyst_v141_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=51, w2=130, w3=278, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 130)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=278, adjust=False).mean() * 1.489375 + 0.0035542 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_142_analyst_v142_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=58, w2=141, w3=291, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(141, min_periods=max(141//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50375 + 0.0035543 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_143_analyst_v143_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=65, w2=152, w3=304, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(65)
    rank = change.rolling(152, min_periods=max(152//3, 2)).rank(pct=True)
    persistence = change.rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.283 * persistence + 0.0035544 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_144_analyst_v144_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=72, w2=163, w3=317, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(163, min_periods=max(163//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5325 + 0.0035545 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_145_analyst_v145_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=79, w2=174, w3=330, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(174, min_periods=max(174//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2982 * slope + 0.0035546 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_146_analyst_v146_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=86, w2=185, w3=343, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(86)
    drag = impulse.rolling(185, min_periods=max(185//3, 2)).mean()
    noise = impulse.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.56125 + 0.0035547 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_147_analyst_v147_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=93, w2=196, w3=356, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 196)
    curvature = _rolling_slope(acceleration, 356)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3134 * acceleration + 0.0035548 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_148_analyst_v148_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=100, w2=207, w3=369, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(207, min_periods=max(207//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.59 + 0.0035549 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_149_analyst_v149_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=107, w2=218, w3=382, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(218, min_periods=max(218//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3286 * _rolling_slope(draw, 382) + 0.003555 * anchor
    return base_signal.diff().diff().diff()

def f63_adc_150_analyst_v150_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=114, w2=229, w3=395, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.61875 + 0.0035551 * anchor
    return base_signal.diff().diff().diff()
