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


# 21d acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accel_21d_3d_v001_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accel_63d_3d_v002_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accel_126d_3d_v003_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accel_norm_63d_3d_v004_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_jerk_21d_3d_v005_signal(insider_buyer_count):
    base = insider_buyer_count
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_jerk_63d_3d_v006_signal(insider_buyer_count):
    base = insider_buyer_count
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accelz_21_252_3d_v007_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accelz_63_504_3d_v008_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_smoothaccel_63_252_3d_v009_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_rngaccel_63_252_3d_v010_signal(insider_buyer_count):
    base = insider_buyer_count
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_ignition_curvature_3d_v011_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accel_252d_3d_v012_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_jerk_126d_3d_v013_signal(insider_buyer_count):
    base = insider_buyer_count
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accelz_126_504_3d_v014_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_accel_norm_21d_3d_v015_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for insider_buy_clustering
def bo_090_insider_buy_clustering_insider_buy_clustering_curvature_gap_3d_v016_signal(insider_buyer_count):
    base = insider_buyer_count
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_21d_3d_v017_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_63d_3d_v018_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_126d_3d_v019_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_norm_63d_3d_v020_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_jerk_21d_3d_v021_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_jerk_63d_3d_v022_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accelz_21_252_3d_v023_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accelz_63_504_3d_v024_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_smoothaccel_63_252_3d_v025_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_rngaccel_63_252_3d_v026_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_ignition_curvature_3d_v027_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_252d_3d_v028_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_jerk_126d_3d_v029_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accelz_126_504_3d_v030_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_norm_21d_3d_v031_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for insider_buy_clustering_mean_14d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_curvature_gap_3d_v032_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 14)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_21d_3d_v033_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_63d_3d_v034_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_126d_3d_v035_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_norm_63d_3d_v036_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_jerk_21d_3d_v037_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_jerk_63d_3d_v038_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accelz_21_252_3d_v039_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accelz_63_504_3d_v040_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_smoothaccel_63_252_3d_v041_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_rngaccel_63_252_3d_v042_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_ignition_curvature_3d_v043_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_252d_3d_v044_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_jerk_126d_3d_v045_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accelz_126_504_3d_v046_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_norm_21d_3d_v047_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for insider_buy_clustering_mean_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_curvature_gap_3d_v048_signal(insider_buyer_count):
    base = _mean(insider_buyer_count, 84)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_21d_3d_v049_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_63d_3d_v050_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_126d_3d_v051_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_norm_63d_3d_v052_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_jerk_21d_3d_v053_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_jerk_63d_3d_v054_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# range-normalized acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_rngaccel_63_252_3d_v058_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# 252d acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_252d_3d_v060_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    result = _accel(base, 252)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_z_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_norm_21d_3d_v063_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 84)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_21d_3d_v065_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_63d_3d_v066_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_126d_3d_v067_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_norm_63d_3d_v068_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_jerk_21d_3d_v069_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_jerk_63d_3d_v070_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accelz_21_252_3d_v071_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accelz_63_504_3d_v072_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_smoothaccel_63_252_3d_v073_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_rngaccel_63_252_3d_v074_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_ignition_curvature_3d_v075_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_252d_3d_v076_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_jerk_126d_3d_v077_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accelz_126_504_3d_v078_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_norm_21d_3d_v079_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for insider_buy_clustering_z_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_curvature_gap_3d_v080_signal(insider_buyer_count):
    base = _z(insider_buyer_count, 252)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_21d_3d_v081_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_63d_3d_v082_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_126d_3d_v083_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_norm_63d_3d_v084_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_jerk_21d_3d_v085_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_jerk_63d_3d_v086_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# smoothed 63d acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_smoothaccel_63_252_3d_v089_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_ignition_curvature_3d_v091_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_252d_3d_v092_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_jerk_126d_3d_v093_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_distmax_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_norm_21d_3d_v095_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_distmin_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_accel_norm_63d_3d_v100_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_distmin_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_jerk_21d_3d_v101_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_distmin_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_jerk_63d_3d_v102_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering_distmin_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_ignition_curvature_3d_v107_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering_distmin_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_jerk_126d_3d_v109_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_distmin_252d
def bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_accel_norm_21d_3d_v111_signal(insider_buyer_count):
    base = _safe_div((insider_buyer_count) - (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min(), (insider_buyer_count).rolling(252, min_periods=max(2, 252//2)).min().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_21d_3d_v129_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_63d_3d_v130_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_126d_3d_v131_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_norm_63d_3d_v132_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_jerk_21d_3d_v133_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_jerk_63d_3d_v134_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accelz_21_252_3d_v135_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accelz_63_504_3d_v136_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_smoothaccel_63_252_3d_v137_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_rngaccel_63_252_3d_v138_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_ignition_curvature_3d_v139_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_252d_3d_v140_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_jerk_126d_3d_v141_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accelz_126_504_3d_v142_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_norm_21d_3d_v143_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for insider_buy_clustering_upper_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_curvature_gap_3d_v144_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for insider_buy_clustering_lower_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_21d_3d_v145_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for insider_buy_clustering_lower_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_63d_3d_v146_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for insider_buy_clustering_lower_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_126d_3d_v147_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for insider_buy_clustering_lower_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_norm_63d_3d_v148_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for insider_buy_clustering_lower_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_jerk_21d_3d_v149_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for insider_buy_clustering_lower_gap_84d
def bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_jerk_63d_3d_v150_signal(insider_buyer_count):
    base = (insider_buyer_count) - (insider_buyer_count).rolling(84, min_periods=max(2, 84//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['insider_buyer_count'], "func": fn} for fn in [bo_090_insider_buy_clustering_insider_buy_clustering_accel_21d_3d_v001_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accel_63d_3d_v002_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accel_126d_3d_v003_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accel_norm_63d_3d_v004_signal, bo_090_insider_buy_clustering_insider_buy_clustering_jerk_21d_3d_v005_signal, bo_090_insider_buy_clustering_insider_buy_clustering_jerk_63d_3d_v006_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accelz_21_252_3d_v007_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accelz_63_504_3d_v008_signal, bo_090_insider_buy_clustering_insider_buy_clustering_smoothaccel_63_252_3d_v009_signal, bo_090_insider_buy_clustering_insider_buy_clustering_rngaccel_63_252_3d_v010_signal, bo_090_insider_buy_clustering_insider_buy_clustering_ignition_curvature_3d_v011_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accel_252d_3d_v012_signal, bo_090_insider_buy_clustering_insider_buy_clustering_jerk_126d_3d_v013_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accelz_126_504_3d_v014_signal, bo_090_insider_buy_clustering_insider_buy_clustering_accel_norm_21d_3d_v015_signal, bo_090_insider_buy_clustering_insider_buy_clustering_curvature_gap_3d_v016_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_21d_3d_v017_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_63d_3d_v018_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_126d_3d_v019_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_norm_63d_3d_v020_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_jerk_21d_3d_v021_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_jerk_63d_3d_v022_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accelz_21_252_3d_v023_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accelz_63_504_3d_v024_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_smoothaccel_63_252_3d_v025_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_rngaccel_63_252_3d_v026_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_ignition_curvature_3d_v027_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_252d_3d_v028_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_jerk_126d_3d_v029_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accelz_126_504_3d_v030_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_accel_norm_21d_3d_v031_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_14d_curvature_gap_3d_v032_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_21d_3d_v033_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_63d_3d_v034_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_126d_3d_v035_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_norm_63d_3d_v036_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_jerk_21d_3d_v037_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_jerk_63d_3d_v038_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accelz_21_252_3d_v039_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accelz_63_504_3d_v040_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_smoothaccel_63_252_3d_v041_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_rngaccel_63_252_3d_v042_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_ignition_curvature_3d_v043_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_252d_3d_v044_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_jerk_126d_3d_v045_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accelz_126_504_3d_v046_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_accel_norm_21d_3d_v047_signal, bo_090_insider_buy_clustering_insider_buy_clustering_mean_84d_curvature_gap_3d_v048_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_21d_3d_v049_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_63d_3d_v050_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_126d_3d_v051_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_norm_63d_3d_v052_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_jerk_21d_3d_v053_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_jerk_63d_3d_v054_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_rngaccel_63_252_3d_v058_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_252d_3d_v060_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_84d_accel_norm_21d_3d_v063_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_21d_3d_v065_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_63d_3d_v066_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_126d_3d_v067_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_norm_63d_3d_v068_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_jerk_21d_3d_v069_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_jerk_63d_3d_v070_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accelz_21_252_3d_v071_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accelz_63_504_3d_v072_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_smoothaccel_63_252_3d_v073_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_rngaccel_63_252_3d_v074_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_ignition_curvature_3d_v075_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_252d_3d_v076_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_jerk_126d_3d_v077_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accelz_126_504_3d_v078_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_accel_norm_21d_3d_v079_signal, bo_090_insider_buy_clustering_insider_buy_clustering_z_252d_curvature_gap_3d_v080_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_21d_3d_v081_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_63d_3d_v082_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_126d_3d_v083_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_norm_63d_3d_v084_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_jerk_21d_3d_v085_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_jerk_63d_3d_v086_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_smoothaccel_63_252_3d_v089_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_ignition_curvature_3d_v091_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_252d_3d_v092_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_jerk_126d_3d_v093_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmax_252d_accel_norm_21d_3d_v095_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_accel_norm_63d_3d_v100_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_jerk_21d_3d_v101_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_jerk_63d_3d_v102_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_ignition_curvature_3d_v107_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_jerk_126d_3d_v109_signal, bo_090_insider_buy_clustering_insider_buy_clustering_distmin_252d_accel_norm_21d_3d_v111_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_21d_3d_v129_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_63d_3d_v130_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_126d_3d_v131_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_norm_63d_3d_v132_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_jerk_21d_3d_v133_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_jerk_63d_3d_v134_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accelz_21_252_3d_v135_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accelz_63_504_3d_v136_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_smoothaccel_63_252_3d_v137_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_rngaccel_63_252_3d_v138_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_ignition_curvature_3d_v139_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_252d_3d_v140_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_jerk_126d_3d_v141_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accelz_126_504_3d_v142_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_accel_norm_21d_3d_v143_signal, bo_090_insider_buy_clustering_insider_buy_clustering_upper_gap_84d_curvature_gap_3d_v144_signal, bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_21d_3d_v145_signal, bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_63d_3d_v146_signal, bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_126d_3d_v147_signal, bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_accel_norm_63d_3d_v148_signal, bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_jerk_21d_3d_v149_signal, bo_090_insider_buy_clustering_insider_buy_clustering_lower_gap_84d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
