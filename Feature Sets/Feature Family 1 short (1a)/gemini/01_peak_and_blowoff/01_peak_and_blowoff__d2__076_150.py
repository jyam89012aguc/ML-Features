"""01 peak and blowoff d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics - Institutional-grade short-side signal.
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

def f01_pab_076_accel_v76_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=35, w2=343, w3=246, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(35)
    drag = impulse.rolling(343, min_periods=max(343//3, 2)).mean()
    noise = impulse.abs().rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.169375 + 7.7e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_077_jerk_v77_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=42, w2=354, w3=259, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 354)
    curvature = _rolling_slope(acceleration, 259)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2438 * acceleration + 7.8e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_078_accel_v78_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=49, w2=365, w3=272, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.198125 + 7.9e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_079_jerk_v79_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=56, w2=376, w3=285, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.259 * _rolling_slope(draw, 285) + 8e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_080_accel_v80_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=63, w2=387, w3=298, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(387, min_periods=max(387//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.226875 + 8.1e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_081_jerk_v81_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=70, w2=398, w3=311, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 398)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.24125 + 8.2e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_082_accel_v82_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=77, w2=409, w3=324, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(409, min_periods=max(409//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.255625 + 8.3e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_083_jerk_v83_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=84, w2=420, w3=337, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(84)
    rank = change.rolling(420, min_periods=max(420//3, 2)).rank(pct=True)
    persistence = change.rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2894 * persistence + 8.4e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_084_accel_v84_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=91, w2=431, w3=350, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(431, min_periods=max(431//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.284375 + 8.5e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_085_jerk_v85_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=98, w2=442, w3=363, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(442, min_periods=max(442//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3046 * slope + 8.6e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_086_accel_v86_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=105, w2=453, w3=376, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(105)
    drag = impulse.rolling(453, min_periods=max(453//3, 2)).mean()
    noise = impulse.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.313125 + 8.7e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_087_jerk_v87_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=112, w2=464, w3=389, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 389)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3198 * acceleration + 8.8e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_088_accel_v88_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=119, w2=475, w3=402, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(475, min_periods=max(475//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.341875 + 8.9e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_089_jerk_v89_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=126, w2=486, w3=415, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.335 * _rolling_slope(draw, 415) + 9e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_090_accel_v90_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=133, w2=497, w3=428, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(497, min_periods=max(497//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.370625 + 9.1e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_091_jerk_v91_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=140, w2=508, w3=441, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 508)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.385 + 9.2e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_092_accel_v92_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=147, w2=16, w3=454, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.399375 + 9.3e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_093_jerk_v93_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=154, w2=27, w3=467, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3654 * persistence + 9.4e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_094_accel_v94_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=161, w2=38, w3=480, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(38, min_periods=max(38//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.428125 + 9.5e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_095_jerk_v95_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=168, w2=49, w3=493, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3806 * slope + 9.6e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_096_accel_v96_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=175, w2=60, w3=506, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.456875 + 9.7e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_097_jerk_v97_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=182, w2=71, w3=519, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 519)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3958 * acceleration + 9.8e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_098_accel_v98_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=189, w2=82, w3=532, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.485625 + 9.9e-06 * anchor
    return base_signal.diff().diff()

def f01_pab_099_jerk_v99_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=196, w2=93, w3=545, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(93, min_periods=max(93//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.411 * _rolling_slope(draw, 545) + 1e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_100_accel_v100_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=203, w2=104, w3=558, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.514375 + 1.01e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_101_jerk_v101_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=210, w2=115, w3=571, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 115)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.52875 + 1.02e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_102_accel_v102_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=217, w2=126, w3=584, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(126, min_periods=max(126//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.543125 + 1.03e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_103_jerk_v103_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=224, w2=137, w3=597, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(137, min_periods=max(137//3, 2)).rank(pct=True)
    persistence = change.rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.065 * persistence + 1.04e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_104_accel_v104_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=231, w2=148, w3=610, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.571875 + 1.05e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_105_jerk_v105_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=238, w2=159, w3=623, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(159, min_periods=max(159//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0802 * slope + 1.06e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_106_accel_v106_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=245, w2=170, w3=636, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(170, min_periods=max(170//3, 2)).mean()
    noise = impulse.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.600625 + 1.07e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_107_jerk_v107_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=252, w2=181, w3=649, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 252)
    acceleration = _rolling_slope(velocity, 181)
    curvature = _rolling_slope(acceleration, 649)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0954 * acceleration + 1.08e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_108_accel_v108_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=8, w2=192, w3=662, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.85625 + 1.09e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_109_jerk_v109_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=15, w2=203, w3=675, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(203, min_periods=max(203//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1106 * _rolling_slope(draw, 675) + 1.1e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_110_accel_v110_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=22, w2=214, w3=688, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.885 + 1.11e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_111_jerk_v111_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=29, w2=225, w3=701, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.899375 + 1.12e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_112_accel_v112_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=36, w2=236, w3=714, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.91375 + 1.13e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_113_jerk_v113_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=43, w2=247, w3=727, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(43)
    rank = change.rolling(247, min_periods=max(247//3, 2)).rank(pct=True)
    persistence = change.rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.141 * persistence + 1.14e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_114_accel_v114_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=50, w2=258, w3=740, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9425 + 1.15e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_115_jerk_v115_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=57, w2=269, w3=753, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(269, min_periods=max(269//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1562 * slope + 1.16e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_116_accel_v116_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=64, w2=280, w3=766, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(64)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.97125 + 1.17e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_117_jerk_v117_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=71, w2=291, w3=22, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 291)
    curvature = _rolling_slope(acceleration, 22)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1714 * acceleration + 1.18e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_118_accel_v118_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=78, w2=302, w3=35, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(35) * 1.0 + 1.19e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_119_jerk_v119_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=85, w2=313, w3=48, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1866 * _rolling_slope(draw, 48) + 1.2e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_120_accel_v120_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=92, w2=324, w3=61, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(324, min_periods=max(324//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.02875 + 1.21e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_121_jerk_v121_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=99, w2=335, w3=74, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 335)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=74, adjust=False).mean() * 1.043125 + 1.22e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_122_accel_v122_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=106, w2=346, w3=87, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(346, min_periods=max(346//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0575 + 1.23e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_123_jerk_v123_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=113, w2=357, w3=100, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(113)
    rank = change.rolling(357, min_periods=max(357//3, 2)).rank(pct=True)
    persistence = change.rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217 * persistence + 1.24e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_124_accel_v124_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=120, w2=368, w3=113, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(368, min_periods=max(368//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.08625 + 1.25e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_125_jerk_v125_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=127, w2=379, w3=126, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(379, min_periods=max(379//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2322 * slope + 1.26e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_126_accel_v126_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=134, w2=390, w3=139, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(390, min_periods=max(390//3, 2)).mean()
    noise = impulse.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.115 + 1.27e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_127_jerk_v127_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=141, w2=401, w3=152, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 401)
    curvature = _rolling_slope(acceleration, 152)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2474 * acceleration + 1.28e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_128_accel_v128_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=148, w2=412, w3=165, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.14375 + 1.29e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_129_jerk_v129_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=155, w2=423, w3=178, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2626 * _rolling_slope(draw, 178) + 1.3e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_130_accel_v130_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=162, w2=434, w3=191, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(434, min_periods=max(434//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1725 + 1.31e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_131_jerk_v131_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=169, w2=445, w3=204, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 445)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=204, adjust=False).mean() * 1.186875 + 1.32e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_132_accel_v132_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=176, w2=456, w3=217, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(456, min_periods=max(456//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.20125 + 1.33e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_133_jerk_v133_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=183, w2=467, w3=230, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(467, min_periods=max(467//3, 2)).rank(pct=True)
    persistence = change.rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.293 * persistence + 1.34e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_134_accel_v134_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=190, w2=478, w3=243, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(478, min_periods=max(478//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.23 + 1.35e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_135_jerk_v135_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=197, w2=489, w3=256, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(489, min_periods=max(489//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3082 * slope + 1.36e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_136_accel_v136_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=204, w2=500, w3=269, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(500, min_periods=max(500//3, 2)).mean()
    noise = impulse.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.25875 + 1.37e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_137_jerk_v137_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=211, w2=511, w3=282, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 511)
    curvature = _rolling_slope(acceleration, 282)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3234 * acceleration + 1.38e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_138_accel_v138_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=218, w2=19, w3=295, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2875 + 1.39e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_139_jerk_v139_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=225, w2=30, w3=308, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(30, min_periods=max(30//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3386 * _rolling_slope(draw, 308) + 1.4e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_140_accel_v140_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=232, w2=41, w3=321, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(41, min_periods=max(41//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.31625 + 1.41e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_141_jerk_v141_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=239, w2=52, w3=334, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 52)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.330625 + 1.42e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_142_accel_v142_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=246, w2=63, w3=347, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(63, min_periods=max(63//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.345 + 1.43e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_143_jerk_v143_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=253, w2=74, w3=360, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(74, min_periods=max(74//3, 2)).rank(pct=True)
    persistence = change.rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.369 * persistence + 1.44e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_144_accel_v144_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=9, w2=85, w3=373, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(85, min_periods=max(85//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37375 + 1.45e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_145_jerk_v145_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=16, w2=96, w3=386, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(96, min_periods=max(96//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3842 * slope + 1.46e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_146_accel_v146_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=23, w2=107, w3=399, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(23)
    drag = impulse.rolling(107, min_periods=max(107//3, 2)).mean()
    noise = impulse.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4025 + 1.47e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_147_jerk_v147_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=30, w2=118, w3=412, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 118)
    curvature = _rolling_slope(acceleration, 412)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3994 * acceleration + 1.48e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_148_accel_v148_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=37, w2=129, w3=425, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(37, min_periods=max(37//3, 2)).mean(), upside.rolling(129, min_periods=max(129//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.43125 + 1.49e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_149_jerk_v149_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=44, w2=140, w3=438, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(140, min_periods=max(140//3, 2)).max()
    rebound = x - x.rolling(44, min_periods=max(44//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0382 * _rolling_slope(draw, 438) + 1.5e-05 * anchor
    return base_signal.diff().diff()

def f01_pab_150_accel_v150_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=51, w2=151, w3=451, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(151, min_periods=max(151//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46 + 1.51e-05 * anchor
    return base_signal.diff().diff()
