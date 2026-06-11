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


def _f030_low_vol_indicator(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 4, 63), min_periods=max(1, w // 2)).std()
    deficit = (long_vol - vol) / long_vol.replace(0, np.nan)
    return deficit * closeadj


def _f030_compression_duration(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 4, 63), min_periods=max(1, w // 2)).std()
    low = (vol < long_vol * 0.7).astype(float)
    grp = (low.diff().fillna(0).abs().cumsum())
    dur = low.groupby(grp).cumsum() * closeadj
    return dur + (long_vol - vol).abs() * closeadj * 0.01


def _f030_coil_length(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 4, 63), min_periods=max(1, w // 2)).std()
    ratio = vol / long_vol.replace(0, np.nan)
    coiled = (ratio < 1.0).astype(float)
    return coiled.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).sum() * closeadj + ratio * closeadj * 0.01

def f030cmd_f030_compression_duration_lowvol_raw_5d_base_v001_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_5d_base_v002_signal(closeadj):
    base = _f030_compression_duration(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_5d_base_v003_signal(closeadj):
    base = _f030_coil_length(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_10d_base_v004_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_10d_base_v005_signal(closeadj):
    base = _f030_compression_duration(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_10d_base_v006_signal(closeadj):
    base = _f030_coil_length(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_21d_base_v007_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_21d_base_v008_signal(closeadj):
    base = _f030_compression_duration(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_21d_base_v009_signal(closeadj):
    base = _f030_coil_length(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_42d_base_v010_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_42d_base_v011_signal(closeadj):
    base = _f030_compression_duration(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_42d_base_v012_signal(closeadj):
    base = _f030_coil_length(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_63d_base_v013_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_63d_base_v014_signal(closeadj):
    base = _f030_compression_duration(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_63d_base_v015_signal(closeadj):
    base = _f030_coil_length(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_126d_base_v016_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_126d_base_v017_signal(closeadj):
    base = _f030_compression_duration(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_126d_base_v018_signal(closeadj):
    base = _f030_coil_length(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_189d_base_v019_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_189d_base_v020_signal(closeadj):
    base = _f030_compression_duration(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_189d_base_v021_signal(closeadj):
    base = _f030_coil_length(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_252d_base_v022_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_252d_base_v023_signal(closeadj):
    base = _f030_compression_duration(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_252d_base_v024_signal(closeadj):
    base = _f030_coil_length(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_378d_base_v025_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_378d_base_v026_signal(closeadj):
    base = _f030_compression_duration(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_378d_base_v027_signal(closeadj):
    base = _f030_coil_length(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_raw_504d_base_v028_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_raw_504d_base_v029_signal(closeadj):
    base = _f030_compression_duration(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_raw_504d_base_v030_signal(closeadj):
    base = _f030_coil_length(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_5d_base_v031_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_5d_base_v032_signal(closeadj):
    base = _f030_compression_duration(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_5d_base_v033_signal(closeadj):
    base = _f030_coil_length(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_10d_base_v034_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_10d_base_v035_signal(closeadj):
    base = _f030_compression_duration(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_10d_base_v036_signal(closeadj):
    base = _f030_coil_length(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_21d_base_v037_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_21d_base_v038_signal(closeadj):
    base = _f030_compression_duration(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_21d_base_v039_signal(closeadj):
    base = _f030_coil_length(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_42d_base_v040_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_42d_base_v041_signal(closeadj):
    base = _f030_compression_duration(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_42d_base_v042_signal(closeadj):
    base = _f030_coil_length(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_63d_base_v043_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_63d_base_v044_signal(closeadj):
    base = _f030_compression_duration(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_63d_base_v045_signal(closeadj):
    base = _f030_coil_length(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_126d_base_v046_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_126d_base_v047_signal(closeadj):
    base = _f030_compression_duration(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_126d_base_v048_signal(closeadj):
    base = _f030_coil_length(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_189d_base_v049_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_189d_base_v050_signal(closeadj):
    base = _f030_compression_duration(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_189d_base_v051_signal(closeadj):
    base = _f030_coil_length(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_252d_base_v052_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_252d_base_v053_signal(closeadj):
    base = _f030_compression_duration(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_252d_base_v054_signal(closeadj):
    base = _f030_coil_length(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_378d_base_v055_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_378d_base_v056_signal(closeadj):
    base = _f030_compression_duration(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_378d_base_v057_signal(closeadj):
    base = _f030_coil_length(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_abs_504d_base_v058_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_abs_504d_base_v059_signal(closeadj):
    base = _f030_compression_duration(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_abs_504d_base_v060_signal(closeadj):
    base = _f030_coil_length(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_sqrt_5d_base_v061_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_sqrt_5d_base_v062_signal(closeadj):
    base = _f030_compression_duration(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_sqrt_5d_base_v063_signal(closeadj):
    base = _f030_coil_length(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_sqrt_10d_base_v064_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_sqrt_10d_base_v065_signal(closeadj):
    base = _f030_compression_duration(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_sqrt_10d_base_v066_signal(closeadj):
    base = _f030_coil_length(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_sqrt_21d_base_v067_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_sqrt_21d_base_v068_signal(closeadj):
    base = _f030_compression_duration(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_sqrt_21d_base_v069_signal(closeadj):
    base = _f030_coil_length(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_sqrt_42d_base_v070_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_sqrt_42d_base_v071_signal(closeadj):
    base = _f030_compression_duration(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_sqrt_42d_base_v072_signal(closeadj):
    base = _f030_coil_length(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_sqrt_63d_base_v073_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_sqrt_63d_base_v074_signal(closeadj):
    base = _f030_compression_duration(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_sqrt_63d_base_v075_signal(closeadj):
    base = _f030_coil_length(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f030cmd_f030_compression_duration_lowvol_raw_5d_base_v001_signal,
    f030cmd_f030_compression_duration_compdur_raw_5d_base_v002_signal,
    f030cmd_f030_compression_duration_coil_raw_5d_base_v003_signal,
    f030cmd_f030_compression_duration_lowvol_raw_10d_base_v004_signal,
    f030cmd_f030_compression_duration_compdur_raw_10d_base_v005_signal,
    f030cmd_f030_compression_duration_coil_raw_10d_base_v006_signal,
    f030cmd_f030_compression_duration_lowvol_raw_21d_base_v007_signal,
    f030cmd_f030_compression_duration_compdur_raw_21d_base_v008_signal,
    f030cmd_f030_compression_duration_coil_raw_21d_base_v009_signal,
    f030cmd_f030_compression_duration_lowvol_raw_42d_base_v010_signal,
    f030cmd_f030_compression_duration_compdur_raw_42d_base_v011_signal,
    f030cmd_f030_compression_duration_coil_raw_42d_base_v012_signal,
    f030cmd_f030_compression_duration_lowvol_raw_63d_base_v013_signal,
    f030cmd_f030_compression_duration_compdur_raw_63d_base_v014_signal,
    f030cmd_f030_compression_duration_coil_raw_63d_base_v015_signal,
    f030cmd_f030_compression_duration_lowvol_raw_126d_base_v016_signal,
    f030cmd_f030_compression_duration_compdur_raw_126d_base_v017_signal,
    f030cmd_f030_compression_duration_coil_raw_126d_base_v018_signal,
    f030cmd_f030_compression_duration_lowvol_raw_189d_base_v019_signal,
    f030cmd_f030_compression_duration_compdur_raw_189d_base_v020_signal,
    f030cmd_f030_compression_duration_coil_raw_189d_base_v021_signal,
    f030cmd_f030_compression_duration_lowvol_raw_252d_base_v022_signal,
    f030cmd_f030_compression_duration_compdur_raw_252d_base_v023_signal,
    f030cmd_f030_compression_duration_coil_raw_252d_base_v024_signal,
    f030cmd_f030_compression_duration_lowvol_raw_378d_base_v025_signal,
    f030cmd_f030_compression_duration_compdur_raw_378d_base_v026_signal,
    f030cmd_f030_compression_duration_coil_raw_378d_base_v027_signal,
    f030cmd_f030_compression_duration_lowvol_raw_504d_base_v028_signal,
    f030cmd_f030_compression_duration_compdur_raw_504d_base_v029_signal,
    f030cmd_f030_compression_duration_coil_raw_504d_base_v030_signal,
    f030cmd_f030_compression_duration_lowvol_abs_5d_base_v031_signal,
    f030cmd_f030_compression_duration_compdur_abs_5d_base_v032_signal,
    f030cmd_f030_compression_duration_coil_abs_5d_base_v033_signal,
    f030cmd_f030_compression_duration_lowvol_abs_10d_base_v034_signal,
    f030cmd_f030_compression_duration_compdur_abs_10d_base_v035_signal,
    f030cmd_f030_compression_duration_coil_abs_10d_base_v036_signal,
    f030cmd_f030_compression_duration_lowvol_abs_21d_base_v037_signal,
    f030cmd_f030_compression_duration_compdur_abs_21d_base_v038_signal,
    f030cmd_f030_compression_duration_coil_abs_21d_base_v039_signal,
    f030cmd_f030_compression_duration_lowvol_abs_42d_base_v040_signal,
    f030cmd_f030_compression_duration_compdur_abs_42d_base_v041_signal,
    f030cmd_f030_compression_duration_coil_abs_42d_base_v042_signal,
    f030cmd_f030_compression_duration_lowvol_abs_63d_base_v043_signal,
    f030cmd_f030_compression_duration_compdur_abs_63d_base_v044_signal,
    f030cmd_f030_compression_duration_coil_abs_63d_base_v045_signal,
    f030cmd_f030_compression_duration_lowvol_abs_126d_base_v046_signal,
    f030cmd_f030_compression_duration_compdur_abs_126d_base_v047_signal,
    f030cmd_f030_compression_duration_coil_abs_126d_base_v048_signal,
    f030cmd_f030_compression_duration_lowvol_abs_189d_base_v049_signal,
    f030cmd_f030_compression_duration_compdur_abs_189d_base_v050_signal,
    f030cmd_f030_compression_duration_coil_abs_189d_base_v051_signal,
    f030cmd_f030_compression_duration_lowvol_abs_252d_base_v052_signal,
    f030cmd_f030_compression_duration_compdur_abs_252d_base_v053_signal,
    f030cmd_f030_compression_duration_coil_abs_252d_base_v054_signal,
    f030cmd_f030_compression_duration_lowvol_abs_378d_base_v055_signal,
    f030cmd_f030_compression_duration_compdur_abs_378d_base_v056_signal,
    f030cmd_f030_compression_duration_coil_abs_378d_base_v057_signal,
    f030cmd_f030_compression_duration_lowvol_abs_504d_base_v058_signal,
    f030cmd_f030_compression_duration_compdur_abs_504d_base_v059_signal,
    f030cmd_f030_compression_duration_coil_abs_504d_base_v060_signal,
    f030cmd_f030_compression_duration_lowvol_sqrt_5d_base_v061_signal,
    f030cmd_f030_compression_duration_compdur_sqrt_5d_base_v062_signal,
    f030cmd_f030_compression_duration_coil_sqrt_5d_base_v063_signal,
    f030cmd_f030_compression_duration_lowvol_sqrt_10d_base_v064_signal,
    f030cmd_f030_compression_duration_compdur_sqrt_10d_base_v065_signal,
    f030cmd_f030_compression_duration_coil_sqrt_10d_base_v066_signal,
    f030cmd_f030_compression_duration_lowvol_sqrt_21d_base_v067_signal,
    f030cmd_f030_compression_duration_compdur_sqrt_21d_base_v068_signal,
    f030cmd_f030_compression_duration_coil_sqrt_21d_base_v069_signal,
    f030cmd_f030_compression_duration_lowvol_sqrt_42d_base_v070_signal,
    f030cmd_f030_compression_duration_compdur_sqrt_42d_base_v071_signal,
    f030cmd_f030_compression_duration_coil_sqrt_42d_base_v072_signal,
    f030cmd_f030_compression_duration_lowvol_sqrt_63d_base_v073_signal,
    f030cmd_f030_compression_duration_compdur_sqrt_63d_base_v074_signal,
    f030cmd_f030_compression_duration_coil_sqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F030_COMPRESSION_DURATION_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f030_low_vol_indicator', '_f030_compression_duration', '_f030_coil_length')
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
    print(f"OK f030_compression_duration_base_001_075_claude: {n_features} features pass")
