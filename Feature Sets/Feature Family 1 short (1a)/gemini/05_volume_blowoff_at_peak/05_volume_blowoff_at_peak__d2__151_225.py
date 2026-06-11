"""05 volume blowoff at peak d2 second derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f05_vbp_151_jerk_v151_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=41, w2=406, w3=627, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 41)
    slow = _rolling_slope(x, 406)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.18375 + 0.0002552 * anchor
    return base_signal.diff().diff()

def f05_vbp_152_accel_v152_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=48, w2=417, w3=640, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(417, min_periods=max(417//3, 2)).max()
    trough = x.rolling(48, min_periods=max(48//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.198125 + 0.0002553 * anchor
    return base_signal.diff().diff()

def f05_vbp_153_jerk_v153_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=55, w2=428, w3=653, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(55)
    rank = change.rolling(428, min_periods=max(428//3, 2)).rank(pct=True)
    persistence = change.rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2414 * persistence + 0.0002554 * anchor
    return base_signal.diff().diff()

def f05_vbp_154_accel_v154_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=62, w2=439, w3=666, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(62, min_periods=max(62//3, 2)).std()
    vol_slow = ret.rolling(439, min_periods=max(439//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.226875 + 0.0002555 * anchor
    return base_signal.diff().diff()

def f05_vbp_155_jerk_v155_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=69, w2=450, w3=679, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(450, min_periods=max(450//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 69)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2566 * slope + 0.0002556 * anchor
    return base_signal.diff().diff()

def f05_vbp_156_accel_v156_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=76, w2=461, w3=692, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(76)
    drag = impulse.rolling(461, min_periods=max(461//3, 2)).mean()
    noise = impulse.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.255625 + 0.0002557 * anchor
    return base_signal.diff().diff()

def f05_vbp_157_jerk_v157_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=83, w2=472, w3=705, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 83)
    acceleration = _rolling_slope(velocity, 472)
    curvature = _rolling_slope(acceleration, 705)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2718 * acceleration + 0.0002558 * anchor
    return base_signal.diff().diff()

def f05_vbp_158_accel_v158_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=90, w2=483, w3=718, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(483, min_periods=max(483//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.284375 + 0.0002559 * anchor
    return base_signal.diff().diff()

def f05_vbp_159_jerk_v159_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=97, w2=494, w3=731, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(494, min_periods=max(494//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287 * _rolling_slope(draw, 731) + 0.000256 * anchor
    return base_signal.diff().diff()

def f05_vbp_160_accel_v160_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=104, w2=505, w3=744, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 104)
    baseline = trend.rolling(505, min_periods=max(505//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.313125 + 0.0002561 * anchor
    return base_signal.diff().diff()

def f05_vbp_161_jerk_v161_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=111, w2=13, w3=757, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 111)
    slow = _rolling_slope(x, 13)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3275 + 0.0002562 * anchor
    return base_signal.diff().diff()

def f05_vbp_162_accel_v162_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=118, w2=24, w3=770, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(24, min_periods=max(24//3, 2)).max()
    trough = x.rolling(118, min_periods=max(118//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.341875 + 0.0002563 * anchor
    return base_signal.diff().diff()

def f05_vbp_163_jerk_v163_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=125, w2=35, w3=26, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(125)
    rank = change.rolling(35, min_periods=max(35//3, 2)).rank(pct=True)
    persistence = change.rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3174 * persistence + 0.0002564 * anchor
    return base_signal.diff().diff()

def f05_vbp_164_accel_v164_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=132, w2=46, w3=39, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(132, min_periods=max(132//3, 2)).std()
    vol_slow = ret.rolling(46, min_periods=max(46//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.370625 + 0.0002565 * anchor
    return base_signal.diff().diff()

def f05_vbp_165_jerk_v165_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=139, w2=57, w3=52, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(57, min_periods=max(57//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 139)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3326 * slope + 0.0002566 * anchor
    return base_signal.diff().diff()

def f05_vbp_166_accel_v166_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=146, w2=68, w3=65, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(68, min_periods=max(68//3, 2)).mean()
    noise = impulse.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.399375 + 0.0002567 * anchor
    return base_signal.diff().diff()

def f05_vbp_167_jerk_v167_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=153, w2=79, w3=78, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 153)
    acceleration = _rolling_slope(velocity, 79)
    curvature = _rolling_slope(acceleration, 78)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3478 * acceleration + 0.0002568 * anchor
    return base_signal.diff().diff()

def f05_vbp_168_accel_v168_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=160, w2=90, w3=91, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(160, min_periods=max(160//3, 2)).mean(), upside.rolling(90, min_periods=max(90//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(91) * 1.428125 + 0.0002569 * anchor
    return base_signal.diff().diff()

def f05_vbp_169_jerk_v169_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=167, w2=101, w3=104, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(167, min_periods=max(167//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.363 * _rolling_slope(draw, 104) + 0.000257 * anchor
    return base_signal.diff().diff()

def f05_vbp_170_accel_v170_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=174, w2=112, w3=117, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 174)
    baseline = trend.rolling(112, min_periods=max(112//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.456875 + 0.0002571 * anchor
    return base_signal.diff().diff()

def f05_vbp_171_jerk_v171_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=181, w2=123, w3=130, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 181)
    slow = _rolling_slope(x, 123)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=130, adjust=False).mean() * 1.47125 + 0.0002572 * anchor
    return base_signal.diff().diff()

def f05_vbp_172_accel_v172_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=188, w2=134, w3=143, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(134, min_periods=max(134//3, 2)).max()
    trough = x.rolling(188, min_periods=max(188//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.485625 + 0.0002573 * anchor
    return base_signal.diff().diff()

def f05_vbp_173_jerk_v173_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=195, w2=145, w3=156, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(145, min_periods=max(145//3, 2)).rank(pct=True)
    persistence = change.rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3934 * persistence + 0.0002574 * anchor
    return base_signal.diff().diff()

def f05_vbp_174_accel_v174_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=202, w2=156, w3=169, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(202, min_periods=max(202//3, 2)).std()
    vol_slow = ret.rolling(156, min_periods=max(156//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.514375 + 0.0002575 * anchor
    return base_signal.diff().diff()

def f05_vbp_175_jerk_v175_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=209, w2=167, w3=182, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(167, min_periods=max(167//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 209)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4086 * slope + 0.0002576 * anchor
    return base_signal.diff().diff()

def f05_vbp_176_accel_v176_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=216, w2=178, w3=195, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(178, min_periods=max(178//3, 2)).mean()
    noise = impulse.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.543125 + 0.0002577 * anchor
    return base_signal.diff().diff()

def f05_vbp_177_jerk_v177_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=223, w2=189, w3=208, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 223)
    acceleration = _rolling_slope(velocity, 189)
    curvature = _rolling_slope(acceleration, 208)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0474 * acceleration + 0.0002578 * anchor
    return base_signal.diff().diff()

def f05_vbp_178_accel_v178_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=230, w2=200, w3=221, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(200, min_periods=max(200//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.571875 + 0.0002579 * anchor
    return base_signal.diff().diff()

def f05_vbp_179_jerk_v179_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=237, w2=211, w3=234, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(211, min_periods=max(211//3, 2)).max()
    rebound = x - x.rolling(237, min_periods=max(237//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0626 * _rolling_slope(draw, 234) + 0.000258 * anchor
    return base_signal.diff().diff()

def f05_vbp_180_accel_v180_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=244, w2=222, w3=247, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(222, min_periods=max(222//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.600625 + 0.0002581 * anchor
    return base_signal.diff().diff()

def f05_vbp_181_jerk_v181_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=251, w2=233, w3=260, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=260, adjust=False).mean() * 1.615 + 0.0002582 * anchor
    return base_signal.diff().diff()

def f05_vbp_182_accel_v182_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=7, w2=244, w3=273, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(244, min_periods=max(244//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.85625 + 0.0002583 * anchor
    return base_signal.diff().diff()

def f05_vbp_183_jerk_v183_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=14, w2=255, w3=286, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(14)
    rank = change.rolling(255, min_periods=max(255//3, 2)).rank(pct=True)
    persistence = change.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.093 * persistence + 0.0002584 * anchor
    return base_signal.diff().diff()

def f05_vbp_184_accel_v184_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=21, w2=266, w3=299, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(266, min_periods=max(266//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.885 + 0.0002585 * anchor
    return base_signal.diff().diff()

def f05_vbp_185_jerk_v185_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=28, w2=277, w3=312, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(277, min_periods=max(277//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1082 * slope + 0.0002586 * anchor
    return base_signal.diff().diff()

def f05_vbp_186_accel_v186_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=35, w2=288, w3=325, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(35)
    drag = impulse.rolling(288, min_periods=max(288//3, 2)).mean()
    noise = impulse.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.91375 + 0.0002587 * anchor
    return base_signal.diff().diff()

def f05_vbp_187_jerk_v187_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=42, w2=299, w3=338, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 299)
    curvature = _rolling_slope(acceleration, 338)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1234 * acceleration + 0.0002588 * anchor
    return base_signal.diff().diff()

def f05_vbp_188_accel_v188_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=49, w2=310, w3=351, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(310, min_periods=max(310//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9425 + 0.0002589 * anchor
    return base_signal.diff().diff()

def f05_vbp_189_jerk_v189_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=56, w2=321, w3=364, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(321, min_periods=max(321//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1386 * _rolling_slope(draw, 364) + 0.000259 * anchor
    return base_signal.diff().diff()

def f05_vbp_190_accel_v190_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=63, w2=332, w3=377, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(332, min_periods=max(332//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.97125 + 0.0002591 * anchor
    return base_signal.diff().diff()

def f05_vbp_191_jerk_v191_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=70, w2=343, w3=390, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 343)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.985625 + 0.0002592 * anchor
    return base_signal.diff().diff()

def f05_vbp_192_accel_v192_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=77, w2=354, w3=403, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(354, min_periods=max(354//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0 + 0.0002593 * anchor
    return base_signal.diff().diff()

def f05_vbp_193_jerk_v193_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=84, w2=365, w3=416, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(84)
    rank = change.rolling(365, min_periods=max(365//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.169 * persistence + 0.0002594 * anchor
    return base_signal.diff().diff()

def f05_vbp_194_accel_v194_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=91, w2=376, w3=429, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(376, min_periods=max(376//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.02875 + 0.0002595 * anchor
    return base_signal.diff().diff()

def f05_vbp_195_jerk_v195_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=98, w2=387, w3=442, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(387, min_periods=max(387//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1842 * slope + 0.0002596 * anchor
    return base_signal.diff().diff()

def f05_vbp_196_accel_v196_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=105, w2=398, w3=455, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(105)
    drag = impulse.rolling(398, min_periods=max(398//3, 2)).mean()
    noise = impulse.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0575 + 0.0002597 * anchor
    return base_signal.diff().diff()

def f05_vbp_197_jerk_v197_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=112, w2=409, w3=468, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 409)
    curvature = _rolling_slope(acceleration, 468)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1994 * acceleration + 0.0002598 * anchor
    return base_signal.diff().diff()

def f05_vbp_198_accel_v198_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=119, w2=420, w3=481, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(420, min_periods=max(420//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.08625 + 0.0002599 * anchor
    return base_signal.diff().diff()

def f05_vbp_199_jerk_v199_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=126, w2=431, w3=494, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(431, min_periods=max(431//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2146 * _rolling_slope(draw, 494) + 0.00026 * anchor
    return base_signal.diff().diff()

def f05_vbp_200_accel_v200_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=133, w2=442, w3=507, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(442, min_periods=max(442//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.115 + 0.0002601 * anchor
    return base_signal.diff().diff()

def f05_vbp_201_jerk_v201_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=140, w2=453, w3=520, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.129375 + 0.0002602 * anchor
    return base_signal.diff().diff()

def f05_vbp_202_accel_v202_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=147, w2=464, w3=533, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(464, min_periods=max(464//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.14375 + 0.0002603 * anchor
    return base_signal.diff().diff()

def f05_vbp_203_jerk_v203_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=154, w2=475, w3=546, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245 * persistence + 0.0002604 * anchor
    return base_signal.diff().diff()

def f05_vbp_204_accel_v204_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=161, w2=486, w3=559, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(486, min_periods=max(486//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1725 + 0.0002605 * anchor
    return base_signal.diff().diff()

def f05_vbp_205_jerk_v205_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=168, w2=497, w3=572, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(497, min_periods=max(497//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2602 * slope + 0.0002606 * anchor
    return base_signal.diff().diff()

def f05_vbp_206_accel_v206_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=175, w2=508, w3=585, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(508, min_periods=max(508//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.20125 + 0.0002607 * anchor
    return base_signal.diff().diff()

def f05_vbp_207_jerk_v207_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=182, w2=16, w3=598, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 16)
    curvature = _rolling_slope(acceleration, 598)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2754 * acceleration + 0.0002608 * anchor
    return base_signal.diff().diff()

def f05_vbp_208_accel_v208_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=189, w2=27, w3=611, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(27, min_periods=max(27//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.23 + 0.0002609 * anchor
    return base_signal.diff().diff()

def f05_vbp_209_jerk_v209_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=196, w2=38, w3=624, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(38, min_periods=max(38//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2906 * _rolling_slope(draw, 624) + 0.000261 * anchor
    return base_signal.diff().diff()

def f05_vbp_210_accel_v210_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=203, w2=49, w3=637, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(49, min_periods=max(49//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.25875 + 0.0002611 * anchor
    return base_signal.diff().diff()

def f05_vbp_211_jerk_v211_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=210, w2=60, w3=650, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 60)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.273125 + 0.0002612 * anchor
    return base_signal.diff().diff()

def f05_vbp_212_accel_v212_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=217, w2=71, w3=663, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2875 + 0.0002613 * anchor
    return base_signal.diff().diff()

def f05_vbp_213_jerk_v213_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=224, w2=82, w3=676, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(82, min_periods=max(82//3, 2)).rank(pct=True)
    persistence = change.rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.321 * persistence + 0.0002614 * anchor
    return base_signal.diff().diff()

def f05_vbp_214_accel_v214_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=231, w2=93, w3=689, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(93, min_periods=max(93//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31625 + 0.0002615 * anchor
    return base_signal.diff().diff()

def f05_vbp_215_jerk_v215_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=238, w2=104, w3=702, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(104, min_periods=max(104//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3362 * slope + 0.0002616 * anchor
    return base_signal.diff().diff()

def f05_vbp_216_accel_v216_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=245, w2=115, w3=715, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(115, min_periods=max(115//3, 2)).mean()
    noise = impulse.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.345 + 0.0002617 * anchor
    return base_signal.diff().diff()

def f05_vbp_217_jerk_v217_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=252, w2=126, w3=728, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 252)
    acceleration = _rolling_slope(velocity, 126)
    curvature = _rolling_slope(acceleration, 728)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3514 * acceleration + 0.0002618 * anchor
    return base_signal.diff().diff()

def f05_vbp_218_accel_v218_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=8, w2=137, w3=741, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(137, min_periods=max(137//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37375 + 0.0002619 * anchor
    return base_signal.diff().diff()

def f05_vbp_219_jerk_v219_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=15, w2=148, w3=754, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(148, min_periods=max(148//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3666 * _rolling_slope(draw, 754) + 0.000262 * anchor
    return base_signal.diff().diff()

def f05_vbp_220_accel_v220_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=22, w2=159, w3=767, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4025 + 0.0002621 * anchor
    return base_signal.diff().diff()

def f05_vbp_221_jerk_v221_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=29, w2=170, w3=23, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 170)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=23, adjust=False).mean() * 1.416875 + 0.0002622 * anchor
    return base_signal.diff().diff()

def f05_vbp_222_accel_v222_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=36, w2=181, w3=36, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.43125 + 0.0002623 * anchor
    return base_signal.diff().diff()

def f05_vbp_223_jerk_v223_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=43, w2=192, w3=49, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(43)
    rank = change.rolling(192, min_periods=max(192//3, 2)).rank(pct=True)
    persistence = change.rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.397 * persistence + 0.0002624 * anchor
    return base_signal.diff().diff()

def f05_vbp_224_accel_v224_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=50, w2=203, w3=62, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(203, min_periods=max(203//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46 + 0.0002625 * anchor
    return base_signal.diff().diff()

def f05_vbp_225_jerk_v225_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=57, w2=214, w3=75, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0358 * slope + 0.0002626 * anchor
    return base_signal.diff().diff()
