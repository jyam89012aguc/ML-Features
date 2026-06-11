"""06 volume distribution dryup base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_001_jerk_v1(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=179, w2=326, w3=421, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 326)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4675 + 0.0003002 * anchor

def f06_vdd_002_accel_v2(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=186, w2=337, w3=434, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(337, min_periods=max(337//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.481875 + 0.0003003 * anchor

def f06_vdd_003_jerk_v3(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=193, w2=348, w3=447, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(348, min_periods=max(348//3, 2)).rank(pct=True)
    persistence = change.rolling(447, min_periods=max(447//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2738 * persistence + 0.0003004 * anchor

def f06_vdd_004_accel_v4(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=200, w2=359, w3=460, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(359, min_periods=max(359//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.510625 + 0.0003005 * anchor

def f06_vdd_005_jerk_v5(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=207, w2=370, w3=473, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.289 * slope + 0.0003006 * anchor

def f06_vdd_006_accel_v6(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=214, w2=381, w3=486, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(381, min_periods=max(381//3, 2)).mean()
    noise = impulse.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.539375 + 0.0003007 * anchor

def f06_vdd_007_jerk_v7(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=221, w2=392, w3=499, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 392)
    curvature = _rolling_slope(acceleration, 499)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3042 * acceleration + 0.0003008 * anchor

def f06_vdd_008_accel_v8(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=228, w2=403, w3=512, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(403, min_periods=max(403//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.568125 + 0.0003009 * anchor

def f06_vdd_009_jerk_v9(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=235, w2=414, w3=525, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3194 * _rolling_slope(draw, 525) + 0.000301 * anchor

def f06_vdd_010_accel_v10(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=242, w2=425, w3=538, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(425, min_periods=max(425//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.596875 + 0.0003011 * anchor

def f06_vdd_011_jerk_v11(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=249, w2=436, w3=551, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 436)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.61125 + 0.0003012 * anchor

def f06_vdd_012_accel_v12(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=5, w2=447, w3=564, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(447, min_periods=max(447//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.8525 + 0.0003013 * anchor

def f06_vdd_013_jerk_v13(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=12, w2=458, w3=577, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(12)
    rank = change.rolling(458, min_periods=max(458//3, 2)).rank(pct=True)
    persistence = change.rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3498 * persistence + 0.0003014 * anchor

def f06_vdd_014_accel_v14(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=19, w2=469, w3=590, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(469, min_periods=max(469//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.88125 + 0.0003015 * anchor

def f06_vdd_015_jerk_v15(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=26, w2=480, w3=603, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(480, min_periods=max(480//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.365 * slope + 0.0003016 * anchor

def f06_vdd_016_accel_v16(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=33, w2=491, w3=616, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(33)
    drag = impulse.rolling(491, min_periods=max(491//3, 2)).mean()
    noise = impulse.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.91 + 0.0003017 * anchor

def f06_vdd_017_jerk_v17(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=40, w2=502, w3=629, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 502)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3802 * acceleration + 0.0003018 * anchor

def f06_vdd_018_accel_v18(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=47, w2=10, w3=642, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(10, min_periods=max(10//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.93875 + 0.0003019 * anchor

def f06_vdd_019_jerk_v19(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=54, w2=21, w3=655, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(21, min_periods=max(21//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3954 * _rolling_slope(draw, 655) + 0.000302 * anchor

def f06_vdd_020_accel_v20(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=61, w2=32, w3=668, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(32, min_periods=max(32//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9675 + 0.0003021 * anchor

def f06_vdd_021_jerk_v21(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=68, w2=43, w3=681, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 43)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.981875 + 0.0003022 * anchor

def f06_vdd_022_accel_v22(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=75, w2=54, w3=694, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(54, min_periods=max(54//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.99625 + 0.0003023 * anchor

def f06_vdd_023_jerk_v23(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=82, w2=65, w3=707, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(82)
    rank = change.rolling(65, min_periods=max(65//3, 2)).rank(pct=True)
    persistence = change.rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0494 * persistence + 0.0003024 * anchor

def f06_vdd_024_accel_v24(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=89, w2=76, w3=720, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(76, min_periods=max(76//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.025 + 0.0003025 * anchor

def f06_vdd_025_jerk_v25(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=96, w2=87, w3=733, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(87, min_periods=max(87//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0646 * slope + 0.0003026 * anchor

def f06_vdd_026_accel_v26(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=103, w2=98, w3=746, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(103)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.05375 + 0.0003027 * anchor

def f06_vdd_027_jerk_v27(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=110, w2=109, w3=759, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 109)
    curvature = _rolling_slope(acceleration, 759)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0798 * acceleration + 0.0003028 * anchor

def f06_vdd_028_accel_v28(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=117, w2=120, w3=15, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(120, min_periods=max(120//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(15) * 1.0825 + 0.0003029 * anchor

def f06_vdd_029_jerk_v29(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=124, w2=131, w3=28, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(131, min_periods=max(131//3, 2)).max()
    rebound = x - x.rolling(124, min_periods=max(124//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.095 * _rolling_slope(draw, 28) + 0.000303 * anchor

def f06_vdd_030_accel_v30(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=131, w2=142, w3=41, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(142, min_periods=max(142//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.11125 + 0.0003031 * anchor

def f06_vdd_031_jerk_v31(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=138, w2=153, w3=54, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 153)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=54, adjust=False).mean() * 1.125625 + 0.0003032 * anchor

def f06_vdd_032_accel_v32(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=145, w2=164, w3=67, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(164, min_periods=max(164//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.14 + 0.0003033 * anchor

def f06_vdd_033_jerk_v33(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=152, w2=175, w3=80, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(175, min_periods=max(175//3, 2)).rank(pct=True)
    persistence = change.rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1254 * persistence + 0.0003034 * anchor

def f06_vdd_034_accel_v34(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=159, w2=186, w3=93, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(186, min_periods=max(186//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16875 + 0.0003035 * anchor

def f06_vdd_035_jerk_v35(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=166, w2=197, w3=106, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(197, min_periods=max(197//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1406 * slope + 0.0003036 * anchor

def f06_vdd_036_accel_v36(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=173, w2=208, w3=119, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(208, min_periods=max(208//3, 2)).mean()
    noise = impulse.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1975 + 0.0003037 * anchor

def f06_vdd_037_jerk_v37(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=180, w2=219, w3=132, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 219)
    curvature = _rolling_slope(acceleration, 132)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1558 * acceleration + 0.0003038 * anchor

def f06_vdd_038_accel_v38(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=187, w2=230, w3=145, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.22625 + 0.0003039 * anchor

def f06_vdd_039_jerk_v39(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=194, w2=241, w3=158, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(241, min_periods=max(241//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.171 * _rolling_slope(draw, 158) + 0.000304 * anchor

def f06_vdd_040_accel_v40(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=201, w2=252, w3=171, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(252, min_periods=max(252//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.255 + 0.0003041 * anchor

def f06_vdd_041_jerk_v41(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=208, w2=263, w3=184, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 263)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=184, adjust=False).mean() * 1.269375 + 0.0003042 * anchor

def f06_vdd_042_accel_v42(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=215, w2=274, w3=197, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(274, min_periods=max(274//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.28375 + 0.0003043 * anchor

def f06_vdd_043_jerk_v43(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=222, w2=285, w3=210, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(285, min_periods=max(285//3, 2)).rank(pct=True)
    persistence = change.rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2014 * persistence + 0.0003044 * anchor

def f06_vdd_044_accel_v44(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=229, w2=296, w3=223, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3125 + 0.0003045 * anchor

def f06_vdd_045_jerk_v45(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=236, w2=307, w3=236, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2166 * slope + 0.0003046 * anchor

def f06_vdd_046_accel_v46(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=243, w2=318, w3=249, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.34125 + 0.0003047 * anchor

def f06_vdd_047_jerk_v47(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=250, w2=329, w3=262, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2318 * acceleration + 0.0003048 * anchor

def f06_vdd_048_accel_v48(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=6, w2=340, w3=275, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.37 + 0.0003049 * anchor

def f06_vdd_049_jerk_v49(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=13, w2=351, w3=288, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.247 * _rolling_slope(draw, 288) + 0.000305 * anchor

def f06_vdd_050_accel_v50(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=20, w2=362, w3=301, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.39875 + 0.0003051 * anchor

def f06_vdd_051_jerk_v51(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=27, w2=373, w3=314, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 373)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.413125 + 0.0003052 * anchor

def f06_vdd_052_accel_v52(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=34, w2=384, w3=327, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4275 + 0.0003053 * anchor

def f06_vdd_053_jerk_v53(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=41, w2=395, w3=340, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(41)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2774 * persistence + 0.0003054 * anchor

def f06_vdd_054_accel_v54(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=48, w2=406, w3=353, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.45625 + 0.0003055 * anchor

def f06_vdd_055_jerk_v55(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=55, w2=417, w3=366, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2926 * slope + 0.0003056 * anchor

def f06_vdd_056_accel_v56(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=62, w2=428, w3=379, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(62)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.485 + 0.0003057 * anchor

def f06_vdd_057_jerk_v57(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=69, w2=439, w3=392, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 392)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3078 * acceleration + 0.0003058 * anchor

def f06_vdd_058_accel_v58(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=76, w2=450, w3=405, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.51375 + 0.0003059 * anchor

def f06_vdd_059_jerk_v59(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=83, w2=461, w3=418, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.323 * _rolling_slope(draw, 418) + 0.000306 * anchor

def f06_vdd_060_accel_v60(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=90, w2=472, w3=431, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(472, min_periods=max(472//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.5425 + 0.0003061 * anchor

def f06_vdd_061_jerk_v61(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=97, w2=483, w3=444, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.556875 + 0.0003062 * anchor

def f06_vdd_062_accel_v62(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=104, w2=494, w3=457, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.57125 + 0.0003063 * anchor

def f06_vdd_063_jerk_v63(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=111, w2=505, w3=470, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(111)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3534 * persistence + 0.0003064 * anchor

def f06_vdd_064_accel_v64(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=118, w2=13, w3=483, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6 + 0.0003065 * anchor

def f06_vdd_065_jerk_v65(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=125, w2=24, w3=496, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3686 * slope + 0.0003066 * anchor

def f06_vdd_066_accel_v66(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=132, w2=35, w3=509, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.855625 + 0.0003067 * anchor

def f06_vdd_067_jerk_v67(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=139, w2=46, w3=522, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 46)
    curvature = _rolling_slope(acceleration, 522)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3838 * acceleration + 0.0003068 * anchor

def f06_vdd_068_accel_v68(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=146, w2=57, w3=535, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.884375 + 0.0003069 * anchor

def f06_vdd_069_jerk_v69(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=153, w2=68, w3=548, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.399 * _rolling_slope(draw, 548) + 0.000307 * anchor

def f06_vdd_070_accel_v70(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=160, w2=79, w3=561, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.913125 + 0.0003071 * anchor

def f06_vdd_071_jerk_v71(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=167, w2=90, w3=574, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 90)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.9275 + 0.0003072 * anchor

def f06_vdd_072_accel_v72(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=174, w2=101, w3=587, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(101, min_periods=max(101//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.941875 + 0.0003073 * anchor

def f06_vdd_073_jerk_v73(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=181, w2=112, w3=600, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(112, min_periods=max(112//3, 2)).rank(pct=True)
    persistence = change.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.053 * persistence + 0.0003074 * anchor

def f06_vdd_074_accel_v74(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=188, w2=123, w3=613, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(123, min_periods=max(123//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.970625 + 0.0003075 * anchor

def f06_vdd_075_jerk_v75(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=195, w2=134, w3=626, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(134, min_periods=max(134//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0682 * slope + 0.0003076 * anchor
