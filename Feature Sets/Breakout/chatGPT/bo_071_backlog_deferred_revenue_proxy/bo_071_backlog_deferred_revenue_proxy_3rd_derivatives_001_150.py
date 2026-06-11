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


# 21d acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_21d_3d_v001_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_63d_3d_v002_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_126d_3d_v003_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_norm_63d_3d_v004_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_jerk_21d_3d_v005_signal(deferredrev):
    base = _growth(deferredrev, 252)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_jerk_63d_3d_v006_signal(deferredrev):
    base = _growth(deferredrev, 252)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accelz_21_252_3d_v007_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accelz_63_504_3d_v008_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_smoothaccel_63_252_3d_v009_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_rngaccel_63_252_3d_v010_signal(deferredrev):
    base = _growth(deferredrev, 252)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_ignition_curvature_3d_v011_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_252d_3d_v012_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_jerk_126d_3d_v013_signal(deferredrev):
    base = _growth(deferredrev, 252)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accelz_126_504_3d_v014_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_norm_21d_3d_v015_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_curvature_gap_3d_v016_signal(deferredrev):
    base = _growth(deferredrev, 252)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_21d_3d_v017_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_63d_3d_v018_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_126d_3d_v019_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_norm_63d_3d_v020_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_jerk_21d_3d_v021_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_jerk_63d_3d_v022_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accelz_21_252_3d_v023_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accelz_63_504_3d_v024_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_smoothaccel_63_252_3d_v025_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_rngaccel_63_252_3d_v026_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_ignition_curvature_3d_v027_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_252d_3d_v028_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_jerk_126d_3d_v029_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accelz_126_504_3d_v030_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_norm_21d_3d_v031_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_mean_21d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_curvature_gap_3d_v032_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 21)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_21d_3d_v033_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_63d_3d_v034_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_126d_3d_v035_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_norm_63d_3d_v036_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_jerk_21d_3d_v037_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_jerk_63d_3d_v038_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accelz_21_252_3d_v039_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accelz_63_504_3d_v040_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_smoothaccel_63_252_3d_v041_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_rngaccel_63_252_3d_v042_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_ignition_curvature_3d_v043_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_252d_3d_v044_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_jerk_126d_3d_v045_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accelz_126_504_3d_v046_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_norm_21d_3d_v047_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_mean_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_curvature_gap_3d_v048_signal(deferredrev):
    base = _mean(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_21d_3d_v049_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_63d_3d_v050_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_126d_3d_v051_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_norm_63d_3d_v052_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_jerk_21d_3d_v053_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_jerk_63d_3d_v054_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accelz_21_252_3d_v055_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accelz_63_504_3d_v056_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_smoothaccel_63_252_3d_v057_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_rngaccel_63_252_3d_v058_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_ignition_curvature_3d_v059_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_252d_3d_v060_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_jerk_126d_3d_v061_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accelz_126_504_3d_v062_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_norm_21d_3d_v063_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_z_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_curvature_gap_3d_v064_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 100)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_21d_3d_v065_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_63d_3d_v066_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_126d_3d_v067_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_norm_63d_3d_v068_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_jerk_21d_3d_v069_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_jerk_63d_3d_v070_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accelz_21_252_3d_v071_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accelz_63_504_3d_v072_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_smoothaccel_63_252_3d_v073_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_rngaccel_63_252_3d_v074_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_ignition_curvature_3d_v075_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_252d_3d_v076_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_jerk_126d_3d_v077_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accelz_126_504_3d_v078_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_norm_21d_3d_v079_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_z_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_curvature_gap_3d_v080_signal(deferredrev):
    base = _z(_growth(deferredrev, 252), 315)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_21d_3d_v081_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_63d_3d_v082_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_126d_3d_v083_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_norm_63d_3d_v084_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_jerk_21d_3d_v085_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_jerk_63d_3d_v086_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accelz_21_252_3d_v087_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accelz_63_504_3d_v088_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_smoothaccel_63_252_3d_v089_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_rngaccel_63_252_3d_v090_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_ignition_curvature_3d_v091_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_252d_3d_v092_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_jerk_126d_3d_v093_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accelz_126_504_3d_v094_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_norm_21d_3d_v095_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_distmax_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_curvature_gap_3d_v096_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).max().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_21d_3d_v097_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_63d_3d_v098_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_126d_3d_v099_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_norm_63d_3d_v100_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_jerk_21d_3d_v101_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_jerk_63d_3d_v102_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accelz_21_252_3d_v103_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accelz_63_504_3d_v104_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_smoothaccel_63_252_3d_v105_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_rngaccel_63_252_3d_v106_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_ignition_curvature_3d_v107_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_252d_3d_v108_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_jerk_126d_3d_v109_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accelz_126_504_3d_v110_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_norm_21d_3d_v111_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_distmin_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_curvature_gap_3d_v112_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).min().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_21d_3d_v113_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_63d_3d_v114_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_126d_3d_v115_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_norm_63d_3d_v116_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_jerk_21d_3d_v117_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_jerk_63d_3d_v118_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accelz_21_252_3d_v119_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accelz_63_504_3d_v120_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_smoothaccel_63_252_3d_v121_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_rngaccel_63_252_3d_v122_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_ignition_curvature_3d_v123_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_252d_3d_v124_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_jerk_126d_3d_v125_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accelz_126_504_3d_v126_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_norm_21d_3d_v127_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_distmed_315d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_curvature_gap_3d_v128_signal(deferredrev):
    base = _safe_div((_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median(), (_growth(deferredrev, 252)).rolling(315, min_periods=max(2, 315//2)).median().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_21d_3d_v129_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_63d_3d_v130_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_126d_3d_v131_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_norm_63d_3d_v132_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_jerk_21d_3d_v133_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_jerk_63d_3d_v134_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accelz_21_252_3d_v135_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accelz_63_504_3d_v136_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_smoothaccel_63_252_3d_v137_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_rngaccel_63_252_3d_v138_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_ignition_curvature_3d_v139_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_252d_3d_v140_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_jerk_126d_3d_v141_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accelz_126_504_3d_v142_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_norm_21d_3d_v143_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for deferred_revenue_proxy_upper_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_curvature_gap_3d_v144_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for deferred_revenue_proxy_lower_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_21d_3d_v145_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for deferred_revenue_proxy_lower_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_63d_3d_v146_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for deferred_revenue_proxy_lower_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_126d_3d_v147_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for deferred_revenue_proxy_lower_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_norm_63d_3d_v148_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for deferred_revenue_proxy_lower_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_jerk_21d_3d_v149_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for deferred_revenue_proxy_lower_gap_100d
def bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_jerk_63d_3d_v150_signal(deferredrev):
    base = (_growth(deferredrev, 252)) - (_growth(deferredrev, 252)).rolling(100, min_periods=max(2, 100//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['deferredrev'], "func": fn} for fn in [bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_21d_3d_v001_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_63d_3d_v002_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_126d_3d_v003_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_norm_63d_3d_v004_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_jerk_21d_3d_v005_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_jerk_63d_3d_v006_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accelz_21_252_3d_v007_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accelz_63_504_3d_v008_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_smoothaccel_63_252_3d_v009_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_rngaccel_63_252_3d_v010_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_ignition_curvature_3d_v011_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_252d_3d_v012_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_jerk_126d_3d_v013_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accelz_126_504_3d_v014_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_accel_norm_21d_3d_v015_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_curvature_gap_3d_v016_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_21d_3d_v017_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_63d_3d_v018_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_126d_3d_v019_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_norm_63d_3d_v020_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_jerk_21d_3d_v021_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_jerk_63d_3d_v022_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accelz_21_252_3d_v023_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accelz_63_504_3d_v024_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_smoothaccel_63_252_3d_v025_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_rngaccel_63_252_3d_v026_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_ignition_curvature_3d_v027_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_252d_3d_v028_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_jerk_126d_3d_v029_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accelz_126_504_3d_v030_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_accel_norm_21d_3d_v031_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_21d_curvature_gap_3d_v032_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_21d_3d_v033_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_63d_3d_v034_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_126d_3d_v035_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_norm_63d_3d_v036_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_jerk_21d_3d_v037_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_jerk_63d_3d_v038_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accelz_21_252_3d_v039_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accelz_63_504_3d_v040_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_smoothaccel_63_252_3d_v041_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_rngaccel_63_252_3d_v042_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_ignition_curvature_3d_v043_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_252d_3d_v044_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_jerk_126d_3d_v045_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accelz_126_504_3d_v046_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_accel_norm_21d_3d_v047_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_mean_100d_curvature_gap_3d_v048_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_21d_3d_v049_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_63d_3d_v050_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_126d_3d_v051_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_norm_63d_3d_v052_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_jerk_21d_3d_v053_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_jerk_63d_3d_v054_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accelz_21_252_3d_v055_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accelz_63_504_3d_v056_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_smoothaccel_63_252_3d_v057_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_rngaccel_63_252_3d_v058_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_ignition_curvature_3d_v059_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_252d_3d_v060_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_jerk_126d_3d_v061_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accelz_126_504_3d_v062_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_accel_norm_21d_3d_v063_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_100d_curvature_gap_3d_v064_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_21d_3d_v065_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_63d_3d_v066_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_126d_3d_v067_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_norm_63d_3d_v068_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_jerk_21d_3d_v069_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_jerk_63d_3d_v070_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accelz_21_252_3d_v071_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accelz_63_504_3d_v072_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_smoothaccel_63_252_3d_v073_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_rngaccel_63_252_3d_v074_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_ignition_curvature_3d_v075_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_252d_3d_v076_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_jerk_126d_3d_v077_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accelz_126_504_3d_v078_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_accel_norm_21d_3d_v079_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_z_315d_curvature_gap_3d_v080_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_21d_3d_v081_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_63d_3d_v082_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_126d_3d_v083_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_norm_63d_3d_v084_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_jerk_21d_3d_v085_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_jerk_63d_3d_v086_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accelz_21_252_3d_v087_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accelz_63_504_3d_v088_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_smoothaccel_63_252_3d_v089_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_rngaccel_63_252_3d_v090_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_ignition_curvature_3d_v091_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_252d_3d_v092_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_jerk_126d_3d_v093_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accelz_126_504_3d_v094_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_accel_norm_21d_3d_v095_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmax_315d_curvature_gap_3d_v096_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_21d_3d_v097_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_63d_3d_v098_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_126d_3d_v099_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_norm_63d_3d_v100_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_jerk_21d_3d_v101_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_jerk_63d_3d_v102_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accelz_21_252_3d_v103_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accelz_63_504_3d_v104_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_smoothaccel_63_252_3d_v105_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_rngaccel_63_252_3d_v106_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_ignition_curvature_3d_v107_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_252d_3d_v108_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_jerk_126d_3d_v109_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accelz_126_504_3d_v110_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_accel_norm_21d_3d_v111_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmin_315d_curvature_gap_3d_v112_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_21d_3d_v113_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_63d_3d_v114_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_126d_3d_v115_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_norm_63d_3d_v116_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_jerk_21d_3d_v117_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_jerk_63d_3d_v118_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accelz_21_252_3d_v119_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accelz_63_504_3d_v120_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_smoothaccel_63_252_3d_v121_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_rngaccel_63_252_3d_v122_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_ignition_curvature_3d_v123_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_252d_3d_v124_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_jerk_126d_3d_v125_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accelz_126_504_3d_v126_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_accel_norm_21d_3d_v127_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_distmed_315d_curvature_gap_3d_v128_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_21d_3d_v129_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_63d_3d_v130_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_126d_3d_v131_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_norm_63d_3d_v132_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_jerk_21d_3d_v133_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_jerk_63d_3d_v134_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accelz_21_252_3d_v135_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accelz_63_504_3d_v136_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_smoothaccel_63_252_3d_v137_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_rngaccel_63_252_3d_v138_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_ignition_curvature_3d_v139_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_252d_3d_v140_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_jerk_126d_3d_v141_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accelz_126_504_3d_v142_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_accel_norm_21d_3d_v143_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_upper_gap_100d_curvature_gap_3d_v144_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_21d_3d_v145_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_63d_3d_v146_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_126d_3d_v147_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_accel_norm_63d_3d_v148_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_jerk_21d_3d_v149_signal, bo_071_backlog_deferred_revenue_proxy_deferred_revenue_proxy_lower_gap_100d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
