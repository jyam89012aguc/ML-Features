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


# 21d acceleration z-score for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_accelz_21_252_3d_v007_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_accelz_63_504_3d_v008_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# curvature plus slope ignition for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_ignition_curvature_3d_v011_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_accelz_126_504_3d_v014_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_curvature_gap_3d_v016_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration z-score for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_accelz_21_252_3d_v023_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_accelz_63_504_3d_v024_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# curvature plus slope ignition for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_ignition_curvature_3d_v027_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_accelz_126_504_3d_v030_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_curvature_gap_3d_v032_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration z-score for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accelz_21_252_3d_v039_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accelz_63_504_3d_v040_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# curvature plus slope ignition for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_ignition_curvature_3d_v043_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accel_252d_3d_v044_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _accel(base, 252)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accelz_126_504_3d_v046_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_curvature_gap_3d_v048_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d acceleration z-score for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accelz_21_252_3d_v055_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accelz_63_504_3d_v056_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# curvature plus slope ignition for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_ignition_curvature_3d_v059_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accel_252d_3d_v060_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _accel(base, 252)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accelz_126_504_3d_v062_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_curvature_gap_3d_v064_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 126d acceleration for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accel_126d_3d_v067_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _accel(base, 126)
    return _clean(result)

# 21d acceleration z-score for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accelz_21_252_3d_v071_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accelz_63_504_3d_v072_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_smoothaccel_63_252_3d_v073_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_rngaccel_63_252_3d_v074_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_ignition_curvature_3d_v075_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accel_252d_3d_v076_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_jerk_126d_3d_v077_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accelz_126_504_3d_v078_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_curvature_gap_3d_v080_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_accelz_63_504_3d_v088_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# 252d acceleration for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_accel_252d_3d_v092_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_accelz_126_504_3d_v094_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_curvature_gap_3d_v096_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 126d acceleration for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accel_126d_3d_v115_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _accel(base, 126)
    return _clean(result)

# 21d acceleration z-score for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accelz_21_252_3d_v119_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_accel(base, 21), 252)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accelz_63_504_3d_v120_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# smoothed 63d acceleration for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_smoothaccel_63_252_3d_v121_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _mean(_accel(base, 63), 252)
    return _clean(result)

# range-normalized acceleration for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_rngaccel_63_252_3d_v122_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# curvature plus slope ignition for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_ignition_curvature_3d_v123_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_accel(base, 21), 252) + _z(_slope(base, 63), 252)
    return _clean(result)

# 252d acceleration for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accel_252d_3d_v124_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _accel(base, 252)
    return _clean(result)

# 126d jerk for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_jerk_126d_3d_v125_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    s = _slope(base, 126); result = _slope(s, 126)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accelz_126_504_3d_v126_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_curvature_gap_3d_v128_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

# 21d jerk for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_jerk_21d_3d_v133_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d acceleration z-score for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_accelz_63_504_3d_v136_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504)
    return _clean(result)

# 252d acceleration for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_accel_252d_3d_v140_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

# 126d acceleration z-score for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_accelz_126_504_3d_v142_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_accel(base, 126), 504)
    return _clean(result)

# curvature regime gap for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_curvature_gap_3d_v144_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_accel(base, 63), 504) - _z(_accel(base, 21), 252)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [bo_017_all_time_high_recency_vs_history_ath_recency_drought_accelz_21_252_3d_v007_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_accelz_63_504_3d_v008_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_ignition_curvature_3d_v011_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_accelz_126_504_3d_v014_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_curvature_gap_3d_v016_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_accelz_21_252_3d_v023_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_accelz_63_504_3d_v024_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_ignition_curvature_3d_v027_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_accelz_126_504_3d_v030_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_curvature_gap_3d_v032_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accelz_21_252_3d_v039_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accelz_63_504_3d_v040_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_ignition_curvature_3d_v043_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accel_252d_3d_v044_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_accelz_126_504_3d_v046_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_curvature_gap_3d_v048_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accelz_21_252_3d_v055_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accelz_63_504_3d_v056_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_ignition_curvature_3d_v059_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accel_252d_3d_v060_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_accelz_126_504_3d_v062_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_curvature_gap_3d_v064_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accel_126d_3d_v067_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accelz_21_252_3d_v071_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accelz_63_504_3d_v072_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_smoothaccel_63_252_3d_v073_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_rngaccel_63_252_3d_v074_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_ignition_curvature_3d_v075_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accel_252d_3d_v076_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_jerk_126d_3d_v077_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_accelz_126_504_3d_v078_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_curvature_gap_3d_v080_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_accelz_63_504_3d_v088_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_accel_252d_3d_v092_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_accelz_126_504_3d_v094_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_curvature_gap_3d_v096_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accel_126d_3d_v115_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accelz_21_252_3d_v119_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accelz_63_504_3d_v120_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_smoothaccel_63_252_3d_v121_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_rngaccel_63_252_3d_v122_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_ignition_curvature_3d_v123_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accel_252d_3d_v124_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_jerk_126d_3d_v125_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_accelz_126_504_3d_v126_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_curvature_gap_3d_v128_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_jerk_21d_3d_v133_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_accelz_63_504_3d_v136_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_accel_252d_3d_v140_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_accelz_126_504_3d_v142_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_curvature_gap_3d_v144_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
