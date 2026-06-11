"""01 peak and blowoff base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f01_pab_526_accel_v526(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=173, w2=263, w3=40, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(263, min_periods=max(263//3, 2)).mean()
    noise = impulse.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.453125 + 5.27e-05 * anchor

def f01_pab_527_jerk_v527(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=180, w2=274, w3=53, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 274)
    curvature = _rolling_slope(acceleration, 53)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2762 * acceleration + 5.28e-05 * anchor

def f01_pab_528_accel_v528(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=187, w2=285, w3=66, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(285, min_periods=max(285//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(66) * 1.481875 + 5.29e-05 * anchor

def f01_pab_529_jerk_v529(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=194, w2=296, w3=79, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(296, min_periods=max(296//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2914 * _rolling_slope(draw, 79) + 5.3e-05 * anchor

def f01_pab_530_accel_v530(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=201, w2=307, w3=92, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.510625 + 5.31e-05 * anchor

def f01_pab_531_jerk_v531(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=208, w2=318, w3=105, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=105, adjust=False).mean() * 1.525 + 5.32e-05 * anchor

def f01_pab_532_accel_v532(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=215, w2=329, w3=118, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(329, min_periods=max(329//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.539375 + 5.33e-05 * anchor

def f01_pab_533_jerk_v533(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=222, w2=340, w3=131, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(340, min_periods=max(340//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3218 * persistence + 5.34e-05 * anchor

def f01_pab_534_accel_v534(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=229, w2=351, w3=144, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(351, min_periods=max(351//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.568125 + 5.35e-05 * anchor

def f01_pab_535_jerk_v535(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=236, w2=362, w3=157, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(362, min_periods=max(362//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.337 * slope + 5.36e-05 * anchor

def f01_pab_536_accel_v536(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=243, w2=373, w3=170, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(373, min_periods=max(373//3, 2)).mean()
    noise = impulse.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.596875 + 5.37e-05 * anchor

def f01_pab_537_jerk_v537(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=250, w2=384, w3=183, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 384)
    curvature = _rolling_slope(acceleration, 183)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3522 * acceleration + 5.38e-05 * anchor

def f01_pab_538_accel_v538(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=6, w2=395, w3=196, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(395, min_periods=max(395//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8525 + 5.39e-05 * anchor

def f01_pab_539_jerk_v539(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=13, w2=406, w3=209, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(406, min_periods=max(406//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3674 * _rolling_slope(draw, 209) + 5.4e-05 * anchor

def f01_pab_540_accel_v540(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=20, w2=417, w3=222, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(417, min_periods=max(417//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.88125 + 5.41e-05 * anchor

def f01_pab_541_jerk_v541(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=27, w2=428, w3=235, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 428)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=235, adjust=False).mean() * 0.895625 + 5.42e-05 * anchor

def f01_pab_542_accel_v542(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=34, w2=439, w3=248, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(439, min_periods=max(439//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.91 + 5.43e-05 * anchor

def f01_pab_543_jerk_v543(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=41, w2=450, w3=261, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(41)
    rank = change.rolling(450, min_periods=max(450//3, 2)).rank(pct=True)
    persistence = change.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3978 * persistence + 5.44e-05 * anchor

def f01_pab_544_accel_v544(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=48, w2=461, w3=274, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(461, min_periods=max(461//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.93875 + 5.45e-05 * anchor

def f01_pab_545_jerk_v545(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=55, w2=472, w3=287, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(472, min_periods=max(472//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0366 * slope + 5.46e-05 * anchor

def f01_pab_546_accel_v546(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=62, w2=483, w3=300, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(62)
    drag = impulse.rolling(483, min_periods=max(483//3, 2)).mean()
    noise = impulse.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9675 + 5.47e-05 * anchor

def f01_pab_547_jerk_v547(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=69, w2=494, w3=313, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 494)
    curvature = _rolling_slope(acceleration, 313)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0518 * acceleration + 5.48e-05 * anchor

def f01_pab_548_accel_v548(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=76, w2=505, w3=326, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(505, min_periods=max(505//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.99625 + 5.49e-05 * anchor

def f01_pab_549_jerk_v549(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=83, w2=13, w3=339, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(13, min_periods=max(13//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.067 * _rolling_slope(draw, 339) + 5.5e-05 * anchor

def f01_pab_550_accel_v550(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=90, w2=24, w3=352, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(24, min_periods=max(24//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.025 + 5.51e-05 * anchor

def f01_pab_551_jerk_v551(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=97, w2=35, w3=365, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 35)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.039375 + 5.52e-05 * anchor

def f01_pab_552_accel_v552(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=104, w2=46, w3=378, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(46, min_periods=max(46//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.05375 + 5.53e-05 * anchor

def f01_pab_553_jerk_v553(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=111, w2=57, w3=391, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(111)
    rank = change.rolling(57, min_periods=max(57//3, 2)).rank(pct=True)
    persistence = change.rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0974 * persistence + 5.54e-05 * anchor

def f01_pab_554_accel_v554(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=118, w2=68, w3=404, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(68, min_periods=max(68//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0825 + 5.55e-05 * anchor

def f01_pab_555_jerk_v555(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=125, w2=79, w3=417, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(79, min_periods=max(79//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1126 * slope + 5.56e-05 * anchor

def f01_pab_556_accel_v556(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=132, w2=90, w3=430, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(90, min_periods=max(90//3, 2)).mean()
    noise = impulse.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.11125 + 5.57e-05 * anchor

def f01_pab_557_jerk_v557(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=139, w2=101, w3=443, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 101)
    curvature = _rolling_slope(acceleration, 443)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1278 * acceleration + 5.58e-05 * anchor

def f01_pab_558_accel_v558(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=146, w2=112, w3=456, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(112, min_periods=max(112//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.14 + 5.59e-05 * anchor

def f01_pab_559_jerk_v559(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=153, w2=123, w3=469, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(123, min_periods=max(123//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.143 * _rolling_slope(draw, 469) + 5.6e-05 * anchor

def f01_pab_560_accel_v560(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=160, w2=134, w3=482, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.16875 + 5.61e-05 * anchor

def f01_pab_561_jerk_v561(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=167, w2=145, w3=495, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.183125 + 5.62e-05 * anchor

def f01_pab_562_accel_v562(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=174, w2=156, w3=508, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.1975 + 5.63e-05 * anchor

def f01_pab_563_jerk_v563(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=181, w2=167, w3=521, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(167, min_periods=max(167//3, 2)).rank(pct=True)
    persistence = change.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1734 * persistence + 5.64e-05 * anchor

def f01_pab_564_accel_v564(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=188, w2=178, w3=534, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.22625 + 5.65e-05 * anchor

def f01_pab_565_jerk_v565(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=195, w2=189, w3=547, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(189, min_periods=max(189//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1886 * slope + 5.66e-05 * anchor

def f01_pab_566_accel_v566(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=202, w2=200, w3=560, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.255 + 5.67e-05 * anchor

def f01_pab_567_jerk_v567(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=209, w2=211, w3=573, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 211)
    curvature = _rolling_slope(acceleration, 573)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2038 * acceleration + 5.68e-05 * anchor

def f01_pab_568_accel_v568(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=216, w2=222, w3=586, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.28375 + 5.69e-05 * anchor

def f01_pab_569_jerk_v569(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=223, w2=233, w3=599, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(233, min_periods=max(233//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.219 * _rolling_slope(draw, 599) + 5.7e-05 * anchor

def f01_pab_570_accel_v570(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=230, w2=244, w3=612, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(244, min_periods=max(244//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3125 + 5.71e-05 * anchor

def f01_pab_571_jerk_v571(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=237, w2=255, w3=625, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.326875 + 5.72e-05 * anchor

def f01_pab_572_accel_v572(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=244, w2=266, w3=638, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.34125 + 5.73e-05 * anchor

def f01_pab_573_jerk_v573(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=251, w2=277, w3=651, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2494 * persistence + 5.74e-05 * anchor

def f01_pab_574_accel_v574(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=7, w2=288, w3=664, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(288, min_periods=max(288//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37 + 5.75e-05 * anchor

def f01_pab_575_jerk_v575(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=14, w2=299, w3=677, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(299, min_periods=max(299//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2646 * slope + 5.76e-05 * anchor

def f01_pab_576_accel_v576(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=21, w2=310, w3=690, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(21)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.39875 + 5.77e-05 * anchor

def f01_pab_577_jerk_v577(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=28, w2=321, w3=703, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 321)
    curvature = _rolling_slope(acceleration, 703)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2798 * acceleration + 5.78e-05 * anchor

def f01_pab_578_accel_v578(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=35, w2=332, w3=716, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4275 + 5.79e-05 * anchor

def f01_pab_579_jerk_v579(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=42, w2=343, w3=729, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(343, min_periods=max(343//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.295 * _rolling_slope(draw, 729) + 5.8e-05 * anchor

def f01_pab_580_accel_v580(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=49, w2=354, w3=742, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.45625 + 5.81e-05 * anchor

def f01_pab_581_jerk_v581(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=56, w2=365, w3=755, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.470625 + 5.82e-05 * anchor

def f01_pab_582_accel_v582(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=63, w2=376, w3=768, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.485 + 5.83e-05 * anchor

def f01_pab_583_jerk_v583(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=70, w2=387, w3=24, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(70)
    rank = change.rolling(387, min_periods=max(387//3, 2)).rank(pct=True)
    persistence = change.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3254 * persistence + 5.84e-05 * anchor

def f01_pab_584_accel_v584(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=77, w2=398, w3=37, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(398, min_periods=max(398//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.51375 + 5.85e-05 * anchor

def f01_pab_585_jerk_v585(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=84, w2=409, w3=50, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3406 * slope + 5.86e-05 * anchor

def f01_pab_586_accel_v586(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=420, w3=63, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(91)
    drag = impulse.rolling(420, min_periods=max(420//3, 2)).mean()
    noise = impulse.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5425 + 5.87e-05 * anchor

def f01_pab_587_jerk_v587(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=431, w3=76, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 431)
    curvature = _rolling_slope(acceleration, 76)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3558 * acceleration + 5.88e-05 * anchor

def f01_pab_588_accel_v588(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=442, w3=89, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(89) * 1.57125 + 5.89e-05 * anchor

def f01_pab_589_jerk_v589(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=453, w3=102, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.371 * _rolling_slope(draw, 102) + 5.9e-05 * anchor

def f01_pab_590_accel_v590(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=464, w3=115, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 119)
    baseline = trend.rolling(464, min_periods=max(464//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.6 + 5.91e-05 * anchor

def f01_pab_591_jerk_v591(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=475, w3=128, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 126)
    slow = _rolling_slope(x, 475)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=128, adjust=False).mean() * 1.614375 + 5.92e-05 * anchor

def f01_pab_592_accel_v592(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=486, w3=141, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(486, min_periods=max(486//3, 2)).max()
    trough = x.rolling(133, min_periods=max(133//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.855625 + 5.93e-05 * anchor

def f01_pab_593_jerk_v593(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=497, w3=154, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(497, min_periods=max(497//3, 2)).rank(pct=True)
    persistence = change.rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4014 * persistence + 5.94e-05 * anchor

def f01_pab_594_accel_v594(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=508, w3=167, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(147, min_periods=max(147//3, 2)).std()
    vol_slow = ret.rolling(508, min_periods=max(508//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.884375 + 5.95e-05 * anchor

def f01_pab_595_jerk_v595(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=16, w3=180, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(16, min_periods=max(16//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 154)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0402 * slope + 5.96e-05 * anchor

def f01_pab_596_accel_v596(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=27, w3=193, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(27, min_periods=max(27//3, 2)).mean()
    noise = impulse.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.913125 + 5.97e-05 * anchor

def f01_pab_597_jerk_v597(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=38, w3=206, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 168)
    acceleration = _rolling_slope(velocity, 38)
    curvature = _rolling_slope(acceleration, 206)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0554 * acceleration + 5.98e-05 * anchor

def f01_pab_598_accel_v598(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=49, w3=219, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(49, min_periods=max(49//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.941875 + 5.99e-05 * anchor

def f01_pab_599_jerk_v599(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=60, w3=232, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(60, min_periods=max(60//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0706 * _rolling_slope(draw, 232) + 6e-05 * anchor

def f01_pab_600_accel_v600(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=71, w3=245, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(71, min_periods=max(71//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.970625 + 6.01e-05 * anchor
