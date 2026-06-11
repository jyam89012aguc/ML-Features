"""49 short squeeze aftermath d2 second derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f49_ssa_151_jerk_v151_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=222, w2=194, w3=609, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 194)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.320625 + 0.0030152 * anchor
    return base_signal.diff().diff()

def f49_ssa_152_accel_v152_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=229, w2=205, w3=622, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(205, min_periods=max(205//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.335 + 0.0030153 * anchor
    return base_signal.diff().diff()

def f49_ssa_153_jerk_v153_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=236, w2=216, w3=635, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(216, min_periods=max(216//3, 2)).rank(pct=True)
    persistence = change.rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3466 * persistence + 0.0030154 * anchor
    return base_signal.diff().diff()

def f49_ssa_154_accel_v154_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=243, w2=227, w3=648, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36375 + 0.0030155 * anchor
    return base_signal.diff().diff()

def f49_ssa_155_jerk_v155_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=250, w2=238, w3=661, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(238, min_periods=max(238//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3618 * slope + 0.0030156 * anchor
    return base_signal.diff().diff()

def f49_ssa_156_accel_v156_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=6, w2=249, w3=674, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(6)
    drag = impulse.rolling(249, min_periods=max(249//3, 2)).mean()
    noise = impulse.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3925 + 0.0030157 * anchor
    return base_signal.diff().diff()

def f49_ssa_157_jerk_v157_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=13, w2=260, w3=687, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 13)
    acceleration = _rolling_slope(velocity, 260)
    curvature = _rolling_slope(acceleration, 687)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.377 * acceleration + 0.0030158 * anchor
    return base_signal.diff().diff()

def f49_ssa_158_accel_v158_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=20, w2=271, w3=700, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(271, min_periods=max(271//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.42125 + 0.0030159 * anchor
    return base_signal.diff().diff()

def f49_ssa_159_jerk_v159_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=27, w2=282, w3=713, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(282, min_periods=max(282//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3922 * _rolling_slope(draw, 713) + 0.003016 * anchor
    return base_signal.diff().diff()

def f49_ssa_160_accel_v160_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=34, w2=293, w3=726, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 34)
    baseline = trend.rolling(293, min_periods=max(293//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.45 + 0.0030161 * anchor
    return base_signal.diff().diff()

def f49_ssa_161_jerk_v161_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=41, w2=304, w3=739, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 41)
    slow = _rolling_slope(x, 304)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.464375 + 0.0030162 * anchor
    return base_signal.diff().diff()

def f49_ssa_162_accel_v162_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=48, w2=315, w3=752, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(315, min_periods=max(315//3, 2)).max()
    trough = x.rolling(48, min_periods=max(48//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47875 + 0.0030163 * anchor
    return base_signal.diff().diff()

def f49_ssa_163_jerk_v163_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=55, w2=326, w3=765, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(55)
    rank = change.rolling(326, min_periods=max(326//3, 2)).rank(pct=True)
    persistence = change.rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0462 * persistence + 0.0030164 * anchor
    return base_signal.diff().diff()

def f49_ssa_164_accel_v164_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=62, w2=337, w3=21, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(62, min_periods=max(62//3, 2)).std()
    vol_slow = ret.rolling(337, min_periods=max(337//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5075 + 0.0030165 * anchor
    return base_signal.diff().diff()

def f49_ssa_165_jerk_v165_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=69, w2=348, w3=34, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(348, min_periods=max(348//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 69)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0614 * slope + 0.0030166 * anchor
    return base_signal.diff().diff()

def f49_ssa_166_accel_v166_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=76, w2=359, w3=47, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(76)
    drag = impulse.rolling(359, min_periods=max(359//3, 2)).mean()
    noise = impulse.abs().rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.53625 + 0.0030167 * anchor
    return base_signal.diff().diff()

def f49_ssa_167_jerk_v167_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=83, w2=370, w3=60, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 83)
    acceleration = _rolling_slope(velocity, 370)
    curvature = _rolling_slope(acceleration, 60)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0766 * acceleration + 0.0030168 * anchor
    return base_signal.diff().diff()

def f49_ssa_168_accel_v168_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=90, w2=381, w3=73, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(381, min_periods=max(381//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(73) * 1.565 + 0.0030169 * anchor
    return base_signal.diff().diff()

def f49_ssa_169_jerk_v169_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=97, w2=392, w3=86, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(392, min_periods=max(392//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0918 * _rolling_slope(draw, 86) + 0.003017 * anchor
    return base_signal.diff().diff()

def f49_ssa_170_accel_v170_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=104, w2=403, w3=99, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 104)
    baseline = trend.rolling(403, min_periods=max(403//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59375 + 0.0030171 * anchor
    return base_signal.diff().diff()

def f49_ssa_171_jerk_v171_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=111, w2=414, w3=112, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 111)
    slow = _rolling_slope(x, 414)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=112, adjust=False).mean() * 1.608125 + 0.0030172 * anchor
    return base_signal.diff().diff()

def f49_ssa_172_accel_v172_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=118, w2=425, w3=125, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(425, min_periods=max(425//3, 2)).max()
    trough = x.rolling(118, min_periods=max(118//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6225 + 0.0030173 * anchor
    return base_signal.diff().diff()

def f49_ssa_173_jerk_v173_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=125, w2=436, w3=138, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(125)
    rank = change.rolling(436, min_periods=max(436//3, 2)).rank(pct=True)
    persistence = change.rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1222 * persistence + 0.0030174 * anchor
    return base_signal.diff().diff()

def f49_ssa_174_accel_v174_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=132, w2=447, w3=151, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(132, min_periods=max(132//3, 2)).std()
    vol_slow = ret.rolling(447, min_periods=max(447//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.878125 + 0.0030175 * anchor
    return base_signal.diff().diff()

def f49_ssa_175_jerk_v175_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=139, w2=458, w3=164, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(458, min_periods=max(458//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 139)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1374 * slope + 0.0030176 * anchor
    return base_signal.diff().diff()

def f49_ssa_176_accel_v176_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=146, w2=469, w3=177, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(469, min_periods=max(469//3, 2)).mean()
    noise = impulse.abs().rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.906875 + 0.0030177 * anchor
    return base_signal.diff().diff()

def f49_ssa_177_jerk_v177_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=153, w2=480, w3=190, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 153)
    acceleration = _rolling_slope(velocity, 480)
    curvature = _rolling_slope(acceleration, 190)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1526 * acceleration + 0.0030178 * anchor
    return base_signal.diff().diff()

def f49_ssa_178_accel_v178_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=160, w2=491, w3=203, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(160, min_periods=max(160//3, 2)).mean(), upside.rolling(491, min_periods=max(491//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.935625 + 0.0030179 * anchor
    return base_signal.diff().diff()

def f49_ssa_179_jerk_v179_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=167, w2=502, w3=216, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(502, min_periods=max(502//3, 2)).max()
    rebound = x - x.rolling(167, min_periods=max(167//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1678 * _rolling_slope(draw, 216) + 0.003018 * anchor
    return base_signal.diff().diff()

def f49_ssa_180_accel_v180_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=174, w2=10, w3=229, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 174)
    baseline = trend.rolling(10, min_periods=max(10//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.964375 + 0.0030181 * anchor
    return base_signal.diff().diff()

def f49_ssa_181_jerk_v181_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=181, w2=21, w3=242, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 181)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=242, adjust=False).mean() * 0.97875 + 0.0030182 * anchor
    return base_signal.diff().diff()

def f49_ssa_182_accel_v182_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=188, w2=32, w3=255, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(188, min_periods=max(188//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.993125 + 0.0030183 * anchor
    return base_signal.diff().diff()

def f49_ssa_183_jerk_v183_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=195, w2=43, w3=268, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1982 * persistence + 0.0030184 * anchor
    return base_signal.diff().diff()

def f49_ssa_184_accel_v184_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=202, w2=54, w3=281, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(202, min_periods=max(202//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.021875 + 0.0030185 * anchor
    return base_signal.diff().diff()

def f49_ssa_185_jerk_v185_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=209, w2=65, w3=294, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 209)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2134 * slope + 0.0030186 * anchor
    return base_signal.diff().diff()

def f49_ssa_186_accel_v186_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=216, w2=76, w3=307, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(76, min_periods=max(76//3, 2)).mean()
    noise = impulse.abs().rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.050625 + 0.0030187 * anchor
    return base_signal.diff().diff()

def f49_ssa_187_jerk_v187_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=223, w2=87, w3=320, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 223)
    acceleration = _rolling_slope(velocity, 87)
    curvature = _rolling_slope(acceleration, 320)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2286 * acceleration + 0.0030188 * anchor
    return base_signal.diff().diff()

def f49_ssa_188_accel_v188_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=230, w2=98, w3=333, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.079375 + 0.0030189 * anchor
    return base_signal.diff().diff()

def f49_ssa_189_jerk_v189_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=237, w2=109, w3=346, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(109, min_periods=max(109//3, 2)).max()
    rebound = x - x.rolling(237, min_periods=max(237//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2438 * _rolling_slope(draw, 346) + 0.003019 * anchor
    return base_signal.diff().diff()

def f49_ssa_190_accel_v190_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=244, w2=120, w3=359, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(120, min_periods=max(120//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.108125 + 0.0030191 * anchor
    return base_signal.diff().diff()

def f49_ssa_191_jerk_v191_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=251, w2=131, w3=372, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 131)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1225 + 0.0030192 * anchor
    return base_signal.diff().diff()

def f49_ssa_192_accel_v192_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=7, w2=142, w3=385, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(142, min_periods=max(142//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.136875 + 0.0030193 * anchor
    return base_signal.diff().diff()

def f49_ssa_193_jerk_v193_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=14, w2=153, w3=398, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(14)
    rank = change.rolling(153, min_periods=max(153//3, 2)).rank(pct=True)
    persistence = change.rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2742 * persistence + 0.0030194 * anchor
    return base_signal.diff().diff()

def f49_ssa_194_accel_v194_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=21, w2=164, w3=411, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(164, min_periods=max(164//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.165625 + 0.0030195 * anchor
    return base_signal.diff().diff()

def f49_ssa_195_jerk_v195_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=28, w2=175, w3=424, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(175, min_periods=max(175//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2894 * slope + 0.0030196 * anchor
    return base_signal.diff().diff()

def f49_ssa_196_accel_v196_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=35, w2=186, w3=437, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(35)
    drag = impulse.rolling(186, min_periods=max(186//3, 2)).mean()
    noise = impulse.abs().rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.194375 + 0.0030197 * anchor
    return base_signal.diff().diff()

def f49_ssa_197_jerk_v197_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=42, w2=197, w3=450, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 197)
    curvature = _rolling_slope(acceleration, 450)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3046 * acceleration + 0.0030198 * anchor
    return base_signal.diff().diff()

def f49_ssa_198_accel_v198_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=49, w2=208, w3=463, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(208, min_periods=max(208//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.223125 + 0.0030199 * anchor
    return base_signal.diff().diff()

def f49_ssa_199_jerk_v199_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=56, w2=219, w3=476, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(219, min_periods=max(219//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3198 * _rolling_slope(draw, 476) + 0.00302 * anchor
    return base_signal.diff().diff()

def f49_ssa_200_accel_v200_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=63, w2=230, w3=489, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(230, min_periods=max(230//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.251875 + 0.0030201 * anchor
    return base_signal.diff().diff()

def f49_ssa_201_jerk_v201_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=70, w2=241, w3=502, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 241)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.26625 + 0.0030202 * anchor
    return base_signal.diff().diff()

def f49_ssa_202_accel_v202_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=77, w2=252, w3=515, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(252, min_periods=max(252//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.280625 + 0.0030203 * anchor
    return base_signal.diff().diff()

def f49_ssa_203_jerk_v203_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=84, w2=263, w3=528, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(84)
    rank = change.rolling(263, min_periods=max(263//3, 2)).rank(pct=True)
    persistence = change.rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3502 * persistence + 0.0030204 * anchor
    return base_signal.diff().diff()

def f49_ssa_204_accel_v204_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=91, w2=274, w3=541, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(274, min_periods=max(274//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.309375 + 0.0030205 * anchor
    return base_signal.diff().diff()

def f49_ssa_205_jerk_v205_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=98, w2=285, w3=554, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3654 * slope + 0.0030206 * anchor
    return base_signal.diff().diff()

def f49_ssa_206_accel_v206_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=105, w2=296, w3=567, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(105)
    drag = impulse.rolling(296, min_periods=max(296//3, 2)).mean()
    noise = impulse.abs().rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.338125 + 0.0030207 * anchor
    return base_signal.diff().diff()

def f49_ssa_207_jerk_v207_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=112, w2=307, w3=580, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 307)
    curvature = _rolling_slope(acceleration, 580)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3806 * acceleration + 0.0030208 * anchor
    return base_signal.diff().diff()

def f49_ssa_208_accel_v208_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=119, w2=318, w3=593, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(318, min_periods=max(318//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.366875 + 0.0030209 * anchor
    return base_signal.diff().diff()

def f49_ssa_209_jerk_v209_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=126, w2=329, w3=606, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(329, min_periods=max(329//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3958 * _rolling_slope(draw, 606) + 0.003021 * anchor
    return base_signal.diff().diff()

def f49_ssa_210_accel_v210_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=133, w2=340, w3=619, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(340, min_periods=max(340//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.395625 + 0.0030211 * anchor
    return base_signal.diff().diff()

def f49_ssa_211_jerk_v211_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=140, w2=351, w3=632, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.41 + 0.0030212 * anchor
    return base_signal.diff().diff()

def f49_ssa_212_accel_v212_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=147, w2=362, w3=645, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(362, min_periods=max(362//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.424375 + 0.0030213 * anchor
    return base_signal.diff().diff()

def f49_ssa_213_jerk_v213_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=154, w2=373, w3=658, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0498 * persistence + 0.0030214 * anchor
    return base_signal.diff().diff()

def f49_ssa_214_accel_v214_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=161, w2=384, w3=671, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(384, min_periods=max(384//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.453125 + 0.0030215 * anchor
    return base_signal.diff().diff()

def f49_ssa_215_jerk_v215_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=168, w2=395, w3=684, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.065 * slope + 0.0030216 * anchor
    return base_signal.diff().diff()

def f49_ssa_216_accel_v216_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=175, w2=406, w3=697, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(406, min_periods=max(406//3, 2)).mean()
    noise = impulse.abs().rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.481875 + 0.0030217 * anchor
    return base_signal.diff().diff()

def f49_ssa_217_jerk_v217_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=182, w2=417, w3=710, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 417)
    curvature = _rolling_slope(acceleration, 710)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0802 * acceleration + 0.0030218 * anchor
    return base_signal.diff().diff()

def f49_ssa_218_accel_v218_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=189, w2=428, w3=723, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(428, min_periods=max(428//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.510625 + 0.0030219 * anchor
    return base_signal.diff().diff()

def f49_ssa_219_jerk_v219_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=196, w2=439, w3=736, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(439, min_periods=max(439//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0954 * _rolling_slope(draw, 736) + 0.003022 * anchor
    return base_signal.diff().diff()

def f49_ssa_220_accel_v220_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=203, w2=450, w3=749, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.539375 + 0.0030221 * anchor
    return base_signal.diff().diff()

def f49_ssa_221_jerk_v221_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=210, w2=461, w3=762, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 461)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.55375 + 0.0030222 * anchor
    return base_signal.diff().diff()

def f49_ssa_222_accel_v222_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=217, w2=472, w3=18, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(472, min_periods=max(472//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.568125 + 0.0030223 * anchor
    return base_signal.diff().diff()

def f49_ssa_223_jerk_v223_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=224, w2=483, w3=31, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(483, min_periods=max(483//3, 2)).rank(pct=True)
    persistence = change.rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1258 * persistence + 0.0030224 * anchor
    return base_signal.diff().diff()

def f49_ssa_224_accel_v224_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=231, w2=494, w3=44, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(494, min_periods=max(494//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.596875 + 0.0030225 * anchor
    return base_signal.diff().diff()

def f49_ssa_225_jerk_v225_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=238, w2=505, w3=57, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.141 * slope + 0.0030226 * anchor
    return base_signal.diff().diff()
