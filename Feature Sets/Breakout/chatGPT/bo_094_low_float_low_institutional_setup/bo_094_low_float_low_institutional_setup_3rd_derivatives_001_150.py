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


# 21d acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_21d_3d_v001_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_63d_3d_v002_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_126d_3d_v003_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_norm_63d_3d_v004_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_jerk_21d_3d_v005_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_jerk_63d_3d_v006_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accelz_21_252_3d_v007_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accelz_63_504_3d_v008_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_smoothaccel_63_252_3d_v009_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_rngaccel_63_252_3d_v010_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_ignition_curvature_3d_v011_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_252d_3d_v012_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_jerk_126d_3d_v013_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accelz_126_504_3d_v014_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_norm_21d_3d_v015_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_curvature_gap_3d_v016_signal(inst_shares, sharesbas):
    base = 1.0 - _safe_div(inst_shares, sharesbas.abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_21d_3d_v017_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_63d_3d_v018_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_126d_3d_v019_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_norm_63d_3d_v020_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_jerk_21d_3d_v021_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_jerk_63d_3d_v022_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accelz_21_252_3d_v023_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accelz_63_504_3d_v024_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_smoothaccel_63_252_3d_v025_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_rngaccel_63_252_3d_v026_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_ignition_curvature_3d_v027_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_252d_3d_v028_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_jerk_126d_3d_v029_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accelz_126_504_3d_v030_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_norm_21d_3d_v031_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_mean_63d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_curvature_gap_3d_v032_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 63)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_21d_3d_v033_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_63d_3d_v034_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_126d_3d_v035_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_norm_63d_3d_v036_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_jerk_21d_3d_v037_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_jerk_63d_3d_v038_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accelz_21_252_3d_v039_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accelz_63_504_3d_v040_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_smoothaccel_63_252_3d_v041_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_rngaccel_63_252_3d_v042_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_ignition_curvature_3d_v043_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_252d_3d_v044_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_jerk_126d_3d_v045_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accelz_126_504_3d_v046_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_norm_21d_3d_v047_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_mean_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_curvature_gap_3d_v048_signal(inst_shares, sharesbas):
    base = _mean(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_21d_3d_v049_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_63d_3d_v050_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_126d_3d_v051_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_norm_63d_3d_v052_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_jerk_21d_3d_v053_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_jerk_63d_3d_v054_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accelz_21_252_3d_v055_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accelz_63_504_3d_v056_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_smoothaccel_63_252_3d_v057_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_rngaccel_63_252_3d_v058_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_ignition_curvature_3d_v059_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_252d_3d_v060_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_jerk_126d_3d_v061_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accelz_126_504_3d_v062_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_norm_21d_3d_v063_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_z_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_curvature_gap_3d_v064_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 200)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_21d_3d_v065_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_63d_3d_v066_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_126d_3d_v067_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_norm_63d_3d_v068_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_jerk_21d_3d_v069_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_jerk_63d_3d_v070_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accelz_21_252_3d_v071_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accelz_63_504_3d_v072_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_smoothaccel_63_252_3d_v073_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_rngaccel_63_252_3d_v074_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_ignition_curvature_3d_v075_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_252d_3d_v076_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_jerk_126d_3d_v077_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accelz_126_504_3d_v078_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_norm_21d_3d_v079_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_z_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_curvature_gap_3d_v080_signal(inst_shares, sharesbas):
    base = _z(1.0 - _safe_div(inst_shares, sharesbas.abs()), 756)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_21d_3d_v081_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_63d_3d_v082_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_126d_3d_v083_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_norm_63d_3d_v084_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_jerk_21d_3d_v085_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_jerk_63d_3d_v086_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accelz_21_252_3d_v087_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accelz_63_504_3d_v088_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_smoothaccel_63_252_3d_v089_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_rngaccel_63_252_3d_v090_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_ignition_curvature_3d_v091_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_252d_3d_v092_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_jerk_126d_3d_v093_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accelz_126_504_3d_v094_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_norm_21d_3d_v095_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_distmax_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_curvature_gap_3d_v096_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_21d_3d_v097_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_63d_3d_v098_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_126d_3d_v099_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_norm_63d_3d_v100_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_jerk_21d_3d_v101_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_jerk_63d_3d_v102_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accelz_21_252_3d_v103_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accelz_63_504_3d_v104_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_smoothaccel_63_252_3d_v105_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_rngaccel_63_252_3d_v106_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_ignition_curvature_3d_v107_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_252d_3d_v108_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_jerk_126d_3d_v109_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accelz_126_504_3d_v110_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_norm_21d_3d_v111_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_distmin_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_curvature_gap_3d_v112_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_21d_3d_v113_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_63d_3d_v114_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_126d_3d_v115_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_norm_63d_3d_v116_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_jerk_21d_3d_v117_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_jerk_63d_3d_v118_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accelz_21_252_3d_v119_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accelz_63_504_3d_v120_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_smoothaccel_63_252_3d_v121_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_rngaccel_63_252_3d_v122_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_ignition_curvature_3d_v123_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_252d_3d_v124_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_jerk_126d_3d_v125_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accelz_126_504_3d_v126_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_norm_21d_3d_v127_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_distmed_756d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_curvature_gap_3d_v128_signal(inst_shares, sharesbas):
    base = _safe_div((1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median(), (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_21d_3d_v129_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_63d_3d_v130_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_126d_3d_v131_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_norm_63d_3d_v132_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_jerk_21d_3d_v133_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_jerk_63d_3d_v134_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accelz_21_252_3d_v135_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accelz_63_504_3d_v136_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_smoothaccel_63_252_3d_v137_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_rngaccel_63_252_3d_v138_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_ignition_curvature_3d_v139_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_252d_3d_v140_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_jerk_126d_3d_v141_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accelz_126_504_3d_v142_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_norm_21d_3d_v143_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for low_float_low_inst_setup_upper_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_curvature_gap_3d_v144_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for low_float_low_inst_setup_lower_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_21d_3d_v145_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for low_float_low_inst_setup_lower_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_63d_3d_v146_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for low_float_low_inst_setup_lower_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_126d_3d_v147_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for low_float_low_inst_setup_lower_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_norm_63d_3d_v148_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for low_float_low_inst_setup_lower_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_jerk_21d_3d_v149_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for low_float_low_inst_setup_lower_gap_200d
def bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_jerk_63d_3d_v150_signal(inst_shares, sharesbas):
    base = (1.0 - _safe_div(inst_shares, sharesbas.abs())) - (1.0 - _safe_div(inst_shares, sharesbas.abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['inst_shares', 'sharesbas'], "func": fn} for fn in [bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_21d_3d_v001_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_63d_3d_v002_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_126d_3d_v003_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_norm_63d_3d_v004_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_jerk_21d_3d_v005_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_jerk_63d_3d_v006_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accelz_21_252_3d_v007_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accelz_63_504_3d_v008_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_smoothaccel_63_252_3d_v009_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_rngaccel_63_252_3d_v010_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_ignition_curvature_3d_v011_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_252d_3d_v012_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_jerk_126d_3d_v013_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accelz_126_504_3d_v014_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_accel_norm_21d_3d_v015_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_curvature_gap_3d_v016_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_21d_3d_v017_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_63d_3d_v018_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_126d_3d_v019_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_norm_63d_3d_v020_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_jerk_21d_3d_v021_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_jerk_63d_3d_v022_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accelz_21_252_3d_v023_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accelz_63_504_3d_v024_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_smoothaccel_63_252_3d_v025_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_rngaccel_63_252_3d_v026_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_ignition_curvature_3d_v027_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_252d_3d_v028_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_jerk_126d_3d_v029_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accelz_126_504_3d_v030_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_accel_norm_21d_3d_v031_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_63d_curvature_gap_3d_v032_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_21d_3d_v033_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_63d_3d_v034_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_126d_3d_v035_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_norm_63d_3d_v036_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_jerk_21d_3d_v037_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_jerk_63d_3d_v038_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accelz_21_252_3d_v039_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accelz_63_504_3d_v040_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_smoothaccel_63_252_3d_v041_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_rngaccel_63_252_3d_v042_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_ignition_curvature_3d_v043_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_252d_3d_v044_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_jerk_126d_3d_v045_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accelz_126_504_3d_v046_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_accel_norm_21d_3d_v047_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_mean_200d_curvature_gap_3d_v048_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_21d_3d_v049_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_63d_3d_v050_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_126d_3d_v051_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_norm_63d_3d_v052_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_jerk_21d_3d_v053_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_jerk_63d_3d_v054_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accelz_21_252_3d_v055_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accelz_63_504_3d_v056_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_smoothaccel_63_252_3d_v057_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_rngaccel_63_252_3d_v058_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_ignition_curvature_3d_v059_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_252d_3d_v060_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_jerk_126d_3d_v061_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accelz_126_504_3d_v062_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_accel_norm_21d_3d_v063_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_200d_curvature_gap_3d_v064_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_21d_3d_v065_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_63d_3d_v066_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_126d_3d_v067_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_norm_63d_3d_v068_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_jerk_21d_3d_v069_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_jerk_63d_3d_v070_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accelz_21_252_3d_v071_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accelz_63_504_3d_v072_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_smoothaccel_63_252_3d_v073_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_rngaccel_63_252_3d_v074_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_ignition_curvature_3d_v075_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_252d_3d_v076_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_jerk_126d_3d_v077_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accelz_126_504_3d_v078_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_accel_norm_21d_3d_v079_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_z_756d_curvature_gap_3d_v080_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_21d_3d_v081_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_63d_3d_v082_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_126d_3d_v083_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_norm_63d_3d_v084_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_jerk_21d_3d_v085_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_jerk_63d_3d_v086_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accelz_21_252_3d_v087_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accelz_63_504_3d_v088_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_smoothaccel_63_252_3d_v089_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_rngaccel_63_252_3d_v090_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_ignition_curvature_3d_v091_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_252d_3d_v092_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_jerk_126d_3d_v093_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accelz_126_504_3d_v094_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_accel_norm_21d_3d_v095_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmax_756d_curvature_gap_3d_v096_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_21d_3d_v097_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_63d_3d_v098_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_126d_3d_v099_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_norm_63d_3d_v100_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_jerk_21d_3d_v101_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_jerk_63d_3d_v102_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accelz_21_252_3d_v103_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accelz_63_504_3d_v104_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_smoothaccel_63_252_3d_v105_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_rngaccel_63_252_3d_v106_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_ignition_curvature_3d_v107_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_252d_3d_v108_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_jerk_126d_3d_v109_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accelz_126_504_3d_v110_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_accel_norm_21d_3d_v111_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmin_756d_curvature_gap_3d_v112_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_21d_3d_v113_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_63d_3d_v114_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_126d_3d_v115_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_norm_63d_3d_v116_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_jerk_21d_3d_v117_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_jerk_63d_3d_v118_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accelz_21_252_3d_v119_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accelz_63_504_3d_v120_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_smoothaccel_63_252_3d_v121_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_rngaccel_63_252_3d_v122_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_ignition_curvature_3d_v123_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_252d_3d_v124_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_jerk_126d_3d_v125_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accelz_126_504_3d_v126_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_accel_norm_21d_3d_v127_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_distmed_756d_curvature_gap_3d_v128_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_21d_3d_v129_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_63d_3d_v130_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_126d_3d_v131_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_norm_63d_3d_v132_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_jerk_21d_3d_v133_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_jerk_63d_3d_v134_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accelz_21_252_3d_v135_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accelz_63_504_3d_v136_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_smoothaccel_63_252_3d_v137_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_rngaccel_63_252_3d_v138_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_ignition_curvature_3d_v139_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_252d_3d_v140_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_jerk_126d_3d_v141_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accelz_126_504_3d_v142_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_accel_norm_21d_3d_v143_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_upper_gap_200d_curvature_gap_3d_v144_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_21d_3d_v145_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_63d_3d_v146_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_126d_3d_v147_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_accel_norm_63d_3d_v148_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_jerk_21d_3d_v149_signal, bo_094_low_float_low_institutional_setup_low_float_low_inst_setup_lower_gap_200d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
