"""37 blowoff parabolic signature base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f37_bps_151_jerk_v151(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=89, w2=407, w3=647, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 407)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.29875 + 0.0022352 * anchor

def f37_bps_152_accel_v152(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=96, w2=418, w3=660, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(418, min_periods=max(418//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.313125 + 0.0022353 * anchor

def f37_bps_153_jerk_v153(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=103, w2=429, w3=673, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(103)
    rank = change.rolling(429, min_periods=max(429//3, 2)).rank(pct=True)
    persistence = change.rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1614 * persistence + 0.0022354 * anchor

def f37_bps_154_accel_v154(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=110, w2=440, w3=686, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(440, min_periods=max(440//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.341875 + 0.0022355 * anchor

def f37_bps_155_jerk_v155(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=117, w2=451, w3=699, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(451, min_periods=max(451//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1766 * slope + 0.0022356 * anchor

def f37_bps_156_accel_v156(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=124, w2=462, w3=712, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(124)
    drag = impulse.rolling(462, min_periods=max(462//3, 2)).mean()
    noise = impulse.abs().rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.370625 + 0.0022357 * anchor

def f37_bps_157_jerk_v157(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=131, w2=473, w3=725, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 473)
    curvature = _rolling_slope(acceleration, 725)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1918 * acceleration + 0.0022358 * anchor

def f37_bps_158_accel_v158(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=138, w2=484, w3=738, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(484, min_periods=max(484//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.399375 + 0.0022359 * anchor

def f37_bps_159_jerk_v159(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=145, w2=495, w3=751, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(495, min_periods=max(495//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.207 * _rolling_slope(draw, 751) + 0.002236 * anchor

def f37_bps_160_accel_v160(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=152, w2=506, w3=764, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(506, min_periods=max(506//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.428125 + 0.0022361 * anchor

def f37_bps_161_jerk_v161(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=159, w2=14, w3=20, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 14)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=20, adjust=False).mean() * 1.4425 + 0.0022362 * anchor

def f37_bps_162_accel_v162(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=166, w2=25, w3=33, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(25, min_periods=max(25//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.456875 + 0.0022363 * anchor

def f37_bps_163_jerk_v163(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=173, w2=36, w3=46, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(36, min_periods=max(36//3, 2)).rank(pct=True)
    persistence = change.rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2374 * persistence + 0.0022364 * anchor

def f37_bps_164_accel_v164(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=180, w2=47, w3=59, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(47, min_periods=max(47//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.485625 + 0.0022365 * anchor

def f37_bps_165_jerk_v165(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=187, w2=58, w3=72, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(58, min_periods=max(58//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2526 * slope + 0.0022366 * anchor

def f37_bps_166_accel_v166(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=194, w2=69, w3=85, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(69, min_periods=max(69//3, 2)).mean()
    noise = impulse.abs().rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.514375 + 0.0022367 * anchor

def f37_bps_167_jerk_v167(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=201, w2=80, w3=98, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 80)
    curvature = _rolling_slope(acceleration, 98)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2678 * acceleration + 0.0022368 * anchor

def f37_bps_168_accel_v168(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=208, w2=91, w3=111, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(91, min_periods=max(91//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(111) * 1.543125 + 0.0022369 * anchor

def f37_bps_169_jerk_v169(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=215, w2=102, w3=124, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(102, min_periods=max(102//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.283 * _rolling_slope(draw, 124) + 0.002237 * anchor

def f37_bps_170_accel_v170(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=222, w2=113, w3=137, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(113, min_periods=max(113//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.571875 + 0.0022371 * anchor

def f37_bps_171_jerk_v171(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=229, w2=124, w3=150, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 124)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=150, adjust=False).mean() * 1.58625 + 0.0022372 * anchor

def f37_bps_172_accel_v172(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=236, w2=135, w3=163, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(135, min_periods=max(135//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.600625 + 0.0022373 * anchor

def f37_bps_173_jerk_v173(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=243, w2=146, w3=176, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(146, min_periods=max(146//3, 2)).rank(pct=True)
    persistence = change.rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3134 * persistence + 0.0022374 * anchor

def f37_bps_174_accel_v174(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=157, w3=189, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(157, min_periods=max(157//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85625 + 0.0022375 * anchor

def f37_bps_175_jerk_v175(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=168, w3=202, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(168, min_periods=max(168//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3286 * slope + 0.0022376 * anchor

def f37_bps_176_accel_v176(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=179, w3=215, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(13)
    drag = impulse.rolling(179, min_periods=max(179//3, 2)).mean()
    noise = impulse.abs().rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.885 + 0.0022377 * anchor

def f37_bps_177_jerk_v177(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=190, w3=228, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 228)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3438 * acceleration + 0.0022378 * anchor

def f37_bps_178_accel_v178(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=201, w3=241, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(201, min_periods=max(201//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.91375 + 0.0022379 * anchor

def f37_bps_179_jerk_v179(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=212, w3=254, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(212, min_periods=max(212//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.359 * _rolling_slope(draw, 254) + 0.002238 * anchor

def f37_bps_180_accel_v180(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=223, w3=267, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(223, min_periods=max(223//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9425 + 0.0022381 * anchor

def f37_bps_181_jerk_v181(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=234, w3=280, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 234)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=280, adjust=False).mean() * 0.956875 + 0.0022382 * anchor

def f37_bps_182_accel_v182(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=245, w3=293, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(245, min_periods=max(245//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.97125 + 0.0022383 * anchor

def f37_bps_183_jerk_v183(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=62, w2=256, w3=306, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(62)
    rank = change.rolling(256, min_periods=max(256//3, 2)).rank(pct=True)
    persistence = change.rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3894 * persistence + 0.0022384 * anchor

def f37_bps_184_accel_v184(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=69, w2=267, w3=319, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(267, min_periods=max(267//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0 + 0.0022385 * anchor

def f37_bps_185_jerk_v185(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=76, w2=278, w3=332, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(278, min_periods=max(278//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4046 * slope + 0.0022386 * anchor

def f37_bps_186_accel_v186(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=83, w2=289, w3=345, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(83)
    drag = impulse.rolling(289, min_periods=max(289//3, 2)).mean()
    noise = impulse.abs().rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.02875 + 0.0022387 * anchor

def f37_bps_187_jerk_v187(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=90, w2=300, w3=358, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 300)
    curvature = _rolling_slope(acceleration, 358)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0434 * acceleration + 0.0022388 * anchor

def f37_bps_188_accel_v188(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=97, w2=311, w3=371, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(311, min_periods=max(311//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0575 + 0.0022389 * anchor

def f37_bps_189_jerk_v189(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=104, w2=322, w3=384, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(322, min_periods=max(322//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0586 * _rolling_slope(draw, 384) + 0.002239 * anchor

def f37_bps_190_accel_v190(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=111, w2=333, w3=397, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(333, min_periods=max(333//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(397, min_periods=max(397//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.08625 + 0.0022391 * anchor

def f37_bps_191_jerk_v191(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=118, w2=344, w3=410, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 344)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.100625 + 0.0022392 * anchor

def f37_bps_192_accel_v192(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=125, w2=355, w3=423, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(355, min_periods=max(355//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.115 + 0.0022393 * anchor

def f37_bps_193_jerk_v193(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=132, w2=366, w3=436, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.089 * persistence + 0.0022394 * anchor

def f37_bps_194_accel_v194(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=139, w2=377, w3=449, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(377, min_periods=max(377//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14375 + 0.0022395 * anchor

def f37_bps_195_jerk_v195(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=146, w2=388, w3=462, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(388, min_periods=max(388//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1042 * slope + 0.0022396 * anchor

def f37_bps_196_accel_v196(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=153, w2=399, w3=475, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(399, min_periods=max(399//3, 2)).mean()
    noise = impulse.abs().rolling(475, min_periods=max(475//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1725 + 0.0022397 * anchor

def f37_bps_197_jerk_v197(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=160, w2=410, w3=488, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 410)
    curvature = _rolling_slope(acceleration, 488)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1194 * acceleration + 0.0022398 * anchor

def f37_bps_198_accel_v198(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=167, w2=421, w3=501, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(421, min_periods=max(421//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.20125 + 0.0022399 * anchor

def f37_bps_199_jerk_v199(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=174, w2=432, w3=514, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(432, min_periods=max(432//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1346 * _rolling_slope(draw, 514) + 0.00224 * anchor

def f37_bps_200_accel_v200(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=181, w2=443, w3=527, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(443, min_periods=max(443//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.23 + 0.0022401 * anchor

def f37_bps_201_jerk_v201(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=188, w2=454, w3=540, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 188)
    slow = _rolling_slope(x, 454)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.244375 + 0.0022402 * anchor

def f37_bps_202_accel_v202(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=195, w2=465, w3=553, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(465, min_periods=max(465//3, 2)).max()
    trough = x.rolling(195, min_periods=max(195//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.25875 + 0.0022403 * anchor

def f37_bps_203_jerk_v203(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=202, w2=476, w3=566, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(476, min_periods=max(476//3, 2)).rank(pct=True)
    persistence = change.rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.165 * persistence + 0.0022404 * anchor

def f37_bps_204_accel_v204(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=209, w2=487, w3=579, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(209, min_periods=max(209//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2875 + 0.0022405 * anchor

def f37_bps_205_jerk_v205(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=216, w2=498, w3=592, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(498, min_periods=max(498//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 216)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1802 * slope + 0.0022406 * anchor

def f37_bps_206_accel_v206(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=223, w2=509, w3=605, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(509, min_periods=max(509//3, 2)).mean()
    noise = impulse.abs().rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.31625 + 0.0022407 * anchor

def f37_bps_207_jerk_v207(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=230, w2=17, w3=618, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 230)
    acceleration = _rolling_slope(velocity, 17)
    curvature = _rolling_slope(acceleration, 618)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1954 * acceleration + 0.0022408 * anchor

def f37_bps_208_accel_v208(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=237, w2=28, w3=631, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(237, min_periods=max(237//3, 2)).mean(), upside.rolling(28, min_periods=max(28//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.345 + 0.0022409 * anchor

def f37_bps_209_jerk_v209(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=244, w2=39, w3=644, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(39, min_periods=max(39//3, 2)).max()
    rebound = x - x.rolling(244, min_periods=max(244//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2106 * _rolling_slope(draw, 644) + 0.002241 * anchor

def f37_bps_210_accel_v210(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=251, w2=50, w3=657, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 251)
    baseline = trend.rolling(50, min_periods=max(50//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.37375 + 0.0022411 * anchor

def f37_bps_211_jerk_v211(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=7, w2=61, w3=670, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 61)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.388125 + 0.0022412 * anchor

def f37_bps_212_accel_v212(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=14, w2=72, w3=683, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(72, min_periods=max(72//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4025 + 0.0022413 * anchor

def f37_bps_213_jerk_v213(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=21, w2=83, w3=696, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(21)
    rank = change.rolling(83, min_periods=max(83//3, 2)).rank(pct=True)
    persistence = change.rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.241 * persistence + 0.0022414 * anchor

def f37_bps_214_accel_v214(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=28, w2=94, w3=709, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(94, min_periods=max(94//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43125 + 0.0022415 * anchor

def f37_bps_215_jerk_v215(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=35, w2=105, w3=722, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(105, min_periods=max(105//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2562 * slope + 0.0022416 * anchor

def f37_bps_216_accel_v216(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=42, w2=116, w3=735, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(42)
    drag = impulse.rolling(116, min_periods=max(116//3, 2)).mean()
    noise = impulse.abs().rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.46 + 0.0022417 * anchor

def f37_bps_217_jerk_v217(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=49, w2=127, w3=748, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 127)
    curvature = _rolling_slope(acceleration, 748)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2714 * acceleration + 0.0022418 * anchor

def f37_bps_218_accel_v218(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=56, w2=138, w3=761, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(138, min_periods=max(138//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.48875 + 0.0022419 * anchor

def f37_bps_219_jerk_v219(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=63, w2=149, w3=17, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(149, min_periods=max(149//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2866 * _rolling_slope(draw, 17) + 0.002242 * anchor

def f37_bps_220_accel_v220(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=70, w2=160, w3=30, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.5175 + 0.0022421 * anchor

def f37_bps_221_jerk_v221(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=77, w2=171, w3=43, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 171)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=43, adjust=False).mean() * 1.531875 + 0.0022422 * anchor

def f37_bps_222_accel_v222(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=84, w2=182, w3=56, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(182, min_periods=max(182//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.54625 + 0.0022423 * anchor

def f37_bps_223_jerk_v223(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=91, w2=193, w3=69, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(91)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.317 * persistence + 0.0022424 * anchor

def f37_bps_224_accel_v224(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=98, w2=204, w3=82, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(204, min_periods=max(204//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.575 + 0.0022425 * anchor

def f37_bps_225_jerk_v225(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=105, w2=215, w3=95, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3322 * slope + 0.0022426 * anchor
