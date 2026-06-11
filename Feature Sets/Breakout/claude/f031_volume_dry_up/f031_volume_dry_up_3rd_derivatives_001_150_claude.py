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
def _f031_vol_ratio(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / avg.replace(0, np.nan)


def _f031_dry_up_signal(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    r = volume / avg.replace(0, np.nan)
    return (1.0 / r.replace(0, np.nan)) - 1.0


def _f031_selling_exhaustion(volume, closeadj, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    ratio = volume / avg.replace(0, np.nan)
    ret = closeadj.pct_change()
    down = (ret < 0).astype(float)
    return (1.0 - ratio).clip(lower=-5, upper=5) * down * closeadj


def f031vdu_f031_volume_dry_up_volratio_21d_jerk_v001_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_21d_jerk_v002_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_63d_jerk_v003_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_63d_jerk_v004_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_126d_jerk_v005_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_126d_jerk_v006_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_252d_jerk_v007_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_252d_jerk_v008_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_252d_jerk_v009_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_252d_jerk_v010_signal(volume, closeadj):
    base = _f031_vol_ratio(volume, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_21d_jerk_v011_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_21d_jerk_v012_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_63d_jerk_v013_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_63d_jerk_v014_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_126d_jerk_v015_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_126d_jerk_v016_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_252d_jerk_v017_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_252d_jerk_v018_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_252d_jerk_v019_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_252d_jerk_v020_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = (1.0 / r.replace(0, np.nan)) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_21d_jerk_v021_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_21d_jerk_v022_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_63d_jerk_v023_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_63d_jerk_v024_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_126d_jerk_v025_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_126d_jerk_v026_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_252d_jerk_v027_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_252d_jerk_v028_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_252d_jerk_v029_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_252d_jerk_v030_signal(volume, closeadj):
    base = _f031_dry_up_signal(volume, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_21d_jerk_v031_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_21d_jerk_v032_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_63d_jerk_v033_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_63d_jerk_v034_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_126d_jerk_v035_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_126d_jerk_v036_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v037_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v038_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v039_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v040_signal(volume, closeadj):
    base = _f031_selling_exhaustion(volume, closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_21d_jerk_v041_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = _mean(r, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_21d_jerk_v042_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = _mean(r, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_63d_jerk_v043_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = _mean(r, 31) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_63d_jerk_v044_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = _mean(r, 31) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_126d_jerk_v045_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = _mean(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_126d_jerk_v046_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = _mean(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v047_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _mean(r, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v048_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _mean(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v049_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _mean(r, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v050_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _mean(r, 126) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_21d_jerk_v051_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_21d_jerk_v052_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_63d_jerk_v053_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_63d_jerk_v054_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_126d_jerk_v055_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = _z(r, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_126d_jerk_v056_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = _z(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v057_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v058_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v059_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v060_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_21d_jerk_v061_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_21d_jerk_v062_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_63d_jerk_v063_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_63d_jerk_v064_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_126d_jerk_v065_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_126d_jerk_v066_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v067_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v068_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v069_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v070_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = np.log(r.clip(lower=1e-6)) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_21d_jerk_v071_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_21d_jerk_v072_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_63d_jerk_v073_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = _std(r, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_63d_jerk_v074_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = _std(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_126d_jerk_v075_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = _std(r, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_126d_jerk_v076_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = _std(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v077_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _std(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v078_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _std(r, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v079_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _std(r, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v080_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = _std(r, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_21d_jerk_v081_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    base = _mean(d, 7) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_21d_jerk_v082_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    base = _mean(d, 7) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_63d_jerk_v083_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_63d_jerk_v084_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_126d_jerk_v085_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    base = _mean(d, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_126d_jerk_v086_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    base = _mean(d, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v087_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _mean(d, 84) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v088_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _mean(d, 84) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v089_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _mean(d, 84) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v090_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _mean(d, 84) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_21d_jerk_v091_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_21d_jerk_v092_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_63d_jerk_v093_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_63d_jerk_v094_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_126d_jerk_v095_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    base = _z(d, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_126d_jerk_v096_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    base = _z(d, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v097_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _z(d, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v098_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _z(d, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v099_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _z(d, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v100_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = _z(d, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_21d_jerk_v101_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    dv = closeadj * volume
    base = d * _mean(dv, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_21d_jerk_v102_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    dv = closeadj * volume
    base = d * _mean(dv, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_63d_jerk_v103_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    dv = closeadj * volume
    base = d * _mean(dv, 31)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_63d_jerk_v104_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    dv = closeadj * volume
    base = d * _mean(dv, 31)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_126d_jerk_v105_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    dv = closeadj * volume
    base = d * _mean(dv, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_126d_jerk_v106_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    dv = closeadj * volume
    base = d * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v107_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v108_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v109_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v110_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 126)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_21d_jerk_v111_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 21)
    base = _z(s, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_21d_jerk_v112_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 21)
    base = _z(s, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_63d_jerk_v113_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 63)
    base = _z(s, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_63d_jerk_v114_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 63)
    base = _z(s, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_126d_jerk_v115_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 126)
    base = _z(s, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_126d_jerk_v116_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 126)
    base = _z(s, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v117_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _z(s, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v118_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _z(s, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v119_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _z(s, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v120_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _z(s, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_21d_jerk_v121_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 21)
    base = _mean(s, 7)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_21d_jerk_v122_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 21)
    base = _mean(s, 7)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_63d_jerk_v123_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 63)
    base = _mean(s, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_63d_jerk_v124_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 63)
    base = _mean(s, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_126d_jerk_v125_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 126)
    base = _mean(s, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_126d_jerk_v126_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 126)
    base = _mean(s, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v127_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _mean(s, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v128_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _mean(s, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v129_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _mean(s, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v130_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    base = _mean(s, 84)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_21d_jerk_v131_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = r.ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_21d_jerk_v132_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    base = r.ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_63d_jerk_v133_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = r.ewm(span=31, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_63d_jerk_v134_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    base = r.ewm(span=31, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_126d_jerk_v135_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = r.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_126d_jerk_v136_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    base = r.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v137_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = r.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v138_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = r.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v139_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = r.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v140_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    base = r.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_21d_jerk_v141_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_21d_jerk_v142_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_63d_jerk_v143_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_63d_jerk_v144_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_126d_jerk_v145_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_126d_jerk_v146_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v147_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v148_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v149_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v150_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    base = (d * d) * np.sign(d) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f031vdu_f031_volume_dry_up_volratio_21d_jerk_v001_signal,
    f031vdu_f031_volume_dry_up_volratio_21d_jerk_v002_signal,
    f031vdu_f031_volume_dry_up_volratio_63d_jerk_v003_signal,
    f031vdu_f031_volume_dry_up_volratio_63d_jerk_v004_signal,
    f031vdu_f031_volume_dry_up_volratio_126d_jerk_v005_signal,
    f031vdu_f031_volume_dry_up_volratio_126d_jerk_v006_signal,
    f031vdu_f031_volume_dry_up_volratio_252d_jerk_v007_signal,
    f031vdu_f031_volume_dry_up_volratio_252d_jerk_v008_signal,
    f031vdu_f031_volume_dry_up_volratio_252d_jerk_v009_signal,
    f031vdu_f031_volume_dry_up_volratio_252d_jerk_v010_signal,
    f031vdu_f031_volume_dry_up_invratio_21d_jerk_v011_signal,
    f031vdu_f031_volume_dry_up_invratio_21d_jerk_v012_signal,
    f031vdu_f031_volume_dry_up_invratio_63d_jerk_v013_signal,
    f031vdu_f031_volume_dry_up_invratio_63d_jerk_v014_signal,
    f031vdu_f031_volume_dry_up_invratio_126d_jerk_v015_signal,
    f031vdu_f031_volume_dry_up_invratio_126d_jerk_v016_signal,
    f031vdu_f031_volume_dry_up_invratio_252d_jerk_v017_signal,
    f031vdu_f031_volume_dry_up_invratio_252d_jerk_v018_signal,
    f031vdu_f031_volume_dry_up_invratio_252d_jerk_v019_signal,
    f031vdu_f031_volume_dry_up_invratio_252d_jerk_v020_signal,
    f031vdu_f031_volume_dry_up_dryup_21d_jerk_v021_signal,
    f031vdu_f031_volume_dry_up_dryup_21d_jerk_v022_signal,
    f031vdu_f031_volume_dry_up_dryup_63d_jerk_v023_signal,
    f031vdu_f031_volume_dry_up_dryup_63d_jerk_v024_signal,
    f031vdu_f031_volume_dry_up_dryup_126d_jerk_v025_signal,
    f031vdu_f031_volume_dry_up_dryup_126d_jerk_v026_signal,
    f031vdu_f031_volume_dry_up_dryup_252d_jerk_v027_signal,
    f031vdu_f031_volume_dry_up_dryup_252d_jerk_v028_signal,
    f031vdu_f031_volume_dry_up_dryup_252d_jerk_v029_signal,
    f031vdu_f031_volume_dry_up_dryup_252d_jerk_v030_signal,
    f031vdu_f031_volume_dry_up_sellexh_21d_jerk_v031_signal,
    f031vdu_f031_volume_dry_up_sellexh_21d_jerk_v032_signal,
    f031vdu_f031_volume_dry_up_sellexh_63d_jerk_v033_signal,
    f031vdu_f031_volume_dry_up_sellexh_63d_jerk_v034_signal,
    f031vdu_f031_volume_dry_up_sellexh_126d_jerk_v035_signal,
    f031vdu_f031_volume_dry_up_sellexh_126d_jerk_v036_signal,
    f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v037_signal,
    f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v038_signal,
    f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v039_signal,
    f031vdu_f031_volume_dry_up_sellexh_252d_jerk_v040_signal,
    f031vdu_f031_volume_dry_up_smvolratio_21d_jerk_v041_signal,
    f031vdu_f031_volume_dry_up_smvolratio_21d_jerk_v042_signal,
    f031vdu_f031_volume_dry_up_smvolratio_63d_jerk_v043_signal,
    f031vdu_f031_volume_dry_up_smvolratio_63d_jerk_v044_signal,
    f031vdu_f031_volume_dry_up_smvolratio_126d_jerk_v045_signal,
    f031vdu_f031_volume_dry_up_smvolratio_126d_jerk_v046_signal,
    f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v047_signal,
    f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v048_signal,
    f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v049_signal,
    f031vdu_f031_volume_dry_up_smvolratio_252d_jerk_v050_signal,
    f031vdu_f031_volume_dry_up_zvolratio_21d_jerk_v051_signal,
    f031vdu_f031_volume_dry_up_zvolratio_21d_jerk_v052_signal,
    f031vdu_f031_volume_dry_up_zvolratio_63d_jerk_v053_signal,
    f031vdu_f031_volume_dry_up_zvolratio_63d_jerk_v054_signal,
    f031vdu_f031_volume_dry_up_zvolratio_126d_jerk_v055_signal,
    f031vdu_f031_volume_dry_up_zvolratio_126d_jerk_v056_signal,
    f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v057_signal,
    f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v058_signal,
    f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v059_signal,
    f031vdu_f031_volume_dry_up_zvolratio_252d_jerk_v060_signal,
    f031vdu_f031_volume_dry_up_logvolratio_21d_jerk_v061_signal,
    f031vdu_f031_volume_dry_up_logvolratio_21d_jerk_v062_signal,
    f031vdu_f031_volume_dry_up_logvolratio_63d_jerk_v063_signal,
    f031vdu_f031_volume_dry_up_logvolratio_63d_jerk_v064_signal,
    f031vdu_f031_volume_dry_up_logvolratio_126d_jerk_v065_signal,
    f031vdu_f031_volume_dry_up_logvolratio_126d_jerk_v066_signal,
    f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v067_signal,
    f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v068_signal,
    f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v069_signal,
    f031vdu_f031_volume_dry_up_logvolratio_252d_jerk_v070_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_21d_jerk_v071_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_21d_jerk_v072_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_63d_jerk_v073_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_63d_jerk_v074_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_126d_jerk_v075_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_126d_jerk_v076_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v077_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v078_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v079_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_252d_jerk_v080_signal,
    f031vdu_f031_volume_dry_up_smdryup_21d_jerk_v081_signal,
    f031vdu_f031_volume_dry_up_smdryup_21d_jerk_v082_signal,
    f031vdu_f031_volume_dry_up_smdryup_63d_jerk_v083_signal,
    f031vdu_f031_volume_dry_up_smdryup_63d_jerk_v084_signal,
    f031vdu_f031_volume_dry_up_smdryup_126d_jerk_v085_signal,
    f031vdu_f031_volume_dry_up_smdryup_126d_jerk_v086_signal,
    f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v087_signal,
    f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v088_signal,
    f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v089_signal,
    f031vdu_f031_volume_dry_up_smdryup_252d_jerk_v090_signal,
    f031vdu_f031_volume_dry_up_zdryup_21d_jerk_v091_signal,
    f031vdu_f031_volume_dry_up_zdryup_21d_jerk_v092_signal,
    f031vdu_f031_volume_dry_up_zdryup_63d_jerk_v093_signal,
    f031vdu_f031_volume_dry_up_zdryup_63d_jerk_v094_signal,
    f031vdu_f031_volume_dry_up_zdryup_126d_jerk_v095_signal,
    f031vdu_f031_volume_dry_up_zdryup_126d_jerk_v096_signal,
    f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v097_signal,
    f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v098_signal,
    f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v099_signal,
    f031vdu_f031_volume_dry_up_zdryup_252d_jerk_v100_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_21d_jerk_v101_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_21d_jerk_v102_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_63d_jerk_v103_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_63d_jerk_v104_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_126d_jerk_v105_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_126d_jerk_v106_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v107_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v108_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v109_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_252d_jerk_v110_signal,
    f031vdu_f031_volume_dry_up_zsellexh_21d_jerk_v111_signal,
    f031vdu_f031_volume_dry_up_zsellexh_21d_jerk_v112_signal,
    f031vdu_f031_volume_dry_up_zsellexh_63d_jerk_v113_signal,
    f031vdu_f031_volume_dry_up_zsellexh_63d_jerk_v114_signal,
    f031vdu_f031_volume_dry_up_zsellexh_126d_jerk_v115_signal,
    f031vdu_f031_volume_dry_up_zsellexh_126d_jerk_v116_signal,
    f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v117_signal,
    f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v118_signal,
    f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v119_signal,
    f031vdu_f031_volume_dry_up_zsellexh_252d_jerk_v120_signal,
    f031vdu_f031_volume_dry_up_smsellexh_21d_jerk_v121_signal,
    f031vdu_f031_volume_dry_up_smsellexh_21d_jerk_v122_signal,
    f031vdu_f031_volume_dry_up_smsellexh_63d_jerk_v123_signal,
    f031vdu_f031_volume_dry_up_smsellexh_63d_jerk_v124_signal,
    f031vdu_f031_volume_dry_up_smsellexh_126d_jerk_v125_signal,
    f031vdu_f031_volume_dry_up_smsellexh_126d_jerk_v126_signal,
    f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v127_signal,
    f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v128_signal,
    f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v129_signal,
    f031vdu_f031_volume_dry_up_smsellexh_252d_jerk_v130_signal,
    f031vdu_f031_volume_dry_up_emavolratio_21d_jerk_v131_signal,
    f031vdu_f031_volume_dry_up_emavolratio_21d_jerk_v132_signal,
    f031vdu_f031_volume_dry_up_emavolratio_63d_jerk_v133_signal,
    f031vdu_f031_volume_dry_up_emavolratio_63d_jerk_v134_signal,
    f031vdu_f031_volume_dry_up_emavolratio_126d_jerk_v135_signal,
    f031vdu_f031_volume_dry_up_emavolratio_126d_jerk_v136_signal,
    f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v137_signal,
    f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v138_signal,
    f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v139_signal,
    f031vdu_f031_volume_dry_up_emavolratio_252d_jerk_v140_signal,
    f031vdu_f031_volume_dry_up_sqdryup_21d_jerk_v141_signal,
    f031vdu_f031_volume_dry_up_sqdryup_21d_jerk_v142_signal,
    f031vdu_f031_volume_dry_up_sqdryup_63d_jerk_v143_signal,
    f031vdu_f031_volume_dry_up_sqdryup_63d_jerk_v144_signal,
    f031vdu_f031_volume_dry_up_sqdryup_126d_jerk_v145_signal,
    f031vdu_f031_volume_dry_up_sqdryup_126d_jerk_v146_signal,
    f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v147_signal,
    f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v148_signal,
    f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v149_signal,
    f031vdu_f031_volume_dry_up_sqdryup_252d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F031_VOLUME_DRY_UP_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ('_f031_vol_ratio', '_f031_dry_up_signal', '_f031_selling_exhaustion')
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
    print(f"OK f031_volume_dry_up_3rd_derivatives_001_150_claude: {n_features} features pass")
