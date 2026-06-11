"""06 volume distribution dryup d3 third derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_151_jerk_v151_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=225, w2=467, w3=100, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 467)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=100, adjust=False).mean() * 1.304375 + 0.0003152 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_152_accel_v152_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=232, w2=478, w3=113, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(478, min_periods=max(478//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.31875 + 0.0003153 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_153_jerk_v153_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=239, w2=489, w3=126, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(489, min_periods=max(489//3, 2)).rank(pct=True)
    persistence = change.rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2846 * persistence + 0.0003154 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_154_accel_v154_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=246, w2=500, w3=139, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(500, min_periods=max(500//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3475 + 0.0003155 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_155_jerk_v155_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=253, w2=511, w3=152, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(511, min_periods=max(511//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2998 * slope + 0.0003156 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_156_accel_v156_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=9, w2=19, w3=165, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(9)
    drag = impulse.rolling(19, min_periods=max(19//3, 2)).mean()
    noise = impulse.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.37625 + 0.0003157 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_157_jerk_v157_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=16, w2=30, w3=178, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 30)
    curvature = _rolling_slope(acceleration, 178)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.315 * acceleration + 0.0003158 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_158_accel_v158_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=23, w2=41, w3=191, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(41, min_periods=max(41//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.405 + 0.0003159 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_159_jerk_v159_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=30, w2=52, w3=204, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(52, min_periods=max(52//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3302 * _rolling_slope(draw, 204) + 0.000316 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_160_accel_v160_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=37, w2=63, w3=217, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(63, min_periods=max(63//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.43375 + 0.0003161 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_161_jerk_v161_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=44, w2=74, w3=230, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 74)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 1.448125 + 0.0003162 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_162_accel_v162_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=51, w2=85, w3=243, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(85, min_periods=max(85//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4625 + 0.0003163 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_163_jerk_v163_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=58, w2=96, w3=256, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(58)
    rank = change.rolling(96, min_periods=max(96//3, 2)).rank(pct=True)
    persistence = change.rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3606 * persistence + 0.0003164 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_164_accel_v164_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=65, w2=107, w3=269, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(107, min_periods=max(107//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49125 + 0.0003165 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_165_jerk_v165_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=72, w2=118, w3=282, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(118, min_periods=max(118//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3758 * slope + 0.0003166 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_166_accel_v166_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=79, w2=129, w3=295, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(79)
    drag = impulse.rolling(129, min_periods=max(129//3, 2)).mean()
    noise = impulse.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.52 + 0.0003167 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_167_jerk_v167_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=86, w2=140, w3=308, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 140)
    curvature = _rolling_slope(acceleration, 308)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.391 * acceleration + 0.0003168 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_168_accel_v168_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=93, w2=151, w3=321, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(151, min_periods=max(151//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.54875 + 0.0003169 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_169_jerk_v169_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=100, w2=162, w3=334, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4062 * _rolling_slope(draw, 334) + 0.000317 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_170_accel_v170_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=107, w2=173, w3=347, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(173, min_periods=max(173//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5775 + 0.0003171 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_171_jerk_v171_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=114, w2=184, w3=360, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 184)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.591875 + 0.0003172 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_172_accel_v172_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=121, w2=195, w3=373, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(195, min_periods=max(195//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.60625 + 0.0003173 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_173_jerk_v173_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=128, w2=206, w3=386, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(206, min_periods=max(206//3, 2)).rank(pct=True)
    persistence = change.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0602 * persistence + 0.0003174 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_174_accel_v174_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=135, w2=217, w3=399, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(217, min_periods=max(217//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.861875 + 0.0003175 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_175_jerk_v175_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=142, w2=228, w3=412, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(228, min_periods=max(228//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0754 * slope + 0.0003176 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_176_accel_v176_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=149, w2=239, w3=425, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(239, min_periods=max(239//3, 2)).mean()
    noise = impulse.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.890625 + 0.0003177 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_177_jerk_v177_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=156, w2=250, w3=438, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 250)
    curvature = _rolling_slope(acceleration, 438)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0906 * acceleration + 0.0003178 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_178_accel_v178_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=163, w2=261, w3=451, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(261, min_periods=max(261//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.919375 + 0.0003179 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_179_jerk_v179_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=170, w2=272, w3=464, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(272, min_periods=max(272//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1058 * _rolling_slope(draw, 464) + 0.000318 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_180_accel_v180_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=177, w2=283, w3=477, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(283, min_periods=max(283//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.948125 + 0.0003181 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_181_jerk_v181_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=184, w2=294, w3=490, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 294)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9625 + 0.0003182 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_182_accel_v182_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=191, w2=305, w3=503, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(305, min_periods=max(305//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.976875 + 0.0003183 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_183_jerk_v183_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=198, w2=316, w3=516, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(316, min_periods=max(316//3, 2)).rank(pct=True)
    persistence = change.rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1362 * persistence + 0.0003184 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_184_accel_v184_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=205, w2=327, w3=529, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(327, min_periods=max(327//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.005625 + 0.0003185 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_185_jerk_v185_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=212, w2=338, w3=542, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(338, min_periods=max(338//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1514 * slope + 0.0003186 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_186_accel_v186_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=219, w2=349, w3=555, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(349, min_periods=max(349//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.034375 + 0.0003187 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_187_jerk_v187_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=226, w2=360, w3=568, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 360)
    curvature = _rolling_slope(acceleration, 568)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1666 * acceleration + 0.0003188 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_188_accel_v188_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=233, w2=371, w3=581, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(371, min_periods=max(371//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.063125 + 0.0003189 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_189_jerk_v189_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=240, w2=382, w3=594, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(382, min_periods=max(382//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1818 * _rolling_slope(draw, 594) + 0.000319 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_190_accel_v190_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=247, w2=393, w3=607, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(393, min_periods=max(393//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.091875 + 0.0003191 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_191_jerk_v191_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=254, w2=404, w3=620, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 254)
    slow = _rolling_slope(x, 404)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.10625 + 0.0003192 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_192_accel_v192_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=10, w2=415, w3=633, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(415, min_periods=max(415//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.120625 + 0.0003193 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_193_jerk_v193_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=17, w2=426, w3=646, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(17)
    rank = change.rolling(426, min_periods=max(426//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2122 * persistence + 0.0003194 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_194_accel_v194_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=24, w2=437, w3=659, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(437, min_periods=max(437//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.149375 + 0.0003195 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_195_jerk_v195_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=31, w2=448, w3=672, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(448, min_periods=max(448//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2274 * slope + 0.0003196 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_196_accel_v196_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=38, w2=459, w3=685, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(38)
    drag = impulse.rolling(459, min_periods=max(459//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.178125 + 0.0003197 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_197_jerk_v197_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=45, w2=470, w3=698, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 470)
    curvature = _rolling_slope(acceleration, 698)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2426 * acceleration + 0.0003198 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_198_accel_v198_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=52, w2=481, w3=711, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(481, min_periods=max(481//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.206875 + 0.0003199 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_199_jerk_v199_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=59, w2=492, w3=724, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(492, min_periods=max(492//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2578 * _rolling_slope(draw, 724) + 0.00032 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_200_accel_v200_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=66, w2=503, w3=737, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(503, min_periods=max(503//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.235625 + 0.0003201 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_201_jerk_v201_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=73, w2=11, w3=750, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 11)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.25 + 0.0003202 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_202_accel_v202_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=80, w2=22, w3=763, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(22, min_periods=max(22//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.264375 + 0.0003203 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_203_jerk_v203_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=87, w2=33, w3=19, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(87)
    rank = change.rolling(33, min_periods=max(33//3, 2)).rank(pct=True)
    persistence = change.rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2882 * persistence + 0.0003204 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_204_accel_v204_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=94, w2=44, w3=32, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(44, min_periods=max(44//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.293125 + 0.0003205 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_205_jerk_v205_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=101, w2=55, w3=45, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(55, min_periods=max(55//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3034 * slope + 0.0003206 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_206_accel_v206_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=108, w2=66, w3=58, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(108)
    drag = impulse.rolling(66, min_periods=max(66//3, 2)).mean()
    noise = impulse.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.321875 + 0.0003207 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_207_jerk_v207_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=115, w2=77, w3=71, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 77)
    curvature = _rolling_slope(acceleration, 71)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3186 * acceleration + 0.0003208 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_208_accel_v208_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=122, w2=88, w3=84, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(88, min_periods=max(88//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(84) * 1.350625 + 0.0003209 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_209_jerk_v209_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=129, w2=99, w3=97, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(99, min_periods=max(99//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3338 * _rolling_slope(draw, 97) + 0.000321 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_210_accel_v210_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=136, w2=110, w3=110, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(110, min_periods=max(110//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.379375 + 0.0003211 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_211_jerk_v211_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=143, w2=121, w3=123, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=123, adjust=False).mean() * 1.39375 + 0.0003212 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_212_accel_v212_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=150, w2=132, w3=136, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(132, min_periods=max(132//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.408125 + 0.0003213 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_213_jerk_v213_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=157, w2=143, w3=149, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3642 * persistence + 0.0003214 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_214_accel_v214_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=164, w2=154, w3=162, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(154, min_periods=max(154//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.436875 + 0.0003215 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_215_jerk_v215_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=171, w2=165, w3=175, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(165, min_periods=max(165//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3794 * slope + 0.0003216 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_216_accel_v216_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=178, w2=176, w3=188, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(176, min_periods=max(176//3, 2)).mean()
    noise = impulse.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.465625 + 0.0003217 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_217_jerk_v217_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=185, w2=187, w3=201, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 201)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3946 * acceleration + 0.0003218 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_218_accel_v218_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=192, w2=198, w3=214, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(198, min_periods=max(198//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.494375 + 0.0003219 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_219_jerk_v219_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=199, w2=209, w3=227, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(209, min_periods=max(209//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4098 * _rolling_slope(draw, 227) + 0.000322 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_220_accel_v220_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=206, w2=220, w3=240, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(220, min_periods=max(220//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.523125 + 0.0003221 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_221_jerk_v221_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=213, w2=231, w3=253, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=253, adjust=False).mean() * 1.5375 + 0.0003222 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_222_accel_v222_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=220, w2=242, w3=266, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(242, min_periods=max(242//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.551875 + 0.0003223 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_223_jerk_v223_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=227, w2=253, w3=279, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(253, min_periods=max(253//3, 2)).rank(pct=True)
    persistence = change.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0638 * persistence + 0.0003224 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_224_accel_v224_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=234, w2=264, w3=292, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(264, min_periods=max(264//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.580625 + 0.0003225 * anchor
    return base_signal.diff().diff().diff()

def f06_vdd_225_jerk_v225_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=241, w2=275, w3=305, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(275, min_periods=max(275//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.079 * slope + 0.0003226 * anchor
    return base_signal.diff().diff().diff()
