"""10 volatility regime at peak base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f10_vreg_001_jerk_v1(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=95, w2=128, w3=57, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=57, adjust=False).mean() * 1.2975 + 0.0006002 * anchor

def f10_vreg_002_accel_v2(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=102, w2=139, w3=70, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.311875 + 0.0006003 * anchor

def f10_vreg_003_jerk_v3(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=109, w2=150, w3=83, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(109)
    rank = change.rolling(150, min_periods=max(150//3, 2)).rank(pct=True)
    persistence = change.rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1134 * persistence + 0.0006004 * anchor

def f10_vreg_004_accel_v4(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=116, w2=161, w3=96, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.340625 + 0.0006005 * anchor

def f10_vreg_005_jerk_v5(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=123, w2=172, w3=109, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1286 * slope + 0.0006006 * anchor

def f10_vreg_006_accel_v6(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=130, w2=183, w3=122, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.369375 + 0.0006007 * anchor

def f10_vreg_007_jerk_v7(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=137, w2=194, w3=135, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 194)
    curvature = _rolling_slope(acceleration, 135)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1438 * acceleration + 0.0006008 * anchor

def f10_vreg_008_accel_v8(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=144, w2=205, w3=148, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(205, min_periods=max(205//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.398125 + 0.0006009 * anchor

def f10_vreg_009_jerk_v9(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=151, w2=216, w3=161, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.159 * _rolling_slope(draw, 161) + 0.000601 * anchor

def f10_vreg_010_accel_v10(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=158, w2=227, w3=174, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(227, min_periods=max(227//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.426875 + 0.0006011 * anchor

def f10_vreg_011_jerk_v11(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=165, w2=238, w3=187, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 238)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=187, adjust=False).mean() * 1.44125 + 0.0006012 * anchor

def f10_vreg_012_accel_v12(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=172, w2=249, w3=200, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(249, min_periods=max(249//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.455625 + 0.0006013 * anchor

def f10_vreg_013_jerk_v13(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=179, w2=260, w3=213, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1894 * persistence + 0.0006014 * anchor

def f10_vreg_014_accel_v14(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=186, w2=271, w3=226, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(271, min_periods=max(271//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.484375 + 0.0006015 * anchor

def f10_vreg_015_jerk_v15(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=193, w2=282, w3=239, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(282, min_periods=max(282//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2046 * slope + 0.0006016 * anchor

def f10_vreg_016_accel_v16(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=200, w2=293, w3=252, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.513125 + 0.0006017 * anchor

def f10_vreg_017_jerk_v17(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=207, w2=304, w3=265, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 304)
    curvature = _rolling_slope(acceleration, 265)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2198 * acceleration + 0.0006018 * anchor

def f10_vreg_018_accel_v18(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=214, w2=315, w3=278, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.541875 + 0.0006019 * anchor

def f10_vreg_019_jerk_v19(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=221, w2=326, w3=291, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.235 * _rolling_slope(draw, 291) + 0.000602 * anchor

def f10_vreg_020_accel_v20(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=228, w2=337, w3=304, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(337, min_periods=max(337//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.570625 + 0.0006021 * anchor

def f10_vreg_021_jerk_v21(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=235, w2=348, w3=317, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.585 + 0.0006022 * anchor

def f10_vreg_022_accel_v22(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=242, w2=359, w3=330, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(359, min_periods=max(359//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.599375 + 0.0006023 * anchor

def f10_vreg_023_jerk_v23(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=249, w2=370, w3=343, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2654 * persistence + 0.0006024 * anchor

def f10_vreg_024_accel_v24(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=5, w2=381, w3=356, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.855 + 0.0006025 * anchor

def f10_vreg_025_jerk_v25(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=12, w2=392, w3=369, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2806 * slope + 0.0006026 * anchor

def f10_vreg_026_accel_v26(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=19, w2=403, w3=382, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(19)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88375 + 0.0006027 * anchor

def f10_vreg_027_jerk_v27(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=26, w2=414, w3=395, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 395)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2958 * acceleration + 0.0006028 * anchor

def f10_vreg_028_accel_v28(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=33, w2=425, w3=408, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9125 + 0.0006029 * anchor

def f10_vreg_029_jerk_v29(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=40, w2=436, w3=421, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.311 * _rolling_slope(draw, 421) + 0.000603 * anchor

def f10_vreg_030_accel_v30(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=47, w2=447, w3=434, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(447, min_periods=max(447//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.94125 + 0.0006031 * anchor

def f10_vreg_031_jerk_v31(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=54, w2=458, w3=447, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 458)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.955625 + 0.0006032 * anchor

def f10_vreg_032_accel_v32(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=61, w2=469, w3=460, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(469, min_periods=max(469//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.97 + 0.0006033 * anchor

def f10_vreg_033_jerk_v33(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=68, w2=480, w3=473, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(68)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3414 * persistence + 0.0006034 * anchor

def f10_vreg_034_accel_v34(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=75, w2=491, w3=486, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99875 + 0.0006035 * anchor

def f10_vreg_035_jerk_v35(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=82, w2=502, w3=499, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3566 * slope + 0.0006036 * anchor

def f10_vreg_036_accel_v36(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=89, w2=10, w3=512, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(89)
    drag = impulse.rolling(10, min_periods=max(10//3, 2)).mean()
    noise = impulse.abs().rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0275 + 0.0006037 * anchor

def f10_vreg_037_jerk_v37(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=96, w2=21, w3=525, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 525)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3718 * acceleration + 0.0006038 * anchor

def f10_vreg_038_accel_v38(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=103, w2=32, w3=538, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(32, min_periods=max(32//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05625 + 0.0006039 * anchor

def f10_vreg_039_jerk_v39(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=110, w2=43, w3=551, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(43, min_periods=max(43//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.387 * _rolling_slope(draw, 551) + 0.000604 * anchor

def f10_vreg_040_accel_v40(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=117, w2=54, w3=564, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.085 + 0.0006041 * anchor

def f10_vreg_041_jerk_v41(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=124, w2=65, w3=577, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.099375 + 0.0006042 * anchor

def f10_vreg_042_accel_v42(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=131, w2=76, w3=590, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(76, min_periods=max(76//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11375 + 0.0006043 * anchor

def f10_vreg_043_jerk_v43(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=138, w2=87, w3=603, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.041 * persistence + 0.0006044 * anchor

def f10_vreg_044_accel_v44(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=145, w2=98, w3=616, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1425 + 0.0006045 * anchor

def f10_vreg_045_jerk_v45(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=152, w2=109, w3=629, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0562 * slope + 0.0006046 * anchor

def f10_vreg_046_accel_v46(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=159, w2=120, w3=642, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.17125 + 0.0006047 * anchor

def f10_vreg_047_jerk_v47(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=166, w2=131, w3=655, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 655)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0714 * acceleration + 0.0006048 * anchor

def f10_vreg_048_accel_v48(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=173, w2=142, w3=668, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2 + 0.0006049 * anchor

def f10_vreg_049_jerk_v49(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=180, w2=153, w3=681, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0866 * _rolling_slope(draw, 681) + 0.000605 * anchor

def f10_vreg_050_accel_v50(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=187, w2=164, w3=694, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.22875 + 0.0006051 * anchor

def f10_vreg_051_jerk_v51(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=194, w2=175, w3=707, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.243125 + 0.0006052 * anchor

def f10_vreg_052_accel_v52(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=201, w2=186, w3=720, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2575 + 0.0006053 * anchor

def f10_vreg_053_jerk_v53(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=208, w2=197, w3=733, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.117 * persistence + 0.0006054 * anchor

def f10_vreg_054_accel_v54(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=215, w2=208, w3=746, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28625 + 0.0006055 * anchor

def f10_vreg_055_jerk_v55(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=222, w2=219, w3=759, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1322 * slope + 0.0006056 * anchor

def f10_vreg_056_accel_v56(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=229, w2=230, w3=15, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.315 + 0.0006057 * anchor

def f10_vreg_057_jerk_v57(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=236, w2=241, w3=28, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 28)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1474 * acceleration + 0.0006058 * anchor

def f10_vreg_058_accel_v58(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=243, w2=252, w3=41, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(41) * 1.34375 + 0.0006059 * anchor

def f10_vreg_059_jerk_v59(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=250, w2=263, w3=54, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1626 * _rolling_slope(draw, 54) + 0.000606 * anchor

def f10_vreg_060_accel_v60(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=6, w2=274, w3=67, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3725 + 0.0006061 * anchor

def f10_vreg_061_jerk_v61(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=13, w2=285, w3=80, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 285)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=80, adjust=False).mean() * 1.386875 + 0.0006062 * anchor

def f10_vreg_062_accel_v62(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=20, w2=296, w3=93, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.40125 + 0.0006063 * anchor

def f10_vreg_063_jerk_v63(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=27, w2=307, w3=106, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(27)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.193 * persistence + 0.0006064 * anchor

def f10_vreg_064_accel_v64(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=34, w2=318, w3=119, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(318, min_periods=max(318//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43 + 0.0006065 * anchor

def f10_vreg_065_jerk_v65(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=41, w2=329, w3=132, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(329, min_periods=max(329//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2082 * slope + 0.0006066 * anchor

def f10_vreg_066_accel_v66(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=48, w2=340, w3=145, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(48)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.45875 + 0.0006067 * anchor

def f10_vreg_067_jerk_v67(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=55, w2=351, w3=158, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 351)
    curvature = _rolling_slope(acceleration, 158)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2234 * acceleration + 0.0006068 * anchor

def f10_vreg_068_accel_v68(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=62, w2=362, w3=171, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(362, min_periods=max(362//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4875 + 0.0006069 * anchor

def f10_vreg_069_jerk_v69(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=69, w2=373, w3=184, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2386 * _rolling_slope(draw, 184) + 0.000607 * anchor

def f10_vreg_070_accel_v70(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=76, w2=384, w3=197, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51625 + 0.0006071 * anchor

def f10_vreg_071_jerk_v71(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=83, w2=395, w3=210, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=210, adjust=False).mean() * 1.530625 + 0.0006072 * anchor

def f10_vreg_072_accel_v72(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=90, w2=406, w3=223, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(406, min_periods=max(406//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.545 + 0.0006073 * anchor

def f10_vreg_073_jerk_v73(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=97, w2=417, w3=236, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(97)
    rank = change.rolling(417, min_periods=max(417//3, 2)).rank(pct=True)
    persistence = change.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.269 * persistence + 0.0006074 * anchor

def f10_vreg_074_accel_v74(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=104, w2=428, w3=249, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(428, min_periods=max(428//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57375 + 0.0006075 * anchor

def f10_vreg_075_jerk_v75(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=111, w2=439, w3=262, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2842 * slope + 0.0006076 * anchor
