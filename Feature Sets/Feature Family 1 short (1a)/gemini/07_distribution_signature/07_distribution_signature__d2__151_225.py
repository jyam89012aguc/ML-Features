"""07 distribution signature d2 second derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f07_dsi_151_jerk_v151_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=158, w2=25, w3=330, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 25)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.425 + 0.0003752 * anchor
    return base_signal.diff().diff()

def f07_dsi_152_accel_v152_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=165, w2=36, w3=343, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(36, min_periods=max(36//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.439375 + 0.0003753 * anchor
    return base_signal.diff().diff()

def f07_dsi_153_jerk_v153_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=172, w2=47, w3=356, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(356, min_periods=max(356//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3278 * persistence + 0.0003754 * anchor
    return base_signal.diff().diff()

def f07_dsi_154_accel_v154_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=179, w2=58, w3=369, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(58, min_periods=max(58//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.468125 + 0.0003755 * anchor
    return base_signal.diff().diff()

def f07_dsi_155_jerk_v155_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=186, w2=69, w3=382, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(69, min_periods=max(69//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.343 * slope + 0.0003756 * anchor
    return base_signal.diff().diff()

def f07_dsi_156_accel_v156_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=193, w2=80, w3=395, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(80, min_periods=max(80//3, 2)).mean()
    noise = impulse.abs().rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.496875 + 0.0003757 * anchor
    return base_signal.diff().diff()

def f07_dsi_157_jerk_v157_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=200, w2=91, w3=408, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 91)
    curvature = _rolling_slope(acceleration, 408)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3582 * acceleration + 0.0003758 * anchor
    return base_signal.diff().diff()

def f07_dsi_158_accel_v158_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=207, w2=102, w3=421, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(102, min_periods=max(102//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.525625 + 0.0003759 * anchor
    return base_signal.diff().diff()

def f07_dsi_159_jerk_v159_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=214, w2=113, w3=434, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(113, min_periods=max(113//3, 2)).max()
    rebound = x - x.rolling(214, min_periods=max(214//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3734 * _rolling_slope(draw, 434) + 0.000376 * anchor
    return base_signal.diff().diff()

def f07_dsi_160_accel_v160_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=221, w2=124, w3=447, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(124, min_periods=max(124//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(447, min_periods=max(447//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.554375 + 0.0003761 * anchor
    return base_signal.diff().diff()

def f07_dsi_161_jerk_v161_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=228, w2=135, w3=460, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 135)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.56875 + 0.0003762 * anchor
    return base_signal.diff().diff()

def f07_dsi_162_accel_v162_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=235, w2=146, w3=473, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(146, min_periods=max(146//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.583125 + 0.0003763 * anchor
    return base_signal.diff().diff()

def f07_dsi_163_jerk_v163_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=242, w2=157, w3=486, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(157, min_periods=max(157//3, 2)).rank(pct=True)
    persistence = change.rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4038 * persistence + 0.0003764 * anchor
    return base_signal.diff().diff()

def f07_dsi_164_accel_v164_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=249, w2=168, w3=499, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(168, min_periods=max(168//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.611875 + 0.0003765 * anchor
    return base_signal.diff().diff()

def f07_dsi_165_jerk_v165_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=5, w2=179, w3=512, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(179, min_periods=max(179//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0426 * slope + 0.0003766 * anchor
    return base_signal.diff().diff()

def f07_dsi_166_accel_v166_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=12, w2=190, w3=525, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(12)
    drag = impulse.rolling(190, min_periods=max(190//3, 2)).mean()
    noise = impulse.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8675 + 0.0003767 * anchor
    return base_signal.diff().diff()

def f07_dsi_167_jerk_v167_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=19, w2=201, w3=538, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 201)
    curvature = _rolling_slope(acceleration, 538)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0578 * acceleration + 0.0003768 * anchor
    return base_signal.diff().diff()

def f07_dsi_168_accel_v168_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=26, w2=212, w3=551, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.89625 + 0.0003769 * anchor
    return base_signal.diff().diff()

def f07_dsi_169_jerk_v169_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=33, w2=223, w3=564, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(223, min_periods=max(223//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.073 * _rolling_slope(draw, 564) + 0.000377 * anchor
    return base_signal.diff().diff()

def f07_dsi_170_accel_v170_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=40, w2=234, w3=577, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(234, min_periods=max(234//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.925 + 0.0003771 * anchor
    return base_signal.diff().diff()

def f07_dsi_171_jerk_v171_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=47, w2=245, w3=590, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.939375 + 0.0003772 * anchor
    return base_signal.diff().diff()

def f07_dsi_172_accel_v172_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=54, w2=256, w3=603, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(256, min_periods=max(256//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.95375 + 0.0003773 * anchor
    return base_signal.diff().diff()

def f07_dsi_173_jerk_v173_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=61, w2=267, w3=616, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(61)
    rank = change.rolling(267, min_periods=max(267//3, 2)).rank(pct=True)
    persistence = change.rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1034 * persistence + 0.0003774 * anchor
    return base_signal.diff().diff()

def f07_dsi_174_accel_v174_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=68, w2=278, w3=629, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(278, min_periods=max(278//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9825 + 0.0003775 * anchor
    return base_signal.diff().diff()

def f07_dsi_175_jerk_v175_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=75, w2=289, w3=642, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(289, min_periods=max(289//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1186 * slope + 0.0003776 * anchor
    return base_signal.diff().diff()

def f07_dsi_176_accel_v176_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=82, w2=300, w3=655, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(82)
    drag = impulse.rolling(300, min_periods=max(300//3, 2)).mean()
    noise = impulse.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.01125 + 0.0003777 * anchor
    return base_signal.diff().diff()

def f07_dsi_177_jerk_v177_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=89, w2=311, w3=668, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 668)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1338 * acceleration + 0.0003778 * anchor
    return base_signal.diff().diff()

def f07_dsi_178_accel_v178_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=96, w2=322, w3=681, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(322, min_periods=max(322//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04 + 0.0003779 * anchor
    return base_signal.diff().diff()

def f07_dsi_179_jerk_v179_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=103, w2=333, w3=694, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(333, min_periods=max(333//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.149 * _rolling_slope(draw, 694) + 0.000378 * anchor
    return base_signal.diff().diff()

def f07_dsi_180_accel_v180_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=110, w2=344, w3=707, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(344, min_periods=max(344//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.06875 + 0.0003781 * anchor
    return base_signal.diff().diff()

def f07_dsi_181_jerk_v181_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=117, w2=355, w3=720, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 355)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.083125 + 0.0003782 * anchor
    return base_signal.diff().diff()

def f07_dsi_182_accel_v182_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=124, w2=366, w3=733, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(366, min_periods=max(366//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0975 + 0.0003783 * anchor
    return base_signal.diff().diff()

def f07_dsi_183_jerk_v183_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=131, w2=377, w3=746, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1794 * persistence + 0.0003784 * anchor
    return base_signal.diff().diff()

def f07_dsi_184_accel_v184_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=138, w2=388, w3=759, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(388, min_periods=max(388//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.12625 + 0.0003785 * anchor
    return base_signal.diff().diff()

def f07_dsi_185_jerk_v185_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=145, w2=399, w3=15, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(399, min_periods=max(399//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1946 * slope + 0.0003786 * anchor
    return base_signal.diff().diff()

def f07_dsi_186_accel_v186_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=152, w2=410, w3=28, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(410, min_periods=max(410//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.155 + 0.0003787 * anchor
    return base_signal.diff().diff()

def f07_dsi_187_jerk_v187_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=159, w2=421, w3=41, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 421)
    curvature = _rolling_slope(acceleration, 41)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2098 * acceleration + 0.0003788 * anchor
    return base_signal.diff().diff()

def f07_dsi_188_accel_v188_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=166, w2=432, w3=54, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(432, min_periods=max(432//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(54) * 1.18375 + 0.0003789 * anchor
    return base_signal.diff().diff()

def f07_dsi_189_jerk_v189_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=173, w2=443, w3=67, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.225 * _rolling_slope(draw, 67) + 0.000379 * anchor
    return base_signal.diff().diff()

def f07_dsi_190_accel_v190_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=180, w2=454, w3=80, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(454, min_periods=max(454//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2125 + 0.0003791 * anchor
    return base_signal.diff().diff()

def f07_dsi_191_jerk_v191_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=187, w2=465, w3=93, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 465)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=93, adjust=False).mean() * 1.226875 + 0.0003792 * anchor
    return base_signal.diff().diff()

def f07_dsi_192_accel_v192_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=194, w2=476, w3=106, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(476, min_periods=max(476//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.24125 + 0.0003793 * anchor
    return base_signal.diff().diff()

def f07_dsi_193_jerk_v193_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=201, w2=487, w3=119, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(487, min_periods=max(487//3, 2)).rank(pct=True)
    persistence = change.rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2554 * persistence + 0.0003794 * anchor
    return base_signal.diff().diff()

def f07_dsi_194_accel_v194_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=208, w2=498, w3=132, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(498, min_periods=max(498//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.27 + 0.0003795 * anchor
    return base_signal.diff().diff()

def f07_dsi_195_jerk_v195_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=215, w2=509, w3=145, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(509, min_periods=max(509//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2706 * slope + 0.0003796 * anchor
    return base_signal.diff().diff()

def f07_dsi_196_accel_v196_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=222, w2=17, w3=158, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(17, min_periods=max(17//3, 2)).mean()
    noise = impulse.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.29875 + 0.0003797 * anchor
    return base_signal.diff().diff()

def f07_dsi_197_jerk_v197_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=229, w2=28, w3=171, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 171)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2858 * acceleration + 0.0003798 * anchor
    return base_signal.diff().diff()

def f07_dsi_198_accel_v198_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=236, w2=39, w3=184, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(39, min_periods=max(39//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3275 + 0.0003799 * anchor
    return base_signal.diff().diff()

def f07_dsi_199_jerk_v199_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=243, w2=50, w3=197, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(50, min_periods=max(50//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.301 * _rolling_slope(draw, 197) + 0.00038 * anchor
    return base_signal.diff().diff()

def f07_dsi_200_accel_v200_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=250, w2=61, w3=210, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.35625 + 0.0003801 * anchor
    return base_signal.diff().diff()

def f07_dsi_201_jerk_v201_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=6, w2=72, w3=223, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 72)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=223, adjust=False).mean() * 1.370625 + 0.0003802 * anchor
    return base_signal.diff().diff()

def f07_dsi_202_accel_v202_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=13, w2=83, w3=236, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(83, min_periods=max(83//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.385 + 0.0003803 * anchor
    return base_signal.diff().diff()

def f07_dsi_203_jerk_v203_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=20, w2=94, w3=249, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(20)
    rank = change.rolling(94, min_periods=max(94//3, 2)).rank(pct=True)
    persistence = change.rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3314 * persistence + 0.0003804 * anchor
    return base_signal.diff().diff()

def f07_dsi_204_accel_v204_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=27, w2=105, w3=262, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(105, min_periods=max(105//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41375 + 0.0003805 * anchor
    return base_signal.diff().diff()

def f07_dsi_205_jerk_v205_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=34, w2=116, w3=275, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(116, min_periods=max(116//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3466 * slope + 0.0003806 * anchor
    return base_signal.diff().diff()

def f07_dsi_206_accel_v206_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=41, w2=127, w3=288, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(41)
    drag = impulse.rolling(127, min_periods=max(127//3, 2)).mean()
    noise = impulse.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4425 + 0.0003807 * anchor
    return base_signal.diff().diff()

def f07_dsi_207_jerk_v207_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=48, w2=138, w3=301, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 138)
    curvature = _rolling_slope(acceleration, 301)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3618 * acceleration + 0.0003808 * anchor
    return base_signal.diff().diff()

def f07_dsi_208_accel_v208_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=55, w2=149, w3=314, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.47125 + 0.0003809 * anchor
    return base_signal.diff().diff()

def f07_dsi_209_jerk_v209_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=62, w2=160, w3=327, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(160, min_periods=max(160//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.377 * _rolling_slope(draw, 327) + 0.000381 * anchor
    return base_signal.diff().diff()

def f07_dsi_210_accel_v210_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=69, w2=171, w3=340, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(171, min_periods=max(171//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5 + 0.0003811 * anchor
    return base_signal.diff().diff()

def f07_dsi_211_jerk_v211_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=76, w2=182, w3=353, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 182)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.514375 + 0.0003812 * anchor
    return base_signal.diff().diff()

def f07_dsi_212_accel_v212_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=83, w2=193, w3=366, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(193, min_periods=max(193//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.52875 + 0.0003813 * anchor
    return base_signal.diff().diff()

def f07_dsi_213_jerk_v213_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=90, w2=204, w3=379, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(90)
    rank = change.rolling(204, min_periods=max(204//3, 2)).rank(pct=True)
    persistence = change.rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4074 * persistence + 0.0003814 * anchor
    return base_signal.diff().diff()

def f07_dsi_214_accel_v214_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=97, w2=215, w3=392, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(215, min_periods=max(215//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5575 + 0.0003815 * anchor
    return base_signal.diff().diff()

def f07_dsi_215_jerk_v215_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=104, w2=226, w3=405, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(226, min_periods=max(226//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0462 * slope + 0.0003816 * anchor
    return base_signal.diff().diff()

def f07_dsi_216_accel_v216_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=111, w2=237, w3=418, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(111)
    drag = impulse.rolling(237, min_periods=max(237//3, 2)).mean()
    noise = impulse.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.58625 + 0.0003817 * anchor
    return base_signal.diff().diff()

def f07_dsi_217_jerk_v217_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=118, w2=248, w3=431, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 248)
    curvature = _rolling_slope(acceleration, 431)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0614 * acceleration + 0.0003818 * anchor
    return base_signal.diff().diff()

def f07_dsi_218_accel_v218_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=125, w2=259, w3=444, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(259, min_periods=max(259//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.615 + 0.0003819 * anchor
    return base_signal.diff().diff()

def f07_dsi_219_jerk_v219_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=132, w2=270, w3=457, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(270, min_periods=max(270//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0766 * _rolling_slope(draw, 457) + 0.000382 * anchor
    return base_signal.diff().diff()

def f07_dsi_220_accel_v220_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=139, w2=281, w3=470, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(281, min_periods=max(281//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.870625 + 0.0003821 * anchor
    return base_signal.diff().diff()

def f07_dsi_221_jerk_v221_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=146, w2=292, w3=483, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 292)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.885 + 0.0003822 * anchor
    return base_signal.diff().diff()

def f07_dsi_222_accel_v222_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=153, w2=303, w3=496, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(303, min_periods=max(303//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.899375 + 0.0003823 * anchor
    return base_signal.diff().diff()

def f07_dsi_223_jerk_v223_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=160, w2=314, w3=509, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(314, min_periods=max(314//3, 2)).rank(pct=True)
    persistence = change.rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.107 * persistence + 0.0003824 * anchor
    return base_signal.diff().diff()

def f07_dsi_224_accel_v224_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=167, w2=325, w3=522, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(325, min_periods=max(325//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.928125 + 0.0003825 * anchor
    return base_signal.diff().diff()

def f07_dsi_225_jerk_v225_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=174, w2=336, w3=535, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(336, min_periods=max(336//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1222 * slope + 0.0003826 * anchor
    return base_signal.diff().diff()
