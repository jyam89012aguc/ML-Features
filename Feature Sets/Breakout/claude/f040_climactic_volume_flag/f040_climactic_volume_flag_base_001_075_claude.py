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
def _f040_vol_extreme(volume, w):
    m = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = volume.rolling(w, min_periods=max(1, w // 2)).std()
    return (volume - m) / sd.replace(0, np.nan)


def _f040_climax_volume(volume, w):
    z = _f040_vol_extreme(volume, w)
    return z.rolling(w, min_periods=max(1, w // 2)).max()


def _f040_climax_intensity(close, volume, w):
    z = _f040_vol_extreme(volume, w)
    range_close = close.rolling(w, min_periods=max(1, w // 2)).max() - close.rolling(w, min_periods=max(1, w // 2)).min()
    return z.abs() * range_close / close.replace(0, np.nan)


# 21d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_21d_base_v001_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_63d_base_v002_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_126d_base_v003_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_252d_base_v004_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_504d_base_v005_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_5d_base_v006_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_10d_base_v007_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_42d_base_v008_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_189d_base_v009_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vol extreme × close
def f040cvf_f040_climactic_volume_flag_vex_378d_base_v010_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax volume × close
def f040cvf_f040_climactic_volume_flag_climax_21d_base_v011_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax volume × close
def f040cvf_f040_climactic_volume_flag_climax_63d_base_v012_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d climax volume × close
def f040cvf_f040_climactic_volume_flag_climax_126d_base_v013_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d climax volume × close
def f040cvf_f040_climactic_volume_flag_climax_252d_base_v014_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d climax volume × close
def f040cvf_f040_climactic_volume_flag_climax_504d_base_v015_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d climax × close
def f040cvf_f040_climactic_volume_flag_climax_5d_base_v016_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d climax × close
def f040cvf_f040_climactic_volume_flag_climax_10d_base_v017_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d climax × close
def f040cvf_f040_climactic_volume_flag_climax_42d_base_v018_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d climax × close
def f040cvf_f040_climactic_volume_flag_climax_189d_base_v019_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d climax × close
def f040cvf_f040_climactic_volume_flag_climax_378d_base_v020_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_21d_base_v021_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_63d_base_v022_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_126d_base_v023_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_252d_base_v024_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_504d_base_v025_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_5d_base_v026_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_10d_base_v027_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_42d_base_v028_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_189d_base_v029_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d climax intensity
def f040cvf_f040_climactic_volume_flag_intens_378d_base_v030_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs vol extreme × close
def f040cvf_f040_climactic_volume_flag_absvex_21d_base_v031_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs vol extreme × close
def f040cvf_f040_climactic_volume_flag_absvex_63d_base_v032_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs vol extreme × close
def f040cvf_f040_climactic_volume_flag_absvex_252d_base_v033_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol extreme squared × close
def f040cvf_f040_climactic_volume_flag_vexsq_21d_base_v034_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 21)
    result = z * z.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol extreme squared × close
def f040cvf_f040_climactic_volume_flag_vexsq_63d_base_v035_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 63)
    result = z * z.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol extreme squared × close
def f040cvf_f040_climactic_volume_flag_vexsq_252d_base_v036_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 252)
    result = z * z.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean vol extreme × close
def f040cvf_f040_climactic_volume_flag_meanvex_21d_base_v037_signal(closeadj, volume):
    result = _mean(_f040_vol_extreme(volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean vol extreme × close
def f040cvf_f040_climactic_volume_flag_meanvex_63d_base_v038_signal(closeadj, volume):
    result = _mean(_f040_vol_extreme(volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean vol extreme × close
def f040cvf_f040_climactic_volume_flag_meanvex_252d_base_v039_signal(closeadj, volume):
    result = _mean(_f040_vol_extreme(volume, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std vol extreme × close
def f040cvf_f040_climactic_volume_flag_stdvex_21d_base_v040_signal(closeadj, volume):
    result = _std(_f040_vol_extreme(volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std vol extreme × close
def f040cvf_f040_climactic_volume_flag_stdvex_63d_base_v041_signal(closeadj, volume):
    result = _std(_f040_vol_extreme(volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score vol extreme × close
def f040cvf_f040_climactic_volume_flag_zvex_21d_base_v042_signal(closeadj, volume):
    result = _z(_f040_vol_extreme(volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score vol extreme × close
def f040cvf_f040_climactic_volume_flag_zvex_63d_base_v043_signal(closeadj, volume):
    result = _z(_f040_vol_extreme(volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × dollar volume
def f040cvf_f040_climactic_volume_flag_climxdv_21d_base_v044_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 21) * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax × dollar volume
def f040cvf_f040_climactic_volume_flag_climxdv_63d_base_v045_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 63) * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d climax × dollar volume
def f040cvf_f040_climactic_volume_flag_climxdv_252d_base_v046_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 252) * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed >2sigma threshold × close × volume
def f040cvf_f040_climactic_volume_flag_thr_21d_base_v047_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 21)
    flag = (z > 2.0).astype(float)
    result = _mean(flag, 63) * closeadj * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed >2sigma threshold × close × volume
def f040cvf_f040_climactic_volume_flag_thr_63d_base_v048_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 63)
    flag = (z > 2.0).astype(float)
    result = _mean(flag, 126) * closeadj * _mean(volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed >2sigma threshold × close × volume
def f040cvf_f040_climactic_volume_flag_thr_252d_base_v049_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 252)
    flag = (z > 2.0).astype(float)
    result = _mean(flag, 252) * closeadj * _mean(volume, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed 3sigma threshold × close × volume
def f040cvf_f040_climactic_volume_flag_thr3_21d_base_v050_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 21)
    flag = (z > 3.0).astype(float)
    result = _mean(flag, 63) * closeadj * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed 3sigma threshold × close × volume
def f040cvf_f040_climactic_volume_flag_thr3_63d_base_v051_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 63)
    flag = (z > 3.0).astype(float)
    result = _mean(flag, 126) * closeadj * _mean(volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of vol extremes (>2σ) × close
def f040cvf_f040_climactic_volume_flag_cntex_21d_base_v052_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 21)
    cnt = (z > 2.0).astype(float).rolling(63, min_periods=10).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of vol extremes × close
def f040cvf_f040_climactic_volume_flag_cntex_63d_base_v053_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 63)
    cnt = (z > 2.0).astype(float).rolling(126, min_periods=21).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of vol extremes × close
def f040cvf_f040_climactic_volume_flag_cntex_252d_base_v054_signal(closeadj, volume):
    z = _f040_vol_extreme(volume, 252)
    cnt = (z > 2.0).astype(float).rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax intensity × dollar volume
def f040cvf_f040_climactic_volume_flag_intxdv_21d_base_v055_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 21) * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax intensity × dollar volume
def f040cvf_f040_climactic_volume_flag_intxdv_63d_base_v056_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 63) * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d climax intensity × dollar volume
def f040cvf_f040_climactic_volume_flag_intxdv_252d_base_v057_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 252) * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of vol extreme × close
def f040cvf_f040_climactic_volume_flag_emavex_21d_base_v058_signal(closeadj, volume):
    base = _f040_vol_extreme(volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of vol extreme × close
def f040cvf_f040_climactic_volume_flag_emavex_63d_base_v059_signal(closeadj, volume):
    base = _f040_vol_extreme(volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of climax × close
def f040cvf_f040_climactic_volume_flag_emaclim_21d_base_v060_signal(closeadj, volume):
    base = _f040_climax_volume(volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of climax × close
def f040cvf_f040_climactic_volume_flag_emaclim_63d_base_v061_signal(closeadj, volume):
    base = _f040_climax_volume(volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of intensity × close
def f040cvf_f040_climactic_volume_flag_emaintens_21d_base_v062_signal(closeadj, volume):
    base = _f040_climax_intensity(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of intensity × close
def f040cvf_f040_climactic_volume_flag_emaintens_63d_base_v063_signal(closeadj, volume):
    base = _f040_climax_intensity(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol extreme × z close
def f040cvf_f040_climactic_volume_flag_vexxzcl_21d_base_v064_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol extreme × z close
def f040cvf_f040_climactic_volume_flag_vexxzcl_63d_base_v065_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * _z(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol extreme × close mean
def f040cvf_f040_climactic_volume_flag_vexxclmn_21d_base_v066_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol extreme × close mean
def f040cvf_f040_climactic_volume_flag_vexxclmn_63d_base_v067_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol extreme × close mean
def f040cvf_f040_climactic_volume_flag_vexxclmn_252d_base_v068_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 252) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol extreme × close std
def f040cvf_f040_climactic_volume_flag_vexxclstd_21d_base_v069_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol extreme × close std
def f040cvf_f040_climactic_volume_flag_vexxclstd_63d_base_v070_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign vol extreme × close
def f040cvf_f040_climactic_volume_flag_signvex_21d_base_v071_signal(closeadj, volume):
    result = np.sign(_f040_vol_extreme(volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign vol extreme × close
def f040cvf_f040_climactic_volume_flag_signvex_63d_base_v072_signal(closeadj, volume):
    result = np.sign(_f040_vol_extreme(volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol extreme × volume
def f040cvf_f040_climactic_volume_flag_vexxvol_21d_base_v073_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * volume * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol extreme × volume
def f040cvf_f040_climactic_volume_flag_vexxvol_63d_base_v074_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * volume * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × log close
def f040cvf_f040_climactic_volume_flag_climxlogcl_21d_base_v075_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f040cvf_f040_climactic_volume_flag_vex_21d_base_v001_signal,
    f040cvf_f040_climactic_volume_flag_vex_63d_base_v002_signal,
    f040cvf_f040_climactic_volume_flag_vex_126d_base_v003_signal,
    f040cvf_f040_climactic_volume_flag_vex_252d_base_v004_signal,
    f040cvf_f040_climactic_volume_flag_vex_504d_base_v005_signal,
    f040cvf_f040_climactic_volume_flag_vex_5d_base_v006_signal,
    f040cvf_f040_climactic_volume_flag_vex_10d_base_v007_signal,
    f040cvf_f040_climactic_volume_flag_vex_42d_base_v008_signal,
    f040cvf_f040_climactic_volume_flag_vex_189d_base_v009_signal,
    f040cvf_f040_climactic_volume_flag_vex_378d_base_v010_signal,
    f040cvf_f040_climactic_volume_flag_climax_21d_base_v011_signal,
    f040cvf_f040_climactic_volume_flag_climax_63d_base_v012_signal,
    f040cvf_f040_climactic_volume_flag_climax_126d_base_v013_signal,
    f040cvf_f040_climactic_volume_flag_climax_252d_base_v014_signal,
    f040cvf_f040_climactic_volume_flag_climax_504d_base_v015_signal,
    f040cvf_f040_climactic_volume_flag_climax_5d_base_v016_signal,
    f040cvf_f040_climactic_volume_flag_climax_10d_base_v017_signal,
    f040cvf_f040_climactic_volume_flag_climax_42d_base_v018_signal,
    f040cvf_f040_climactic_volume_flag_climax_189d_base_v019_signal,
    f040cvf_f040_climactic_volume_flag_climax_378d_base_v020_signal,
    f040cvf_f040_climactic_volume_flag_intens_21d_base_v021_signal,
    f040cvf_f040_climactic_volume_flag_intens_63d_base_v022_signal,
    f040cvf_f040_climactic_volume_flag_intens_126d_base_v023_signal,
    f040cvf_f040_climactic_volume_flag_intens_252d_base_v024_signal,
    f040cvf_f040_climactic_volume_flag_intens_504d_base_v025_signal,
    f040cvf_f040_climactic_volume_flag_intens_5d_base_v026_signal,
    f040cvf_f040_climactic_volume_flag_intens_10d_base_v027_signal,
    f040cvf_f040_climactic_volume_flag_intens_42d_base_v028_signal,
    f040cvf_f040_climactic_volume_flag_intens_189d_base_v029_signal,
    f040cvf_f040_climactic_volume_flag_intens_378d_base_v030_signal,
    f040cvf_f040_climactic_volume_flag_absvex_21d_base_v031_signal,
    f040cvf_f040_climactic_volume_flag_absvex_63d_base_v032_signal,
    f040cvf_f040_climactic_volume_flag_absvex_252d_base_v033_signal,
    f040cvf_f040_climactic_volume_flag_vexsq_21d_base_v034_signal,
    f040cvf_f040_climactic_volume_flag_vexsq_63d_base_v035_signal,
    f040cvf_f040_climactic_volume_flag_vexsq_252d_base_v036_signal,
    f040cvf_f040_climactic_volume_flag_meanvex_21d_base_v037_signal,
    f040cvf_f040_climactic_volume_flag_meanvex_63d_base_v038_signal,
    f040cvf_f040_climactic_volume_flag_meanvex_252d_base_v039_signal,
    f040cvf_f040_climactic_volume_flag_stdvex_21d_base_v040_signal,
    f040cvf_f040_climactic_volume_flag_stdvex_63d_base_v041_signal,
    f040cvf_f040_climactic_volume_flag_zvex_21d_base_v042_signal,
    f040cvf_f040_climactic_volume_flag_zvex_63d_base_v043_signal,
    f040cvf_f040_climactic_volume_flag_climxdv_21d_base_v044_signal,
    f040cvf_f040_climactic_volume_flag_climxdv_63d_base_v045_signal,
    f040cvf_f040_climactic_volume_flag_climxdv_252d_base_v046_signal,
    f040cvf_f040_climactic_volume_flag_thr_21d_base_v047_signal,
    f040cvf_f040_climactic_volume_flag_thr_63d_base_v048_signal,
    f040cvf_f040_climactic_volume_flag_thr_252d_base_v049_signal,
    f040cvf_f040_climactic_volume_flag_thr3_21d_base_v050_signal,
    f040cvf_f040_climactic_volume_flag_thr3_63d_base_v051_signal,
    f040cvf_f040_climactic_volume_flag_cntex_21d_base_v052_signal,
    f040cvf_f040_climactic_volume_flag_cntex_63d_base_v053_signal,
    f040cvf_f040_climactic_volume_flag_cntex_252d_base_v054_signal,
    f040cvf_f040_climactic_volume_flag_intxdv_21d_base_v055_signal,
    f040cvf_f040_climactic_volume_flag_intxdv_63d_base_v056_signal,
    f040cvf_f040_climactic_volume_flag_intxdv_252d_base_v057_signal,
    f040cvf_f040_climactic_volume_flag_emavex_21d_base_v058_signal,
    f040cvf_f040_climactic_volume_flag_emavex_63d_base_v059_signal,
    f040cvf_f040_climactic_volume_flag_emaclim_21d_base_v060_signal,
    f040cvf_f040_climactic_volume_flag_emaclim_63d_base_v061_signal,
    f040cvf_f040_climactic_volume_flag_emaintens_21d_base_v062_signal,
    f040cvf_f040_climactic_volume_flag_emaintens_63d_base_v063_signal,
    f040cvf_f040_climactic_volume_flag_vexxzcl_21d_base_v064_signal,
    f040cvf_f040_climactic_volume_flag_vexxzcl_63d_base_v065_signal,
    f040cvf_f040_climactic_volume_flag_vexxclmn_21d_base_v066_signal,
    f040cvf_f040_climactic_volume_flag_vexxclmn_63d_base_v067_signal,
    f040cvf_f040_climactic_volume_flag_vexxclmn_252d_base_v068_signal,
    f040cvf_f040_climactic_volume_flag_vexxclstd_21d_base_v069_signal,
    f040cvf_f040_climactic_volume_flag_vexxclstd_63d_base_v070_signal,
    f040cvf_f040_climactic_volume_flag_signvex_21d_base_v071_signal,
    f040cvf_f040_climactic_volume_flag_signvex_63d_base_v072_signal,
    f040cvf_f040_climactic_volume_flag_vexxvol_21d_base_v073_signal,
    f040cvf_f040_climactic_volume_flag_vexxvol_63d_base_v074_signal,
    f040cvf_f040_climactic_volume_flag_climxlogcl_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F040_CLIMACTIC_VOLUME_FLAG_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f040_vol_extreme", "_f040_climax_volume", "_f040_climax_intensity")
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
    print(f"OK f040_climactic_volume_flag_base_001_075_claude: {n_features} features pass")
