"""08 moving average extension dynamics base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f08_mae_001_jerk_v1(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=45, w2=448, w3=124, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=124, adjust=False).mean() * 0.935625 + 0.0004202 * anchor

def f08_mae_002_accel_v2(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=52, w2=459, w3=137, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(459, min_periods=max(459//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.95 + 0.0004203 * anchor

def f08_mae_003_jerk_v3(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=59, w2=470, w3=150, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(59)
    rank = change.rolling(470, min_periods=max(470//3, 2)).rank(pct=True)
    persistence = change.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3602 * persistence + 0.0004204 * anchor

def f08_mae_004_accel_v4(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=66, w2=481, w3=163, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(481, min_periods=max(481//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97875 + 0.0004205 * anchor

def f08_mae_005_jerk_v5(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=73, w2=492, w3=176, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(492, min_periods=max(492//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3754 * slope + 0.0004206 * anchor

def f08_mae_006_accel_v6(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=80, w2=503, w3=189, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(80)
    drag = impulse.rolling(503, min_periods=max(503//3, 2)).mean()
    noise = impulse.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0075 + 0.0004207 * anchor

def f08_mae_007_jerk_v7(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=87, w2=11, w3=202, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 11)
    curvature = _rolling_slope(acceleration, 202)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3906 * acceleration + 0.0004208 * anchor

def f08_mae_008_accel_v8(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=94, w2=22, w3=215, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(22, min_periods=max(22//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.03625 + 0.0004209 * anchor

def f08_mae_009_jerk_v9(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=101, w2=33, w3=228, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(33, min_periods=max(33//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4058 * _rolling_slope(draw, 228) + 0.000421 * anchor

def f08_mae_010_accel_v10(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=108, w2=44, w3=241, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(44, min_periods=max(44//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.065 + 0.0004211 * anchor

def f08_mae_011_jerk_v11(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=115, w2=55, w3=254, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 55)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=254, adjust=False).mean() * 1.079375 + 0.0004212 * anchor

def f08_mae_012_accel_v12(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=122, w2=66, w3=267, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(66, min_periods=max(66//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.09375 + 0.0004213 * anchor

def f08_mae_013_jerk_v13(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=129, w2=77, w3=280, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(77, min_periods=max(77//3, 2)).rank(pct=True)
    persistence = change.rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0598 * persistence + 0.0004214 * anchor

def f08_mae_014_accel_v14(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=136, w2=88, w3=293, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(88, min_periods=max(88//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1225 + 0.0004215 * anchor

def f08_mae_015_jerk_v15(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=143, w2=99, w3=306, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(99, min_periods=max(99//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.075 * slope + 0.0004216 * anchor

def f08_mae_016_accel_v16(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=150, w2=110, w3=319, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(110, min_periods=max(110//3, 2)).mean()
    noise = impulse.abs().rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.15125 + 0.0004217 * anchor

def f08_mae_017_jerk_v17(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=157, w2=121, w3=332, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 121)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0902 * acceleration + 0.0004218 * anchor

def f08_mae_018_accel_v18(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=164, w2=132, w3=345, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(132, min_periods=max(132//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.18 + 0.0004219 * anchor

def f08_mae_019_jerk_v19(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=171, w2=143, w3=358, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(143, min_periods=max(143//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1054 * _rolling_slope(draw, 358) + 0.000422 * anchor

def f08_mae_020_accel_v20(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=178, w2=154, w3=371, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(154, min_periods=max(154//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.20875 + 0.0004221 * anchor

def f08_mae_021_jerk_v21(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=185, w2=165, w3=384, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 165)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.223125 + 0.0004222 * anchor

def f08_mae_022_accel_v22(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=192, w2=176, w3=397, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(176, min_periods=max(176//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2375 + 0.0004223 * anchor

def f08_mae_023_jerk_v23(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=199, w2=187, w3=410, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(187, min_periods=max(187//3, 2)).rank(pct=True)
    persistence = change.rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1358 * persistence + 0.0004224 * anchor

def f08_mae_024_accel_v24(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=206, w2=198, w3=423, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(198, min_periods=max(198//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26625 + 0.0004225 * anchor

def f08_mae_025_jerk_v25(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=213, w2=209, w3=436, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(209, min_periods=max(209//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.151 * slope + 0.0004226 * anchor

def f08_mae_026_accel_v26(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=220, w2=220, w3=449, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(220, min_periods=max(220//3, 2)).mean()
    noise = impulse.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.295 + 0.0004227 * anchor

def f08_mae_027_jerk_v27(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=227, w2=231, w3=462, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 231)
    curvature = _rolling_slope(acceleration, 462)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1662 * acceleration + 0.0004228 * anchor

def f08_mae_028_accel_v28(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=234, w2=242, w3=475, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(242, min_periods=max(242//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.32375 + 0.0004229 * anchor

def f08_mae_029_jerk_v29(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=241, w2=253, w3=488, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(253, min_periods=max(253//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1814 * _rolling_slope(draw, 488) + 0.000423 * anchor

def f08_mae_030_accel_v30(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=248, w2=264, w3=501, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(264, min_periods=max(264//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3525 + 0.0004231 * anchor

def f08_mae_031_jerk_v31(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=255, w2=275, w3=514, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 255)
    slow = _rolling_slope(x, 275)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.366875 + 0.0004232 * anchor

def f08_mae_032_accel_v32(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=11, w2=286, w3=527, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(286, min_periods=max(286//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.38125 + 0.0004233 * anchor

def f08_mae_033_jerk_v33(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=18, w2=297, w3=540, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(18)
    rank = change.rolling(297, min_periods=max(297//3, 2)).rank(pct=True)
    persistence = change.rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2118 * persistence + 0.0004234 * anchor

def f08_mae_034_accel_v34(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=25, w2=308, w3=553, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(308, min_periods=max(308//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41 + 0.0004235 * anchor

def f08_mae_035_jerk_v35(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=32, w2=319, w3=566, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(319, min_periods=max(319//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.227 * slope + 0.0004236 * anchor

def f08_mae_036_accel_v36(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=39, w2=330, w3=579, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(39)
    drag = impulse.rolling(330, min_periods=max(330//3, 2)).mean()
    noise = impulse.abs().rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.43875 + 0.0004237 * anchor

def f08_mae_037_jerk_v37(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=46, w2=341, w3=592, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 341)
    curvature = _rolling_slope(acceleration, 592)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2422 * acceleration + 0.0004238 * anchor

def f08_mae_038_accel_v38(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=53, w2=352, w3=605, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(352, min_periods=max(352//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4675 + 0.0004239 * anchor

def f08_mae_039_jerk_v39(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=60, w2=363, w3=618, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(363, min_periods=max(363//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2574 * _rolling_slope(draw, 618) + 0.000424 * anchor

def f08_mae_040_accel_v40(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=67, w2=374, w3=631, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(374, min_periods=max(374//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.49625 + 0.0004241 * anchor

def f08_mae_041_jerk_v41(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=74, w2=385, w3=644, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 385)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.510625 + 0.0004242 * anchor

def f08_mae_042_accel_v42(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=81, w2=396, w3=657, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(396, min_periods=max(396//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.525 + 0.0004243 * anchor

def f08_mae_043_jerk_v43(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=88, w2=407, w3=670, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(88)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2878 * persistence + 0.0004244 * anchor

def f08_mae_044_accel_v44(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=95, w2=418, w3=683, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(418, min_periods=max(418//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55375 + 0.0004245 * anchor

def f08_mae_045_jerk_v45(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=102, w2=429, w3=696, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(429, min_periods=max(429//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.303 * slope + 0.0004246 * anchor

def f08_mae_046_accel_v46(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=109, w2=440, w3=709, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(109)
    drag = impulse.rolling(440, min_periods=max(440//3, 2)).mean()
    noise = impulse.abs().rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5825 + 0.0004247 * anchor

def f08_mae_047_jerk_v47(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=116, w2=451, w3=722, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 451)
    curvature = _rolling_slope(acceleration, 722)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3182 * acceleration + 0.0004248 * anchor

def f08_mae_048_accel_v48(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=123, w2=462, w3=735, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(462, min_periods=max(462//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.61125 + 0.0004249 * anchor

def f08_mae_049_jerk_v49(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=130, w2=473, w3=748, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(473, min_periods=max(473//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3334 * _rolling_slope(draw, 748) + 0.000425 * anchor

def f08_mae_050_accel_v50(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=137, w2=484, w3=761, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(484, min_periods=max(484//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.866875 + 0.0004251 * anchor

def f08_mae_051_jerk_v51(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=144, w2=495, w3=17, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=17, adjust=False).mean() * 0.88125 + 0.0004252 * anchor

def f08_mae_052_accel_v52(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=151, w2=506, w3=30, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(506, min_periods=max(506//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.895625 + 0.0004253 * anchor

def f08_mae_053_jerk_v53(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=158, w2=14, w3=43, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(14, min_periods=max(14//3, 2)).rank(pct=True)
    persistence = change.rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3638 * persistence + 0.0004254 * anchor

def f08_mae_054_accel_v54(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=165, w2=25, w3=56, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(25, min_periods=max(25//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.924375 + 0.0004255 * anchor

def f08_mae_055_jerk_v55(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=172, w2=36, w3=69, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.379 * slope + 0.0004256 * anchor

def f08_mae_056_accel_v56(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=179, w2=47, w3=82, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.953125 + 0.0004257 * anchor

def f08_mae_057_jerk_v57(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=186, w2=58, w3=95, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 58)
    curvature = _rolling_slope(acceleration, 95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3942 * acceleration + 0.0004258 * anchor

def f08_mae_058_accel_v58(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=193, w2=69, w3=108, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(69, min_periods=max(69//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(108) * 0.981875 + 0.0004259 * anchor

def f08_mae_059_jerk_v59(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=200, w2=80, w3=121, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(80, min_periods=max(80//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4094 * _rolling_slope(draw, 121) + 0.000426 * anchor

def f08_mae_060_accel_v60(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=207, w2=91, w3=134, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(91, min_periods=max(91//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.010625 + 0.0004261 * anchor

def f08_mae_061_jerk_v61(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=214, w2=102, w3=147, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 102)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=147, adjust=False).mean() * 1.025 + 0.0004262 * anchor

def f08_mae_062_accel_v62(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=221, w2=113, w3=160, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(113, min_periods=max(113//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.039375 + 0.0004263 * anchor

def f08_mae_063_jerk_v63(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=228, w2=124, w3=173, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(124, min_periods=max(124//3, 2)).rank(pct=True)
    persistence = change.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0634 * persistence + 0.0004264 * anchor

def f08_mae_064_accel_v64(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=235, w2=135, w3=186, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.068125 + 0.0004265 * anchor

def f08_mae_065_jerk_v65(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=242, w2=146, w3=199, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(146, min_periods=max(146//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0786 * slope + 0.0004266 * anchor

def f08_mae_066_accel_v66(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=249, w2=157, w3=212, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(157, min_periods=max(157//3, 2)).mean()
    noise = impulse.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.096875 + 0.0004267 * anchor

def f08_mae_067_jerk_v67(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=5, w2=168, w3=225, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 168)
    curvature = _rolling_slope(acceleration, 225)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0938 * acceleration + 0.0004268 * anchor

def f08_mae_068_accel_v68(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=12, w2=179, w3=238, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(179, min_periods=max(179//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.125625 + 0.0004269 * anchor

def f08_mae_069_jerk_v69(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=19, w2=190, w3=251, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(190, min_periods=max(190//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.109 * _rolling_slope(draw, 251) + 0.000427 * anchor

def f08_mae_070_accel_v70(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=26, w2=201, w3=264, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(201, min_periods=max(201//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.154375 + 0.0004271 * anchor

def f08_mae_071_jerk_v71(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=33, w2=212, w3=277, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=277, adjust=False).mean() * 1.16875 + 0.0004272 * anchor

def f08_mae_072_accel_v72(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=40, w2=223, w3=290, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.183125 + 0.0004273 * anchor

def f08_mae_073_jerk_v73(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=47, w2=234, w3=303, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(47)
    rank = change.rolling(234, min_periods=max(234//3, 2)).rank(pct=True)
    persistence = change.rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1394 * persistence + 0.0004274 * anchor

def f08_mae_074_accel_v74(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=54, w2=245, w3=316, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(245, min_periods=max(245//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.211875 + 0.0004275 * anchor

def f08_mae_075_jerk_v75(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=61, w2=256, w3=329, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1546 * slope + 0.0004276 * anchor
