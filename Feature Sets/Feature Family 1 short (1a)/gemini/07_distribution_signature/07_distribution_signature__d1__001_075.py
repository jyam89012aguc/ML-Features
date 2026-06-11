"""07 distribution signature d1 first derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f07_dsi_001_jerk_v1_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=112, w2=387, w3=651, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 387)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.588125 + 0.0003602 * anchor
    return base_signal.diff()

def f07_dsi_002_accel_v2_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=119, w2=398, w3=664, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(398, min_periods=max(398//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6025 + 0.0003603 * anchor
    return base_signal.diff()

def f07_dsi_003_jerk_v3_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=126, w2=409, w3=677, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(409, min_periods=max(409//3, 2)).rank(pct=True)
    persistence = change.rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.317 * persistence + 0.0003604 * anchor
    return base_signal.diff()

def f07_dsi_004_accel_v4_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=133, w2=420, w3=690, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(420, min_periods=max(420//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.858125 + 0.0003605 * anchor
    return base_signal.diff()

def f07_dsi_005_jerk_v5_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=140, w2=431, w3=703, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(431, min_periods=max(431//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3322 * slope + 0.0003606 * anchor
    return base_signal.diff()

def f07_dsi_006_accel_v6_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=147, w2=442, w3=716, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(442, min_periods=max(442//3, 2)).mean()
    noise = impulse.abs().rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.886875 + 0.0003607 * anchor
    return base_signal.diff()

def f07_dsi_007_jerk_v7_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=154, w2=453, w3=729, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 453)
    curvature = _rolling_slope(acceleration, 729)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3474 * acceleration + 0.0003608 * anchor
    return base_signal.diff()

def f07_dsi_008_accel_v8_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=161, w2=464, w3=742, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(464, min_periods=max(464//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.915625 + 0.0003609 * anchor
    return base_signal.diff()

def f07_dsi_009_jerk_v9_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=168, w2=475, w3=755, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(475, min_periods=max(475//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3626 * _rolling_slope(draw, 755) + 0.000361 * anchor
    return base_signal.diff()

def f07_dsi_010_accel_v10_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=175, w2=486, w3=768, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(486, min_periods=max(486//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.944375 + 0.0003611 * anchor
    return base_signal.diff()

def f07_dsi_011_jerk_v11_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=182, w2=497, w3=24, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 497)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=24, adjust=False).mean() * 0.95875 + 0.0003612 * anchor
    return base_signal.diff()

def f07_dsi_012_accel_v12_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=189, w2=508, w3=37, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.973125 + 0.0003613 * anchor
    return base_signal.diff()

def f07_dsi_013_jerk_v13_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=196, w2=16, w3=50, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(16, min_periods=max(16//3, 2)).rank(pct=True)
    persistence = change.rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.393 * persistence + 0.0003614 * anchor
    return base_signal.diff()

def f07_dsi_014_accel_v14_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=203, w2=27, w3=63, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(27, min_periods=max(27//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.001875 + 0.0003615 * anchor
    return base_signal.diff()

def f07_dsi_015_jerk_v15_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=210, w2=38, w3=76, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(38, min_periods=max(38//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4082 * slope + 0.0003616 * anchor
    return base_signal.diff()

def f07_dsi_016_accel_v16_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=217, w2=49, w3=89, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.030625 + 0.0003617 * anchor
    return base_signal.diff()

def f07_dsi_017_jerk_v17_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=224, w2=60, w3=102, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 102)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.047 * acceleration + 0.0003618 * anchor
    return base_signal.diff()

def f07_dsi_018_accel_v18_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=231, w2=71, w3=115, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(71, min_periods=max(71//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(115) * 1.059375 + 0.0003619 * anchor
    return base_signal.diff()

def f07_dsi_019_jerk_v19_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=238, w2=82, w3=128, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(82, min_periods=max(82//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0622 * _rolling_slope(draw, 128) + 0.000362 * anchor
    return base_signal.diff()

def f07_dsi_020_accel_v20_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=245, w2=93, w3=141, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(93, min_periods=max(93//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.088125 + 0.0003621 * anchor
    return base_signal.diff()

def f07_dsi_021_jerk_v21_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=252, w2=104, w3=154, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 104)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=154, adjust=False).mean() * 1.1025 + 0.0003622 * anchor
    return base_signal.diff()

def f07_dsi_022_accel_v22_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=8, w2=115, w3=167, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(115, min_periods=max(115//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.116875 + 0.0003623 * anchor
    return base_signal.diff()

def f07_dsi_023_jerk_v23_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=15, w2=126, w3=180, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(15)
    rank = change.rolling(126, min_periods=max(126//3, 2)).rank(pct=True)
    persistence = change.rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0926 * persistence + 0.0003624 * anchor
    return base_signal.diff()

def f07_dsi_024_accel_v24_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=22, w2=137, w3=193, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(137, min_periods=max(137//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.145625 + 0.0003625 * anchor
    return base_signal.diff()

def f07_dsi_025_jerk_v25_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=29, w2=148, w3=206, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(148, min_periods=max(148//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1078 * slope + 0.0003626 * anchor
    return base_signal.diff()

def f07_dsi_026_accel_v26_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=36, w2=159, w3=219, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(36)
    drag = impulse.rolling(159, min_periods=max(159//3, 2)).mean()
    noise = impulse.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.174375 + 0.0003627 * anchor
    return base_signal.diff()

def f07_dsi_027_jerk_v27_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=43, w2=170, w3=232, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 170)
    curvature = _rolling_slope(acceleration, 232)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.123 * acceleration + 0.0003628 * anchor
    return base_signal.diff()

def f07_dsi_028_accel_v28_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=50, w2=181, w3=245, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(181, min_periods=max(181//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.203125 + 0.0003629 * anchor
    return base_signal.diff()

def f07_dsi_029_jerk_v29_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=57, w2=192, w3=258, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(192, min_periods=max(192//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1382 * _rolling_slope(draw, 258) + 0.000363 * anchor
    return base_signal.diff()

def f07_dsi_030_accel_v30_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=64, w2=203, w3=271, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(203, min_periods=max(203//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.231875 + 0.0003631 * anchor
    return base_signal.diff()

def f07_dsi_031_jerk_v31_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=71, w2=214, w3=284, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 214)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=284, adjust=False).mean() * 1.24625 + 0.0003632 * anchor
    return base_signal.diff()

def f07_dsi_032_accel_v32_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=78, w2=225, w3=297, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(225, min_periods=max(225//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.260625 + 0.0003633 * anchor
    return base_signal.diff()

def f07_dsi_033_jerk_v33_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=85, w2=236, w3=310, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(85)
    rank = change.rolling(236, min_periods=max(236//3, 2)).rank(pct=True)
    persistence = change.rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1686 * persistence + 0.0003634 * anchor
    return base_signal.diff()

def f07_dsi_034_accel_v34_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=92, w2=247, w3=323, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(247, min_periods=max(247//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.289375 + 0.0003635 * anchor
    return base_signal.diff()

def f07_dsi_035_jerk_v35_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=99, w2=258, w3=336, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(258, min_periods=max(258//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1838 * slope + 0.0003636 * anchor
    return base_signal.diff()

def f07_dsi_036_accel_v36_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=106, w2=269, w3=349, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(106)
    drag = impulse.rolling(269, min_periods=max(269//3, 2)).mean()
    noise = impulse.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.318125 + 0.0003637 * anchor
    return base_signal.diff()

def f07_dsi_037_jerk_v37_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=113, w2=280, w3=362, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 280)
    curvature = _rolling_slope(acceleration, 362)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.199 * acceleration + 0.0003638 * anchor
    return base_signal.diff()

def f07_dsi_038_accel_v38_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=120, w2=291, w3=375, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(291, min_periods=max(291//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.346875 + 0.0003639 * anchor
    return base_signal.diff()

def f07_dsi_039_jerk_v39_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=127, w2=302, w3=388, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(302, min_periods=max(302//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2142 * _rolling_slope(draw, 388) + 0.000364 * anchor
    return base_signal.diff()

def f07_dsi_040_accel_v40_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=134, w2=313, w3=401, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(313, min_periods=max(313//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.375625 + 0.0003641 * anchor
    return base_signal.diff()

def f07_dsi_041_jerk_v41_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=141, w2=324, w3=414, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 324)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.39 + 0.0003642 * anchor
    return base_signal.diff()

def f07_dsi_042_accel_v42_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=148, w2=335, w3=427, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(335, min_periods=max(335//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.404375 + 0.0003643 * anchor
    return base_signal.diff()

def f07_dsi_043_jerk_v43_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=155, w2=346, w3=440, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(346, min_periods=max(346//3, 2)).rank(pct=True)
    persistence = change.rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2446 * persistence + 0.0003644 * anchor
    return base_signal.diff()

def f07_dsi_044_accel_v44_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=162, w2=357, w3=453, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(357, min_periods=max(357//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.433125 + 0.0003645 * anchor
    return base_signal.diff()

def f07_dsi_045_jerk_v45_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=169, w2=368, w3=466, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(368, min_periods=max(368//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2598 * slope + 0.0003646 * anchor
    return base_signal.diff()

def f07_dsi_046_accel_v46_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=176, w2=379, w3=479, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(379, min_periods=max(379//3, 2)).mean()
    noise = impulse.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.461875 + 0.0003647 * anchor
    return base_signal.diff()

def f07_dsi_047_jerk_v47_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=183, w2=390, w3=492, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 390)
    curvature = _rolling_slope(acceleration, 492)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.275 * acceleration + 0.0003648 * anchor
    return base_signal.diff()

def f07_dsi_048_accel_v48_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=190, w2=401, w3=505, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(401, min_periods=max(401//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.490625 + 0.0003649 * anchor
    return base_signal.diff()

def f07_dsi_049_jerk_v49_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=197, w2=412, w3=518, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(412, min_periods=max(412//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2902 * _rolling_slope(draw, 518) + 0.000365 * anchor
    return base_signal.diff()

def f07_dsi_050_accel_v50_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=204, w2=423, w3=531, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(423, min_periods=max(423//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.519375 + 0.0003651 * anchor
    return base_signal.diff()

def f07_dsi_051_jerk_v51_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=211, w2=434, w3=544, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 434)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.53375 + 0.0003652 * anchor
    return base_signal.diff()

def f07_dsi_052_accel_v52_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=218, w2=445, w3=557, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(445, min_periods=max(445//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.548125 + 0.0003653 * anchor
    return base_signal.diff()

def f07_dsi_053_jerk_v53_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=225, w2=456, w3=570, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(456, min_periods=max(456//3, 2)).rank(pct=True)
    persistence = change.rolling(570, min_periods=max(570//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3206 * persistence + 0.0003654 * anchor
    return base_signal.diff()

def f07_dsi_054_accel_v54_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=232, w2=467, w3=583, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(467, min_periods=max(467//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.576875 + 0.0003655 * anchor
    return base_signal.diff()

def f07_dsi_055_jerk_v55_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=239, w2=478, w3=596, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(478, min_periods=max(478//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3358 * slope + 0.0003656 * anchor
    return base_signal.diff()

def f07_dsi_056_accel_v56_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=246, w2=489, w3=609, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(489, min_periods=max(489//3, 2)).mean()
    noise = impulse.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.605625 + 0.0003657 * anchor
    return base_signal.diff()

def f07_dsi_057_jerk_v57_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=253, w2=500, w3=622, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 253)
    acceleration = _rolling_slope(velocity, 500)
    curvature = _rolling_slope(acceleration, 622)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351 * acceleration + 0.0003658 * anchor
    return base_signal.diff()

def f07_dsi_058_accel_v58_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=9, w2=511, w3=635, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(511, min_periods=max(511//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.86125 + 0.0003659 * anchor
    return base_signal.diff()

def f07_dsi_059_jerk_v59_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=16, w2=19, w3=648, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(19, min_periods=max(19//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3662 * _rolling_slope(draw, 648) + 0.000366 * anchor
    return base_signal.diff()

def f07_dsi_060_accel_v60_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=23, w2=30, w3=661, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(30, min_periods=max(30//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.89 + 0.0003661 * anchor
    return base_signal.diff()

def f07_dsi_061_jerk_v61_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=30, w2=41, w3=674, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 41)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.904375 + 0.0003662 * anchor
    return base_signal.diff()

def f07_dsi_062_accel_v62_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=37, w2=52, w3=687, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(52, min_periods=max(52//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.91875 + 0.0003663 * anchor
    return base_signal.diff()

def f07_dsi_063_jerk_v63_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=44, w2=63, w3=700, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(44)
    rank = change.rolling(63, min_periods=max(63//3, 2)).rank(pct=True)
    persistence = change.rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3966 * persistence + 0.0003664 * anchor
    return base_signal.diff()

def f07_dsi_064_accel_v64_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=51, w2=74, w3=713, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(74, min_periods=max(74//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9475 + 0.0003665 * anchor
    return base_signal.diff()

def f07_dsi_065_jerk_v65_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=58, w2=85, w3=726, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0354 * slope + 0.0003666 * anchor
    return base_signal.diff()

def f07_dsi_066_accel_v66_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=65, w2=96, w3=739, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(65)
    drag = impulse.rolling(96, min_periods=max(96//3, 2)).mean()
    noise = impulse.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.97625 + 0.0003667 * anchor
    return base_signal.diff()

def f07_dsi_067_jerk_v67_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=72, w2=107, w3=752, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 107)
    curvature = _rolling_slope(acceleration, 752)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0506 * acceleration + 0.0003668 * anchor
    return base_signal.diff()

def f07_dsi_068_accel_v68_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=79, w2=118, w3=765, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(118, min_periods=max(118//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.005 + 0.0003669 * anchor
    return base_signal.diff()

def f07_dsi_069_jerk_v69_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=86, w2=129, w3=21, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(129, min_periods=max(129//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0658 * _rolling_slope(draw, 21) + 0.000367 * anchor
    return base_signal.diff()

def f07_dsi_070_accel_v70_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=93, w2=140, w3=34, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(140, min_periods=max(140//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.03375 + 0.0003671 * anchor
    return base_signal.diff()

def f07_dsi_071_jerk_v71_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=100, w2=151, w3=47, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 151)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=47, adjust=False).mean() * 1.048125 + 0.0003672 * anchor
    return base_signal.diff()

def f07_dsi_072_accel_v72_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=107, w2=162, w3=60, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(162, min_periods=max(162//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0625 + 0.0003673 * anchor
    return base_signal.diff()

def f07_dsi_073_jerk_v73_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=114, w2=173, w3=73, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(114)
    rank = change.rolling(173, min_periods=max(173//3, 2)).rank(pct=True)
    persistence = change.rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0962 * persistence + 0.0003674 * anchor
    return base_signal.diff()

def f07_dsi_074_accel_v74_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=121, w2=184, w3=86, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(184, min_periods=max(184//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09125 + 0.0003675 * anchor
    return base_signal.diff()

def f07_dsi_075_jerk_v75_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=128, w2=195, w3=99, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(195, min_periods=max(195//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1114 * slope + 0.0003676 * anchor
    return base_signal.diff()
