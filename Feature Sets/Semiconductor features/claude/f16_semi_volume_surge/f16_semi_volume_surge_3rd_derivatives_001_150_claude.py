import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f16_log_vol(volume):
    return np.log(volume.replace(0, np.nan).abs())


def _f16_surge_ratio(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _f16_z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _vol_level(volume, w):
    v = _f16_log_vol(volume)
    return v - _mean(v, w)


def _vol_z(volume, w):
    v = _f16_log_vol(volume)
    return _f16_z(v, w)


def _vol_robust_z(volume, w):
    v = _f16_log_vol(volume)
    med = v.rolling(w, min_periods=max(1, w // 2)).median()
    mad = (v - med).abs().rolling(w, min_periods=max(1, w // 2)).median()
    return (v - med) / (1.4826 * mad).replace(0, np.nan)


def _vol_std(volume, w):
    v = _f16_log_vol(volume).diff()
    return _std(v, w)


def _vol_max(volume, w):
    v = _f16_log_vol(volume)
    return v.rolling(w, min_periods=max(1, w // 2)).max()


def _vol_min(volume, w):
    v = _f16_log_vol(volume)
    return v.rolling(w, min_periods=max(1, w // 2)).min()


def _vol_range(volume, w):
    v = _f16_log_vol(volume)
    return v.rolling(w, min_periods=max(1, w // 2)).max() - v.rolling(w, min_periods=max(1, w // 2)).min()


def _vol_pos(volume, w):
    v = _f16_log_vol(volume)
    lo = v.rolling(w, min_periods=max(1, w // 2)).min()
    hi = v.rolling(w, min_periods=max(1, w // 2)).max()
    return (v - lo) / (hi - lo).replace(0, np.nan)


def _vol_dd(volume, w):
    v = _f16_log_vol(volume)
    return v - v.rolling(w, min_periods=max(1, w // 2)).max()


def _vol_up(volume, w):
    v = _f16_log_vol(volume)
    return v - v.rolling(w, min_periods=max(1, w // 2)).min()


def _surge_frac(volume, w):
    r = _f16_surge_ratio(volume, w)
    return (r > 1.5).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


def _surge_hits(volume, w):
    r = _f16_surge_ratio(volume, w)
    return (r > 1.5).astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _vol_skew(volume, w):
    v = _f16_log_vol(volume).diff()
    return v.rolling(w, min_periods=max(1, w // 2)).skew()


def _vol_kurt(volume, w):
    v = _f16_log_vol(volume).diff()
    return v.rolling(w, min_periods=max(1, w // 2)).kurt()


def _vol_cv(volume, w):
    return _std(volume, w) / _mean(volume, w).replace(0, np.nan)


def _vol_signcum(volume, w):
    d = _f16_log_vol(volume).diff()
    return pd.Series(np.sign(d), index=d.index).rolling(w, min_periods=max(1, w // 2)).sum()


def _signed_surge(volume, closeadj, w):
    v = _f16_log_vol(volume)
    ret = closeadj.pct_change()
    return _f16_z(v, w) * np.sign(ret)


# 5d curvature of 21d log-volume level
def f16vs_f16_semi_volume_surge_vollevel_21d_curv_v001_signal(volume, closeadj):
    base = _vol_level(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d log-volume level
def f16vs_f16_semi_volume_surge_vollevel_21d_curv_v002_signal(volume, closeadj):
    base = _vol_level(volume, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d log-volume level
def f16vs_f16_semi_volume_surge_vollevel_63d_curv_v003_signal(volume, closeadj):
    base = _vol_level(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d log-volume level
def f16vs_f16_semi_volume_surge_vollevel_126d_curv_v004_signal(volume, closeadj):
    base = _vol_level(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d log-volume level
def f16vs_f16_semi_volume_surge_vollevel_252d_curv_v005_signal(volume, closeadj):
    base = _vol_level(volume, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d volume z-score
def f16vs_f16_semi_volume_surge_volz_21d_curv_v006_signal(volume, closeadj):
    base = _vol_z(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d volume z-score
def f16vs_f16_semi_volume_surge_volz_21d_curv_v007_signal(volume, closeadj):
    base = _vol_z(volume, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d volume z-score
def f16vs_f16_semi_volume_surge_volz_63d_curv_v008_signal(volume, closeadj):
    base = _vol_z(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d volume z-score
def f16vs_f16_semi_volume_surge_volz_126d_curv_v009_signal(volume, closeadj):
    base = _vol_z(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d volume z-score
def f16vs_f16_semi_volume_surge_volz_252d_curv_v010_signal(volume, closeadj):
    base = _vol_z(volume, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d robust z
def f16vs_f16_semi_volume_surge_volrobustz_21d_curv_v011_signal(volume, closeadj):
    base = _vol_robust_z(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z
def f16vs_f16_semi_volume_surge_volrobustz_63d_curv_v012_signal(volume, closeadj):
    base = _vol_robust_z(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d robust z
def f16vs_f16_semi_volume_surge_volrobustz_126d_curv_v013_signal(volume, closeadj):
    base = _vol_robust_z(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d robust z
def f16vs_f16_semi_volume_surge_volrobustz_252d_curv_v014_signal(volume, closeadj):
    base = _vol_robust_z(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robust z
def f16vs_f16_semi_volume_surge_volrobustz_504d_curv_v015_signal(volume, closeadj):
    base = _vol_robust_z(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d surge ratio
def f16vs_f16_semi_volume_surge_surge_21d_curv_v016_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d surge ratio
def f16vs_f16_semi_volume_surge_surge_21d_curv_v017_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d surge ratio
def f16vs_f16_semi_volume_surge_surge_63d_curv_v018_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d surge ratio
def f16vs_f16_semi_volume_surge_surge_126d_curv_v019_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d surge ratio
def f16vs_f16_semi_volume_surge_surge_252d_curv_v020_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d std of log-volume diff
def f16vs_f16_semi_volume_surge_volstd_21d_curv_v021_signal(volume, closeadj):
    base = _vol_std(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d std
def f16vs_f16_semi_volume_surge_volstd_21d_curv_v022_signal(volume, closeadj):
    base = _vol_std(volume, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std
def f16vs_f16_semi_volume_surge_volstd_63d_curv_v023_signal(volume, closeadj):
    base = _vol_std(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d std
def f16vs_f16_semi_volume_surge_volstd_126d_curv_v024_signal(volume, closeadj):
    base = _vol_std(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d std
def f16vs_f16_semi_volume_surge_volstd_252d_curv_v025_signal(volume, closeadj):
    base = _vol_std(volume, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d max log-volume
def f16vs_f16_semi_volume_surge_volmax_21d_curv_v026_signal(volume, closeadj):
    base = _vol_max(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d max log-volume
def f16vs_f16_semi_volume_surge_volmax_63d_curv_v027_signal(volume, closeadj):
    base = _vol_max(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d max log-volume
def f16vs_f16_semi_volume_surge_volmax_126d_curv_v028_signal(volume, closeadj):
    base = _vol_max(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d max log-volume
def f16vs_f16_semi_volume_surge_volmax_252d_curv_v029_signal(volume, closeadj):
    base = _vol_max(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d max log-volume
def f16vs_f16_semi_volume_surge_volmax_504d_curv_v030_signal(volume, closeadj):
    base = _vol_max(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d min log-volume
def f16vs_f16_semi_volume_surge_volmin_21d_curv_v031_signal(volume, closeadj):
    base = _vol_min(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d min log-volume
def f16vs_f16_semi_volume_surge_volmin_63d_curv_v032_signal(volume, closeadj):
    base = _vol_min(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d min log-volume
def f16vs_f16_semi_volume_surge_volmin_126d_curv_v033_signal(volume, closeadj):
    base = _vol_min(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d min log-volume
def f16vs_f16_semi_volume_surge_volmin_252d_curv_v034_signal(volume, closeadj):
    base = _vol_min(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d min log-volume
def f16vs_f16_semi_volume_surge_volmin_504d_curv_v035_signal(volume, closeadj):
    base = _vol_min(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d range
def f16vs_f16_semi_volume_surge_volrng_21d_curv_v036_signal(volume, closeadj):
    base = _vol_range(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range
def f16vs_f16_semi_volume_surge_volrng_63d_curv_v037_signal(volume, closeadj):
    base = _vol_range(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d range
def f16vs_f16_semi_volume_surge_volrng_126d_curv_v038_signal(volume, closeadj):
    base = _vol_range(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d range
def f16vs_f16_semi_volume_surge_volrng_252d_curv_v039_signal(volume, closeadj):
    base = _vol_range(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d range
def f16vs_f16_semi_volume_surge_volrng_504d_curv_v040_signal(volume, closeadj):
    base = _vol_range(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d position-in-range
def f16vs_f16_semi_volume_surge_volpos_21d_curv_v041_signal(volume, closeadj):
    base = _vol_pos(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position-in-range
def f16vs_f16_semi_volume_surge_volpos_63d_curv_v042_signal(volume, closeadj):
    base = _vol_pos(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d position-in-range
def f16vs_f16_semi_volume_surge_volpos_126d_curv_v043_signal(volume, closeadj):
    base = _vol_pos(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d position-in-range
def f16vs_f16_semi_volume_surge_volpos_252d_curv_v044_signal(volume, closeadj):
    base = _vol_pos(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d position-in-range
def f16vs_f16_semi_volume_surge_volpos_504d_curv_v045_signal(volume, closeadj):
    base = _vol_pos(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d drawdown
def f16vs_f16_semi_volume_surge_voldd_21d_curv_v046_signal(volume, closeadj):
    base = _vol_dd(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown
def f16vs_f16_semi_volume_surge_voldd_63d_curv_v047_signal(volume, closeadj):
    base = _vol_dd(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d drawdown
def f16vs_f16_semi_volume_surge_voldd_126d_curv_v048_signal(volume, closeadj):
    base = _vol_dd(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d drawdown
def f16vs_f16_semi_volume_surge_voldd_252d_curv_v049_signal(volume, closeadj):
    base = _vol_dd(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d drawdown
def f16vs_f16_semi_volume_surge_voldd_504d_curv_v050_signal(volume, closeadj):
    base = _vol_dd(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d run-up
def f16vs_f16_semi_volume_surge_volup_21d_curv_v051_signal(volume, closeadj):
    base = _vol_up(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up
def f16vs_f16_semi_volume_surge_volup_63d_curv_v052_signal(volume, closeadj):
    base = _vol_up(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d run-up
def f16vs_f16_semi_volume_surge_volup_126d_curv_v053_signal(volume, closeadj):
    base = _vol_up(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d run-up
def f16vs_f16_semi_volume_surge_volup_252d_curv_v054_signal(volume, closeadj):
    base = _vol_up(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d run-up
def f16vs_f16_semi_volume_surge_volup_504d_curv_v055_signal(volume, closeadj):
    base = _vol_up(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d surge hits
def f16vs_f16_semi_volume_surge_surgehits_21d_curv_v056_signal(volume, closeadj):
    base = _surge_hits(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d surge hits
def f16vs_f16_semi_volume_surge_surgehits_63d_curv_v057_signal(volume, closeadj):
    base = _surge_hits(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d surge hits
def f16vs_f16_semi_volume_surge_surgehits_126d_curv_v058_signal(volume, closeadj):
    base = _surge_hits(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d surge hits
def f16vs_f16_semi_volume_surge_surgehits_252d_curv_v059_signal(volume, closeadj):
    base = _surge_hits(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d surge hits
def f16vs_f16_semi_volume_surge_surgehits_504d_curv_v060_signal(volume, closeadj):
    base = _surge_hits(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d surge hit ratio
def f16vs_f16_semi_volume_surge_surgefrac_21d_curv_v061_signal(volume, closeadj):
    base = _surge_frac(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d surge hit ratio
def f16vs_f16_semi_volume_surge_surgefrac_63d_curv_v062_signal(volume, closeadj):
    base = _surge_frac(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d surge hit ratio
def f16vs_f16_semi_volume_surge_surgefrac_126d_curv_v063_signal(volume, closeadj):
    base = _surge_frac(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d surge hit ratio
def f16vs_f16_semi_volume_surge_surgefrac_252d_curv_v064_signal(volume, closeadj):
    base = _surge_frac(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d surge hit ratio
def f16vs_f16_semi_volume_surge_surgefrac_504d_curv_v065_signal(volume, closeadj):
    base = _surge_frac(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d skew
def f16vs_f16_semi_volume_surge_volskew_21d_curv_v066_signal(volume, closeadj):
    base = _vol_skew(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew
def f16vs_f16_semi_volume_surge_volskew_63d_curv_v067_signal(volume, closeadj):
    base = _vol_skew(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d skew
def f16vs_f16_semi_volume_surge_volskew_126d_curv_v068_signal(volume, closeadj):
    base = _vol_skew(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d skew
def f16vs_f16_semi_volume_surge_volskew_252d_curv_v069_signal(volume, closeadj):
    base = _vol_skew(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d skew
def f16vs_f16_semi_volume_surge_volskew_504d_curv_v070_signal(volume, closeadj):
    base = _vol_skew(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d kurtosis
def f16vs_f16_semi_volume_surge_volkurt_21d_curv_v071_signal(volume, closeadj):
    base = _vol_kurt(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d kurtosis
def f16vs_f16_semi_volume_surge_volkurt_63d_curv_v072_signal(volume, closeadj):
    base = _vol_kurt(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d kurtosis
def f16vs_f16_semi_volume_surge_volkurt_126d_curv_v073_signal(volume, closeadj):
    base = _vol_kurt(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d kurtosis
def f16vs_f16_semi_volume_surge_volkurt_252d_curv_v074_signal(volume, closeadj):
    base = _vol_kurt(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d kurtosis
def f16vs_f16_semi_volume_surge_volkurt_504d_curv_v075_signal(volume, closeadj):
    base = _vol_kurt(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d CV
def f16vs_f16_semi_volume_surge_volcv_21d_curv_v076_signal(volume, closeadj):
    base = _vol_cv(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d CV
def f16vs_f16_semi_volume_surge_volcv_63d_curv_v077_signal(volume, closeadj):
    base = _vol_cv(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d CV
def f16vs_f16_semi_volume_surge_volcv_126d_curv_v078_signal(volume, closeadj):
    base = _vol_cv(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d CV
def f16vs_f16_semi_volume_surge_volcv_252d_curv_v079_signal(volume, closeadj):
    base = _vol_cv(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d CV
def f16vs_f16_semi_volume_surge_volcv_504d_curv_v080_signal(volume, closeadj):
    base = _vol_cv(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d signed cumulative
def f16vs_f16_semi_volume_surge_volsigncum_21d_curv_v081_signal(volume, closeadj):
    base = _vol_signcum(volume, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative
def f16vs_f16_semi_volume_surge_volsigncum_63d_curv_v082_signal(volume, closeadj):
    base = _vol_signcum(volume, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d signed cumulative
def f16vs_f16_semi_volume_surge_volsigncum_126d_curv_v083_signal(volume, closeadj):
    base = _vol_signcum(volume, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d signed cumulative
def f16vs_f16_semi_volume_surge_volsigncum_252d_curv_v084_signal(volume, closeadj):
    base = _vol_signcum(volume, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d signed cumulative
def f16vs_f16_semi_volume_surge_volsigncum_504d_curv_v085_signal(volume, closeadj):
    base = _vol_signcum(volume, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d log-surge
def f16vs_f16_semi_volume_surge_logsurge_21d_curv_v086_signal(volume, closeadj):
    base = np.log(volume.replace(0, np.nan) / _mean(volume, 21).replace(0, np.nan))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d log-surge
def f16vs_f16_semi_volume_surge_logsurge_63d_curv_v087_signal(volume, closeadj):
    base = np.log(volume.replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d log-surge
def f16vs_f16_semi_volume_surge_logsurge_126d_curv_v088_signal(volume, closeadj):
    base = np.log(volume.replace(0, np.nan) / _mean(volume, 126).replace(0, np.nan))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d log-surge
def f16vs_f16_semi_volume_surge_logsurge_252d_curv_v089_signal(volume, closeadj):
    base = np.log(volume.replace(0, np.nan) / _mean(volume, 252).replace(0, np.nan))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d log-surge
def f16vs_f16_semi_volume_surge_logsurge_504d_curv_v090_signal(volume, closeadj):
    base = np.log(volume.replace(0, np.nan) / _mean(volume, 504).replace(0, np.nan))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d signed surge
def f16vs_f16_semi_volume_surge_signedsurge_21d_curv_v091_signal(volume, closeadj):
    base = _signed_surge(volume, closeadj, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed surge
def f16vs_f16_semi_volume_surge_signedsurge_63d_curv_v092_signal(volume, closeadj):
    base = _signed_surge(volume, closeadj, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d signed surge
def f16vs_f16_semi_volume_surge_signedsurge_126d_curv_v093_signal(volume, closeadj):
    base = _signed_surge(volume, closeadj, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d signed surge
def f16vs_f16_semi_volume_surge_signedsurge_252d_curv_v094_signal(volume, closeadj):
    base = _signed_surge(volume, closeadj, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d signed surge
def f16vs_f16_semi_volume_surge_signedsurge_504d_curv_v095_signal(volume, closeadj):
    base = _signed_surge(volume, closeadj, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d surge up-day cond
def f16vs_f16_semi_volume_surge_surgeup_21d_curv_v096_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 21).where(ret > 0), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d surge up-day cond
def f16vs_f16_semi_volume_surge_surgeup_63d_curv_v097_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 63).where(ret > 0), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d surge up-day cond
def f16vs_f16_semi_volume_surge_surgeup_126d_curv_v098_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 126).where(ret > 0), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d surge up-day cond
def f16vs_f16_semi_volume_surge_surgeup_252d_curv_v099_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 252).where(ret > 0), 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d surge up-day cond
def f16vs_f16_semi_volume_surge_surgeup_504d_curv_v100_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 504).where(ret > 0), 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d surge down-day cond
def f16vs_f16_semi_volume_surge_surgedn_21d_curv_v101_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 21).where(ret < 0), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d surge down-day cond
def f16vs_f16_semi_volume_surge_surgedn_63d_curv_v102_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 63).where(ret < 0), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d surge down-day cond
def f16vs_f16_semi_volume_surge_surgedn_126d_curv_v103_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 126).where(ret < 0), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d surge down-day cond
def f16vs_f16_semi_volume_surge_surgedn_252d_curv_v104_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 252).where(ret < 0), 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d surge down-day cond
def f16vs_f16_semi_volume_surge_surgedn_504d_curv_v105_signal(volume, closeadj):
    ret = closeadj.pct_change()
    base = _mean(_f16_surge_ratio(volume, 504).where(ret < 0), 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d 95th pct surge
def f16vs_f16_semi_volume_surge_surgep95_21d_curv_v106_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 21).rolling(21, min_periods=11).quantile(0.95)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d 95th pct surge
def f16vs_f16_semi_volume_surge_surgep95_63d_curv_v107_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 63).rolling(63, min_periods=32).quantile(0.95)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d 95th pct surge
def f16vs_f16_semi_volume_surge_surgep95_126d_curv_v108_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 126).rolling(126, min_periods=63).quantile(0.95)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d 95th pct surge
def f16vs_f16_semi_volume_surge_surgep95_252d_curv_v109_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 252).rolling(252, min_periods=126).quantile(0.95)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d 95th pct surge
def f16vs_f16_semi_volume_surge_surgep95_504d_curv_v110_signal(volume, closeadj):
    base = _f16_surge_ratio(volume, 504).rolling(504, min_periods=252).quantile(0.95)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d dry-up hits
def f16vs_f16_semi_volume_surge_dryhits_21d_curv_v111_signal(volume, closeadj):
    base = (_f16_surge_ratio(volume, 21) < 0.5).astype(float).rolling(21, min_periods=11).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d dry-up hits
def f16vs_f16_semi_volume_surge_dryhits_63d_curv_v112_signal(volume, closeadj):
    base = (_f16_surge_ratio(volume, 63) < 0.5).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d dry-up hits
def f16vs_f16_semi_volume_surge_dryhits_126d_curv_v113_signal(volume, closeadj):
    base = (_f16_surge_ratio(volume, 126) < 0.5).astype(float).rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d dry-up hits
def f16vs_f16_semi_volume_surge_dryhits_252d_curv_v114_signal(volume, closeadj):
    base = (_f16_surge_ratio(volume, 252) < 0.5).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d dry-up hits
def f16vs_f16_semi_volume_surge_dryhits_504d_curv_v115_signal(volume, closeadj):
    base = (_f16_surge_ratio(volume, 504) < 0.5).astype(float).rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d extreme hits
def f16vs_f16_semi_volume_surge_extremehits_21d_curv_v116_signal(volume, closeadj):
    z = _vol_z(volume, 63)
    base = (z > 2).astype(float).rolling(21, min_periods=11).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d extreme hits
def f16vs_f16_semi_volume_surge_extremehits_63d_curv_v117_signal(volume, closeadj):
    z = _vol_z(volume, 63)
    base = (z > 2).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d extreme hits
def f16vs_f16_semi_volume_surge_extremehits_126d_curv_v118_signal(volume, closeadj):
    z = _vol_z(volume, 126)
    base = (z > 2).astype(float).rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d extreme hits
def f16vs_f16_semi_volume_surge_extremehits_252d_curv_v119_signal(volume, closeadj):
    z = _vol_z(volume, 252)
    base = (z > 2).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d extreme hits
def f16vs_f16_semi_volume_surge_extremehits_504d_curv_v120_signal(volume, closeadj):
    z = _vol_z(volume, 504)
    base = (z > 2).astype(float).rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d autocorr
def f16vs_f16_semi_volume_surge_volautocorr_21d_curv_v121_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.rolling(21, min_periods=11).corr(v.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d autocorr
def f16vs_f16_semi_volume_surge_volautocorr_63d_curv_v122_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.rolling(63, min_periods=32).corr(v.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d autocorr
def f16vs_f16_semi_volume_surge_volautocorr_126d_curv_v123_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.rolling(126, min_periods=63).corr(v.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d autocorr
def f16vs_f16_semi_volume_surge_volautocorr_252d_curv_v124_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.rolling(252, min_periods=126).corr(v.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d autocorr
def f16vs_f16_semi_volume_surge_volautocorr_504d_curv_v125_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.rolling(504, min_periods=252).corr(v.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of mean-ratio 21v63
def f16vs_f16_semi_volume_surge_meanratio_21v63_curv_v126_signal(volume, closeadj):
    base = _mean(volume, 21) / _mean(volume, 63).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of mean-ratio 63v126
def f16vs_f16_semi_volume_surge_meanratio_63v126_curv_v127_signal(volume, closeadj):
    base = _mean(volume, 63) / _mean(volume, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of mean-ratio 126v252
def f16vs_f16_semi_volume_surge_meanratio_126v252_curv_v128_signal(volume, closeadj):
    base = _mean(volume, 126) / _mean(volume, 252).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of mean-ratio 252v504
def f16vs_f16_semi_volume_surge_meanratio_252v504_curv_v129_signal(volume, closeadj):
    base = _mean(volume, 252) / _mean(volume, 504).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of mean-ratio 21v252
def f16vs_f16_semi_volume_surge_meanratio_21v252_curv_v130_signal(volume, closeadj):
    base = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d surge maxratio
def f16vs_f16_semi_volume_surge_surgemaxratio_21d_curv_v131_signal(volume, closeadj):
    base = volume.rolling(21, min_periods=11).max() / volume.rolling(252, min_periods=126).median().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d surge maxratio
def f16vs_f16_semi_volume_surge_surgemaxratio_63d_curv_v132_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=32).max() / volume.rolling(252, min_periods=126).median().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d surge maxratio
def f16vs_f16_semi_volume_surge_surgemaxratio_126d_curv_v133_signal(volume, closeadj):
    base = volume.rolling(126, min_periods=63).max() / volume.rolling(504, min_periods=252).median().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d surge maxratio
def f16vs_f16_semi_volume_surge_surgemaxratio_252d_curv_v134_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=126).max() / volume.rolling(504, min_periods=252).median().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d surge maxratio
def f16vs_f16_semi_volume_surge_surgemaxratio_504d_curv_v135_signal(volume, closeadj):
    base = volume.rolling(504, min_periods=252).max() / volume.rolling(756, min_periods=378).median().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d cumulative log-vol
def f16vs_f16_semi_volume_surge_volcum_21d_curv_v136_signal(volume, closeadj):
    base = _f16_log_vol(volume).diff().rolling(21, min_periods=11).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cumulative log-vol
def f16vs_f16_semi_volume_surge_volcum_63d_curv_v137_signal(volume, closeadj):
    base = _f16_log_vol(volume).diff().rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cumulative log-vol
def f16vs_f16_semi_volume_surge_volcum_126d_curv_v138_signal(volume, closeadj):
    base = _f16_log_vol(volume).diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d cumulative log-vol
def f16vs_f16_semi_volume_surge_volcum_252d_curv_v139_signal(volume, closeadj):
    base = _f16_log_vol(volume).diff().rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d cumulative log-vol
def f16vs_f16_semi_volume_surge_volcum_504d_curv_v140_signal(volume, closeadj):
    base = _f16_log_vol(volume).diff().rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of EMA crossover (5v21)
def f16vs_f16_semi_volume_surge_volema_5v21_curv_v141_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.ewm(span=5, adjust=False).mean() - v.ewm(span=21, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of EMA crossover (21v63)
def f16vs_f16_semi_volume_surge_volema_21v63_curv_v142_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.ewm(span=21, adjust=False).mean() - v.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of EMA crossover (63v126)
def f16vs_f16_semi_volume_surge_volema_63v126_curv_v143_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.ewm(span=63, adjust=False).mean() - v.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of EMA crossover (126v252)
def f16vs_f16_semi_volume_surge_volema_126v252_curv_v144_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.ewm(span=126, adjust=False).mean() - v.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of EMA crossover (252v504)
def f16vs_f16_semi_volume_surge_volema_252v504_curv_v145_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = v.ewm(span=252, adjust=False).mean() - v.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of composite short
def f16vs_f16_semi_volume_surge_composite_short_curv_v146_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = _f16_z(v, 21) + _f16_z(v, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of composite long
def f16vs_f16_semi_volume_surge_composite_long_curv_v147_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = _f16_z(v, 63) + _f16_z(v, 126) + _f16_z(v, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of composite long
def f16vs_f16_semi_volume_surge_composite_long_curv_v148_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    base = _f16_z(v, 63) + _f16_z(v, 126) + _f16_z(v, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d surge quality
def f16vs_f16_semi_volume_surge_surgequality_63d_curv_v149_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _f16_z(v, 63)
    hit = (_f16_surge_ratio(volume, 63) > 1.5).astype(float).rolling(63, min_periods=32).mean()
    base = z * hit
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d surge quality
def f16vs_f16_semi_volume_surge_surgequality_252d_curv_v150_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _f16_z(v, 252)
    hit = (_f16_surge_ratio(volume, 252) > 1.5).astype(float).rolling(252, min_periods=126).mean()
    base = z * hit
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)
