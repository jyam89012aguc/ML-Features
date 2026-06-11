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


# 21d acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accel_21d_3d_v001_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accel_63d_3d_v002_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accel_126d_3d_v003_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accel_norm_63d_3d_v004_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_jerk_21d_3d_v005_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_jerk_63d_3d_v006_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accelz_21_252_3d_v007_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accelz_63_504_3d_v008_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_smoothaccel_63_252_3d_v009_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_rngaccel_63_252_3d_v010_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_ignition_curvature_3d_v011_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accel_252d_3d_v012_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_jerk_126d_3d_v013_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accelz_126_504_3d_v014_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_accel_norm_21d_3d_v015_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_curvature_gap_3d_v016_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_21d_3d_v017_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_63d_3d_v018_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_126d_3d_v019_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_norm_63d_3d_v020_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_jerk_21d_3d_v021_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_jerk_63d_3d_v022_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accelz_21_252_3d_v023_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accelz_63_504_3d_v024_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_smoothaccel_63_252_3d_v025_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_rngaccel_63_252_3d_v026_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_ignition_curvature_3d_v027_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_252d_3d_v028_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_jerk_126d_3d_v029_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accelz_126_504_3d_v030_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_norm_21d_3d_v031_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_curvature_gap_3d_v032_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_21d_3d_v033_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_63d_3d_v034_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_126d_3d_v035_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_norm_63d_3d_v036_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_jerk_21d_3d_v037_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_jerk_63d_3d_v038_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accelz_21_252_3d_v039_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accelz_63_504_3d_v040_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_smoothaccel_63_252_3d_v041_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_rngaccel_63_252_3d_v042_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_ignition_curvature_3d_v043_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_252d_3d_v044_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_jerk_126d_3d_v045_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accelz_126_504_3d_v046_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_norm_21d_3d_v047_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_curvature_gap_3d_v048_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accel_21d_3d_v049_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accel_63d_3d_v050_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accel_126d_3d_v051_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accel_norm_63d_3d_v052_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_jerk_21d_3d_v053_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_jerk_63d_3d_v054_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accelz_21_252_3d_v055_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accelz_63_504_3d_v056_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_smoothaccel_63_252_3d_v057_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_rngaccel_63_252_3d_v058_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_ignition_curvature_3d_v059_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accel_252d_3d_v060_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_jerk_126d_3d_v061_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accelz_126_504_3d_v062_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_accel_norm_21d_3d_v063_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_curvature_gap_3d_v064_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accel_21d_3d_v065_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accel_63d_3d_v066_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accel_126d_3d_v067_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accel_norm_63d_3d_v068_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_jerk_21d_3d_v069_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_jerk_63d_3d_v070_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accelz_21_252_3d_v071_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accelz_63_504_3d_v072_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_smoothaccel_63_252_3d_v073_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_rngaccel_63_252_3d_v074_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_ignition_curvature_3d_v075_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d jerk for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_jerk_126d_3d_v077_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_accel_norm_21d_3d_v079_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_curvature_gap_3d_v080_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_21d_3d_v097_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_63d_3d_v098_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_126d_3d_v099_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_norm_63d_3d_v100_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_jerk_21d_3d_v101_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_jerk_63d_3d_v102_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accelz_21_252_3d_v103_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accelz_63_504_3d_v104_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_smoothaccel_63_252_3d_v105_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_rngaccel_63_252_3d_v106_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_ignition_curvature_3d_v107_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d jerk for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_jerk_126d_3d_v109_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_norm_21d_3d_v111_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_curvature_gap_3d_v112_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_21d_3d_v113_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_63d_3d_v114_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_126d_3d_v115_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_norm_63d_3d_v116_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_jerk_21d_3d_v117_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_jerk_63d_3d_v118_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accelz_21_252_3d_v119_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accelz_63_504_3d_v120_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_smoothaccel_63_252_3d_v121_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_rngaccel_63_252_3d_v122_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_ignition_curvature_3d_v123_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d jerk for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_jerk_126d_3d_v125_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_norm_21d_3d_v127_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_curvature_gap_3d_v128_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_21d_3d_v129_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_63d_3d_v130_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_126d_3d_v131_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_norm_63d_3d_v132_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_jerk_21d_3d_v133_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_jerk_63d_3d_v134_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accelz_21_252_3d_v135_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accelz_63_504_3d_v136_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_smoothaccel_63_252_3d_v137_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_rngaccel_63_252_3d_v138_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_ignition_curvature_3d_v139_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_252d_3d_v140_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_jerk_126d_3d_v141_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accelz_126_504_3d_v142_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_norm_21d_3d_v143_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_curvature_gap_3d_v144_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_21d_3d_v145_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_63d_3d_v146_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_126d_3d_v147_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_norm_63d_3d_v148_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_jerk_21d_3d_v149_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_jerk_63d_3d_v150_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['opinc', 'revenue'], "func": fn} for fn in [bo_078_margin_acceleration_margin_acceleration_accel_21d_3d_v001_signal, bo_078_margin_acceleration_margin_acceleration_accel_63d_3d_v002_signal, bo_078_margin_acceleration_margin_acceleration_accel_126d_3d_v003_signal, bo_078_margin_acceleration_margin_acceleration_accel_norm_63d_3d_v004_signal, bo_078_margin_acceleration_margin_acceleration_jerk_21d_3d_v005_signal, bo_078_margin_acceleration_margin_acceleration_jerk_63d_3d_v006_signal, bo_078_margin_acceleration_margin_acceleration_accelz_21_252_3d_v007_signal, bo_078_margin_acceleration_margin_acceleration_accelz_63_504_3d_v008_signal, bo_078_margin_acceleration_margin_acceleration_smoothaccel_63_252_3d_v009_signal, bo_078_margin_acceleration_margin_acceleration_rngaccel_63_252_3d_v010_signal, bo_078_margin_acceleration_margin_acceleration_ignition_curvature_3d_v011_signal, bo_078_margin_acceleration_margin_acceleration_accel_252d_3d_v012_signal, bo_078_margin_acceleration_margin_acceleration_jerk_126d_3d_v013_signal, bo_078_margin_acceleration_margin_acceleration_accelz_126_504_3d_v014_signal, bo_078_margin_acceleration_margin_acceleration_accel_norm_21d_3d_v015_signal, bo_078_margin_acceleration_margin_acceleration_curvature_gap_3d_v016_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_21d_3d_v017_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_63d_3d_v018_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_126d_3d_v019_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_norm_63d_3d_v020_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_jerk_21d_3d_v021_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_jerk_63d_3d_v022_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accelz_21_252_3d_v023_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accelz_63_504_3d_v024_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_smoothaccel_63_252_3d_v025_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_rngaccel_63_252_3d_v026_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_ignition_curvature_3d_v027_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_252d_3d_v028_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_jerk_126d_3d_v029_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accelz_126_504_3d_v030_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_accel_norm_21d_3d_v031_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_curvature_gap_3d_v032_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_21d_3d_v033_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_63d_3d_v034_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_126d_3d_v035_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_norm_63d_3d_v036_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_jerk_21d_3d_v037_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_jerk_63d_3d_v038_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accelz_21_252_3d_v039_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accelz_63_504_3d_v040_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_smoothaccel_63_252_3d_v041_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_rngaccel_63_252_3d_v042_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_ignition_curvature_3d_v043_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_252d_3d_v044_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_jerk_126d_3d_v045_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accelz_126_504_3d_v046_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_accel_norm_21d_3d_v047_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_curvature_gap_3d_v048_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accel_21d_3d_v049_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accel_63d_3d_v050_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accel_126d_3d_v051_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accel_norm_63d_3d_v052_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_jerk_21d_3d_v053_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_jerk_63d_3d_v054_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accelz_21_252_3d_v055_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accelz_63_504_3d_v056_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_smoothaccel_63_252_3d_v057_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_rngaccel_63_252_3d_v058_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_ignition_curvature_3d_v059_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accel_252d_3d_v060_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_jerk_126d_3d_v061_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accelz_126_504_3d_v062_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_accel_norm_21d_3d_v063_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_curvature_gap_3d_v064_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accel_21d_3d_v065_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accel_63d_3d_v066_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accel_126d_3d_v067_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accel_norm_63d_3d_v068_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_jerk_21d_3d_v069_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_jerk_63d_3d_v070_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accelz_21_252_3d_v071_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accelz_63_504_3d_v072_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_smoothaccel_63_252_3d_v073_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_rngaccel_63_252_3d_v074_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_ignition_curvature_3d_v075_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_jerk_126d_3d_v077_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_accel_norm_21d_3d_v079_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_curvature_gap_3d_v080_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_21d_3d_v097_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_63d_3d_v098_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_126d_3d_v099_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_norm_63d_3d_v100_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_jerk_21d_3d_v101_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_jerk_63d_3d_v102_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accelz_21_252_3d_v103_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accelz_63_504_3d_v104_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_smoothaccel_63_252_3d_v105_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_rngaccel_63_252_3d_v106_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_ignition_curvature_3d_v107_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_jerk_126d_3d_v109_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_accel_norm_21d_3d_v111_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_curvature_gap_3d_v112_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_21d_3d_v113_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_63d_3d_v114_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_126d_3d_v115_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_norm_63d_3d_v116_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_jerk_21d_3d_v117_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_jerk_63d_3d_v118_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accelz_21_252_3d_v119_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accelz_63_504_3d_v120_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_smoothaccel_63_252_3d_v121_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_rngaccel_63_252_3d_v122_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_ignition_curvature_3d_v123_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_jerk_126d_3d_v125_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_accel_norm_21d_3d_v127_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_curvature_gap_3d_v128_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_21d_3d_v129_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_63d_3d_v130_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_126d_3d_v131_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_norm_63d_3d_v132_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_jerk_21d_3d_v133_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_jerk_63d_3d_v134_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accelz_21_252_3d_v135_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accelz_63_504_3d_v136_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_smoothaccel_63_252_3d_v137_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_rngaccel_63_252_3d_v138_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_ignition_curvature_3d_v139_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_252d_3d_v140_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_jerk_126d_3d_v141_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accelz_126_504_3d_v142_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_accel_norm_21d_3d_v143_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_curvature_gap_3d_v144_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_21d_3d_v145_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_63d_3d_v146_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_126d_3d_v147_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_accel_norm_63d_3d_v148_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_jerk_21d_3d_v149_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
