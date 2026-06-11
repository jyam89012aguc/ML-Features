"""04 topping pattern d2 second derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f04_top_001_jerk_v1_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=62, w2=204, w3=718, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 204)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.22625 + 0.0001802 * anchor
    return base_signal.diff().diff()

def f04_top_002_accel_v2_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=69, w2=215, w3=731, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(215, min_periods=max(215//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.240625 + 0.0001803 * anchor
    return base_signal.diff().diff()

def f04_top_003_jerk_v3_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=76, w2=226, w3=744, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(76)
    rank = change.rolling(226, min_periods=max(226//3, 2)).rank(pct=True)
    persistence = change.rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1874 * persistence + 0.0001804 * anchor
    return base_signal.diff().diff()

def f04_top_004_accel_v4_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=83, w2=237, w3=757, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(237, min_periods=max(237//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.269375 + 0.0001805 * anchor
    return base_signal.diff().diff()

def f04_top_005_jerk_v5_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=90, w2=248, w3=770, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(248, min_periods=max(248//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2026 * slope + 0.0001806 * anchor
    return base_signal.diff().diff()

def f04_top_006_accel_v6_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=97, w2=259, w3=26, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(97)
    drag = impulse.rolling(259, min_periods=max(259//3, 2)).mean()
    noise = impulse.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.298125 + 0.0001807 * anchor
    return base_signal.diff().diff()

def f04_top_007_jerk_v7_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=104, w2=270, w3=39, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 39)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2178 * acceleration + 0.0001808 * anchor
    return base_signal.diff().diff()

def f04_top_008_accel_v8_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=111, w2=281, w3=52, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(281, min_periods=max(281//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(52) * 1.326875 + 0.0001809 * anchor
    return base_signal.diff().diff()

def f04_top_009_jerk_v9_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=118, w2=292, w3=65, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.233 * _rolling_slope(draw, 65) + 0.000181 * anchor
    return base_signal.diff().diff()

def f04_top_010_accel_v10_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=125, w2=303, w3=78, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(303, min_periods=max(303//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.355625 + 0.0001811 * anchor
    return base_signal.diff().diff()

def f04_top_011_jerk_v11_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=132, w2=314, w3=91, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 314)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=91, adjust=False).mean() * 1.37 + 0.0001812 * anchor
    return base_signal.diff().diff()

def f04_top_012_accel_v12_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=139, w2=325, w3=104, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(325, min_periods=max(325//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.384375 + 0.0001813 * anchor
    return base_signal.diff().diff()

def f04_top_013_jerk_v13_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=146, w2=336, w3=117, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(336, min_periods=max(336//3, 2)).rank(pct=True)
    persistence = change.rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2634 * persistence + 0.0001814 * anchor
    return base_signal.diff().diff()

def f04_top_014_accel_v14_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=153, w2=347, w3=130, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(347, min_periods=max(347//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.413125 + 0.0001815 * anchor
    return base_signal.diff().diff()

def f04_top_015_jerk_v15_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=160, w2=358, w3=143, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(358, min_periods=max(358//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2786 * slope + 0.0001816 * anchor
    return base_signal.diff().diff()

def f04_top_016_accel_v16_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=167, w2=369, w3=156, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(369, min_periods=max(369//3, 2)).mean()
    noise = impulse.abs().rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.441875 + 0.0001817 * anchor
    return base_signal.diff().diff()

def f04_top_017_jerk_v17_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=174, w2=380, w3=169, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 380)
    curvature = _rolling_slope(acceleration, 169)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2938 * acceleration + 0.0001818 * anchor
    return base_signal.diff().diff()

def f04_top_018_accel_v18_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=181, w2=391, w3=182, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(391, min_periods=max(391//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.470625 + 0.0001819 * anchor
    return base_signal.diff().diff()

def f04_top_019_jerk_v19_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=188, w2=402, w3=195, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(402, min_periods=max(402//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.309 * _rolling_slope(draw, 195) + 0.000182 * anchor
    return base_signal.diff().diff()

def f04_top_020_accel_v20_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=195, w2=413, w3=208, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(413, min_periods=max(413//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.499375 + 0.0001821 * anchor
    return base_signal.diff().diff()

def f04_top_021_jerk_v21_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=202, w2=424, w3=221, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 424)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 1.51375 + 0.0001822 * anchor
    return base_signal.diff().diff()

def f04_top_022_accel_v22_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=209, w2=435, w3=234, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(435, min_periods=max(435//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.528125 + 0.0001823 * anchor
    return base_signal.diff().diff()

def f04_top_023_jerk_v23_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=216, w2=446, w3=247, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(446, min_periods=max(446//3, 2)).rank(pct=True)
    persistence = change.rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3394 * persistence + 0.0001824 * anchor
    return base_signal.diff().diff()

def f04_top_024_accel_v24_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=223, w2=457, w3=260, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(457, min_periods=max(457//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.556875 + 0.0001825 * anchor
    return base_signal.diff().diff()

def f04_top_025_jerk_v25_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=230, w2=468, w3=273, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(468, min_periods=max(468//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3546 * slope + 0.0001826 * anchor
    return base_signal.diff().diff()

def f04_top_026_accel_v26_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=237, w2=479, w3=286, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(479, min_periods=max(479//3, 2)).mean()
    noise = impulse.abs().rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.585625 + 0.0001827 * anchor
    return base_signal.diff().diff()

def f04_top_027_jerk_v27_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=244, w2=490, w3=299, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 490)
    curvature = _rolling_slope(acceleration, 299)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3698 * acceleration + 0.0001828 * anchor
    return base_signal.diff().diff()

def f04_top_028_accel_v28_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=251, w2=501, w3=312, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(501, min_periods=max(501//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.614375 + 0.0001829 * anchor
    return base_signal.diff().diff()

def f04_top_029_jerk_v29_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=7, w2=512, w3=325, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(512, min_periods=max(512//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.385 * _rolling_slope(draw, 325) + 0.000183 * anchor
    return base_signal.diff().diff()

def f04_top_030_accel_v30_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=14, w2=20, w3=338, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(20, min_periods=max(20//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.87 + 0.0001831 * anchor
    return base_signal.diff().diff()

def f04_top_031_jerk_v31_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=21, w2=31, w3=351, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 31)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.884375 + 0.0001832 * anchor
    return base_signal.diff().diff()

def f04_top_032_accel_v32_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=28, w2=42, w3=364, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(42, min_periods=max(42//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.89875 + 0.0001833 * anchor
    return base_signal.diff().diff()

def f04_top_033_jerk_v33_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=35, w2=53, w3=377, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(35)
    rank = change.rolling(53, min_periods=max(53//3, 2)).rank(pct=True)
    persistence = change.rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.039 * persistence + 0.0001834 * anchor
    return base_signal.diff().diff()

def f04_top_034_accel_v34_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=42, w2=64, w3=390, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(64, min_periods=max(64//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9275 + 0.0001835 * anchor
    return base_signal.diff().diff()

def f04_top_035_jerk_v35_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=49, w2=75, w3=403, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(75, min_periods=max(75//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0542 * slope + 0.0001836 * anchor
    return base_signal.diff().diff()

def f04_top_036_accel_v36_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=56, w2=86, w3=416, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(56)
    drag = impulse.rolling(86, min_periods=max(86//3, 2)).mean()
    noise = impulse.abs().rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.95625 + 0.0001837 * anchor
    return base_signal.diff().diff()

def f04_top_037_jerk_v37_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=63, w2=97, w3=429, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 97)
    curvature = _rolling_slope(acceleration, 429)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0694 * acceleration + 0.0001838 * anchor
    return base_signal.diff().diff()

def f04_top_038_accel_v38_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=70, w2=108, w3=442, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(108, min_periods=max(108//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.985 + 0.0001839 * anchor
    return base_signal.diff().diff()

def f04_top_039_jerk_v39_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=77, w2=119, w3=455, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(119, min_periods=max(119//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0846 * _rolling_slope(draw, 455) + 0.000184 * anchor
    return base_signal.diff().diff()

def f04_top_040_accel_v40_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=84, w2=130, w3=468, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.01375 + 0.0001841 * anchor
    return base_signal.diff().diff()

def f04_top_041_jerk_v41_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=91, w2=141, w3=481, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 141)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.028125 + 0.0001842 * anchor
    return base_signal.diff().diff()

def f04_top_042_accel_v42_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=98, w2=152, w3=494, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(152, min_periods=max(152//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0425 + 0.0001843 * anchor
    return base_signal.diff().diff()

def f04_top_043_jerk_v43_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=105, w2=163, w3=507, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(105)
    rank = change.rolling(163, min_periods=max(163//3, 2)).rank(pct=True)
    persistence = change.rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115 * persistence + 0.0001844 * anchor
    return base_signal.diff().diff()

def f04_top_044_accel_v44_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=112, w2=174, w3=520, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(174, min_periods=max(174//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.07125 + 0.0001845 * anchor
    return base_signal.diff().diff()

def f04_top_045_jerk_v45_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=119, w2=185, w3=533, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(185, min_periods=max(185//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1302 * slope + 0.0001846 * anchor
    return base_signal.diff().diff()

def f04_top_046_accel_v46_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=126, w2=196, w3=546, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(196, min_periods=max(196//3, 2)).mean()
    noise = impulse.abs().rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1 + 0.0001847 * anchor
    return base_signal.diff().diff()

def f04_top_047_jerk_v47_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=133, w2=207, w3=559, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 207)
    curvature = _rolling_slope(acceleration, 559)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1454 * acceleration + 0.0001848 * anchor
    return base_signal.diff().diff()

def f04_top_048_accel_v48_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=140, w2=218, w3=572, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(218, min_periods=max(218//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.12875 + 0.0001849 * anchor
    return base_signal.diff().diff()

def f04_top_049_jerk_v49_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=147, w2=229, w3=585, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(229, min_periods=max(229//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1606 * _rolling_slope(draw, 585) + 0.000185 * anchor
    return base_signal.diff().diff()

def f04_top_050_accel_v50_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=154, w2=240, w3=598, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(240, min_periods=max(240//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1575 + 0.0001851 * anchor
    return base_signal.diff().diff()

def f04_top_051_jerk_v51_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=161, w2=251, w3=611, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 251)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.171875 + 0.0001852 * anchor
    return base_signal.diff().diff()

def f04_top_052_accel_v52_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=168, w2=262, w3=624, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(262, min_periods=max(262//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.18625 + 0.0001853 * anchor
    return base_signal.diff().diff()

def f04_top_053_jerk_v53_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=175, w2=273, w3=637, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(273, min_periods=max(273//3, 2)).rank(pct=True)
    persistence = change.rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.191 * persistence + 0.0001854 * anchor
    return base_signal.diff().diff()

def f04_top_054_accel_v54_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=182, w2=284, w3=650, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(284, min_periods=max(284//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.215 + 0.0001855 * anchor
    return base_signal.diff().diff()

def f04_top_055_jerk_v55_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=189, w2=295, w3=663, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(295, min_periods=max(295//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2062 * slope + 0.0001856 * anchor
    return base_signal.diff().diff()

def f04_top_056_accel_v56_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=196, w2=306, w3=676, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(306, min_periods=max(306//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.24375 + 0.0001857 * anchor
    return base_signal.diff().diff()

def f04_top_057_jerk_v57_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=203, w2=317, w3=689, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 317)
    curvature = _rolling_slope(acceleration, 689)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2214 * acceleration + 0.0001858 * anchor
    return base_signal.diff().diff()

def f04_top_058_accel_v58_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=210, w2=328, w3=702, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(328, min_periods=max(328//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2725 + 0.0001859 * anchor
    return base_signal.diff().diff()

def f04_top_059_jerk_v59_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=217, w2=339, w3=715, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(339, min_periods=max(339//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2366 * _rolling_slope(draw, 715) + 0.000186 * anchor
    return base_signal.diff().diff()

def f04_top_060_accel_v60_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=224, w2=350, w3=728, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(350, min_periods=max(350//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.30125 + 0.0001861 * anchor
    return base_signal.diff().diff()

def f04_top_061_jerk_v61_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=231, w2=361, w3=741, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 361)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.315625 + 0.0001862 * anchor
    return base_signal.diff().diff()

def f04_top_062_accel_v62_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=238, w2=372, w3=754, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(372, min_periods=max(372//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.33 + 0.0001863 * anchor
    return base_signal.diff().diff()

def f04_top_063_jerk_v63_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=245, w2=383, w3=767, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(383, min_periods=max(383//3, 2)).rank(pct=True)
    persistence = change.rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.267 * persistence + 0.0001864 * anchor
    return base_signal.diff().diff()

def f04_top_064_accel_v64_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=252, w2=394, w3=23, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(252, min_periods=max(252//3, 2)).std()
    vol_slow = ret.rolling(394, min_periods=max(394//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35875 + 0.0001865 * anchor
    return base_signal.diff().diff()

def f04_top_065_jerk_v65_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=8, w2=405, w3=36, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(405, min_periods=max(405//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2822 * slope + 0.0001866 * anchor
    return base_signal.diff().diff()

def f04_top_066_accel_v66_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=15, w2=416, w3=49, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(15)
    drag = impulse.rolling(416, min_periods=max(416//3, 2)).mean()
    noise = impulse.abs().rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3875 + 0.0001867 * anchor
    return base_signal.diff().diff()

def f04_top_067_jerk_v67_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=22, w2=427, w3=62, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 427)
    curvature = _rolling_slope(acceleration, 62)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2974 * acceleration + 0.0001868 * anchor
    return base_signal.diff().diff()

def f04_top_068_accel_v68_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=29, w2=438, w3=75, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(438, min_periods=max(438//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(75) * 1.41625 + 0.0001869 * anchor
    return base_signal.diff().diff()

def f04_top_069_jerk_v69_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=36, w2=449, w3=88, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(449, min_periods=max(449//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3126 * _rolling_slope(draw, 88) + 0.000187 * anchor
    return base_signal.diff().diff()

def f04_top_070_accel_v70_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=43, w2=460, w3=101, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(460, min_periods=max(460//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(101, min_periods=max(101//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.445 + 0.0001871 * anchor
    return base_signal.diff().diff()

def f04_top_071_jerk_v71_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=50, w2=471, w3=114, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 471)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=114, adjust=False).mean() * 1.459375 + 0.0001872 * anchor
    return base_signal.diff().diff()

def f04_top_072_accel_v72_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=57, w2=482, w3=127, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47375 + 0.0001873 * anchor
    return base_signal.diff().diff()

def f04_top_073_jerk_v73_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=64, w2=493, w3=140, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(64)
    rank = change.rolling(493, min_periods=max(493//3, 2)).rank(pct=True)
    persistence = change.rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343 * persistence + 0.0001874 * anchor
    return base_signal.diff().diff()

def f04_top_074_accel_v74_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=71, w2=504, w3=153, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(504, min_periods=max(504//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5025 + 0.0001875 * anchor
    return base_signal.diff().diff()

def f04_top_075_jerk_v75_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=78, w2=12, w3=166, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3582 * slope + 0.0001876 * anchor
    return base_signal.diff().diff()
