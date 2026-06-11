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


# 21d acceleration for cash_runway
def bo_083_cash_runway_cash_runway_accel_21d_3d_v001_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway
def bo_083_cash_runway_cash_runway_accel_63d_3d_v002_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway
def bo_083_cash_runway_cash_runway_accel_126d_3d_v003_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway
def bo_083_cash_runway_cash_runway_accel_norm_63d_3d_v004_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway
def bo_083_cash_runway_cash_runway_jerk_21d_3d_v005_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway
def bo_083_cash_runway_cash_runway_jerk_63d_3d_v006_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway
def bo_083_cash_runway_cash_runway_accelz_21_252_3d_v007_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway
def bo_083_cash_runway_cash_runway_accelz_63_504_3d_v008_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway
def bo_083_cash_runway_cash_runway_smoothaccel_63_252_3d_v009_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway
def bo_083_cash_runway_cash_runway_rngaccel_63_252_3d_v010_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway
def bo_083_cash_runway_cash_runway_ignition_curvature_3d_v011_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway
def bo_083_cash_runway_cash_runway_accel_252d_3d_v012_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway
def bo_083_cash_runway_cash_runway_jerk_126d_3d_v013_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway
def bo_083_cash_runway_cash_runway_accelz_126_504_3d_v014_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway
def bo_083_cash_runway_cash_runway_accel_norm_21d_3d_v015_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway
def bo_083_cash_runway_cash_runway_curvature_gap_3d_v016_signal(cashneq, ncfo, capex):
    base = _safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accel_21d_3d_v017_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accel_63d_3d_v018_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accel_126d_3d_v019_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accel_norm_63d_3d_v020_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_jerk_21d_3d_v021_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_jerk_63d_3d_v022_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accelz_21_252_3d_v023_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accelz_63_504_3d_v024_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_smoothaccel_63_252_3d_v025_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_rngaccel_63_252_3d_v026_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_ignition_curvature_3d_v027_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accel_252d_3d_v028_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_jerk_126d_3d_v029_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accelz_126_504_3d_v030_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_accel_norm_21d_3d_v031_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_mean_55d
def bo_083_cash_runway_cash_runway_mean_55d_curvature_gap_3d_v032_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 55)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accel_21d_3d_v033_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accel_63d_3d_v034_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accel_126d_3d_v035_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accel_norm_63d_3d_v036_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_jerk_21d_3d_v037_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_jerk_63d_3d_v038_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accelz_21_252_3d_v039_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accelz_63_504_3d_v040_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_smoothaccel_63_252_3d_v041_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_rngaccel_63_252_3d_v042_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_ignition_curvature_3d_v043_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accel_252d_3d_v044_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_jerk_126d_3d_v045_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accelz_126_504_3d_v046_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_accel_norm_21d_3d_v047_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_mean_150d
def bo_083_cash_runway_cash_runway_mean_150d_curvature_gap_3d_v048_signal(cashneq, ncfo, capex):
    base = _mean(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accel_21d_3d_v049_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accel_63d_3d_v050_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accel_126d_3d_v051_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accel_norm_63d_3d_v052_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_jerk_21d_3d_v053_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_jerk_63d_3d_v054_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accelz_21_252_3d_v055_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accelz_63_504_3d_v056_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_smoothaccel_63_252_3d_v057_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_rngaccel_63_252_3d_v058_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_ignition_curvature_3d_v059_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accel_252d_3d_v060_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_jerk_126d_3d_v061_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accelz_126_504_3d_v062_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_accel_norm_21d_3d_v063_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_z_150d
def bo_083_cash_runway_cash_runway_z_150d_curvature_gap_3d_v064_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 150)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accel_21d_3d_v065_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accel_63d_3d_v066_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accel_126d_3d_v067_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accel_norm_63d_3d_v068_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_jerk_21d_3d_v069_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_jerk_63d_3d_v070_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accelz_21_252_3d_v071_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accelz_63_504_3d_v072_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_smoothaccel_63_252_3d_v073_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_rngaccel_63_252_3d_v074_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_ignition_curvature_3d_v075_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accel_252d_3d_v076_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_jerk_126d_3d_v077_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accelz_126_504_3d_v078_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_accel_norm_21d_3d_v079_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_z_504d
def bo_083_cash_runway_cash_runway_z_504d_curvature_gap_3d_v080_signal(cashneq, ncfo, capex):
    base = _z(_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean()), 504)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accel_21d_3d_v081_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accel_63d_3d_v082_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accel_126d_3d_v083_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accel_norm_63d_3d_v084_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_jerk_21d_3d_v085_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_jerk_63d_3d_v086_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accelz_21_252_3d_v087_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accelz_63_504_3d_v088_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_smoothaccel_63_252_3d_v089_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_rngaccel_63_252_3d_v090_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_ignition_curvature_3d_v091_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accel_252d_3d_v092_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_jerk_126d_3d_v093_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accelz_126_504_3d_v094_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_accel_norm_21d_3d_v095_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_distmax_504d
def bo_083_cash_runway_cash_runway_distmax_504d_curvature_gap_3d_v096_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).max().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accel_21d_3d_v097_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accel_63d_3d_v098_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accel_126d_3d_v099_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accel_norm_63d_3d_v100_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_jerk_21d_3d_v101_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_jerk_63d_3d_v102_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accelz_21_252_3d_v103_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accelz_63_504_3d_v104_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_smoothaccel_63_252_3d_v105_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_rngaccel_63_252_3d_v106_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_ignition_curvature_3d_v107_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accel_252d_3d_v108_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_jerk_126d_3d_v109_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accelz_126_504_3d_v110_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_accel_norm_21d_3d_v111_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_distmin_504d
def bo_083_cash_runway_cash_runway_distmin_504d_curvature_gap_3d_v112_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accel_21d_3d_v113_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accel_63d_3d_v114_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accel_126d_3d_v115_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accel_norm_63d_3d_v116_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_jerk_21d_3d_v117_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_jerk_63d_3d_v118_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accelz_21_252_3d_v119_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accelz_63_504_3d_v120_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_smoothaccel_63_252_3d_v121_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_rngaccel_63_252_3d_v122_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_ignition_curvature_3d_v123_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accel_252d_3d_v124_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_jerk_126d_3d_v125_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accelz_126_504_3d_v126_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_accel_norm_21d_3d_v127_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_distmed_504d
def bo_083_cash_runway_cash_runway_distmed_504d_curvature_gap_3d_v128_signal(cashneq, ncfo, capex):
    base = _safe_div((_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median(), (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accel_21d_3d_v129_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accel_63d_3d_v130_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accel_126d_3d_v131_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accel_norm_63d_3d_v132_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_jerk_21d_3d_v133_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_jerk_63d_3d_v134_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# 21d acceleration z-score for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accelz_21_252_3d_v135_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accelz_63_504_3d_v136_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_smoothaccel_63_252_3d_v137_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_rngaccel_63_252_3d_v138_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_ignition_curvature_3d_v139_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accel_252d_3d_v140_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_jerk_126d_3d_v141_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accelz_126_504_3d_v142_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# 21d normalized acceleration for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_accel_norm_21d_3d_v143_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# curvature regime gap for cash_runway_upper_gap_150d
def bo_083_cash_runway_cash_runway_upper_gap_150d_curvature_gap_3d_v144_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration for cash_runway_lower_gap_150d
def bo_083_cash_runway_cash_runway_lower_gap_150d_accel_21d_3d_v145_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for cash_runway_lower_gap_150d
def bo_083_cash_runway_cash_runway_lower_gap_150d_accel_63d_3d_v146_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for cash_runway_lower_gap_150d
def bo_083_cash_runway_cash_runway_lower_gap_150d_accel_126d_3d_v147_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for cash_runway_lower_gap_150d
def bo_083_cash_runway_cash_runway_lower_gap_150d_accel_norm_63d_3d_v148_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for cash_runway_lower_gap_150d
def bo_083_cash_runway_cash_runway_lower_gap_150d_jerk_21d_3d_v149_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for cash_runway_lower_gap_150d
def bo_083_cash_runway_cash_runway_lower_gap_150d_jerk_63d_3d_v150_signal(cashneq, ncfo, capex):
    base = (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())) - (_safe_div(cashneq, (-(ncfo + capex)).clip(lower=0).rolling(252, min_periods=126).mean())).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['cashneq', 'ncfo', 'capex'], "func": fn} for fn in [bo_083_cash_runway_cash_runway_accel_21d_3d_v001_signal, bo_083_cash_runway_cash_runway_accel_63d_3d_v002_signal, bo_083_cash_runway_cash_runway_accel_126d_3d_v003_signal, bo_083_cash_runway_cash_runway_accel_norm_63d_3d_v004_signal, bo_083_cash_runway_cash_runway_jerk_21d_3d_v005_signal, bo_083_cash_runway_cash_runway_jerk_63d_3d_v006_signal, bo_083_cash_runway_cash_runway_accelz_21_252_3d_v007_signal, bo_083_cash_runway_cash_runway_accelz_63_504_3d_v008_signal, bo_083_cash_runway_cash_runway_smoothaccel_63_252_3d_v009_signal, bo_083_cash_runway_cash_runway_rngaccel_63_252_3d_v010_signal, bo_083_cash_runway_cash_runway_ignition_curvature_3d_v011_signal, bo_083_cash_runway_cash_runway_accel_252d_3d_v012_signal, bo_083_cash_runway_cash_runway_jerk_126d_3d_v013_signal, bo_083_cash_runway_cash_runway_accelz_126_504_3d_v014_signal, bo_083_cash_runway_cash_runway_accel_norm_21d_3d_v015_signal, bo_083_cash_runway_cash_runway_curvature_gap_3d_v016_signal, bo_083_cash_runway_cash_runway_mean_55d_accel_21d_3d_v017_signal, bo_083_cash_runway_cash_runway_mean_55d_accel_63d_3d_v018_signal, bo_083_cash_runway_cash_runway_mean_55d_accel_126d_3d_v019_signal, bo_083_cash_runway_cash_runway_mean_55d_accel_norm_63d_3d_v020_signal, bo_083_cash_runway_cash_runway_mean_55d_jerk_21d_3d_v021_signal, bo_083_cash_runway_cash_runway_mean_55d_jerk_63d_3d_v022_signal, bo_083_cash_runway_cash_runway_mean_55d_accelz_21_252_3d_v023_signal, bo_083_cash_runway_cash_runway_mean_55d_accelz_63_504_3d_v024_signal, bo_083_cash_runway_cash_runway_mean_55d_smoothaccel_63_252_3d_v025_signal, bo_083_cash_runway_cash_runway_mean_55d_rngaccel_63_252_3d_v026_signal, bo_083_cash_runway_cash_runway_mean_55d_ignition_curvature_3d_v027_signal, bo_083_cash_runway_cash_runway_mean_55d_accel_252d_3d_v028_signal, bo_083_cash_runway_cash_runway_mean_55d_jerk_126d_3d_v029_signal, bo_083_cash_runway_cash_runway_mean_55d_accelz_126_504_3d_v030_signal, bo_083_cash_runway_cash_runway_mean_55d_accel_norm_21d_3d_v031_signal, bo_083_cash_runway_cash_runway_mean_55d_curvature_gap_3d_v032_signal, bo_083_cash_runway_cash_runway_mean_150d_accel_21d_3d_v033_signal, bo_083_cash_runway_cash_runway_mean_150d_accel_63d_3d_v034_signal, bo_083_cash_runway_cash_runway_mean_150d_accel_126d_3d_v035_signal, bo_083_cash_runway_cash_runway_mean_150d_accel_norm_63d_3d_v036_signal, bo_083_cash_runway_cash_runway_mean_150d_jerk_21d_3d_v037_signal, bo_083_cash_runway_cash_runway_mean_150d_jerk_63d_3d_v038_signal, bo_083_cash_runway_cash_runway_mean_150d_accelz_21_252_3d_v039_signal, bo_083_cash_runway_cash_runway_mean_150d_accelz_63_504_3d_v040_signal, bo_083_cash_runway_cash_runway_mean_150d_smoothaccel_63_252_3d_v041_signal, bo_083_cash_runway_cash_runway_mean_150d_rngaccel_63_252_3d_v042_signal, bo_083_cash_runway_cash_runway_mean_150d_ignition_curvature_3d_v043_signal, bo_083_cash_runway_cash_runway_mean_150d_accel_252d_3d_v044_signal, bo_083_cash_runway_cash_runway_mean_150d_jerk_126d_3d_v045_signal, bo_083_cash_runway_cash_runway_mean_150d_accelz_126_504_3d_v046_signal, bo_083_cash_runway_cash_runway_mean_150d_accel_norm_21d_3d_v047_signal, bo_083_cash_runway_cash_runway_mean_150d_curvature_gap_3d_v048_signal, bo_083_cash_runway_cash_runway_z_150d_accel_21d_3d_v049_signal, bo_083_cash_runway_cash_runway_z_150d_accel_63d_3d_v050_signal, bo_083_cash_runway_cash_runway_z_150d_accel_126d_3d_v051_signal, bo_083_cash_runway_cash_runway_z_150d_accel_norm_63d_3d_v052_signal, bo_083_cash_runway_cash_runway_z_150d_jerk_21d_3d_v053_signal, bo_083_cash_runway_cash_runway_z_150d_jerk_63d_3d_v054_signal, bo_083_cash_runway_cash_runway_z_150d_accelz_21_252_3d_v055_signal, bo_083_cash_runway_cash_runway_z_150d_accelz_63_504_3d_v056_signal, bo_083_cash_runway_cash_runway_z_150d_smoothaccel_63_252_3d_v057_signal, bo_083_cash_runway_cash_runway_z_150d_rngaccel_63_252_3d_v058_signal, bo_083_cash_runway_cash_runway_z_150d_ignition_curvature_3d_v059_signal, bo_083_cash_runway_cash_runway_z_150d_accel_252d_3d_v060_signal, bo_083_cash_runway_cash_runway_z_150d_jerk_126d_3d_v061_signal, bo_083_cash_runway_cash_runway_z_150d_accelz_126_504_3d_v062_signal, bo_083_cash_runway_cash_runway_z_150d_accel_norm_21d_3d_v063_signal, bo_083_cash_runway_cash_runway_z_150d_curvature_gap_3d_v064_signal, bo_083_cash_runway_cash_runway_z_504d_accel_21d_3d_v065_signal, bo_083_cash_runway_cash_runway_z_504d_accel_63d_3d_v066_signal, bo_083_cash_runway_cash_runway_z_504d_accel_126d_3d_v067_signal, bo_083_cash_runway_cash_runway_z_504d_accel_norm_63d_3d_v068_signal, bo_083_cash_runway_cash_runway_z_504d_jerk_21d_3d_v069_signal, bo_083_cash_runway_cash_runway_z_504d_jerk_63d_3d_v070_signal, bo_083_cash_runway_cash_runway_z_504d_accelz_21_252_3d_v071_signal, bo_083_cash_runway_cash_runway_z_504d_accelz_63_504_3d_v072_signal, bo_083_cash_runway_cash_runway_z_504d_smoothaccel_63_252_3d_v073_signal, bo_083_cash_runway_cash_runway_z_504d_rngaccel_63_252_3d_v074_signal, bo_083_cash_runway_cash_runway_z_504d_ignition_curvature_3d_v075_signal, bo_083_cash_runway_cash_runway_z_504d_accel_252d_3d_v076_signal, bo_083_cash_runway_cash_runway_z_504d_jerk_126d_3d_v077_signal, bo_083_cash_runway_cash_runway_z_504d_accelz_126_504_3d_v078_signal, bo_083_cash_runway_cash_runway_z_504d_accel_norm_21d_3d_v079_signal, bo_083_cash_runway_cash_runway_z_504d_curvature_gap_3d_v080_signal, bo_083_cash_runway_cash_runway_distmax_504d_accel_21d_3d_v081_signal, bo_083_cash_runway_cash_runway_distmax_504d_accel_63d_3d_v082_signal, bo_083_cash_runway_cash_runway_distmax_504d_accel_126d_3d_v083_signal, bo_083_cash_runway_cash_runway_distmax_504d_accel_norm_63d_3d_v084_signal, bo_083_cash_runway_cash_runway_distmax_504d_jerk_21d_3d_v085_signal, bo_083_cash_runway_cash_runway_distmax_504d_jerk_63d_3d_v086_signal, bo_083_cash_runway_cash_runway_distmax_504d_accelz_21_252_3d_v087_signal, bo_083_cash_runway_cash_runway_distmax_504d_accelz_63_504_3d_v088_signal, bo_083_cash_runway_cash_runway_distmax_504d_smoothaccel_63_252_3d_v089_signal, bo_083_cash_runway_cash_runway_distmax_504d_rngaccel_63_252_3d_v090_signal, bo_083_cash_runway_cash_runway_distmax_504d_ignition_curvature_3d_v091_signal, bo_083_cash_runway_cash_runway_distmax_504d_accel_252d_3d_v092_signal, bo_083_cash_runway_cash_runway_distmax_504d_jerk_126d_3d_v093_signal, bo_083_cash_runway_cash_runway_distmax_504d_accelz_126_504_3d_v094_signal, bo_083_cash_runway_cash_runway_distmax_504d_accel_norm_21d_3d_v095_signal, bo_083_cash_runway_cash_runway_distmax_504d_curvature_gap_3d_v096_signal, bo_083_cash_runway_cash_runway_distmin_504d_accel_21d_3d_v097_signal, bo_083_cash_runway_cash_runway_distmin_504d_accel_63d_3d_v098_signal, bo_083_cash_runway_cash_runway_distmin_504d_accel_126d_3d_v099_signal, bo_083_cash_runway_cash_runway_distmin_504d_accel_norm_63d_3d_v100_signal, bo_083_cash_runway_cash_runway_distmin_504d_jerk_21d_3d_v101_signal, bo_083_cash_runway_cash_runway_distmin_504d_jerk_63d_3d_v102_signal, bo_083_cash_runway_cash_runway_distmin_504d_accelz_21_252_3d_v103_signal, bo_083_cash_runway_cash_runway_distmin_504d_accelz_63_504_3d_v104_signal, bo_083_cash_runway_cash_runway_distmin_504d_smoothaccel_63_252_3d_v105_signal, bo_083_cash_runway_cash_runway_distmin_504d_rngaccel_63_252_3d_v106_signal, bo_083_cash_runway_cash_runway_distmin_504d_ignition_curvature_3d_v107_signal, bo_083_cash_runway_cash_runway_distmin_504d_accel_252d_3d_v108_signal, bo_083_cash_runway_cash_runway_distmin_504d_jerk_126d_3d_v109_signal, bo_083_cash_runway_cash_runway_distmin_504d_accelz_126_504_3d_v110_signal, bo_083_cash_runway_cash_runway_distmin_504d_accel_norm_21d_3d_v111_signal, bo_083_cash_runway_cash_runway_distmin_504d_curvature_gap_3d_v112_signal, bo_083_cash_runway_cash_runway_distmed_504d_accel_21d_3d_v113_signal, bo_083_cash_runway_cash_runway_distmed_504d_accel_63d_3d_v114_signal, bo_083_cash_runway_cash_runway_distmed_504d_accel_126d_3d_v115_signal, bo_083_cash_runway_cash_runway_distmed_504d_accel_norm_63d_3d_v116_signal, bo_083_cash_runway_cash_runway_distmed_504d_jerk_21d_3d_v117_signal, bo_083_cash_runway_cash_runway_distmed_504d_jerk_63d_3d_v118_signal, bo_083_cash_runway_cash_runway_distmed_504d_accelz_21_252_3d_v119_signal, bo_083_cash_runway_cash_runway_distmed_504d_accelz_63_504_3d_v120_signal, bo_083_cash_runway_cash_runway_distmed_504d_smoothaccel_63_252_3d_v121_signal, bo_083_cash_runway_cash_runway_distmed_504d_rngaccel_63_252_3d_v122_signal, bo_083_cash_runway_cash_runway_distmed_504d_ignition_curvature_3d_v123_signal, bo_083_cash_runway_cash_runway_distmed_504d_accel_252d_3d_v124_signal, bo_083_cash_runway_cash_runway_distmed_504d_jerk_126d_3d_v125_signal, bo_083_cash_runway_cash_runway_distmed_504d_accelz_126_504_3d_v126_signal, bo_083_cash_runway_cash_runway_distmed_504d_accel_norm_21d_3d_v127_signal, bo_083_cash_runway_cash_runway_distmed_504d_curvature_gap_3d_v128_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accel_21d_3d_v129_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accel_63d_3d_v130_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accel_126d_3d_v131_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accel_norm_63d_3d_v132_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_jerk_21d_3d_v133_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_jerk_63d_3d_v134_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accelz_21_252_3d_v135_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accelz_63_504_3d_v136_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_smoothaccel_63_252_3d_v137_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_rngaccel_63_252_3d_v138_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_ignition_curvature_3d_v139_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accel_252d_3d_v140_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_jerk_126d_3d_v141_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accelz_126_504_3d_v142_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_accel_norm_21d_3d_v143_signal, bo_083_cash_runway_cash_runway_upper_gap_150d_curvature_gap_3d_v144_signal, bo_083_cash_runway_cash_runway_lower_gap_150d_accel_21d_3d_v145_signal, bo_083_cash_runway_cash_runway_lower_gap_150d_accel_63d_3d_v146_signal, bo_083_cash_runway_cash_runway_lower_gap_150d_accel_126d_3d_v147_signal, bo_083_cash_runway_cash_runway_lower_gap_150d_accel_norm_63d_3d_v148_signal, bo_083_cash_runway_cash_runway_lower_gap_150d_jerk_21d_3d_v149_signal, bo_083_cash_runway_cash_runway_lower_gap_150d_jerk_63d_3d_v150_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
