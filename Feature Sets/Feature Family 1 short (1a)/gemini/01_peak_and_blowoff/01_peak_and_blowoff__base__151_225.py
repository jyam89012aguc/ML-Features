"""01 peak and blowoff base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f01_pab_151_jerk_v151(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=58, w2=162, w3=464, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 162)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.474375 + 1.52e-05 * anchor

def f01_pab_152_accel_v152(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=65, w2=173, w3=477, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(173, min_periods=max(173//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.48875 + 1.53e-05 * anchor

def f01_pab_153_jerk_v153(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=72, w2=184, w3=490, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(72)
    rank = change.rolling(184, min_periods=max(184//3, 2)).rank(pct=True)
    persistence = change.rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0686 * persistence + 1.54e-05 * anchor

def f01_pab_154_accel_v154(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=79, w2=195, w3=503, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(195, min_periods=max(195//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5175 + 1.55e-05 * anchor

def f01_pab_155_jerk_v155(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=86, w2=206, w3=516, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(206, min_periods=max(206//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0838 * slope + 1.56e-05 * anchor

def f01_pab_156_accel_v156(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=93, w2=217, w3=529, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(93)
    drag = impulse.rolling(217, min_periods=max(217//3, 2)).mean()
    noise = impulse.abs().rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.54625 + 1.57e-05 * anchor

def f01_pab_157_jerk_v157(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=100, w2=228, w3=542, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 228)
    curvature = _rolling_slope(acceleration, 542)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.099 * acceleration + 1.58e-05 * anchor

def f01_pab_158_accel_v158(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=107, w2=239, w3=555, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(239, min_periods=max(239//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.575 + 1.59e-05 * anchor

def f01_pab_159_jerk_v159(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=114, w2=250, w3=568, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(250, min_periods=max(250//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1142 * _rolling_slope(draw, 568) + 1.6e-05 * anchor

def f01_pab_160_accel_v160(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=121, w2=261, w3=581, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.60375 + 1.61e-05 * anchor

def f01_pab_161_jerk_v161(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=128, w2=272, w3=594, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 272)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.618125 + 1.62e-05 * anchor

def f01_pab_162_accel_v162(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=135, w2=283, w3=607, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(283, min_periods=max(283//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.859375 + 1.63e-05 * anchor

def f01_pab_163_jerk_v163(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=142, w2=294, w3=620, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(294, min_periods=max(294//3, 2)).rank(pct=True)
    persistence = change.rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1446 * persistence + 1.64e-05 * anchor

def f01_pab_164_accel_v164(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=149, w2=305, w3=633, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(305, min_periods=max(305//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.888125 + 1.65e-05 * anchor

def f01_pab_165_jerk_v165(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=156, w2=316, w3=646, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(316, min_periods=max(316//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1598 * slope + 1.66e-05 * anchor

def f01_pab_166_accel_v166(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=163, w2=327, w3=659, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(327, min_periods=max(327//3, 2)).mean()
    noise = impulse.abs().rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.916875 + 1.67e-05 * anchor

def f01_pab_167_jerk_v167(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=170, w2=338, w3=672, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 338)
    curvature = _rolling_slope(acceleration, 672)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.175 * acceleration + 1.68e-05 * anchor

def f01_pab_168_accel_v168(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=177, w2=349, w3=685, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(349, min_periods=max(349//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.945625 + 1.69e-05 * anchor

def f01_pab_169_jerk_v169(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=184, w2=360, w3=698, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(360, min_periods=max(360//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1902 * _rolling_slope(draw, 698) + 1.7e-05 * anchor

def f01_pab_170_accel_v170(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=191, w2=371, w3=711, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(371, min_periods=max(371//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.974375 + 1.71e-05 * anchor

def f01_pab_171_jerk_v171(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=198, w2=382, w3=724, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 382)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.98875 + 1.72e-05 * anchor

def f01_pab_172_accel_v172(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=205, w2=393, w3=737, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(393, min_periods=max(393//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.003125 + 1.73e-05 * anchor

def f01_pab_173_jerk_v173(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=212, w2=404, w3=750, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(404, min_periods=max(404//3, 2)).rank(pct=True)
    persistence = change.rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2206 * persistence + 1.74e-05 * anchor

def f01_pab_174_accel_v174(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=219, w2=415, w3=763, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(415, min_periods=max(415//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.031875 + 1.75e-05 * anchor

def f01_pab_175_jerk_v175(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=226, w2=426, w3=19, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(426, min_periods=max(426//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2358 * slope + 1.76e-05 * anchor

def f01_pab_176_accel_v176(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=233, w2=437, w3=32, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(437, min_periods=max(437//3, 2)).mean()
    noise = impulse.abs().rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.060625 + 1.77e-05 * anchor

def f01_pab_177_jerk_v177(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=240, w2=448, w3=45, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 448)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.251 * acceleration + 1.78e-05 * anchor

def f01_pab_178_accel_v178(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=247, w2=459, w3=58, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(459, min_periods=max(459//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(58) * 1.089375 + 1.79e-05 * anchor

def f01_pab_179_jerk_v179(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=254, w2=470, w3=71, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(470, min_periods=max(470//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2662 * _rolling_slope(draw, 71) + 1.8e-05 * anchor

def f01_pab_180_accel_v180(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=10, w2=481, w3=84, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(481, min_periods=max(481//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.118125 + 1.81e-05 * anchor

def f01_pab_181_jerk_v181(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=17, w2=492, w3=97, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 492)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=97, adjust=False).mean() * 1.1325 + 1.82e-05 * anchor

def f01_pab_182_accel_v182(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=24, w2=503, w3=110, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(503, min_periods=max(503//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.146875 + 1.83e-05 * anchor

def f01_pab_183_jerk_v183(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=31, w2=11, w3=123, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(31)
    rank = change.rolling(11, min_periods=max(11//3, 2)).rank(pct=True)
    persistence = change.rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2966 * persistence + 1.84e-05 * anchor

def f01_pab_184_accel_v184(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=38, w2=22, w3=136, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(22, min_periods=max(22//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.175625 + 1.85e-05 * anchor

def f01_pab_185_jerk_v185(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=45, w2=33, w3=149, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(33, min_periods=max(33//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3118 * slope + 1.86e-05 * anchor

def f01_pab_186_accel_v186(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=52, w2=44, w3=162, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(52)
    drag = impulse.rolling(44, min_periods=max(44//3, 2)).mean()
    noise = impulse.abs().rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.204375 + 1.87e-05 * anchor

def f01_pab_187_jerk_v187(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=59, w2=55, w3=175, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 55)
    curvature = _rolling_slope(acceleration, 175)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.327 * acceleration + 1.88e-05 * anchor

def f01_pab_188_accel_v188(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=66, w2=66, w3=188, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(66, min_periods=max(66//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.233125 + 1.89e-05 * anchor

def f01_pab_189_jerk_v189(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=73, w2=77, w3=201, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(77, min_periods=max(77//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3422 * _rolling_slope(draw, 201) + 1.9e-05 * anchor

def f01_pab_190_accel_v190(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=80, w2=88, w3=214, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(88, min_periods=max(88//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.261875 + 1.91e-05 * anchor

def f01_pab_191_jerk_v191(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=87, w2=99, w3=227, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 99)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=227, adjust=False).mean() * 1.27625 + 1.92e-05 * anchor

def f01_pab_192_accel_v192(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=94, w2=110, w3=240, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(110, min_periods=max(110//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.290625 + 1.93e-05 * anchor

def f01_pab_193_jerk_v193(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=101, w2=121, w3=253, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(101)
    rank = change.rolling(121, min_periods=max(121//3, 2)).rank(pct=True)
    persistence = change.rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3726 * persistence + 1.94e-05 * anchor

def f01_pab_194_accel_v194(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=108, w2=132, w3=266, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(132, min_periods=max(132//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.319375 + 1.95e-05 * anchor

def f01_pab_195_jerk_v195(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=115, w2=143, w3=279, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(143, min_periods=max(143//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3878 * slope + 1.96e-05 * anchor

def f01_pab_196_accel_v196(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=122, w2=154, w3=292, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(122)
    drag = impulse.rolling(154, min_periods=max(154//3, 2)).mean()
    noise = impulse.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.348125 + 1.97e-05 * anchor

def f01_pab_197_jerk_v197(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=129, w2=165, w3=305, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 165)
    curvature = _rolling_slope(acceleration, 305)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.403 * acceleration + 1.98e-05 * anchor

def f01_pab_198_accel_v198(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=136, w2=176, w3=318, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.376875 + 1.99e-05 * anchor

def f01_pab_199_jerk_v199(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=143, w2=187, w3=331, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(187, min_periods=max(187//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0418 * _rolling_slope(draw, 331) + 2e-05 * anchor

def f01_pab_200_accel_v200(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=150, w2=198, w3=344, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(198, min_periods=max(198//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.405625 + 2.01e-05 * anchor

def f01_pab_201_jerk_v201(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=157, w2=209, w3=357, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.42 + 2.02e-05 * anchor

def f01_pab_202_accel_v202(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=164, w2=220, w3=370, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(220, min_periods=max(220//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.434375 + 2.03e-05 * anchor

def f01_pab_203_jerk_v203(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=171, w2=231, w3=383, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(231, min_periods=max(231//3, 2)).rank(pct=True)
    persistence = change.rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0722 * persistence + 2.04e-05 * anchor

def f01_pab_204_accel_v204(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=178, w2=242, w3=396, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(242, min_periods=max(242//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.463125 + 2.05e-05 * anchor

def f01_pab_205_jerk_v205(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=185, w2=253, w3=409, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(253, min_periods=max(253//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0874 * slope + 2.06e-05 * anchor

def f01_pab_206_accel_v206(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=192, w2=264, w3=422, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(264, min_periods=max(264//3, 2)).mean()
    noise = impulse.abs().rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.491875 + 2.07e-05 * anchor

def f01_pab_207_jerk_v207(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=199, w2=275, w3=435, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 275)
    curvature = _rolling_slope(acceleration, 435)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1026 * acceleration + 2.08e-05 * anchor

def f01_pab_208_accel_v208(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=206, w2=286, w3=448, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(286, min_periods=max(286//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.520625 + 2.09e-05 * anchor

def f01_pab_209_jerk_v209(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=213, w2=297, w3=461, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(297, min_periods=max(297//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1178 * _rolling_slope(draw, 461) + 2.1e-05 * anchor

def f01_pab_210_accel_v210(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=220, w2=308, w3=474, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(308, min_periods=max(308//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.549375 + 2.11e-05 * anchor

def f01_pab_211_jerk_v211(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=227, w2=319, w3=487, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 319)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.56375 + 2.12e-05 * anchor

def f01_pab_212_accel_v212(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=234, w2=330, w3=500, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.578125 + 2.13e-05 * anchor

def f01_pab_213_jerk_v213(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=241, w2=341, w3=513, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(341, min_periods=max(341//3, 2)).rank(pct=True)
    persistence = change.rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1482 * persistence + 2.14e-05 * anchor

def f01_pab_214_accel_v214(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=248, w2=352, w3=526, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(352, min_periods=max(352//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.606875 + 2.15e-05 * anchor

def f01_pab_215_jerk_v215(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=255, w2=363, w3=539, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 255)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1634 * slope + 2.16e-05 * anchor

def f01_pab_216_accel_v216(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=11, w2=374, w3=552, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(11)
    drag = impulse.rolling(374, min_periods=max(374//3, 2)).mean()
    noise = impulse.abs().rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.8625 + 2.17e-05 * anchor

def f01_pab_217_jerk_v217(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=18, w2=385, w3=565, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 385)
    curvature = _rolling_slope(acceleration, 565)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1786 * acceleration + 2.18e-05 * anchor

def f01_pab_218_accel_v218(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=25, w2=396, w3=578, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(396, min_periods=max(396//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.89125 + 2.19e-05 * anchor

def f01_pab_219_jerk_v219(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=32, w2=407, w3=591, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(407, min_periods=max(407//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1938 * _rolling_slope(draw, 591) + 2.2e-05 * anchor

def f01_pab_220_accel_v220(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=39, w2=418, w3=604, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(418, min_periods=max(418//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.92 + 2.21e-05 * anchor

def f01_pab_221_jerk_v221(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=46, w2=429, w3=617, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 429)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.934375 + 2.22e-05 * anchor

def f01_pab_222_accel_v222(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=53, w2=440, w3=630, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.94875 + 2.23e-05 * anchor

def f01_pab_223_jerk_v223(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=60, w2=451, w3=643, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(60)
    rank = change.rolling(451, min_periods=max(451//3, 2)).rank(pct=True)
    persistence = change.rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2242 * persistence + 2.24e-05 * anchor

def f01_pab_224_accel_v224(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=67, w2=462, w3=656, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9775 + 2.25e-05 * anchor

def f01_pab_225_jerk_v225(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=74, w2=473, w3=669, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(473, min_periods=max(473//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2394 * slope + 2.26e-05 * anchor
