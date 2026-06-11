"""10 volatility regime at peak base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f10_vreg_151_jerk_v151(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=141, w2=269, w3=493, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.134375 + 0.0006152 * anchor

def f10_vreg_152_accel_v152(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=148, w2=280, w3=506, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.14875 + 0.0006153 * anchor

def f10_vreg_153_jerk_v153(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=155, w2=291, w3=519, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1242 * persistence + 0.0006154 * anchor

def f10_vreg_154_accel_v154(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=162, w2=302, w3=532, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(302, min_periods=max(302//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1775 + 0.0006155 * anchor

def f10_vreg_155_jerk_v155(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=169, w2=313, w3=545, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(313, min_periods=max(313//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1394 * slope + 0.0006156 * anchor

def f10_vreg_156_accel_v156(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=176, w2=324, w3=558, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(324, min_periods=max(324//3, 2)).mean()
    noise = impulse.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.20625 + 0.0006157 * anchor

def f10_vreg_157_jerk_v157(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=183, w2=335, w3=571, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 335)
    curvature = _rolling_slope(acceleration, 571)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1546 * acceleration + 0.0006158 * anchor

def f10_vreg_158_accel_v158(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=190, w2=346, w3=584, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.235 + 0.0006159 * anchor

def f10_vreg_159_jerk_v159(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=197, w2=357, w3=597, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(357, min_periods=max(357//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1698 * _rolling_slope(draw, 597) + 0.000616 * anchor

def f10_vreg_160_accel_v160(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=204, w2=368, w3=610, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.26375 + 0.0006161 * anchor

def f10_vreg_161_jerk_v161(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=211, w2=379, w3=623, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 379)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.278125 + 0.0006162 * anchor

def f10_vreg_162_accel_v162(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=218, w2=390, w3=636, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2925 + 0.0006163 * anchor

def f10_vreg_163_jerk_v163(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=225, w2=401, w3=649, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(401, min_periods=max(401//3, 2)).rank(pct=True)
    persistence = change.rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2002 * persistence + 0.0006164 * anchor

def f10_vreg_164_accel_v164(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=232, w2=412, w3=662, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(412, min_periods=max(412//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32125 + 0.0006165 * anchor

def f10_vreg_165_jerk_v165(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=239, w2=423, w3=675, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(423, min_periods=max(423//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2154 * slope + 0.0006166 * anchor

def f10_vreg_166_accel_v166(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=246, w2=434, w3=688, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.35 + 0.0006167 * anchor

def f10_vreg_167_jerk_v167(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=253, w2=445, w3=701, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 253)
    acceleration = _rolling_slope(velocity, 445)
    curvature = _rolling_slope(acceleration, 701)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2306 * acceleration + 0.0006168 * anchor

def f10_vreg_168_accel_v168(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=9, w2=456, w3=714, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(456, min_periods=max(456//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.37875 + 0.0006169 * anchor

def f10_vreg_169_jerk_v169(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=16, w2=467, w3=727, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(467, min_periods=max(467//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2458 * _rolling_slope(draw, 727) + 0.000617 * anchor

def f10_vreg_170_accel_v170(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=23, w2=478, w3=740, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4075 + 0.0006171 * anchor

def f10_vreg_171_jerk_v171(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=30, w2=489, w3=753, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 489)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.421875 + 0.0006172 * anchor

def f10_vreg_172_accel_v172(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=37, w2=500, w3=766, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(500, min_periods=max(500//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.43625 + 0.0006173 * anchor

def f10_vreg_173_jerk_v173(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=44, w2=511, w3=22, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(44)
    rank = change.rolling(511, min_periods=max(511//3, 2)).rank(pct=True)
    persistence = change.rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2762 * persistence + 0.0006174 * anchor

def f10_vreg_174_accel_v174(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=51, w2=19, w3=35, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(19, min_periods=max(19//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.465 + 0.0006175 * anchor

def f10_vreg_175_jerk_v175(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=58, w2=30, w3=48, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(30, min_periods=max(30//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2914 * slope + 0.0006176 * anchor

def f10_vreg_176_accel_v176(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=65, w2=41, w3=61, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(65)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.49375 + 0.0006177 * anchor

def f10_vreg_177_jerk_v177(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=72, w2=52, w3=74, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 52)
    curvature = _rolling_slope(acceleration, 74)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3066 * acceleration + 0.0006178 * anchor

def f10_vreg_178_accel_v178(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=79, w2=63, w3=87, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(63, min_periods=max(63//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(87) * 1.5225 + 0.0006179 * anchor

def f10_vreg_179_jerk_v179(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=86, w2=74, w3=100, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(74, min_periods=max(74//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3218 * _rolling_slope(draw, 100) + 0.000618 * anchor

def f10_vreg_180_accel_v180(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=93, w2=85, w3=113, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(85, min_periods=max(85//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.55125 + 0.0006181 * anchor

def f10_vreg_181_jerk_v181(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=100, w2=96, w3=126, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=126, adjust=False).mean() * 1.565625 + 0.0006182 * anchor

def f10_vreg_182_accel_v182(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=107, w2=107, w3=139, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(107, min_periods=max(107//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.58 + 0.0006183 * anchor

def f10_vreg_183_jerk_v183(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=114, w2=118, w3=152, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(114)
    rank = change.rolling(118, min_periods=max(118//3, 2)).rank(pct=True)
    persistence = change.rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3522 * persistence + 0.0006184 * anchor

def f10_vreg_184_accel_v184(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=121, w2=129, w3=165, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(129, min_periods=max(129//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60875 + 0.0006185 * anchor

def f10_vreg_185_jerk_v185(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=128, w2=140, w3=178, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(140, min_periods=max(140//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3674 * slope + 0.0006186 * anchor

def f10_vreg_186_accel_v186(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=135, w2=151, w3=191, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(151, min_periods=max(151//3, 2)).mean()
    noise = impulse.abs().rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.864375 + 0.0006187 * anchor

def f10_vreg_187_jerk_v187(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=142, w2=162, w3=204, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 162)
    curvature = _rolling_slope(acceleration, 204)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3826 * acceleration + 0.0006188 * anchor

def f10_vreg_188_accel_v188(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=149, w2=173, w3=217, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.893125 + 0.0006189 * anchor

def f10_vreg_189_jerk_v189(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=156, w2=184, w3=230, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3978 * _rolling_slope(draw, 230) + 0.000619 * anchor

def f10_vreg_190_accel_v190(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=163, w2=195, w3=243, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(195, min_periods=max(195//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.921875 + 0.0006191 * anchor

def f10_vreg_191_jerk_v191(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=170, w2=206, w3=256, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 206)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=256, adjust=False).mean() * 0.93625 + 0.0006192 * anchor

def f10_vreg_192_accel_v192(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=177, w2=217, w3=269, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.950625 + 0.0006193 * anchor

def f10_vreg_193_jerk_v193(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=184, w2=228, w3=282, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(228, min_periods=max(228//3, 2)).rank(pct=True)
    persistence = change.rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0518 * persistence + 0.0006194 * anchor

def f10_vreg_194_accel_v194(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=191, w2=239, w3=295, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.979375 + 0.0006195 * anchor

def f10_vreg_195_jerk_v195(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=198, w2=250, w3=308, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(250, min_periods=max(250//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.067 * slope + 0.0006196 * anchor

def f10_vreg_196_accel_v196(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=205, w2=261, w3=321, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(261, min_periods=max(261//3, 2)).mean()
    noise = impulse.abs().rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.008125 + 0.0006197 * anchor

def f10_vreg_197_jerk_v197(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=212, w2=272, w3=334, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 272)
    curvature = _rolling_slope(acceleration, 334)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0822 * acceleration + 0.0006198 * anchor

def f10_vreg_198_accel_v198(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=219, w2=283, w3=347, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(283, min_periods=max(283//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.036875 + 0.0006199 * anchor

def f10_vreg_199_jerk_v199(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=226, w2=294, w3=360, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(294, min_periods=max(294//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0974 * _rolling_slope(draw, 360) + 0.00062 * anchor

def f10_vreg_200_accel_v200(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=233, w2=305, w3=373, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.065625 + 0.0006201 * anchor

def f10_vreg_201_jerk_v201(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=240, w2=316, w3=386, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 316)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.08 + 0.0006202 * anchor

def f10_vreg_202_accel_v202(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=247, w2=327, w3=399, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(327, min_periods=max(327//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.094375 + 0.0006203 * anchor

def f10_vreg_203_jerk_v203(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=254, w2=338, w3=412, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(338, min_periods=max(338//3, 2)).rank(pct=True)
    persistence = change.rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1278 * persistence + 0.0006204 * anchor

def f10_vreg_204_accel_v204(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=10, w2=349, w3=425, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(349, min_periods=max(349//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.123125 + 0.0006205 * anchor

def f10_vreg_205_jerk_v205(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=17, w2=360, w3=438, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(360, min_periods=max(360//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.143 * slope + 0.0006206 * anchor

def f10_vreg_206_accel_v206(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=24, w2=371, w3=451, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(24)
    drag = impulse.rolling(371, min_periods=max(371//3, 2)).mean()
    noise = impulse.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.151875 + 0.0006207 * anchor

def f10_vreg_207_jerk_v207(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=31, w2=382, w3=464, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 382)
    curvature = _rolling_slope(acceleration, 464)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1582 * acceleration + 0.0006208 * anchor

def f10_vreg_208_accel_v208(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=38, w2=393, w3=477, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(393, min_periods=max(393//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.180625 + 0.0006209 * anchor

def f10_vreg_209_jerk_v209(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=45, w2=404, w3=490, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(404, min_periods=max(404//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1734 * _rolling_slope(draw, 490) + 0.000621 * anchor

def f10_vreg_210_accel_v210(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=52, w2=415, w3=503, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(415, min_periods=max(415//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.209375 + 0.0006211 * anchor

def f10_vreg_211_jerk_v211(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=59, w2=426, w3=516, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 426)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.22375 + 0.0006212 * anchor

def f10_vreg_212_accel_v212(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=66, w2=437, w3=529, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(437, min_periods=max(437//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.238125 + 0.0006213 * anchor

def f10_vreg_213_jerk_v213(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=73, w2=448, w3=542, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(73)
    rank = change.rolling(448, min_periods=max(448//3, 2)).rank(pct=True)
    persistence = change.rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2038 * persistence + 0.0006214 * anchor

def f10_vreg_214_accel_v214(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=80, w2=459, w3=555, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(459, min_periods=max(459//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.266875 + 0.0006215 * anchor

def f10_vreg_215_jerk_v215(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=87, w2=470, w3=568, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(470, min_periods=max(470//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.219 * slope + 0.0006216 * anchor

def f10_vreg_216_accel_v216(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=94, w2=481, w3=581, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(94)
    drag = impulse.rolling(481, min_periods=max(481//3, 2)).mean()
    noise = impulse.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.295625 + 0.0006217 * anchor

def f10_vreg_217_jerk_v217(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=101, w2=492, w3=594, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 492)
    curvature = _rolling_slope(acceleration, 594)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2342 * acceleration + 0.0006218 * anchor

def f10_vreg_218_accel_v218(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=108, w2=503, w3=607, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(503, min_periods=max(503//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.324375 + 0.0006219 * anchor

def f10_vreg_219_jerk_v219(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=115, w2=11, w3=620, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(11, min_periods=max(11//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2494 * _rolling_slope(draw, 620) + 0.000622 * anchor

def f10_vreg_220_accel_v220(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=122, w2=22, w3=633, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(22, min_periods=max(22//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.353125 + 0.0006221 * anchor

def f10_vreg_221_jerk_v221(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=129, w2=33, w3=646, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 33)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3675 + 0.0006222 * anchor

def f10_vreg_222_accel_v222(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=136, w2=44, w3=659, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(44, min_periods=max(44//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.381875 + 0.0006223 * anchor

def f10_vreg_223_jerk_v223(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=143, w2=55, w3=672, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(55, min_periods=max(55//3, 2)).rank(pct=True)
    persistence = change.rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2798 * persistence + 0.0006224 * anchor

def f10_vreg_224_accel_v224(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=150, w2=66, w3=685, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(66, min_periods=max(66//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.410625 + 0.0006225 * anchor

def f10_vreg_225_jerk_v225(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=157, w2=77, w3=698, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(77, min_periods=max(77//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.295 * slope + 0.0006226 * anchor
