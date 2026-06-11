import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f027_parkinson(high, low, w):
    hi = high.replace(0, np.nan).abs()
    lo = low.replace(0, np.nan).abs()
    lr = np.log(hi / lo)
    sq = (lr * lr) / (4.0 * np.log(2.0))
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f027_garman_klass(high, low, closeadj, w):
    hi = high.replace(0, np.nan).abs()
    lo = low.replace(0, np.nan).abs()
    cl = closeadj.replace(0, np.nan).abs()
    op = cl.shift(1).replace(0, np.nan)
    lr_hl = np.log(hi / lo)
    lr_co = np.log(cl / op)
    val = 0.5 * lr_hl * lr_hl - (2.0 * np.log(2.0) - 1.0) * lr_co * lr_co
    return val.rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=0).pow(0.5)


def _f027_hl_vol_compress(high, low, w):
    rng = (high - low).abs()
    short_std = rng.rolling(max(2, w // 4), min_periods=1).std()
    long_std = rng.rolling(w, min_periods=max(1, w // 2)).std()
    return short_std / long_std.replace(0, np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_5d_jerk_v001_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_10d_jerk_v002_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_21d_jerk_v003_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_42d_jerk_v004_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_63d_jerk_v005_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_126d_jerk_v006_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_5d_jerk_v007_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_10d_jerk_v008_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_21d_jerk_v009_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_42d_jerk_v010_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_63d_jerk_v011_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_126d_jerk_v012_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_5d_jerk_v013_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_10d_jerk_v014_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_21d_jerk_v015_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_42d_jerk_v016_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_63d_jerk_v017_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_126d_jerk_v018_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_5d_jerk_v019_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_10d_jerk_v020_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_21d_jerk_v021_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_42d_jerk_v022_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_63d_jerk_v023_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_126d_jerk_v024_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_5d_jerk_v025_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_10d_jerk_v026_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_21d_jerk_v027_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_42d_jerk_v028_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_63d_jerk_v029_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_126d_jerk_v030_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_5d_jerk_v031_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _std(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_10d_jerk_v032_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _std(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_21d_jerk_v033_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _std(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_42d_jerk_v034_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _std(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_63d_jerk_v035_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _std(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_126d_jerk_v036_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * _std(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_5d_jerk_v037_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_10d_jerk_v038_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_21d_jerk_v039_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_42d_jerk_v040_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_63d_jerk_v041_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_126d_jerk_v042_signal(high, low, closeadj):
    base = (_f027_parkinson(high, low, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_5d_jerk_v043_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_10d_jerk_v044_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_21d_jerk_v045_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_42d_jerk_v046_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_63d_jerk_v047_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_126d_jerk_v048_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_5d_jerk_v049_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_10d_jerk_v050_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_21d_jerk_v051_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_42d_jerk_v052_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_63d_jerk_v053_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_126d_jerk_v054_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_5d_jerk_v055_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_10d_jerk_v056_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_21d_jerk_v057_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_42d_jerk_v058_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_63d_jerk_v059_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_126d_jerk_v060_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_5d_jerk_v061_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_10d_jerk_v062_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_21d_jerk_v063_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_42d_jerk_v064_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_63d_jerk_v065_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_126d_jerk_v066_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_5d_jerk_v067_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_10d_jerk_v068_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_21d_jerk_v069_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_42d_jerk_v070_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_63d_jerk_v071_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_126d_jerk_v072_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_5d_jerk_v073_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_10d_jerk_v074_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_21d_jerk_v075_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_42d_jerk_v076_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_63d_jerk_v077_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_126d_jerk_v078_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_5d_jerk_v079_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_10d_jerk_v080_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_21d_jerk_v081_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_42d_jerk_v082_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_63d_jerk_v083_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_126d_jerk_v084_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_5d_jerk_v085_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_10d_jerk_v086_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_21d_jerk_v087_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_42d_jerk_v088_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_63d_jerk_v089_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_126d_jerk_v090_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_5d_jerk_v091_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_10d_jerk_v092_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_21d_jerk_v093_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_42d_jerk_v094_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_63d_jerk_v095_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_126d_jerk_v096_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_5d_jerk_v097_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_10d_jerk_v098_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_21d_jerk_v099_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_42d_jerk_v100_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_63d_jerk_v101_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_126d_jerk_v102_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_5d_jerk_v103_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_10d_jerk_v104_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_21d_jerk_v105_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_42d_jerk_v106_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_63d_jerk_v107_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_126d_jerk_v108_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_5d_jerk_v109_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj.shift(1).bfill()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_10d_jerk_v110_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj.shift(1).bfill()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_21d_jerk_v111_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj.shift(1).bfill()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_42d_jerk_v112_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj.shift(1).bfill()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_63d_jerk_v113_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj.shift(1).bfill()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_126d_jerk_v114_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * closeadj.shift(1).bfill()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_5d_jerk_v115_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_10d_jerk_v116_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_21d_jerk_v117_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_42d_jerk_v118_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_63d_jerk_v119_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_126d_jerk_v120_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 5)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_5d_jerk_v121_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_10d_jerk_v122_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_21d_jerk_v123_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_42d_jerk_v124_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_63d_jerk_v125_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_126d_jerk_v126_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 10)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_5d_jerk_v127_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_10d_jerk_v128_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_21d_jerk_v129_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_42d_jerk_v130_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_63d_jerk_v131_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_126d_jerk_v132_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 21)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_5d_jerk_v133_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_10d_jerk_v134_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_21d_jerk_v135_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_42d_jerk_v136_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_63d_jerk_v137_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_126d_jerk_v138_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 42)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_5d_jerk_v139_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_10d_jerk_v140_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_21d_jerk_v141_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_42d_jerk_v142_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_63d_jerk_v143_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_126d_jerk_v144_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 63)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_5d_jerk_v145_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_10d_jerk_v146_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * _ema(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_21d_jerk_v147_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * _ema(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_42d_jerk_v148_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * _ema(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_63d_jerk_v149_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * _ema(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_126d_jerk_v150_signal(high, low, closeadj):
    base = (_mean(_f027_parkinson(high, low, 5), 126)) * _ema(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_5d_jerk_v001_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_10d_jerk_v002_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_21d_jerk_v003_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_42d_jerk_v004_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_63d_jerk_v005_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_126d_jerk_v006_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_5d_jerk_v007_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_10d_jerk_v008_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_21d_jerk_v009_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_42d_jerk_v010_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_63d_jerk_v011_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_lag_126d_jerk_v012_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_5d_jerk_v013_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_10d_jerk_v014_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_21d_jerk_v015_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_42d_jerk_v016_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_63d_jerk_v017_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xema_126d_jerk_v018_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_5d_jerk_v019_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_10d_jerk_v020_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_21d_jerk_v021_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_42d_jerk_v022_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_63d_jerk_v023_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean21_126d_jerk_v024_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_5d_jerk_v025_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_10d_jerk_v026_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_21d_jerk_v027_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_42d_jerk_v028_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_63d_jerk_v029_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xmean63_126d_jerk_v030_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_5d_jerk_v031_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_10d_jerk_v032_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_21d_jerk_v033_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_42d_jerk_v034_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_63d_jerk_v035_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xstd21close_126d_jerk_v036_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_5d_jerk_v037_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_10d_jerk_v038_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_21d_jerk_v039_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_42d_jerk_v040_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_63d_jerk_v041_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_raw5_xclose_norm_126d_jerk_v042_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_5d_jerk_v043_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_10d_jerk_v044_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_21d_jerk_v045_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_42d_jerk_v046_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_63d_jerk_v047_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_126d_jerk_v048_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_5d_jerk_v049_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_10d_jerk_v050_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_21d_jerk_v051_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_42d_jerk_v052_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_63d_jerk_v053_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_126d_jerk_v054_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_5d_jerk_v055_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_10d_jerk_v056_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_21d_jerk_v057_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_42d_jerk_v058_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_63d_jerk_v059_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_126d_jerk_v060_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_5d_jerk_v061_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_10d_jerk_v062_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_21d_jerk_v063_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_42d_jerk_v064_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_63d_jerk_v065_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_126d_jerk_v066_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_5d_jerk_v067_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_10d_jerk_v068_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_21d_jerk_v069_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_42d_jerk_v070_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_63d_jerk_v071_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_126d_jerk_v072_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_5d_jerk_v073_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_10d_jerk_v074_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_21d_jerk_v075_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_42d_jerk_v076_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_63d_jerk_v077_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_126d_jerk_v078_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_5d_jerk_v079_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_10d_jerk_v080_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_21d_jerk_v081_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_42d_jerk_v082_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_63d_jerk_v083_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xclose_lag_126d_jerk_v084_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_5d_jerk_v085_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_10d_jerk_v086_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_21d_jerk_v087_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_42d_jerk_v088_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_63d_jerk_v089_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xclose_lag_126d_jerk_v090_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_5d_jerk_v091_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_10d_jerk_v092_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_21d_jerk_v093_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_42d_jerk_v094_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_63d_jerk_v095_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xclose_lag_126d_jerk_v096_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_5d_jerk_v097_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_10d_jerk_v098_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_21d_jerk_v099_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_42d_jerk_v100_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_63d_jerk_v101_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xclose_lag_126d_jerk_v102_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_5d_jerk_v103_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_10d_jerk_v104_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_21d_jerk_v105_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_42d_jerk_v106_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_63d_jerk_v107_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xclose_lag_126d_jerk_v108_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_5d_jerk_v109_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_10d_jerk_v110_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_21d_jerk_v111_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_42d_jerk_v112_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_63d_jerk_v113_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xclose_lag_126d_jerk_v114_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_5d_jerk_v115_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_10d_jerk_v116_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_21d_jerk_v117_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_42d_jerk_v118_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_63d_jerk_v119_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean5_xema_126d_jerk_v120_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_5d_jerk_v121_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_10d_jerk_v122_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_21d_jerk_v123_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_42d_jerk_v124_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_63d_jerk_v125_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean10_xema_126d_jerk_v126_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_5d_jerk_v127_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_10d_jerk_v128_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_21d_jerk_v129_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_42d_jerk_v130_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_63d_jerk_v131_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean21_xema_126d_jerk_v132_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_5d_jerk_v133_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_10d_jerk_v134_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_21d_jerk_v135_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_42d_jerk_v136_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_63d_jerk_v137_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean42_xema_126d_jerk_v138_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_5d_jerk_v139_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_10d_jerk_v140_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_21d_jerk_v141_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_42d_jerk_v142_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_63d_jerk_v143_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean63_xema_126d_jerk_v144_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_5d_jerk_v145_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_10d_jerk_v146_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_21d_jerk_v147_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_42d_jerk_v148_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_63d_jerk_v149_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinson_5d_mean126_xema_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F027_PARKINSON_GARMAN_KLASS_VOL_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f027_parkinson', '_f027_garman_klass', '_f027_hl_vol_compress')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f027_parkinson_garman_klass_vol_3rd_derivatives_001_150_claude: {n_features} features pass")
