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


# 21d acceleration for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_21d_3d_v001_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_63d_3d_v002_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_126d_3d_v003_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_norm_63d_3d_v004_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_jerk_21d_3d_v005_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_jerk_63d_3d_v006_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accelz_21_252_3d_v007_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accelz_63_504_3d_v008_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_smoothaccel_63_252_3d_v009_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_ignition_curvature_3d_v011_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_252d_3d_v012_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_jerk_126d_3d_v013_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_accelz_126_504_3d_v014_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_curvature_gap_3d_v016_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_21d_3d_v017_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_63d_3d_v018_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_126d_3d_v019_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_norm_63d_3d_v020_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_jerk_21d_3d_v021_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_jerk_63d_3d_v022_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accelz_21_252_3d_v023_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accelz_63_504_3d_v024_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_smoothaccel_63_252_3d_v025_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rngaccel_63_252_3d_v026_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_ignition_curvature_3d_v027_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_252d_3d_v028_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_jerk_126d_3d_v029_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accelz_126_504_3d_v030_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_norm_21d_3d_v031_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_curvature_gap_3d_v032_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_21d_3d_v033_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_63d_3d_v034_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_126d_3d_v035_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_norm_63d_3d_v036_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_jerk_21d_3d_v037_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_jerk_63d_3d_v038_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accelz_21_252_3d_v039_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accelz_63_504_3d_v040_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_smoothaccel_63_252_3d_v041_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rngaccel_63_252_3d_v042_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_ignition_curvature_3d_v043_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_252d_3d_v044_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_jerk_126d_3d_v045_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accelz_126_504_3d_v046_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_norm_21d_3d_v047_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_curvature_gap_3d_v048_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_21d_3d_v049_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_63d_3d_v050_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_126d_3d_v051_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_norm_63d_3d_v052_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_jerk_21d_3d_v053_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_jerk_63d_3d_v054_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accelz_21_252_3d_v055_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# range-normalized acceleration for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_rngaccel_63_252_3d_v058_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_ignition_curvature_3d_v059_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 21d normalized acceleration for revenue_growth_persistence_z_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_norm_21d_3d_v063_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_21d_3d_v065_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_63d_3d_v066_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_126d_3d_v067_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_norm_63d_3d_v068_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_jerk_21d_3d_v069_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_jerk_63d_3d_v070_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accelz_21_252_3d_v071_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accelz_63_504_3d_v072_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_smoothaccel_63_252_3d_v073_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_rngaccel_63_252_3d_v074_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_ignition_curvature_3d_v075_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_252d_3d_v076_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_jerk_126d_3d_v077_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accelz_126_504_3d_v078_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_norm_21d_3d_v079_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for revenue_growth_persistence_z_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_curvature_gap_3d_v080_signal(revenue):
    base = _z((_growth(revenue, 252).diff(252) > 0).astype(float), 756)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accel_norm_63d_3d_v084_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_jerk_21d_3d_v085_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_jerk_63d_3d_v086_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accelz_21_252_3d_v087_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accelz_63_504_3d_v088_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_smoothaccel_63_252_3d_v089_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_ignition_curvature_3d_v091_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d jerk for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_jerk_126d_3d_v093_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accelz_126_504_3d_v094_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for revenue_growth_persistence_distmax_756d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accel_norm_21d_3d_v095_signal(revenue):
    base = _safe_div(((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max(), ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_21d_3d_v129_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_63d_3d_v130_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_126d_3d_v131_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_norm_63d_3d_v132_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_jerk_21d_3d_v133_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_jerk_63d_3d_v134_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accelz_21_252_3d_v135_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accelz_63_504_3d_v136_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_smoothaccel_63_252_3d_v137_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_rngaccel_63_252_3d_v138_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_ignition_curvature_3d_v139_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_252d_3d_v140_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_jerk_126d_3d_v141_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accelz_126_504_3d_v142_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_norm_21d_3d_v143_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for revenue_growth_persistence_upper_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_curvature_gap_3d_v144_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for revenue_growth_persistence_lower_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_21d_3d_v145_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for revenue_growth_persistence_lower_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_63d_3d_v146_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for revenue_growth_persistence_lower_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_126d_3d_v147_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for revenue_growth_persistence_lower_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_norm_63d_3d_v148_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for revenue_growth_persistence_lower_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_jerk_21d_3d_v149_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for revenue_growth_persistence_lower_gap_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_jerk_63d_3d_v150_signal(revenue):
    base = ((_growth(revenue, 252).diff(252) > 0).astype(float)) - ((_growth(revenue, 252).diff(252) > 0).astype(float)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['revenue'], "func": fn} for fn in [bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_21d_3d_v001_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_63d_3d_v002_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_126d_3d_v003_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_norm_63d_3d_v004_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_jerk_21d_3d_v005_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_jerk_63d_3d_v006_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accelz_21_252_3d_v007_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accelz_63_504_3d_v008_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_smoothaccel_63_252_3d_v009_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_ignition_curvature_3d_v011_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accel_252d_3d_v012_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_jerk_126d_3d_v013_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_accelz_126_504_3d_v014_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_curvature_gap_3d_v016_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_21d_3d_v017_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_63d_3d_v018_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_126d_3d_v019_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_norm_63d_3d_v020_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_jerk_21d_3d_v021_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_jerk_63d_3d_v022_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accelz_21_252_3d_v023_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accelz_63_504_3d_v024_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_smoothaccel_63_252_3d_v025_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rngaccel_63_252_3d_v026_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_ignition_curvature_3d_v027_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_252d_3d_v028_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_jerk_126d_3d_v029_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accelz_126_504_3d_v030_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_accel_norm_21d_3d_v031_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_curvature_gap_3d_v032_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_21d_3d_v033_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_63d_3d_v034_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_126d_3d_v035_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_norm_63d_3d_v036_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_jerk_21d_3d_v037_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_jerk_63d_3d_v038_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accelz_21_252_3d_v039_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accelz_63_504_3d_v040_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_smoothaccel_63_252_3d_v041_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rngaccel_63_252_3d_v042_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_ignition_curvature_3d_v043_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_252d_3d_v044_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_jerk_126d_3d_v045_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accelz_126_504_3d_v046_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_accel_norm_21d_3d_v047_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_curvature_gap_3d_v048_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_21d_3d_v049_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_63d_3d_v050_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_126d_3d_v051_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_norm_63d_3d_v052_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_jerk_21d_3d_v053_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_jerk_63d_3d_v054_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accelz_21_252_3d_v055_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_rngaccel_63_252_3d_v058_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_ignition_curvature_3d_v059_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_200d_accel_norm_21d_3d_v063_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_21d_3d_v065_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_63d_3d_v066_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_126d_3d_v067_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_norm_63d_3d_v068_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_jerk_21d_3d_v069_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_jerk_63d_3d_v070_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accelz_21_252_3d_v071_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accelz_63_504_3d_v072_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_smoothaccel_63_252_3d_v073_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_rngaccel_63_252_3d_v074_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_ignition_curvature_3d_v075_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_252d_3d_v076_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_jerk_126d_3d_v077_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accelz_126_504_3d_v078_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_accel_norm_21d_3d_v079_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_756d_curvature_gap_3d_v080_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accel_norm_63d_3d_v084_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_jerk_21d_3d_v085_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_jerk_63d_3d_v086_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accelz_21_252_3d_v087_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accelz_63_504_3d_v088_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_smoothaccel_63_252_3d_v089_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_ignition_curvature_3d_v091_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_jerk_126d_3d_v093_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accelz_126_504_3d_v094_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_756d_accel_norm_21d_3d_v095_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_21d_3d_v129_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_63d_3d_v130_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_126d_3d_v131_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_norm_63d_3d_v132_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_jerk_21d_3d_v133_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_jerk_63d_3d_v134_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accelz_21_252_3d_v135_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accelz_63_504_3d_v136_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_smoothaccel_63_252_3d_v137_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_rngaccel_63_252_3d_v138_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_ignition_curvature_3d_v139_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_252d_3d_v140_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_jerk_126d_3d_v141_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accelz_126_504_3d_v142_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_accel_norm_21d_3d_v143_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_upper_gap_200d_curvature_gap_3d_v144_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_21d_3d_v145_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_63d_3d_v146_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_126d_3d_v147_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_accel_norm_63d_3d_v148_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_jerk_21d_3d_v149_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_lower_gap_200d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
