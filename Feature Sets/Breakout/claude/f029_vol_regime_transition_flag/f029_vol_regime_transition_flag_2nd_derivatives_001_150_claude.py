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


def _f029_vol_regime(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).std()
    return vol / long_vol.replace(0, np.nan)


def _f029_regime_transition(closeadj, w):
    ret = closeadj.pct_change()
    vol_now = ret.rolling(w, min_periods=max(1, w // 2)).std()
    vol_prev = vol_now.shift(w)
    return (vol_now - vol_prev) / vol_prev.replace(0, np.nan).abs()


def _f029_transition_strength(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    m = vol.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).mean()
    sd = vol.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).std()
    return (vol - m) / sd.replace(0, np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_5d_slope_v001_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_10d_slope_v002_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_21d_slope_v003_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_42d_slope_v004_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_63d_slope_v005_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_126d_slope_v006_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_5d_slope_v007_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_10d_slope_v008_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_21d_slope_v009_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_42d_slope_v010_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_63d_slope_v011_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_126d_slope_v012_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_5d_slope_v013_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_10d_slope_v014_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_21d_slope_v015_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_42d_slope_v016_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_63d_slope_v017_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_126d_slope_v018_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_5d_slope_v019_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_10d_slope_v020_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_21d_slope_v021_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_42d_slope_v022_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_63d_slope_v023_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_126d_slope_v024_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_5d_slope_v025_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_10d_slope_v026_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_21d_slope_v027_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_42d_slope_v028_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_63d_slope_v029_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_126d_slope_v030_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_5d_slope_v031_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_10d_slope_v032_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_21d_slope_v033_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_42d_slope_v034_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_63d_slope_v035_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_126d_slope_v036_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_5d_slope_v037_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_10d_slope_v038_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_21d_slope_v039_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_42d_slope_v040_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_63d_slope_v041_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_126d_slope_v042_signal(closeadj):
    base = (_f029_vol_regime(closeadj, 5)) * closeadj / _mean(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_5d_slope_v043_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_10d_slope_v044_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_21d_slope_v045_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_42d_slope_v046_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_63d_slope_v047_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_126d_slope_v048_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_5d_slope_v049_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_10d_slope_v050_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_21d_slope_v051_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_42d_slope_v052_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_63d_slope_v053_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_126d_slope_v054_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_5d_slope_v055_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_10d_slope_v056_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_21d_slope_v057_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_42d_slope_v058_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_63d_slope_v059_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_126d_slope_v060_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_5d_slope_v061_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_10d_slope_v062_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_21d_slope_v063_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_42d_slope_v064_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_63d_slope_v065_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_126d_slope_v066_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_5d_slope_v067_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_10d_slope_v068_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_21d_slope_v069_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_42d_slope_v070_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_63d_slope_v071_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_126d_slope_v072_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_5d_slope_v073_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_10d_slope_v074_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_21d_slope_v075_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_42d_slope_v076_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_63d_slope_v077_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_126d_slope_v078_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_5d_slope_v079_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_10d_slope_v080_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_21d_slope_v081_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_42d_slope_v082_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_63d_slope_v083_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_126d_slope_v084_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_5d_slope_v085_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_10d_slope_v086_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_21d_slope_v087_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_42d_slope_v088_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_63d_slope_v089_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_126d_slope_v090_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_5d_slope_v091_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_10d_slope_v092_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_21d_slope_v093_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_42d_slope_v094_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_63d_slope_v095_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_126d_slope_v096_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_5d_slope_v097_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_10d_slope_v098_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_21d_slope_v099_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_42d_slope_v100_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_63d_slope_v101_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_126d_slope_v102_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_5d_slope_v103_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_10d_slope_v104_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_21d_slope_v105_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_42d_slope_v106_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_63d_slope_v107_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_126d_slope_v108_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_5d_slope_v109_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_10d_slope_v110_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_21d_slope_v111_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_42d_slope_v112_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_63d_slope_v113_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_126d_slope_v114_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * closeadj.shift(1).bfill()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_5d_slope_v115_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_10d_slope_v116_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_21d_slope_v117_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_42d_slope_v118_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_63d_slope_v119_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_126d_slope_v120_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 5)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_5d_slope_v121_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_10d_slope_v122_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_21d_slope_v123_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_42d_slope_v124_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_63d_slope_v125_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_126d_slope_v126_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 10)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_5d_slope_v127_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_10d_slope_v128_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_21d_slope_v129_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_42d_slope_v130_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_63d_slope_v131_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_126d_slope_v132_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 21)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_5d_slope_v133_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_10d_slope_v134_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_21d_slope_v135_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_42d_slope_v136_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_63d_slope_v137_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_126d_slope_v138_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 42)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_5d_slope_v139_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_10d_slope_v140_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_21d_slope_v141_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_42d_slope_v142_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_63d_slope_v143_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_126d_slope_v144_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 63)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_5d_slope_v145_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_10d_slope_v146_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_21d_slope_v147_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_42d_slope_v148_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_63d_slope_v149_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_126d_slope_v150_signal(closeadj):
    base = (_mean(_f029_vol_regime(closeadj, 5), 126)) * _ema(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_5d_slope_v001_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_10d_slope_v002_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_21d_slope_v003_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_42d_slope_v004_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_63d_slope_v005_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_126d_slope_v006_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_5d_slope_v007_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_10d_slope_v008_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_21d_slope_v009_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_42d_slope_v010_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_63d_slope_v011_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_lag_126d_slope_v012_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_5d_slope_v013_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_10d_slope_v014_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_21d_slope_v015_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_42d_slope_v016_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_63d_slope_v017_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xema_126d_slope_v018_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_5d_slope_v019_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_10d_slope_v020_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_21d_slope_v021_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_42d_slope_v022_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_63d_slope_v023_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean21_126d_slope_v024_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_5d_slope_v025_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_10d_slope_v026_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_21d_slope_v027_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_42d_slope_v028_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_63d_slope_v029_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xmean63_126d_slope_v030_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_5d_slope_v031_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_10d_slope_v032_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_21d_slope_v033_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_42d_slope_v034_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_63d_slope_v035_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xstd21close_126d_slope_v036_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_5d_slope_v037_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_10d_slope_v038_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_21d_slope_v039_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_42d_slope_v040_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_63d_slope_v041_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_raw5_xclose_norm_126d_slope_v042_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_5d_slope_v043_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_10d_slope_v044_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_21d_slope_v045_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_42d_slope_v046_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_63d_slope_v047_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_126d_slope_v048_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_5d_slope_v049_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_10d_slope_v050_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_21d_slope_v051_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_42d_slope_v052_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_63d_slope_v053_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_126d_slope_v054_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_5d_slope_v055_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_10d_slope_v056_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_21d_slope_v057_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_42d_slope_v058_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_63d_slope_v059_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_126d_slope_v060_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_5d_slope_v061_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_10d_slope_v062_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_21d_slope_v063_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_42d_slope_v064_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_63d_slope_v065_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_126d_slope_v066_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_5d_slope_v067_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_10d_slope_v068_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_21d_slope_v069_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_42d_slope_v070_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_63d_slope_v071_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_126d_slope_v072_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_5d_slope_v073_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_10d_slope_v074_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_21d_slope_v075_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_42d_slope_v076_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_63d_slope_v077_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_126d_slope_v078_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_5d_slope_v079_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_10d_slope_v080_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_21d_slope_v081_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_42d_slope_v082_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_63d_slope_v083_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xclose_lag_126d_slope_v084_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_5d_slope_v085_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_10d_slope_v086_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_21d_slope_v087_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_42d_slope_v088_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_63d_slope_v089_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xclose_lag_126d_slope_v090_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_5d_slope_v091_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_10d_slope_v092_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_21d_slope_v093_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_42d_slope_v094_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_63d_slope_v095_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xclose_lag_126d_slope_v096_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_5d_slope_v097_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_10d_slope_v098_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_21d_slope_v099_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_42d_slope_v100_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_63d_slope_v101_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xclose_lag_126d_slope_v102_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_5d_slope_v103_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_10d_slope_v104_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_21d_slope_v105_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_42d_slope_v106_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_63d_slope_v107_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xclose_lag_126d_slope_v108_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_5d_slope_v109_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_10d_slope_v110_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_21d_slope_v111_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_42d_slope_v112_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_63d_slope_v113_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xclose_lag_126d_slope_v114_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_5d_slope_v115_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_10d_slope_v116_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_21d_slope_v117_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_42d_slope_v118_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_63d_slope_v119_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean5_xema_126d_slope_v120_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_5d_slope_v121_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_10d_slope_v122_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_21d_slope_v123_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_42d_slope_v124_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_63d_slope_v125_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean10_xema_126d_slope_v126_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_5d_slope_v127_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_10d_slope_v128_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_21d_slope_v129_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_42d_slope_v130_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_63d_slope_v131_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean21_xema_126d_slope_v132_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_5d_slope_v133_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_10d_slope_v134_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_21d_slope_v135_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_42d_slope_v136_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_63d_slope_v137_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean42_xema_126d_slope_v138_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_5d_slope_v139_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_10d_slope_v140_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_21d_slope_v141_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_42d_slope_v142_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_63d_slope_v143_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean63_xema_126d_slope_v144_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_5d_slope_v145_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_10d_slope_v146_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_21d_slope_v147_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_42d_slope_v148_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_63d_slope_v149_signal,
    f029vrt_f029_vol_regime_transition_flag_volregime_5d_mean126_xema_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F029_VOL_REGIME_TRANSITION_FLAG_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ('_f029_vol_regime', '_f029_regime_transition', '_f029_transition_strength')
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
    print(f"OK f029_vol_regime_transition_flag_2nd_derivatives_001_150_claude: {n_features} features pass")
