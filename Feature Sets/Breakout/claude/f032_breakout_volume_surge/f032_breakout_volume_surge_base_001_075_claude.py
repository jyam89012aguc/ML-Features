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


def f032bvs_f032_breakout_volume_surge_surge_5d_base_v001_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_10d_base_v002_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_21d_base_v003_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_42d_base_v004_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_63d_base_v005_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_126d_base_v006_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_189d_base_v007_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_252d_base_v008_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_378d_base_v009_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surge_504d_base_v010_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_5d_base_v011_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_10d_base_v012_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_21d_base_v013_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_42d_base_v014_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_63d_base_v015_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_126d_base_v016_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_189d_base_v017_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_252d_base_v018_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_378d_base_v019_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_bovol_504d_base_v020_signal(closeadj, volume):
    result = _f032_breakout_volume(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_5d_base_v021_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_10d_base_v022_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_21d_base_v023_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_42d_base_v024_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_63d_base_v025_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_126d_base_v026_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_189d_base_v027_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_252d_base_v028_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_378d_base_v029_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirm_504d_base_v030_signal(closeadj, volume):
    result = _f032_confirmation_score(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_5d_base_v031_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    result = _mean(s, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_10d_base_v032_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    result = _mean(s, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_21d_base_v033_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    result = _mean(s, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_42d_base_v034_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_63d_base_v035_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    result = _mean(s, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_126d_base_v036_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    result = _mean(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_189d_base_v037_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    result = _mean(s, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_252d_base_v038_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    result = _mean(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_378d_base_v039_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    result = _mean(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smsurge_504d_base_v040_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    result = _mean(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_5d_base_v041_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_10d_base_v042_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_21d_base_v043_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_42d_base_v044_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_63d_base_v045_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_126d_base_v046_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_189d_base_v047_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    result = _z(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_252d_base_v048_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_378d_base_v049_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    result = _z(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zsurge_504d_base_v050_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_5d_base_v051_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_10d_base_v052_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_21d_base_v053_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_42d_base_v054_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_63d_base_v055_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_126d_base_v056_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_189d_base_v057_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_252d_base_v058_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_378d_base_v059_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_logsurge_504d_base_v060_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    result = np.log(s.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_5d_base_v061_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_10d_base_v062_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_21d_base_v063_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_42d_base_v064_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    result = _std(s, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_63d_base_v065_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    result = _std(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_126d_base_v066_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    result = _std(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_189d_base_v067_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    result = _std(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_252d_base_v068_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    result = _std(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_378d_base_v069_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    result = _std(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_stdsurge_504d_base_v070_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    result = _std(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_5d_base_v071_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 5)
    dv = closeadj * volume
    result = c * _mean(dv, 5) / _mean(dv, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_10d_base_v072_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 10)
    dv = closeadj * volume
    result = c * _mean(dv, 5) / _mean(dv, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_21d_base_v073_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    dv = closeadj * volume
    result = c * _mean(dv, 10) / _mean(dv, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_42d_base_v074_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 42)
    dv = closeadj * volume
    result = c * _mean(dv, 21) / _mean(dv, 42).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_63d_base_v075_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    dv = closeadj * volume
    result = c * _mean(dv, 31) / _mean(dv, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f032bvs_f032_breakout_volume_surge_surge_5d_base_v001_signal,
    f032bvs_f032_breakout_volume_surge_surge_10d_base_v002_signal,
    f032bvs_f032_breakout_volume_surge_surge_21d_base_v003_signal,
    f032bvs_f032_breakout_volume_surge_surge_42d_base_v004_signal,
    f032bvs_f032_breakout_volume_surge_surge_63d_base_v005_signal,
    f032bvs_f032_breakout_volume_surge_surge_126d_base_v006_signal,
    f032bvs_f032_breakout_volume_surge_surge_189d_base_v007_signal,
    f032bvs_f032_breakout_volume_surge_surge_252d_base_v008_signal,
    f032bvs_f032_breakout_volume_surge_surge_378d_base_v009_signal,
    f032bvs_f032_breakout_volume_surge_surge_504d_base_v010_signal,
    f032bvs_f032_breakout_volume_surge_bovol_5d_base_v011_signal,
    f032bvs_f032_breakout_volume_surge_bovol_10d_base_v012_signal,
    f032bvs_f032_breakout_volume_surge_bovol_21d_base_v013_signal,
    f032bvs_f032_breakout_volume_surge_bovol_42d_base_v014_signal,
    f032bvs_f032_breakout_volume_surge_bovol_63d_base_v015_signal,
    f032bvs_f032_breakout_volume_surge_bovol_126d_base_v016_signal,
    f032bvs_f032_breakout_volume_surge_bovol_189d_base_v017_signal,
    f032bvs_f032_breakout_volume_surge_bovol_252d_base_v018_signal,
    f032bvs_f032_breakout_volume_surge_bovol_378d_base_v019_signal,
    f032bvs_f032_breakout_volume_surge_bovol_504d_base_v020_signal,
    f032bvs_f032_breakout_volume_surge_confirm_5d_base_v021_signal,
    f032bvs_f032_breakout_volume_surge_confirm_10d_base_v022_signal,
    f032bvs_f032_breakout_volume_surge_confirm_21d_base_v023_signal,
    f032bvs_f032_breakout_volume_surge_confirm_42d_base_v024_signal,
    f032bvs_f032_breakout_volume_surge_confirm_63d_base_v025_signal,
    f032bvs_f032_breakout_volume_surge_confirm_126d_base_v026_signal,
    f032bvs_f032_breakout_volume_surge_confirm_189d_base_v027_signal,
    f032bvs_f032_breakout_volume_surge_confirm_252d_base_v028_signal,
    f032bvs_f032_breakout_volume_surge_confirm_378d_base_v029_signal,
    f032bvs_f032_breakout_volume_surge_confirm_504d_base_v030_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_5d_base_v031_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_10d_base_v032_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_21d_base_v033_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_42d_base_v034_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_63d_base_v035_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_126d_base_v036_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_189d_base_v037_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_252d_base_v038_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_378d_base_v039_signal,
    f032bvs_f032_breakout_volume_surge_smsurge_504d_base_v040_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_5d_base_v041_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_10d_base_v042_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_21d_base_v043_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_42d_base_v044_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_63d_base_v045_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_126d_base_v046_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_189d_base_v047_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_252d_base_v048_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_378d_base_v049_signal,
    f032bvs_f032_breakout_volume_surge_zsurge_504d_base_v050_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_5d_base_v051_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_10d_base_v052_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_21d_base_v053_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_42d_base_v054_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_63d_base_v055_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_126d_base_v056_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_189d_base_v057_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_252d_base_v058_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_378d_base_v059_signal,
    f032bvs_f032_breakout_volume_surge_logsurge_504d_base_v060_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_5d_base_v061_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_10d_base_v062_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_21d_base_v063_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_42d_base_v064_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_63d_base_v065_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_126d_base_v066_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_189d_base_v067_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_252d_base_v068_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_378d_base_v069_signal,
    f032bvs_f032_breakout_volume_surge_stdsurge_504d_base_v070_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_5d_base_v071_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_10d_base_v072_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_21d_base_v073_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_42d_base_v074_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F032_BREAKOUT_VOLUME_SURGE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f032_breakout_volume_surge_base_001_075_claude: {n_features} features pass")
