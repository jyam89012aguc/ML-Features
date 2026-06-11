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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f032_vol_surge(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / avg.replace(0, np.nan)


def _f032_breakout_volume(closeadj, volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    surge = volume / avg.replace(0, np.nan)
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    break_flag = (closeadj >= hi).astype(float)
    return surge * break_flag * closeadj


def _f032_confirmation_score(closeadj, volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    surge = volume / avg.replace(0, np.nan)
    ret = closeadj.pct_change(w)
    return surge * ret * closeadj


def f032bvs_f032_breakout_volume_surge_surge_21d_jerk_v001_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_21d_jerk_v002_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_63d_jerk_v003_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_63d_jerk_v004_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_126d_jerk_v005_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_126d_jerk_v006_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v007_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v008_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v009_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v010_signal(closeadj, volume):
    base = _f032_vol_surge(volume, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_21d_jerk_v011_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = b.ewm(span=10, adjust=False).mean() + _f032_vol_surge(volume, 21) * closeadj * 0.001
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_21d_jerk_v012_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = b.ewm(span=10, adjust=False).mean() + _f032_vol_surge(volume, 21) * closeadj * 0.001
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_63d_jerk_v013_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = b.ewm(span=31, adjust=False).mean() + _f032_vol_surge(volume, 63) * closeadj * 0.001
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_63d_jerk_v014_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = b.ewm(span=31, adjust=False).mean() + _f032_vol_surge(volume, 63) * closeadj * 0.001
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_126d_jerk_v015_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = b.ewm(span=63, adjust=False).mean() + _f032_vol_surge(volume, 126) * closeadj * 0.001
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_126d_jerk_v016_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = b.ewm(span=63, adjust=False).mean() + _f032_vol_surge(volume, 126) * closeadj * 0.001
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v017_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.ewm(span=126, adjust=False).mean() + _f032_vol_surge(volume, 252) * closeadj * 0.001
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v018_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.ewm(span=126, adjust=False).mean() + _f032_vol_surge(volume, 252) * closeadj * 0.001
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v019_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.ewm(span=126, adjust=False).mean() + _f032_vol_surge(volume, 252) * closeadj * 0.001
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v020_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.ewm(span=126, adjust=False).mean() + _f032_vol_surge(volume, 252) * closeadj * 0.001
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_21d_jerk_v021_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_21d_jerk_v022_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_63d_jerk_v023_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_63d_jerk_v024_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_126d_jerk_v025_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_126d_jerk_v026_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v027_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v028_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v029_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v030_signal(closeadj, volume):
    base = _f032_confirmation_score(closeadj, volume, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_21d_jerk_v031_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = _mean(s, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_21d_jerk_v032_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = _mean(s, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_63d_jerk_v033_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = _mean(s, 31) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_63d_jerk_v034_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = _mean(s, 31) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_126d_jerk_v035_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = _mean(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_126d_jerk_v036_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = _mean(s, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v037_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _mean(s, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v038_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _mean(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v039_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _mean(s, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v040_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _mean(s, 126) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_21d_jerk_v041_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_21d_jerk_v042_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_63d_jerk_v043_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_63d_jerk_v044_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_126d_jerk_v045_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = _z(s, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_126d_jerk_v046_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = _z(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v047_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v048_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v049_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v050_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_21d_jerk_v051_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_21d_jerk_v052_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_63d_jerk_v053_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_63d_jerk_v054_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_126d_jerk_v055_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_126d_jerk_v056_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v057_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v058_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v059_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v060_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = np.log(s.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_21d_jerk_v061_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_21d_jerk_v062_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_63d_jerk_v063_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = _std(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_63d_jerk_v064_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = _std(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_126d_jerk_v065_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = _std(s, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_126d_jerk_v066_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = _std(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v067_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _std(s, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v068_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _std(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v069_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _std(s, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v070_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = _std(s, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_21d_jerk_v071_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    dv = closeadj * volume
    base = c * _mean(dv, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_21d_jerk_v072_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    dv = closeadj * volume
    base = c * _mean(dv, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_63d_jerk_v073_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    dv = closeadj * volume
    base = c * _mean(dv, 31)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_63d_jerk_v074_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    dv = closeadj * volume
    base = c * _mean(dv, 31)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_126d_jerk_v075_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    dv = closeadj * volume
    base = c * _mean(dv, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_126d_jerk_v076_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    dv = closeadj * volume
    base = c * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v077_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    dv = closeadj * volume
    base = c * _mean(dv, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v078_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    dv = closeadj * volume
    base = c * _mean(dv, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v079_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    dv = closeadj * volume
    base = c * _mean(dv, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v080_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    dv = closeadj * volume
    base = c * _mean(dv, 126)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_21d_jerk_v081_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = _mean(b, 7)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_21d_jerk_v082_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = _mean(b, 7)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_63d_jerk_v083_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = _mean(b, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_63d_jerk_v084_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = _mean(b, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_126d_jerk_v085_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = _mean(b, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_126d_jerk_v086_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = _mean(b, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v087_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _mean(b, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v088_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _mean(b, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v089_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _mean(b, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v090_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _mean(b, 84)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_21d_jerk_v091_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = _z(b, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_21d_jerk_v092_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = _z(b, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_63d_jerk_v093_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = _z(b, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_63d_jerk_v094_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = _z(b, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_126d_jerk_v095_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = _z(b, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_126d_jerk_v096_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = _z(b, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v097_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _z(b, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v098_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _z(b, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v099_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _z(b, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v100_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = _z(b, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_21d_jerk_v101_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_21d_jerk_v102_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_63d_jerk_v103_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_63d_jerk_v104_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_126d_jerk_v105_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_126d_jerk_v106_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v107_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v108_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v109_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v110_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = (c * c) * np.sign(c)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_21d_jerk_v111_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = s.ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_21d_jerk_v112_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    base = s.ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_63d_jerk_v113_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = s.ewm(span=31, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_63d_jerk_v114_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    base = s.ewm(span=31, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_126d_jerk_v115_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = s.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_126d_jerk_v116_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    base = s.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v117_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = s.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v118_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = s.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v119_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = s.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v120_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    base = s.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_21d_jerk_v121_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    base = _mean(c, 7)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_21d_jerk_v122_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    base = _mean(c, 7)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_63d_jerk_v123_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    base = _mean(c, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_63d_jerk_v124_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    base = _mean(c, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_126d_jerk_v125_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    base = _mean(c, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_126d_jerk_v126_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    base = _mean(c, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v127_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = _mean(c, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v128_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = _mean(c, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v129_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = _mean(c, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v130_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    base = _mean(c, 84)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_21d_jerk_v131_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    ret = closeadj.pct_change(4)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_21d_jerk_v132_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    ret = closeadj.pct_change(4)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_63d_jerk_v133_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    ret = closeadj.pct_change(12)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_63d_jerk_v134_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    ret = closeadj.pct_change(12)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_126d_jerk_v135_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    ret = closeadj.pct_change(25)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_126d_jerk_v136_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    ret = closeadj.pct_change(25)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v137_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    ret = closeadj.pct_change(50)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v138_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    ret = closeadj.pct_change(50)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v139_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    ret = closeadj.pct_change(50)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v140_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    ret = closeadj.pct_change(50)
    up = (ret > 0).astype(float)
    base = s * up * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_21d_jerk_v141_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = b.abs().rolling(21, min_periods=5).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_21d_jerk_v142_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    base = b.abs().rolling(21, min_periods=5).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_63d_jerk_v143_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = b.abs().rolling(63, min_periods=15).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_63d_jerk_v144_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    base = b.abs().rolling(63, min_periods=15).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_126d_jerk_v145_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = b.abs().rolling(126, min_periods=31).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_126d_jerk_v146_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    base = b.abs().rolling(126, min_periods=31).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v147_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.abs().rolling(252, min_periods=63).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v148_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.abs().rolling(252, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v149_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.abs().rolling(252, min_periods=63).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v150_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    base = b.abs().rolling(252, min_periods=63).mean()
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f032bvs_f032_breakout_volume_surge_surge_21d_jerk_v001_signal,
    f032bvs_f032_breakout_volume_surge_surge_21d_jerk_v002_signal,
    f032bvs_f032_breakout_volume_surge_surge_63d_jerk_v003_signal,
    f032bvs_f032_breakout_volume_surge_surge_63d_jerk_v004_signal,
    f032bvs_f032_breakout_volume_surge_surge_126d_jerk_v005_signal,
    f032bvs_f032_breakout_volume_surge_surge_126d_jerk_v006_signal,
    f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v007_signal,
    f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v008_signal,
    f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v009_signal,
    f032bvs_f032_breakout_volume_surge_surge_252d_jerk_v010_signal,
    f032bvs_f032_breakout_volume_surge_bovol_21d_jerk_v011_signal,
    f032bvs_f032_breakout_volume_surge_bovol_21d_jerk_v012_signal,
    f032bvs_f032_breakout_volume_surge_bovol_63d_jerk_v013_signal,
    f032bvs_f032_breakout_volume_surge_bovol_63d_jerk_v014_signal,
    f032bvs_f032_breakout_volume_surge_bovol_126d_jerk_v015_signal,
    f032bvs_f032_breakout_volume_surge_bovol_126d_jerk_v016_signal,
    f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v017_signal,
    f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v018_signal,
    f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v019_signal,
    f032bvs_f032_breakout_volume_surge_bovol_252d_jerk_v020_signal,
    f032bvs_f032_breakout_volume_surge_confirm_21d_jerk_v021_signal,
    f032bvs_f032_breakout_volume_surge_confirm_21d_jerk_v022_signal,
    f032bvs_f032_breakout_volume_surge_confirm_63d_jerk_v023_signal,
    f032bvs_f032_breakout_volume_surge_confirm_63d_jerk_v024_signal,
    f032bvs_f032_breakout_volume_surge_confirm_126d_jerk_v025_signal,
    f032bvs_f032_breakout_volume_surge_confirm_126d_jerk_v026_signal,
    f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v027_signal,
    f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v028_signal,
    f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v029_signal,
    f032bvs_f032_breakout_volume_surge_confirm_252d_jerk_v030_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_21d_jerk_v031_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_21d_jerk_v032_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_63d_jerk_v033_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_63d_jerk_v034_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_126d_jerk_v035_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_126d_jerk_v036_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v037_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v038_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v039_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_252d_jerk_v040_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_21d_jerk_v041_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_21d_jerk_v042_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_63d_jerk_v043_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_63d_jerk_v044_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_126d_jerk_v045_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_126d_jerk_v046_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v047_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v048_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v049_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_252d_jerk_v050_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_21d_jerk_v051_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_21d_jerk_v052_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_63d_jerk_v053_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_63d_jerk_v054_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_126d_jerk_v055_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_126d_jerk_v056_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v057_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v058_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v059_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_252d_jerk_v060_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_21d_jerk_v061_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_21d_jerk_v062_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_63d_jerk_v063_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_63d_jerk_v064_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_126d_jerk_v065_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_126d_jerk_v066_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v067_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v068_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v069_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_252d_jerk_v070_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_21d_jerk_v071_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_21d_jerk_v072_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_63d_jerk_v073_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_63d_jerk_v074_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_126d_jerk_v075_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_126d_jerk_v076_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v077_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v078_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v079_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_252d_jerk_v080_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_21d_jerk_v081_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_21d_jerk_v082_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_63d_jerk_v083_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_63d_jerk_v084_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_126d_jerk_v085_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_126d_jerk_v086_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v087_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v088_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v089_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_252d_jerk_v090_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_21d_jerk_v091_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_21d_jerk_v092_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_63d_jerk_v093_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_63d_jerk_v094_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_126d_jerk_v095_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_126d_jerk_v096_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v097_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v098_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v099_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_252d_jerk_v100_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_21d_jerk_v101_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_21d_jerk_v102_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_63d_jerk_v103_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_63d_jerk_v104_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_126d_jerk_v105_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_126d_jerk_v106_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v107_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v108_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v109_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_252d_jerk_v110_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_21d_jerk_v111_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_21d_jerk_v112_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_63d_jerk_v113_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_63d_jerk_v114_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_126d_jerk_v115_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_126d_jerk_v116_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v117_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v118_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v119_signal,
    f032bvs_f032_breakout_volume_surge_emasurge_252d_jerk_v120_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_21d_jerk_v121_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_21d_jerk_v122_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_63d_jerk_v123_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_63d_jerk_v124_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_126d_jerk_v125_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_126d_jerk_v126_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v127_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v128_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v129_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_252d_jerk_v130_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_21d_jerk_v131_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_21d_jerk_v132_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_63d_jerk_v133_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_63d_jerk_v134_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_126d_jerk_v135_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_126d_jerk_v136_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v137_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v138_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v139_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_252d_jerk_v140_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_21d_jerk_v141_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_21d_jerk_v142_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_63d_jerk_v143_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_63d_jerk_v144_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_126d_jerk_v145_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_126d_jerk_v146_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v147_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v148_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v149_signal,
    f032bvs_f032_breakout_volume_surge_absbovol_252d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F032_BREAKOUT_VOLUME_SURGE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f032_vol_surge', '_f032_breakout_volume', '_f032_confirmation_score')
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
    print(f"OK f032_breakout_volume_surge_3rd_derivatives_001_150_claude: {n_features} features pass")
