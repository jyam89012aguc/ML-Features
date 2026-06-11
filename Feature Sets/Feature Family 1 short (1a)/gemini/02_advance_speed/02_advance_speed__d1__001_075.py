"""02 advance speed d1 first derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f02_adv_001_jerk_v1_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=196, w2=82, w3=258, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 82)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=258, adjust=False).mean() * 0.985 + 6.02e-05 * anchor
    return base_signal.diff()

def f02_adv_002_accel_v2_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=203, w2=93, w3=271, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.999375 + 6.03e-05 * anchor
    return base_signal.diff()

def f02_adv_003_jerk_v3_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=210, w2=104, w3=284, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(104, min_periods=max(104//3, 2)).rank(pct=True)
    persistence = change.rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.101 * persistence + 6.04e-05 * anchor
    return base_signal.diff()

def f02_adv_004_accel_v4_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=217, w2=115, w3=297, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.028125 + 6.05e-05 * anchor
    return base_signal.diff()

def f02_adv_005_jerk_v5_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=224, w2=126, w3=310, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(126, min_periods=max(126//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1162 * slope + 6.06e-05 * anchor
    return base_signal.diff()

def f02_adv_006_accel_v6_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=231, w2=137, w3=323, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(137, min_periods=max(137//3, 2)).mean()
    noise = impulse.abs().rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.056875 + 6.07e-05 * anchor
    return base_signal.diff()

def f02_adv_007_jerk_v7_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=238, w2=148, w3=336, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 148)
    curvature = _rolling_slope(acceleration, 336)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1314 * acceleration + 6.08e-05 * anchor
    return base_signal.diff()

def f02_adv_008_accel_v8_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=245, w2=159, w3=349, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(159, min_periods=max(159//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.085625 + 6.09e-05 * anchor
    return base_signal.diff()

def f02_adv_009_jerk_v9_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=252, w2=170, w3=362, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(170, min_periods=max(170//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1466 * _rolling_slope(draw, 362) + 6.1e-05 * anchor
    return base_signal.diff()

def f02_adv_010_accel_v10_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=8, w2=181, w3=375, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(181, min_periods=max(181//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.114375 + 6.11e-05 * anchor
    return base_signal.diff()

def f02_adv_011_jerk_v11_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=15, w2=192, w3=388, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 192)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.12875 + 6.12e-05 * anchor
    return base_signal.diff()

def f02_adv_012_accel_v12_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=22, w2=203, w3=401, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(203, min_periods=max(203//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.143125 + 6.13e-05 * anchor
    return base_signal.diff()

def f02_adv_013_jerk_v13_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=29, w2=214, w3=414, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(29)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.177 * persistence + 6.14e-05 * anchor
    return base_signal.diff()

def f02_adv_014_accel_v14_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=36, w2=225, w3=427, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(225, min_periods=max(225//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.171875 + 6.15e-05 * anchor
    return base_signal.diff()

def f02_adv_015_jerk_v15_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=43, w2=236, w3=440, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(236, min_periods=max(236//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1922 * slope + 6.16e-05 * anchor
    return base_signal.diff()

def f02_adv_016_accel_v16_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=50, w2=247, w3=453, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(50)
    drag = impulse.rolling(247, min_periods=max(247//3, 2)).mean()
    noise = impulse.abs().rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.200625 + 6.17e-05 * anchor
    return base_signal.diff()

def f02_adv_017_jerk_v17_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=57, w2=258, w3=466, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 258)
    curvature = _rolling_slope(acceleration, 466)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2074 * acceleration + 6.18e-05 * anchor
    return base_signal.diff()

def f02_adv_018_accel_v18_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=64, w2=269, w3=479, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(269, min_periods=max(269//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.229375 + 6.19e-05 * anchor
    return base_signal.diff()

def f02_adv_019_jerk_v19_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=71, w2=280, w3=492, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(280, min_periods=max(280//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2226 * _rolling_slope(draw, 492) + 6.2e-05 * anchor
    return base_signal.diff()

def f02_adv_020_accel_v20_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=78, w2=291, w3=505, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(291, min_periods=max(291//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.258125 + 6.21e-05 * anchor
    return base_signal.diff()

def f02_adv_021_jerk_v21_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=85, w2=302, w3=518, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 302)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2725 + 6.22e-05 * anchor
    return base_signal.diff()

def f02_adv_022_accel_v22_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=92, w2=313, w3=531, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(313, min_periods=max(313//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.286875 + 6.23e-05 * anchor
    return base_signal.diff()

def f02_adv_023_jerk_v23_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=99, w2=324, w3=544, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(99)
    rank = change.rolling(324, min_periods=max(324//3, 2)).rank(pct=True)
    persistence = change.rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.253 * persistence + 6.24e-05 * anchor
    return base_signal.diff()

def f02_adv_024_accel_v24_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=106, w2=335, w3=557, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(335, min_periods=max(335//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.315625 + 6.25e-05 * anchor
    return base_signal.diff()

def f02_adv_025_jerk_v25_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=113, w2=346, w3=570, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(346, min_periods=max(346//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2682 * slope + 6.26e-05 * anchor
    return base_signal.diff()

def f02_adv_026_accel_v26_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=120, w2=357, w3=583, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(120)
    drag = impulse.rolling(357, min_periods=max(357//3, 2)).mean()
    noise = impulse.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.344375 + 6.27e-05 * anchor
    return base_signal.diff()

def f02_adv_027_jerk_v27_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=127, w2=368, w3=596, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 368)
    curvature = _rolling_slope(acceleration, 596)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2834 * acceleration + 6.28e-05 * anchor
    return base_signal.diff()

def f02_adv_028_accel_v28_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=134, w2=379, w3=609, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(379, min_periods=max(379//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.373125 + 6.29e-05 * anchor
    return base_signal.diff()

def f02_adv_029_jerk_v29_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=141, w2=390, w3=622, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(390, min_periods=max(390//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2986 * _rolling_slope(draw, 622) + 6.3e-05 * anchor
    return base_signal.diff()

def f02_adv_030_accel_v30_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=148, w2=401, w3=635, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(401, min_periods=max(401//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.401875 + 6.31e-05 * anchor
    return base_signal.diff()

def f02_adv_031_jerk_v31_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=155, w2=412, w3=648, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 412)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.41625 + 6.32e-05 * anchor
    return base_signal.diff()

def f02_adv_032_accel_v32_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=162, w2=423, w3=661, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(423, min_periods=max(423//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.430625 + 6.33e-05 * anchor
    return base_signal.diff()

def f02_adv_033_jerk_v33_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=169, w2=434, w3=674, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(434, min_periods=max(434//3, 2)).rank(pct=True)
    persistence = change.rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.329 * persistence + 6.34e-05 * anchor
    return base_signal.diff()

def f02_adv_034_accel_v34_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=176, w2=445, w3=687, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(445, min_periods=max(445//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.459375 + 6.35e-05 * anchor
    return base_signal.diff()

def f02_adv_035_jerk_v35_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=183, w2=456, w3=700, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(456, min_periods=max(456//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3442 * slope + 6.36e-05 * anchor
    return base_signal.diff()

def f02_adv_036_accel_v36_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=190, w2=467, w3=713, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(467, min_periods=max(467//3, 2)).mean()
    noise = impulse.abs().rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.488125 + 6.37e-05 * anchor
    return base_signal.diff()

def f02_adv_037_jerk_v37_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=197, w2=478, w3=726, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 478)
    curvature = _rolling_slope(acceleration, 726)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3594 * acceleration + 6.38e-05 * anchor
    return base_signal.diff()

def f02_adv_038_accel_v38_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=204, w2=489, w3=739, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(489, min_periods=max(489//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.516875 + 6.39e-05 * anchor
    return base_signal.diff()

def f02_adv_039_jerk_v39_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=211, w2=500, w3=752, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(500, min_periods=max(500//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3746 * _rolling_slope(draw, 752) + 6.4e-05 * anchor
    return base_signal.diff()

def f02_adv_040_accel_v40_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=218, w2=511, w3=765, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(511, min_periods=max(511//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.545625 + 6.41e-05 * anchor
    return base_signal.diff()

def f02_adv_041_jerk_v41_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=225, w2=19, w3=21, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=21, adjust=False).mean() * 1.56 + 6.42e-05 * anchor
    return base_signal.diff()

def f02_adv_042_accel_v42_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=232, w2=30, w3=34, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.574375 + 6.43e-05 * anchor
    return base_signal.diff()

def f02_adv_043_jerk_v43_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=239, w2=41, w3=47, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.405 * persistence + 6.44e-05 * anchor
    return base_signal.diff()

def f02_adv_044_accel_v44_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=246, w2=52, w3=60, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.603125 + 6.45e-05 * anchor
    return base_signal.diff()

def f02_adv_045_jerk_v45_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=253, w2=63, w3=73, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(63, min_periods=max(63//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0438 * slope + 6.46e-05 * anchor
    return base_signal.diff()

def f02_adv_046_accel_v46_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=9, w2=74, w3=86, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(9)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.85875 + 6.47e-05 * anchor
    return base_signal.diff()

def f02_adv_047_jerk_v47_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=16, w2=85, w3=99, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 85)
    curvature = _rolling_slope(acceleration, 99)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.059 * acceleration + 6.48e-05 * anchor
    return base_signal.diff()

def f02_adv_048_accel_v48_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=23, w2=96, w3=112, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(96, min_periods=max(96//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(112) * 0.8875 + 6.49e-05 * anchor
    return base_signal.diff()

def f02_adv_049_jerk_v49_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=30, w2=107, w3=125, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(107, min_periods=max(107//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0742 * _rolling_slope(draw, 125) + 6.5e-05 * anchor
    return base_signal.diff()

def f02_adv_050_accel_v50_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=37, w2=118, w3=138, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(118, min_periods=max(118//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.91625 + 6.51e-05 * anchor
    return base_signal.diff()

def f02_adv_051_jerk_v51_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=44, w2=129, w3=151, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 129)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=151, adjust=False).mean() * 0.930625 + 6.52e-05 * anchor
    return base_signal.diff()

def f02_adv_052_accel_v52_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=51, w2=140, w3=164, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(140, min_periods=max(140//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.945 + 6.53e-05 * anchor
    return base_signal.diff()

def f02_adv_053_jerk_v53_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=58, w2=151, w3=177, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(58)
    rank = change.rolling(151, min_periods=max(151//3, 2)).rank(pct=True)
    persistence = change.rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1046 * persistence + 6.54e-05 * anchor
    return base_signal.diff()

def f02_adv_054_accel_v54_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=65, w2=162, w3=190, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(162, min_periods=max(162//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97375 + 6.55e-05 * anchor
    return base_signal.diff()

def f02_adv_055_jerk_v55_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=72, w2=173, w3=203, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(173, min_periods=max(173//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1198 * slope + 6.56e-05 * anchor
    return base_signal.diff()

def f02_adv_056_accel_v56_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=79, w2=184, w3=216, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(79)
    drag = impulse.rolling(184, min_periods=max(184//3, 2)).mean()
    noise = impulse.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0025 + 6.57e-05 * anchor
    return base_signal.diff()

def f02_adv_057_jerk_v57_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=86, w2=195, w3=229, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 229)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.135 * acceleration + 6.58e-05 * anchor
    return base_signal.diff()

def f02_adv_058_accel_v58_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=93, w2=206, w3=242, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.03125 + 6.59e-05 * anchor
    return base_signal.diff()

def f02_adv_059_jerk_v59_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=100, w2=217, w3=255, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(217, min_periods=max(217//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1502 * _rolling_slope(draw, 255) + 6.6e-05 * anchor
    return base_signal.diff()

def f02_adv_060_accel_v60_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=107, w2=228, w3=268, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(228, min_periods=max(228//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.06 + 6.61e-05 * anchor
    return base_signal.diff()

def f02_adv_061_jerk_v61_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=114, w2=239, w3=281, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 239)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=281, adjust=False).mean() * 1.074375 + 6.62e-05 * anchor
    return base_signal.diff()

def f02_adv_062_accel_v62_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=121, w2=250, w3=294, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(250, min_periods=max(250//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.08875 + 6.63e-05 * anchor
    return base_signal.diff()

def f02_adv_063_jerk_v63_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=128, w2=261, w3=307, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(261, min_periods=max(261//3, 2)).rank(pct=True)
    persistence = change.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1806 * persistence + 6.64e-05 * anchor
    return base_signal.diff()

def f02_adv_064_accel_v64_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=135, w2=272, w3=320, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(272, min_periods=max(272//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1175 + 6.65e-05 * anchor
    return base_signal.diff()

def f02_adv_065_jerk_v65_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=142, w2=283, w3=333, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(283, min_periods=max(283//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1958 * slope + 6.66e-05 * anchor
    return base_signal.diff()

def f02_adv_066_accel_v66_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=149, w2=294, w3=346, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(294, min_periods=max(294//3, 2)).mean()
    noise = impulse.abs().rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.14625 + 6.67e-05 * anchor
    return base_signal.diff()

def f02_adv_067_jerk_v67_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=156, w2=305, w3=359, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 305)
    curvature = _rolling_slope(acceleration, 359)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211 * acceleration + 6.68e-05 * anchor
    return base_signal.diff()

def f02_adv_068_accel_v68_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=163, w2=316, w3=372, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(316, min_periods=max(316//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.175 + 6.69e-05 * anchor
    return base_signal.diff()

def f02_adv_069_jerk_v69_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=170, w2=327, w3=385, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(327, min_periods=max(327//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2262 * _rolling_slope(draw, 385) + 6.7e-05 * anchor
    return base_signal.diff()

def f02_adv_070_accel_v70_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=177, w2=338, w3=398, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.20375 + 6.71e-05 * anchor
    return base_signal.diff()

def f02_adv_071_jerk_v71_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=184, w2=349, w3=411, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 349)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.218125 + 6.72e-05 * anchor
    return base_signal.diff()

def f02_adv_072_accel_v72_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=191, w2=360, w3=424, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2325 + 6.73e-05 * anchor
    return base_signal.diff()

def f02_adv_073_jerk_v73_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=198, w2=371, w3=437, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(371, min_periods=max(371//3, 2)).rank(pct=True)
    persistence = change.rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2566 * persistence + 6.74e-05 * anchor
    return base_signal.diff()

def f02_adv_074_accel_v74_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=205, w2=382, w3=450, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26125 + 6.75e-05 * anchor
    return base_signal.diff()

def f02_adv_075_jerk_v75_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=212, w2=393, w3=463, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(393, min_periods=max(393//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2718 * slope + 6.76e-05 * anchor
    return base_signal.diff()
