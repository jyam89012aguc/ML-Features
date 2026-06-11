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


# 21d acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_21d_3d_v001_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_63d_3d_v002_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_126d_3d_v003_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_norm_63d_3d_v004_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_jerk_21d_3d_v005_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_jerk_63d_3d_v006_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accelz_21_252_3d_v007_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accelz_63_504_3d_v008_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_smoothaccel_63_252_3d_v009_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_ignition_curvature_3d_v011_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_252d_3d_v012_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_jerk_126d_3d_v013_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accelz_126_504_3d_v014_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_norm_21d_3d_v015_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for keltner_bollinger_squeeze
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_curvature_gap_3d_v016_signal(high, low, closeadj):
    base = (_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_21d_3d_v017_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_63d_3d_v018_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_126d_3d_v019_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_norm_63d_3d_v020_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_jerk_21d_3d_v021_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_jerk_63d_3d_v022_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accelz_21_252_3d_v023_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accelz_63_504_3d_v024_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_smoothaccel_63_252_3d_v025_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_rngaccel_63_252_3d_v026_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_ignition_curvature_3d_v027_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_252d_3d_v028_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_jerk_126d_3d_v029_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accelz_126_504_3d_v030_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_norm_21d_3d_v031_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for keltner_bollinger_squeeze_mean_55d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_curvature_gap_3d_v032_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 55)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_21d_3d_v033_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_63d_3d_v034_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_126d_3d_v035_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_norm_63d_3d_v036_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_jerk_21d_3d_v037_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_jerk_63d_3d_v038_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accelz_21_252_3d_v039_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accelz_63_504_3d_v040_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_smoothaccel_63_252_3d_v041_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_rngaccel_63_252_3d_v042_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_ignition_curvature_3d_v043_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_252d_3d_v044_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_jerk_126d_3d_v045_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accelz_126_504_3d_v046_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_norm_21d_3d_v047_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for keltner_bollinger_squeeze_mean_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_curvature_gap_3d_v048_signal(high, low, closeadj):
    base = _mean((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_21d_3d_v049_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_63d_3d_v050_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_126d_3d_v051_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_norm_63d_3d_v052_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_jerk_21d_3d_v053_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_jerk_63d_3d_v054_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accelz_21_252_3d_v055_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accelz_63_504_3d_v056_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_smoothaccel_63_252_3d_v057_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_rngaccel_63_252_3d_v058_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_ignition_curvature_3d_v059_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_252d_3d_v060_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_jerk_126d_3d_v061_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accelz_126_504_3d_v062_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_norm_21d_3d_v063_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for keltner_bollinger_squeeze_z_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_curvature_gap_3d_v064_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 150)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_21d_3d_v065_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_63d_3d_v066_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_126d_3d_v067_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_norm_63d_3d_v068_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_jerk_21d_3d_v069_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_jerk_63d_3d_v070_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accelz_21_252_3d_v071_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accelz_63_504_3d_v072_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_smoothaccel_63_252_3d_v073_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_rngaccel_63_252_3d_v074_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_ignition_curvature_3d_v075_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_252d_3d_v076_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_jerk_126d_3d_v077_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accelz_126_504_3d_v078_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_norm_21d_3d_v079_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for keltner_bollinger_squeeze_z_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_curvature_gap_3d_v080_signal(high, low, closeadj):
    base = _z((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float), 504)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_accel_norm_63d_3d_v084_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_jerk_21d_3d_v085_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_jerk_63d_3d_v086_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_ignition_curvature_3d_v091_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d jerk for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_jerk_126d_3d_v093_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_accelz_126_504_3d_v094_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze_distmax_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_accel_norm_21d_3d_v095_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accel_norm_63d_3d_v116_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d acceleration z-score for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accelz_21_252_3d_v119_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accelz_63_504_3d_v120_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_smoothaccel_63_252_3d_v121_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# curvature plus slope ignition for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_ignition_curvature_3d_v123_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accel_252d_3d_v124_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accelz_126_504_3d_v126_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accel_norm_21d_3d_v127_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for keltner_bollinger_squeeze_distmed_504d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_curvature_gap_3d_v128_signal(high, low, closeadj):
    base = _safe_div(((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median(), ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 126d acceleration z-score for keltner_bollinger_squeeze_upper_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_upper_gap_150d_accelz_126_504_3d_v142_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d acceleration for keltner_bollinger_squeeze_lower_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_21d_3d_v145_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for keltner_bollinger_squeeze_lower_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_63d_3d_v146_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for keltner_bollinger_squeeze_lower_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_126d_3d_v147_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for keltner_bollinger_squeeze_lower_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_norm_63d_3d_v148_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for keltner_bollinger_squeeze_lower_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_jerk_21d_3d_v149_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for keltner_bollinger_squeeze_lower_gap_150d
def bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_jerk_63d_3d_v150_signal(high, low, closeadj):
    base = ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)) - ((_safe_div(4.0 * closeadj.rolling(20, min_periods=10).std(), closeadj.rolling(20, min_periods=10).mean().abs()) < _safe_div(2.0 * _atr(high, low, closeadj, 20), closeadj.abs())).astype(float)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'closeadj'], "func": fn} for fn in [bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_21d_3d_v001_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_63d_3d_v002_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_126d_3d_v003_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_norm_63d_3d_v004_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_jerk_21d_3d_v005_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_jerk_63d_3d_v006_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accelz_21_252_3d_v007_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accelz_63_504_3d_v008_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_smoothaccel_63_252_3d_v009_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_ignition_curvature_3d_v011_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_252d_3d_v012_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_jerk_126d_3d_v013_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accelz_126_504_3d_v014_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_accel_norm_21d_3d_v015_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_curvature_gap_3d_v016_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_21d_3d_v017_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_63d_3d_v018_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_126d_3d_v019_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_norm_63d_3d_v020_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_jerk_21d_3d_v021_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_jerk_63d_3d_v022_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accelz_21_252_3d_v023_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accelz_63_504_3d_v024_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_smoothaccel_63_252_3d_v025_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_rngaccel_63_252_3d_v026_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_ignition_curvature_3d_v027_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_252d_3d_v028_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_jerk_126d_3d_v029_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accelz_126_504_3d_v030_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_accel_norm_21d_3d_v031_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_55d_curvature_gap_3d_v032_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_21d_3d_v033_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_63d_3d_v034_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_126d_3d_v035_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_norm_63d_3d_v036_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_jerk_21d_3d_v037_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_jerk_63d_3d_v038_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accelz_21_252_3d_v039_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accelz_63_504_3d_v040_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_smoothaccel_63_252_3d_v041_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_rngaccel_63_252_3d_v042_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_ignition_curvature_3d_v043_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_252d_3d_v044_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_jerk_126d_3d_v045_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accelz_126_504_3d_v046_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_accel_norm_21d_3d_v047_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_mean_150d_curvature_gap_3d_v048_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_21d_3d_v049_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_63d_3d_v050_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_126d_3d_v051_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_norm_63d_3d_v052_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_jerk_21d_3d_v053_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_jerk_63d_3d_v054_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accelz_21_252_3d_v055_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accelz_63_504_3d_v056_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_smoothaccel_63_252_3d_v057_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_rngaccel_63_252_3d_v058_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_ignition_curvature_3d_v059_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_252d_3d_v060_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_jerk_126d_3d_v061_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accelz_126_504_3d_v062_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_accel_norm_21d_3d_v063_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_150d_curvature_gap_3d_v064_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_21d_3d_v065_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_63d_3d_v066_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_126d_3d_v067_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_norm_63d_3d_v068_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_jerk_21d_3d_v069_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_jerk_63d_3d_v070_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accelz_21_252_3d_v071_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accelz_63_504_3d_v072_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_smoothaccel_63_252_3d_v073_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_rngaccel_63_252_3d_v074_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_ignition_curvature_3d_v075_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_252d_3d_v076_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_jerk_126d_3d_v077_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accelz_126_504_3d_v078_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_accel_norm_21d_3d_v079_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_z_504d_curvature_gap_3d_v080_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_accel_norm_63d_3d_v084_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_jerk_21d_3d_v085_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_jerk_63d_3d_v086_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_ignition_curvature_3d_v091_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_jerk_126d_3d_v093_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_accelz_126_504_3d_v094_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmax_504d_accel_norm_21d_3d_v095_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accel_norm_63d_3d_v116_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accelz_21_252_3d_v119_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accelz_63_504_3d_v120_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_smoothaccel_63_252_3d_v121_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_ignition_curvature_3d_v123_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accel_252d_3d_v124_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accelz_126_504_3d_v126_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_accel_norm_21d_3d_v127_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_distmed_504d_curvature_gap_3d_v128_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_upper_gap_150d_accelz_126_504_3d_v142_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_21d_3d_v145_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_63d_3d_v146_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_126d_3d_v147_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_accel_norm_63d_3d_v148_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_jerk_21d_3d_v149_signal, bo_023_keltner_vs_bollinger_squeeze_keltner_bollinger_squeeze_lower_gap_150d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
