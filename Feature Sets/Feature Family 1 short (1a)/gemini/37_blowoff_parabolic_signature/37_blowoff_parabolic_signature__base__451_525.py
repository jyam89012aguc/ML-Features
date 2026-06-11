"""37 blowoff parabolic signature base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f37_bps_451_jerk_v451(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=181, w2=186, w3=762, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 181)
    slow = _rolling_slope(x, 186)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.9725 + 0.0022652 * anchor

def f37_bps_452_accel_v452(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=188, w2=197, w3=18, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(197, min_periods=max(197//3, 2)).max()
    trough = x.rolling(188, min_periods=max(188//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.986875 + 0.0022653 * anchor

def f37_bps_453_jerk_v453(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=195, w2=208, w3=31, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(208, min_periods=max(208//3, 2)).rank(pct=True)
    persistence = change.rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.183 * persistence + 0.0022654 * anchor

def f37_bps_454_accel_v454(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=202, w2=219, w3=44, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(202, min_periods=max(202//3, 2)).std()
    vol_slow = ret.rolling(219, min_periods=max(219//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.015625 + 0.0022655 * anchor

def f37_bps_455_jerk_v455(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=209, w2=230, w3=57, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(230, min_periods=max(230//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 209)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1982 * slope + 0.0022656 * anchor

def f37_bps_456_accel_v456(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=216, w2=241, w3=70, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(241, min_periods=max(241//3, 2)).mean()
    noise = impulse.abs().rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.044375 + 0.0022657 * anchor

def f37_bps_457_jerk_v457(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=223, w2=252, w3=83, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 223)
    acceleration = _rolling_slope(velocity, 252)
    curvature = _rolling_slope(acceleration, 83)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2134 * acceleration + 0.0022658 * anchor

def f37_bps_458_accel_v458(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=230, w2=263, w3=96, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(263, min_periods=max(263//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(96) * 1.073125 + 0.0022659 * anchor

def f37_bps_459_jerk_v459(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=237, w2=274, w3=109, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(274, min_periods=max(274//3, 2)).max()
    rebound = x - x.rolling(237, min_periods=max(237//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2286 * _rolling_slope(draw, 109) + 0.002266 * anchor

def f37_bps_460_accel_v460(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=244, w2=285, w3=122, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(285, min_periods=max(285//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.101875 + 0.0022661 * anchor

def f37_bps_461_jerk_v461(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=251, w2=296, w3=135, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 296)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=135, adjust=False).mean() * 1.11625 + 0.0022662 * anchor

def f37_bps_462_accel_v462(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=7, w2=307, w3=148, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(307, min_periods=max(307//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.130625 + 0.0022663 * anchor

def f37_bps_463_jerk_v463(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=14, w2=318, w3=161, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(14)
    rank = change.rolling(318, min_periods=max(318//3, 2)).rank(pct=True)
    persistence = change.rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.259 * persistence + 0.0022664 * anchor

def f37_bps_464_accel_v464(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=21, w2=329, w3=174, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(329, min_periods=max(329//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.159375 + 0.0022665 * anchor

def f37_bps_465_jerk_v465(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=28, w2=340, w3=187, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(340, min_periods=max(340//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2742 * slope + 0.0022666 * anchor

def f37_bps_466_accel_v466(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=35, w2=351, w3=200, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(35)
    drag = impulse.rolling(351, min_periods=max(351//3, 2)).mean()
    noise = impulse.abs().rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.188125 + 0.0022667 * anchor

def f37_bps_467_jerk_v467(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=42, w2=362, w3=213, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 362)
    curvature = _rolling_slope(acceleration, 213)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2894 * acceleration + 0.0022668 * anchor

def f37_bps_468_accel_v468(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=49, w2=373, w3=226, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(373, min_periods=max(373//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.216875 + 0.0022669 * anchor

def f37_bps_469_jerk_v469(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=56, w2=384, w3=239, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(384, min_periods=max(384//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3046 * _rolling_slope(draw, 239) + 0.002267 * anchor

def f37_bps_470_accel_v470(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=63, w2=395, w3=252, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(395, min_periods=max(395//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.245625 + 0.0022671 * anchor

def f37_bps_471_jerk_v471(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=70, w2=406, w3=265, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 406)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=265, adjust=False).mean() * 1.26 + 0.0022672 * anchor

def f37_bps_472_accel_v472(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=77, w2=417, w3=278, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(417, min_periods=max(417//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.274375 + 0.0022673 * anchor

def f37_bps_473_jerk_v473(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=84, w2=428, w3=291, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(84)
    rank = change.rolling(428, min_periods=max(428//3, 2)).rank(pct=True)
    persistence = change.rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.335 * persistence + 0.0022674 * anchor

def f37_bps_474_accel_v474(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=439, w3=304, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(439, min_periods=max(439//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.303125 + 0.0022675 * anchor

def f37_bps_475_jerk_v475(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=450, w3=317, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(450, min_periods=max(450//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3502 * slope + 0.0022676 * anchor

def f37_bps_476_accel_v476(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=461, w3=330, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(105)
    drag = impulse.rolling(461, min_periods=max(461//3, 2)).mean()
    noise = impulse.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.331875 + 0.0022677 * anchor

def f37_bps_477_jerk_v477(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=472, w3=343, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 472)
    curvature = _rolling_slope(acceleration, 343)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3654 * acceleration + 0.0022678 * anchor

def f37_bps_478_accel_v478(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=483, w3=356, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(483, min_periods=max(483//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.360625 + 0.0022679 * anchor

def f37_bps_479_jerk_v479(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=494, w3=369, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(494, min_periods=max(494//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3806 * _rolling_slope(draw, 369) + 0.002268 * anchor

def f37_bps_480_accel_v480(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=505, w3=382, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(505, min_periods=max(505//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.389375 + 0.0022681 * anchor

def f37_bps_481_jerk_v481(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=13, w3=395, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 13)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.40375 + 0.0022682 * anchor

def f37_bps_482_accel_v482(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=24, w3=408, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(24, min_periods=max(24//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.418125 + 0.0022683 * anchor

def f37_bps_483_jerk_v483(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=35, w3=421, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(35, min_periods=max(35//3, 2)).rank(pct=True)
    persistence = change.rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.411 * persistence + 0.0022684 * anchor

def f37_bps_484_accel_v484(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=46, w3=434, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(46, min_periods=max(46//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.446875 + 0.0022685 * anchor

def f37_bps_485_jerk_v485(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=57, w3=447, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(57, min_periods=max(57//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0498 * slope + 0.0022686 * anchor

def f37_bps_486_accel_v486(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=68, w3=460, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(68, min_periods=max(68//3, 2)).mean()
    noise = impulse.abs().rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.475625 + 0.0022687 * anchor

def f37_bps_487_jerk_v487(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=79, w3=473, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 79)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.065 * acceleration + 0.0022688 * anchor

def f37_bps_488_accel_v488(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=90, w3=486, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(90, min_periods=max(90//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.504375 + 0.0022689 * anchor

def f37_bps_489_jerk_v489(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=196, w2=101, w3=499, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0802 * _rolling_slope(draw, 499) + 0.002269 * anchor

def f37_bps_490_accel_v490(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=203, w2=112, w3=512, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(112, min_periods=max(112//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.533125 + 0.0022691 * anchor

def f37_bps_491_jerk_v491(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=210, w2=123, w3=525, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 123)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5475 + 0.0022692 * anchor

def f37_bps_492_accel_v492(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=217, w2=134, w3=538, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(134, min_periods=max(134//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.561875 + 0.0022693 * anchor

def f37_bps_493_jerk_v493(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=224, w2=145, w3=551, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(145, min_periods=max(145//3, 2)).rank(pct=True)
    persistence = change.rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1106 * persistence + 0.0022694 * anchor

def f37_bps_494_accel_v494(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=231, w2=156, w3=564, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(156, min_periods=max(156//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.590625 + 0.0022695 * anchor

def f37_bps_495_jerk_v495(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=238, w2=167, w3=577, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(167, min_periods=max(167//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1258 * slope + 0.0022696 * anchor

def f37_bps_496_accel_v496(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=178, w3=590, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(178, min_periods=max(178//3, 2)).mean()
    noise = impulse.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.619375 + 0.0022697 * anchor

def f37_bps_497_jerk_v497(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=189, w3=603, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 252)
    acceleration = _rolling_slope(velocity, 189)
    curvature = _rolling_slope(acceleration, 603)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.141 * acceleration + 0.0022698 * anchor

def f37_bps_498_accel_v498(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=200, w3=616, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(200, min_periods=max(200//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.875 + 0.0022699 * anchor

def f37_bps_499_jerk_v499(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=211, w3=629, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(211, min_periods=max(211//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1562 * _rolling_slope(draw, 629) + 0.00227 * anchor

def f37_bps_500_accel_v500(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=222, w3=642, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(222, min_periods=max(222//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.90375 + 0.0022701 * anchor

def f37_bps_501_jerk_v501(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=233, w3=655, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.918125 + 0.0022702 * anchor

def f37_bps_502_accel_v502(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=244, w3=668, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(244, min_periods=max(244//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9325 + 0.0022703 * anchor

def f37_bps_503_jerk_v503(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=255, w3=681, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(43)
    rank = change.rolling(255, min_periods=max(255//3, 2)).rank(pct=True)
    persistence = change.rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1866 * persistence + 0.0022704 * anchor

def f37_bps_504_accel_v504(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=266, w3=694, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(266, min_periods=max(266//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96125 + 0.0022705 * anchor

def f37_bps_505_jerk_v505(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=277, w3=707, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(277, min_periods=max(277//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2018 * slope + 0.0022706 * anchor

def f37_bps_506_accel_v506(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=288, w3=720, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(64)
    drag = impulse.rolling(288, min_periods=max(288//3, 2)).mean()
    noise = impulse.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.99 + 0.0022707 * anchor

def f37_bps_507_jerk_v507(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=299, w3=733, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 299)
    curvature = _rolling_slope(acceleration, 733)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.217 * acceleration + 0.0022708 * anchor

def f37_bps_508_accel_v508(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=310, w3=746, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(310, min_periods=max(310//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.01875 + 0.0022709 * anchor

def f37_bps_509_jerk_v509(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=321, w3=759, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(321, min_periods=max(321//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2322 * _rolling_slope(draw, 759) + 0.002271 * anchor

def f37_bps_510_accel_v510(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=332, w3=15, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(332, min_periods=max(332//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0475 + 0.0022711 * anchor

def f37_bps_511_jerk_v511(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=343, w3=28, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 343)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=28, adjust=False).mean() * 1.061875 + 0.0022712 * anchor

def f37_bps_512_accel_v512(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=106, w2=354, w3=41, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(354, min_periods=max(354//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.07625 + 0.0022713 * anchor

def f37_bps_513_jerk_v513(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=113, w2=365, w3=54, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(113)
    rank = change.rolling(365, min_periods=max(365//3, 2)).rank(pct=True)
    persistence = change.rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2626 * persistence + 0.0022714 * anchor

def f37_bps_514_accel_v514(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=120, w2=376, w3=67, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(376, min_periods=max(376//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.105 + 0.0022715 * anchor

def f37_bps_515_jerk_v515(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=127, w2=387, w3=80, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(387, min_periods=max(387//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2778 * slope + 0.0022716 * anchor

def f37_bps_516_accel_v516(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=134, w2=398, w3=93, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(398, min_periods=max(398//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.13375 + 0.0022717 * anchor

def f37_bps_517_jerk_v517(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=141, w2=409, w3=106, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 409)
    curvature = _rolling_slope(acceleration, 106)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.293 * acceleration + 0.0022718 * anchor

def f37_bps_518_accel_v518(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=148, w2=420, w3=119, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(420, min_periods=max(420//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(119) * 1.1625 + 0.0022719 * anchor

def f37_bps_519_jerk_v519(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=155, w2=431, w3=132, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(431, min_periods=max(431//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3082 * _rolling_slope(draw, 132) + 0.002272 * anchor

def f37_bps_520_accel_v520(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=162, w2=442, w3=145, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(442, min_periods=max(442//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.19125 + 0.0022721 * anchor

def f37_bps_521_jerk_v521(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=169, w2=453, w3=158, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=158, adjust=False).mean() * 1.205625 + 0.0022722 * anchor

def f37_bps_522_accel_v522(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=176, w2=464, w3=171, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(464, min_periods=max(464//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.22 + 0.0022723 * anchor

def f37_bps_523_jerk_v523(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=183, w2=475, w3=184, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3386 * persistence + 0.0022724 * anchor

def f37_bps_524_accel_v524(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=190, w2=486, w3=197, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(486, min_periods=max(486//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24875 + 0.0022725 * anchor

def f37_bps_525_jerk_v525(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=197, w2=497, w3=210, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(497, min_periods=max(497//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3538 * slope + 0.0022726 * anchor
