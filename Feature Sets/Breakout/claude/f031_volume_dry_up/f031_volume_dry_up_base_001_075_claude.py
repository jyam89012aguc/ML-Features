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


def f031vdu_f031_volume_dry_up_volratio_5d_base_v001_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_10d_base_v002_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_21d_base_v003_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_42d_base_v004_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_63d_base_v005_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_126d_base_v006_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_189d_base_v007_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_252d_base_v008_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_378d_base_v009_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_volratio_504d_base_v010_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_5d_base_v011_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_10d_base_v012_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_21d_base_v013_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_42d_base_v014_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_63d_base_v015_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_126d_base_v016_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_189d_base_v017_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_252d_base_v018_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_378d_base_v019_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_invratio_504d_base_v020_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = (1.0 / r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_5d_base_v021_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_10d_base_v022_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_21d_base_v023_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_42d_base_v024_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_63d_base_v025_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_126d_base_v026_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_189d_base_v027_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_252d_base_v028_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_378d_base_v029_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryup_504d_base_v030_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_5d_base_v031_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_10d_base_v032_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_21d_base_v033_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_42d_base_v034_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_63d_base_v035_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_126d_base_v036_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_189d_base_v037_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_252d_base_v038_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_378d_base_v039_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sellexh_504d_base_v040_signal(volume, closeadj):
    result = _f031_selling_exhaustion(volume, closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_5d_base_v041_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = _mean(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_10d_base_v042_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = _mean(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_21d_base_v043_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = _mean(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_42d_base_v044_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = _mean(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_63d_base_v045_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = _mean(r, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_126d_base_v046_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = _mean(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_189d_base_v047_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = _mean(r, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_252d_base_v048_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = _mean(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_378d_base_v049_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = _mean(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smvolratio_504d_base_v050_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = _mean(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_5d_base_v051_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_10d_base_v052_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_21d_base_v053_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_42d_base_v054_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_63d_base_v055_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_126d_base_v056_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_189d_base_v057_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_252d_base_v058_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_378d_base_v059_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zvolratio_504d_base_v060_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_5d_base_v061_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_10d_base_v062_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_21d_base_v063_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_42d_base_v064_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_63d_base_v065_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_126d_base_v066_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_189d_base_v067_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_252d_base_v068_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_378d_base_v069_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_logvolratio_504d_base_v070_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = np.log(r.clip(lower=1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_5d_base_v071_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_10d_base_v072_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_21d_base_v073_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_42d_base_v074_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = _std(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_63d_base_v075_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = _std(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f031vdu_f031_volume_dry_up_volratio_5d_base_v001_signal,
    f031vdu_f031_volume_dry_up_volratio_10d_base_v002_signal,
    f031vdu_f031_volume_dry_up_volratio_21d_base_v003_signal,
    f031vdu_f031_volume_dry_up_volratio_42d_base_v004_signal,
    f031vdu_f031_volume_dry_up_volratio_63d_base_v005_signal,
    f031vdu_f031_volume_dry_up_volratio_126d_base_v006_signal,
    f031vdu_f031_volume_dry_up_volratio_189d_base_v007_signal,
    f031vdu_f031_volume_dry_up_volratio_252d_base_v008_signal,
    f031vdu_f031_volume_dry_up_volratio_378d_base_v009_signal,
    f031vdu_f031_volume_dry_up_volratio_504d_base_v010_signal,
    f031vdu_f031_volume_dry_up_invratio_5d_base_v011_signal,
    f031vdu_f031_volume_dry_up_invratio_10d_base_v012_signal,
    f031vdu_f031_volume_dry_up_invratio_21d_base_v013_signal,
    f031vdu_f031_volume_dry_up_invratio_42d_base_v014_signal,
    f031vdu_f031_volume_dry_up_invratio_63d_base_v015_signal,
    f031vdu_f031_volume_dry_up_invratio_126d_base_v016_signal,
    f031vdu_f031_volume_dry_up_invratio_189d_base_v017_signal,
    f031vdu_f031_volume_dry_up_invratio_252d_base_v018_signal,
    f031vdu_f031_volume_dry_up_invratio_378d_base_v019_signal,
    f031vdu_f031_volume_dry_up_invratio_504d_base_v020_signal,
    f031vdu_f031_volume_dry_up_dryup_5d_base_v021_signal,
    f031vdu_f031_volume_dry_up_dryup_10d_base_v022_signal,
    f031vdu_f031_volume_dry_up_dryup_21d_base_v023_signal,
    f031vdu_f031_volume_dry_up_dryup_42d_base_v024_signal,
    f031vdu_f031_volume_dry_up_dryup_63d_base_v025_signal,
    f031vdu_f031_volume_dry_up_dryup_126d_base_v026_signal,
    f031vdu_f031_volume_dry_up_dryup_189d_base_v027_signal,
    f031vdu_f031_volume_dry_up_dryup_252d_base_v028_signal,
    f031vdu_f031_volume_dry_up_dryup_378d_base_v029_signal,
    f031vdu_f031_volume_dry_up_dryup_504d_base_v030_signal,
    f031vdu_f031_volume_dry_up_sellexh_5d_base_v031_signal,
    f031vdu_f031_volume_dry_up_sellexh_10d_base_v032_signal,
    f031vdu_f031_volume_dry_up_sellexh_21d_base_v033_signal,
    f031vdu_f031_volume_dry_up_sellexh_42d_base_v034_signal,
    f031vdu_f031_volume_dry_up_sellexh_63d_base_v035_signal,
    f031vdu_f031_volume_dry_up_sellexh_126d_base_v036_signal,
    f031vdu_f031_volume_dry_up_sellexh_189d_base_v037_signal,
    f031vdu_f031_volume_dry_up_sellexh_252d_base_v038_signal,
    f031vdu_f031_volume_dry_up_sellexh_378d_base_v039_signal,
    f031vdu_f031_volume_dry_up_sellexh_504d_base_v040_signal,
    f031vdu_f031_volume_dry_up_smvolratio_5d_base_v041_signal,
    f031vdu_f031_volume_dry_up_smvolratio_10d_base_v042_signal,
    f031vdu_f031_volume_dry_up_smvolratio_21d_base_v043_signal,
    f031vdu_f031_volume_dry_up_smvolratio_42d_base_v044_signal,
    f031vdu_f031_volume_dry_up_smvolratio_63d_base_v045_signal,
    f031vdu_f031_volume_dry_up_smvolratio_126d_base_v046_signal,
    f031vdu_f031_volume_dry_up_smvolratio_189d_base_v047_signal,
    f031vdu_f031_volume_dry_up_smvolratio_252d_base_v048_signal,
    f031vdu_f031_volume_dry_up_smvolratio_378d_base_v049_signal,
    f031vdu_f031_volume_dry_up_smvolratio_504d_base_v050_signal,
    f031vdu_f031_volume_dry_up_zvolratio_5d_base_v051_signal,
    f031vdu_f031_volume_dry_up_zvolratio_10d_base_v052_signal,
    f031vdu_f031_volume_dry_up_zvolratio_21d_base_v053_signal,
    f031vdu_f031_volume_dry_up_zvolratio_42d_base_v054_signal,
    f031vdu_f031_volume_dry_up_zvolratio_63d_base_v055_signal,
    f031vdu_f031_volume_dry_up_zvolratio_126d_base_v056_signal,
    f031vdu_f031_volume_dry_up_zvolratio_189d_base_v057_signal,
    f031vdu_f031_volume_dry_up_zvolratio_252d_base_v058_signal,
    f031vdu_f031_volume_dry_up_zvolratio_378d_base_v059_signal,
    f031vdu_f031_volume_dry_up_zvolratio_504d_base_v060_signal,
    f031vdu_f031_volume_dry_up_logvolratio_5d_base_v061_signal,
    f031vdu_f031_volume_dry_up_logvolratio_10d_base_v062_signal,
    f031vdu_f031_volume_dry_up_logvolratio_21d_base_v063_signal,
    f031vdu_f031_volume_dry_up_logvolratio_42d_base_v064_signal,
    f031vdu_f031_volume_dry_up_logvolratio_63d_base_v065_signal,
    f031vdu_f031_volume_dry_up_logvolratio_126d_base_v066_signal,
    f031vdu_f031_volume_dry_up_logvolratio_189d_base_v067_signal,
    f031vdu_f031_volume_dry_up_logvolratio_252d_base_v068_signal,
    f031vdu_f031_volume_dry_up_logvolratio_378d_base_v069_signal,
    f031vdu_f031_volume_dry_up_logvolratio_504d_base_v070_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_5d_base_v071_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_10d_base_v072_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_21d_base_v073_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_42d_base_v074_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F031_VOLUME_DRY_UP_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f031_volume_dry_up_base_001_075_claude: {n_features} features pass")
