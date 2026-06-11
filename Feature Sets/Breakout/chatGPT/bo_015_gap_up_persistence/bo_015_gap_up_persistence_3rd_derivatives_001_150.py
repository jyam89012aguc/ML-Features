import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _safe_div(a, b):
    if hasattr(b, "replace"):
        denom = b.replace(0, np.nan)
    else:
        denom = np.nan if b == 0 else b
    return a / denom


def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return _safe_div(s - m, sd)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _ret(s, n):
    denom = s.shift(n).abs()
    denom = denom.where(denom != 0, 1.0)
    return (s - s.shift(n)) / denom


def _slope(s, w):
    denom = s.abs().rolling(w, min_periods=max(2, w // 2)).mean()
    denom = denom.where(denom != 0, 1.0)
    return s.diff(periods=w) / denom


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(2, span // 2)).mean()


def _true_range(high, low, close):
    prev = close.shift(1)
    a = high - low
    b = (high - prev).abs()
    c = (low - prev).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _atr(high, low, close, w):
    return _true_range(high, low, close).rolling(w, min_periods=max(2, w // 2)).mean()


def _roll_slope(s, w):
    x = pd.Series(np.arange(w), index=range(w), dtype=float)
    xm = x.mean()
    denom = ((x - xm) ** 2).sum()
    return s.rolling(w, min_periods=max(3, w // 2)).apply(
        lambda y: float(np.dot(np.asarray(y) - np.nanmean(y), x[-len(y):] - x[-len(y):].mean()) / denom)
        if len(y) >= 3 and denom != 0 else np.nan,
        raw=False,
    )


def _obv(close, volume):
    direction = np.sign(close.diff()).fillna(0.0)
    return (direction * volume).cumsum()


def _adline(high, low, close, volume):
    mfm = _safe_div((close - low) - (high - close), high - low)
    return (mfm.fillna(0.0) * volume).cumsum()


def _mfi(high, low, close, volume, w):
    typical = (high + low + close) / 3.0
    flow = typical * volume
    pos = flow.where(typical.diff() > 0, 0.0).rolling(w, min_periods=max(2, w // 2)).sum()
    neg = flow.where(typical.diff() < 0, 0.0).abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return 100.0 - (100.0 / (1.0 + _safe_div(pos, neg)))


def _growth(s, n):
    return _safe_div(s - s.shift(n), s.shift(n).abs())


def _margin(num, den):
    return _safe_div(num, den.abs())



def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


# 21d acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accel_21d_3d_v001_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accel_63d_3d_v002_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accel_126d_3d_v003_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accel_norm_63d_3d_v004_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_jerk_21d_3d_v005_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_jerk_63d_3d_v006_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accelz_21_252_3d_v007_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accelz_63_504_3d_v008_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_smoothaccel_63_252_3d_v009_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_rngaccel_63_252_3d_v010_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_ignition_curvature_3d_v011_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accel_252d_3d_v012_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_jerk_126d_3d_v013_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accelz_126_504_3d_v014_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_accel_norm_21d_3d_v015_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence
def bo_015_gap_up_persistence_gap_up_persistence_curvature_gap_3d_v016_signal(open, closeadj):
    base = _safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_21d_3d_v017_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_63d_3d_v018_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_126d_3d_v019_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_norm_63d_3d_v020_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_jerk_21d_3d_v021_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_jerk_63d_3d_v022_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accelz_21_252_3d_v023_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accelz_63_504_3d_v024_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_smoothaccel_63_252_3d_v025_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_rngaccel_63_252_3d_v026_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_ignition_curvature_3d_v027_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_252d_3d_v028_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_jerk_126d_3d_v029_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accelz_126_504_3d_v030_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_norm_21d_3d_v031_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_mean_14d
def bo_015_gap_up_persistence_gap_up_persistence_mean_14d_curvature_gap_3d_v032_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 14)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_21d_3d_v033_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_63d_3d_v034_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_126d_3d_v035_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_norm_63d_3d_v036_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_jerk_21d_3d_v037_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_jerk_63d_3d_v038_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accelz_21_252_3d_v039_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accelz_63_504_3d_v040_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_smoothaccel_63_252_3d_v041_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_rngaccel_63_252_3d_v042_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_ignition_curvature_3d_v043_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_252d_3d_v044_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_jerk_126d_3d_v045_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accelz_126_504_3d_v046_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_norm_21d_3d_v047_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_curvature_gap_3d_v048_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_21d_3d_v049_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_63d_3d_v050_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_126d_3d_v051_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_norm_63d_3d_v052_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_jerk_21d_3d_v053_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_jerk_63d_3d_v054_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accelz_21_252_3d_v055_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accelz_63_504_3d_v056_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_smoothaccel_63_252_3d_v057_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_rngaccel_63_252_3d_v058_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_ignition_curvature_3d_v059_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_252d_3d_v060_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_jerk_126d_3d_v061_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accelz_126_504_3d_v062_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_norm_21d_3d_v063_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_curvature_gap_3d_v064_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_21d_3d_v065_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_63d_3d_v066_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_126d_3d_v067_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_norm_63d_3d_v068_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_jerk_21d_3d_v069_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_jerk_63d_3d_v070_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accelz_21_252_3d_v071_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accelz_63_504_3d_v072_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_smoothaccel_63_252_3d_v073_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_rngaccel_63_252_3d_v074_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_ignition_curvature_3d_v075_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_252d_3d_v076_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_jerk_126d_3d_v077_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accelz_126_504_3d_v078_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_norm_21d_3d_v079_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_curvature_gap_3d_v080_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_21d_3d_v081_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_63d_3d_v082_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_126d_3d_v083_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_norm_63d_3d_v084_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_jerk_21d_3d_v085_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_jerk_63d_3d_v086_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accelz_21_252_3d_v087_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accelz_63_504_3d_v088_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_smoothaccel_63_252_3d_v089_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_rngaccel_63_252_3d_v090_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_ignition_curvature_3d_v091_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_252d_3d_v092_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_jerk_126d_3d_v093_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accelz_126_504_3d_v094_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_norm_21d_3d_v095_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_distmax_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_curvature_gap_3d_v096_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_21d_3d_v097_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_63d_3d_v098_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_126d_3d_v099_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_norm_63d_3d_v100_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_jerk_21d_3d_v101_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_jerk_63d_3d_v102_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accelz_21_252_3d_v103_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accelz_63_504_3d_v104_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_smoothaccel_63_252_3d_v105_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_rngaccel_63_252_3d_v106_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_ignition_curvature_3d_v107_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_252d_3d_v108_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_jerk_126d_3d_v109_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accelz_126_504_3d_v110_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_norm_21d_3d_v111_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_distmin_252d
def bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_curvature_gap_3d_v112_signal(open, closeadj):
    base = _safe_div((_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min(), (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_21d_3d_v129_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_63d_3d_v130_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_126d_3d_v131_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_norm_63d_3d_v132_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_jerk_21d_3d_v133_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_jerk_63d_3d_v134_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accelz_21_252_3d_v135_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accelz_63_504_3d_v136_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_smoothaccel_63_252_3d_v137_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_rngaccel_63_252_3d_v138_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_ignition_curvature_3d_v139_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_252d_3d_v140_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_jerk_126d_3d_v141_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accelz_126_504_3d_v142_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_norm_21d_3d_v143_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for gap_up_persistence_upper_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_curvature_gap_3d_v144_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for gap_up_persistence_lower_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_21d_3d_v145_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for gap_up_persistence_lower_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_63d_3d_v146_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for gap_up_persistence_lower_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_126d_3d_v147_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for gap_up_persistence_lower_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_norm_63d_3d_v148_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for gap_up_persistence_lower_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_jerk_21d_3d_v149_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for gap_up_persistence_lower_gap_84d
def bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_jerk_63d_3d_v150_signal(open, closeadj):
    base = (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)) - (_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float)).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['open', 'closeadj'], "func": fn} for fn in [bo_015_gap_up_persistence_gap_up_persistence_accel_21d_3d_v001_signal, bo_015_gap_up_persistence_gap_up_persistence_accel_63d_3d_v002_signal, bo_015_gap_up_persistence_gap_up_persistence_accel_126d_3d_v003_signal, bo_015_gap_up_persistence_gap_up_persistence_accel_norm_63d_3d_v004_signal, bo_015_gap_up_persistence_gap_up_persistence_jerk_21d_3d_v005_signal, bo_015_gap_up_persistence_gap_up_persistence_jerk_63d_3d_v006_signal, bo_015_gap_up_persistence_gap_up_persistence_accelz_21_252_3d_v007_signal, bo_015_gap_up_persistence_gap_up_persistence_accelz_63_504_3d_v008_signal, bo_015_gap_up_persistence_gap_up_persistence_smoothaccel_63_252_3d_v009_signal, bo_015_gap_up_persistence_gap_up_persistence_rngaccel_63_252_3d_v010_signal, bo_015_gap_up_persistence_gap_up_persistence_ignition_curvature_3d_v011_signal, bo_015_gap_up_persistence_gap_up_persistence_accel_252d_3d_v012_signal, bo_015_gap_up_persistence_gap_up_persistence_jerk_126d_3d_v013_signal, bo_015_gap_up_persistence_gap_up_persistence_accelz_126_504_3d_v014_signal, bo_015_gap_up_persistence_gap_up_persistence_accel_norm_21d_3d_v015_signal, bo_015_gap_up_persistence_gap_up_persistence_curvature_gap_3d_v016_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_21d_3d_v017_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_63d_3d_v018_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_126d_3d_v019_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_norm_63d_3d_v020_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_jerk_21d_3d_v021_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_jerk_63d_3d_v022_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accelz_21_252_3d_v023_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accelz_63_504_3d_v024_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_smoothaccel_63_252_3d_v025_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_rngaccel_63_252_3d_v026_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_ignition_curvature_3d_v027_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_252d_3d_v028_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_jerk_126d_3d_v029_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accelz_126_504_3d_v030_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_accel_norm_21d_3d_v031_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_14d_curvature_gap_3d_v032_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_21d_3d_v033_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_63d_3d_v034_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_126d_3d_v035_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_norm_63d_3d_v036_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_jerk_21d_3d_v037_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_jerk_63d_3d_v038_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accelz_21_252_3d_v039_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accelz_63_504_3d_v040_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_smoothaccel_63_252_3d_v041_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_rngaccel_63_252_3d_v042_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_ignition_curvature_3d_v043_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_252d_3d_v044_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_jerk_126d_3d_v045_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accelz_126_504_3d_v046_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_accel_norm_21d_3d_v047_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_curvature_gap_3d_v048_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_21d_3d_v049_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_63d_3d_v050_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_126d_3d_v051_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_norm_63d_3d_v052_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_jerk_21d_3d_v053_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_jerk_63d_3d_v054_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accelz_21_252_3d_v055_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accelz_63_504_3d_v056_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_smoothaccel_63_252_3d_v057_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_rngaccel_63_252_3d_v058_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_ignition_curvature_3d_v059_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_252d_3d_v060_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_jerk_126d_3d_v061_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accelz_126_504_3d_v062_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_accel_norm_21d_3d_v063_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_curvature_gap_3d_v064_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_21d_3d_v065_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_63d_3d_v066_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_126d_3d_v067_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_norm_63d_3d_v068_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_jerk_21d_3d_v069_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_jerk_63d_3d_v070_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accelz_21_252_3d_v071_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accelz_63_504_3d_v072_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_smoothaccel_63_252_3d_v073_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_rngaccel_63_252_3d_v074_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_ignition_curvature_3d_v075_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_252d_3d_v076_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_jerk_126d_3d_v077_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accelz_126_504_3d_v078_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_accel_norm_21d_3d_v079_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_curvature_gap_3d_v080_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_21d_3d_v081_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_63d_3d_v082_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_126d_3d_v083_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_norm_63d_3d_v084_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_jerk_21d_3d_v085_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_jerk_63d_3d_v086_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accelz_21_252_3d_v087_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accelz_63_504_3d_v088_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_smoothaccel_63_252_3d_v089_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_rngaccel_63_252_3d_v090_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_ignition_curvature_3d_v091_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_252d_3d_v092_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_jerk_126d_3d_v093_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accelz_126_504_3d_v094_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_accel_norm_21d_3d_v095_signal, bo_015_gap_up_persistence_gap_up_persistence_distmax_252d_curvature_gap_3d_v096_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_21d_3d_v097_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_63d_3d_v098_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_126d_3d_v099_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_norm_63d_3d_v100_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_jerk_21d_3d_v101_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_jerk_63d_3d_v102_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accelz_21_252_3d_v103_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accelz_63_504_3d_v104_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_smoothaccel_63_252_3d_v105_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_rngaccel_63_252_3d_v106_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_ignition_curvature_3d_v107_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_252d_3d_v108_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_jerk_126d_3d_v109_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accelz_126_504_3d_v110_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_accel_norm_21d_3d_v111_signal, bo_015_gap_up_persistence_gap_up_persistence_distmin_252d_curvature_gap_3d_v112_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_21d_3d_v129_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_63d_3d_v130_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_126d_3d_v131_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_norm_63d_3d_v132_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_jerk_21d_3d_v133_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_jerk_63d_3d_v134_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accelz_21_252_3d_v135_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accelz_63_504_3d_v136_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_smoothaccel_63_252_3d_v137_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_rngaccel_63_252_3d_v138_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_ignition_curvature_3d_v139_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_252d_3d_v140_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_jerk_126d_3d_v141_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accelz_126_504_3d_v142_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_accel_norm_21d_3d_v143_signal, bo_015_gap_up_persistence_gap_up_persistence_upper_gap_84d_curvature_gap_3d_v144_signal, bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_21d_3d_v145_signal, bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_63d_3d_v146_signal, bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_126d_3d_v147_signal, bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_accel_norm_63d_3d_v148_signal, bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_jerk_21d_3d_v149_signal, bo_015_gap_up_persistence_gap_up_persistence_lower_gap_84d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
