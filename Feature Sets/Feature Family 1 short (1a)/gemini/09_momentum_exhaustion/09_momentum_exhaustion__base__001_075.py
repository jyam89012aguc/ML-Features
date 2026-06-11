"""09 momentum exhaustion base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f09_mex_001_jerk_v1(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=229, w2=509, w3=354, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 509)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.05625 + 0.0004802 * anchor

def f09_mex_002_accel_v2(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=236, w2=17, w3=367, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(17, min_periods=max(17//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.070625 + 0.0004803 * anchor

def f09_mex_003_jerk_v3(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=243, w2=28, w3=380, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(28, min_periods=max(28//3, 2)).rank(pct=True)
    persistence = change.rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4034 * persistence + 0.0004804 * anchor

def f09_mex_004_accel_v4(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=39, w3=393, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(39, min_periods=max(39//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.099375 + 0.0004805 * anchor

def f09_mex_005_jerk_v5(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=50, w3=406, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(50, min_periods=max(50//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0422 * slope + 0.0004806 * anchor

def f09_mex_006_accel_v6(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=61, w3=419, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(13)
    drag = impulse.rolling(61, min_periods=max(61//3, 2)).mean()
    noise = impulse.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.128125 + 0.0004807 * anchor

def f09_mex_007_jerk_v7(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=72, w3=432, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 72)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0574 * acceleration + 0.0004808 * anchor

def f09_mex_008_accel_v8(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=83, w3=445, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(83, min_periods=max(83//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.156875 + 0.0004809 * anchor

def f09_mex_009_jerk_v9(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=94, w3=458, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(94, min_periods=max(94//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0726 * _rolling_slope(draw, 458) + 0.000481 * anchor

def f09_mex_010_accel_v10(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=105, w3=471, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(105, min_periods=max(105//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.185625 + 0.0004811 * anchor

def f09_mex_011_jerk_v11(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=116, w3=484, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 116)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.2 + 0.0004812 * anchor

def f09_mex_012_accel_v12(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=127, w3=497, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(127, min_periods=max(127//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.214375 + 0.0004813 * anchor

def f09_mex_013_jerk_v13(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=62, w2=138, w3=510, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(62)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.103 * persistence + 0.0004814 * anchor

def f09_mex_014_accel_v14(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=69, w2=149, w3=523, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(149, min_periods=max(149//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.243125 + 0.0004815 * anchor

def f09_mex_015_jerk_v15(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=76, w2=160, w3=536, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(160, min_periods=max(160//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1182 * slope + 0.0004816 * anchor

def f09_mex_016_accel_v16(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=83, w2=171, w3=549, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(83)
    drag = impulse.rolling(171, min_periods=max(171//3, 2)).mean()
    noise = impulse.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.271875 + 0.0004817 * anchor

def f09_mex_017_jerk_v17(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=90, w2=182, w3=562, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 182)
    curvature = _rolling_slope(acceleration, 562)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1334 * acceleration + 0.0004818 * anchor

def f09_mex_018_accel_v18(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=97, w2=193, w3=575, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(193, min_periods=max(193//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.300625 + 0.0004819 * anchor

def f09_mex_019_jerk_v19(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=104, w2=204, w3=588, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(204, min_periods=max(204//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1486 * _rolling_slope(draw, 588) + 0.000482 * anchor

def f09_mex_020_accel_v20(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=111, w2=215, w3=601, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(215, min_periods=max(215//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.329375 + 0.0004821 * anchor

def f09_mex_021_jerk_v21(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=118, w2=226, w3=614, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 226)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.34375 + 0.0004822 * anchor

def f09_mex_022_accel_v22(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=125, w2=237, w3=627, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(237, min_periods=max(237//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.358125 + 0.0004823 * anchor

def f09_mex_023_jerk_v23(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=132, w2=248, w3=640, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(248, min_periods=max(248//3, 2)).rank(pct=True)
    persistence = change.rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.179 * persistence + 0.0004824 * anchor

def f09_mex_024_accel_v24(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=139, w2=259, w3=653, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(259, min_periods=max(259//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.386875 + 0.0004825 * anchor

def f09_mex_025_jerk_v25(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=146, w2=270, w3=666, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(270, min_periods=max(270//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1942 * slope + 0.0004826 * anchor

def f09_mex_026_accel_v26(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=153, w2=281, w3=679, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(281, min_periods=max(281//3, 2)).mean()
    noise = impulse.abs().rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.415625 + 0.0004827 * anchor

def f09_mex_027_jerk_v27(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=160, w2=292, w3=692, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 292)
    curvature = _rolling_slope(acceleration, 692)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2094 * acceleration + 0.0004828 * anchor

def f09_mex_028_accel_v28(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=167, w2=303, w3=705, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(303, min_periods=max(303//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.444375 + 0.0004829 * anchor

def f09_mex_029_jerk_v29(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=174, w2=314, w3=718, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2246 * _rolling_slope(draw, 718) + 0.000483 * anchor

def f09_mex_030_accel_v30(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=181, w2=325, w3=731, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(325, min_periods=max(325//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.473125 + 0.0004831 * anchor

def f09_mex_031_jerk_v31(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=188, w2=336, w3=744, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 188)
    slow = _rolling_slope(x, 336)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4875 + 0.0004832 * anchor

def f09_mex_032_accel_v32(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=195, w2=347, w3=757, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(347, min_periods=max(347//3, 2)).max()
    trough = x.rolling(195, min_periods=max(195//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.501875 + 0.0004833 * anchor

def f09_mex_033_jerk_v33(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=202, w2=358, w3=770, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(358, min_periods=max(358//3, 2)).rank(pct=True)
    persistence = change.rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.255 * persistence + 0.0004834 * anchor

def f09_mex_034_accel_v34(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=209, w2=369, w3=26, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(209, min_periods=max(209//3, 2)).std()
    vol_slow = ret.rolling(369, min_periods=max(369//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.530625 + 0.0004835 * anchor

def f09_mex_035_jerk_v35(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=216, w2=380, w3=39, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(380, min_periods=max(380//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 216)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2702 * slope + 0.0004836 * anchor

def f09_mex_036_accel_v36(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=223, w2=391, w3=52, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(391, min_periods=max(391//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.559375 + 0.0004837 * anchor

def f09_mex_037_jerk_v37(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=230, w2=402, w3=65, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 230)
    acceleration = _rolling_slope(velocity, 402)
    curvature = _rolling_slope(acceleration, 65)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2854 * acceleration + 0.0004838 * anchor

def f09_mex_038_accel_v38(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=237, w2=413, w3=78, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(237, min_periods=max(237//3, 2)).mean(), upside.rolling(413, min_periods=max(413//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(78) * 1.588125 + 0.0004839 * anchor

def f09_mex_039_jerk_v39(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=244, w2=424, w3=91, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(424, min_periods=max(424//3, 2)).max()
    rebound = x - x.rolling(244, min_periods=max(244//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3006 * _rolling_slope(draw, 91) + 0.000484 * anchor

def f09_mex_040_accel_v40(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=251, w2=435, w3=104, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 251)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.616875 + 0.0004841 * anchor

def f09_mex_041_jerk_v41(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=7, w2=446, w3=117, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 446)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=117, adjust=False).mean() * 0.858125 + 0.0004842 * anchor

def f09_mex_042_accel_v42(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=14, w2=457, w3=130, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(457, min_periods=max(457//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.8725 + 0.0004843 * anchor

def f09_mex_043_jerk_v43(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=21, w2=468, w3=143, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(21)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.331 * persistence + 0.0004844 * anchor

def f09_mex_044_accel_v44(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=28, w2=479, w3=156, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(479, min_periods=max(479//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90125 + 0.0004845 * anchor

def f09_mex_045_jerk_v45(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=35, w2=490, w3=169, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(490, min_periods=max(490//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3462 * slope + 0.0004846 * anchor

def f09_mex_046_accel_v46(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=42, w2=501, w3=182, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(42)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.93 + 0.0004847 * anchor

def f09_mex_047_jerk_v47(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=49, w2=512, w3=195, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 512)
    curvature = _rolling_slope(acceleration, 195)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3614 * acceleration + 0.0004848 * anchor

def f09_mex_048_accel_v48(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=56, w2=20, w3=208, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(20, min_periods=max(20//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.95875 + 0.0004849 * anchor

def f09_mex_049_jerk_v49(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=63, w2=31, w3=221, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(31, min_periods=max(31//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3766 * _rolling_slope(draw, 221) + 0.000485 * anchor

def f09_mex_050_accel_v50(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=70, w2=42, w3=234, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(42, min_periods=max(42//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9875 + 0.0004851 * anchor

def f09_mex_051_jerk_v51(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=77, w2=53, w3=247, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 53)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=247, adjust=False).mean() * 1.001875 + 0.0004852 * anchor

def f09_mex_052_accel_v52(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=84, w2=64, w3=260, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(64, min_periods=max(64//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.01625 + 0.0004853 * anchor

def f09_mex_053_jerk_v53(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=91, w2=75, w3=273, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(91)
    rank = change.rolling(75, min_periods=max(75//3, 2)).rank(pct=True)
    persistence = change.rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.407 * persistence + 0.0004854 * anchor

def f09_mex_054_accel_v54(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=98, w2=86, w3=286, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(86, min_periods=max(86//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.045 + 0.0004855 * anchor

def f09_mex_055_jerk_v55(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=105, w2=97, w3=299, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(97, min_periods=max(97//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0458 * slope + 0.0004856 * anchor

def f09_mex_056_accel_v56(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=112, w2=108, w3=312, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(112)
    drag = impulse.rolling(108, min_periods=max(108//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.07375 + 0.0004857 * anchor

def f09_mex_057_jerk_v57(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=119, w2=119, w3=325, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 119)
    curvature = _rolling_slope(acceleration, 325)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.061 * acceleration + 0.0004858 * anchor

def f09_mex_058_accel_v58(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=126, w2=130, w3=338, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(130, min_periods=max(130//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1025 + 0.0004859 * anchor

def f09_mex_059_jerk_v59(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=133, w2=141, w3=351, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0762 * _rolling_slope(draw, 351) + 0.000486 * anchor

def f09_mex_060_accel_v60(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=140, w2=152, w3=364, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(152, min_periods=max(152//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.13125 + 0.0004861 * anchor

def f09_mex_061_jerk_v61(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=147, w2=163, w3=377, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 163)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.145625 + 0.0004862 * anchor

def f09_mex_062_accel_v62(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=154, w2=174, w3=390, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(174, min_periods=max(174//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.16 + 0.0004863 * anchor

def f09_mex_063_jerk_v63(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=161, w2=185, w3=403, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(185, min_periods=max(185//3, 2)).rank(pct=True)
    persistence = change.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1066 * persistence + 0.0004864 * anchor

def f09_mex_064_accel_v64(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=168, w2=196, w3=416, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(196, min_periods=max(196//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18875 + 0.0004865 * anchor

def f09_mex_065_jerk_v65(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=175, w2=207, w3=429, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(207, min_periods=max(207//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1218 * slope + 0.0004866 * anchor

def f09_mex_066_accel_v66(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=182, w2=218, w3=442, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(218, min_periods=max(218//3, 2)).mean()
    noise = impulse.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2175 + 0.0004867 * anchor

def f09_mex_067_jerk_v67(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=189, w2=229, w3=455, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 229)
    curvature = _rolling_slope(acceleration, 455)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.137 * acceleration + 0.0004868 * anchor

def f09_mex_068_accel_v68(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=196, w2=240, w3=468, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(196, min_periods=max(196//3, 2)).mean(), upside.rolling(240, min_periods=max(240//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.24625 + 0.0004869 * anchor

def f09_mex_069_jerk_v69(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=203, w2=251, w3=481, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(251, min_periods=max(251//3, 2)).max()
    rebound = x - x.rolling(203, min_periods=max(203//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1522 * _rolling_slope(draw, 481) + 0.000487 * anchor

def f09_mex_070_accel_v70(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=210, w2=262, w3=494, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(262, min_periods=max(262//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.275 + 0.0004871 * anchor

def f09_mex_071_jerk_v71(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=217, w2=273, w3=507, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 273)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.289375 + 0.0004872 * anchor

def f09_mex_072_accel_v72(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=224, w2=284, w3=520, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(284, min_periods=max(284//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.30375 + 0.0004873 * anchor

def f09_mex_073_jerk_v73(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=231, w2=295, w3=533, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1826 * persistence + 0.0004874 * anchor

def f09_mex_074_accel_v74(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=238, w2=306, w3=546, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(306, min_periods=max(306//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3325 + 0.0004875 * anchor

def f09_mex_075_jerk_v75(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=245, w2=317, w3=559, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(317, min_periods=max(317//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1978 * slope + 0.0004876 * anchor
